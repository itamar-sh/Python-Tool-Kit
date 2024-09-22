from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path
from jinja2 import Template
from constraints import AssignmentPreference

TIME_TABLE_PATH = str(Path(__file__).resolve().parent / "html_templates" / "schedule.html")
OUTPUT_HTML_PATH_HTML = str(Path(__file__).resolve().parent / f"time_table_result{str(datetime.now())}.html")
OUTPUT_HTML_PATH_CSV = str(Path(__file__).resolve().parent / f"time_table_last_result.csv")


COMMANDER_STR = "מפקד"
HIGH_LEVEL = "פלוגה"
MID_LEVEL = "מחלקה"
LOW_LEVEL = "כיתה"


class Schedule:
    def __init__(self, company) -> None:
        self.company = company
        self.time_table = None

    def get_empty_tasks_table(self, hours_to_init, cur_time):
        time_windows = [f"{self.increment_hours(cur_time, i).hour} {self.increment_hours(cur_time, i).strftime('%A')}" for i in range(0, hours_to_init, 1)]
        tasks = []
        for assignment in self.company.assignments:
            captions = assignment.get_task_captions()
            tasks.extend(captions)
        return pd.DataFrame(columns=tasks, index=time_windows)

    def increment_hours(self, cur_time, hours_to_add):
        return cur_time + timedelta(hours=hours_to_add)

    def get_next_tasks_table(self, hours_to_extend):
        if self.time_table is None:
            return self.get_empty_tasks_table(hours_to_extend, datetime.now())
        else:
            return self.augment_existing_time_table_with_empty_cells(hours_to_extend)

    def find_solution(self, hours_to_extend=24):
        time_table = self.get_next_tasks_table(hours_to_extend)
        for row_index, (hour, row) in enumerate(time_table.iterrows()):
            print(datetime.now())
            print(time_table)
            for assignment_name in time_table.columns:
                time_frame = self.company.find_assignment_by_name(assignment_name).time_frame
                if row_index % time_frame == 0:
                    # Access the current cell value
                    if pd.isna(row[assignment_name]):
                        available_soldier = self.find_available_soldier(time_frame, time_table, row_index, assignment_name)
                        for i in range(time_frame):
                            time_table.iat[row_index + i, time_table.columns.get_loc(assignment_name)] = available_soldier.name  # Update the next column

        assignments_names = []
        for assignment in self.company.assignments:
            assignments_names.extend([assignment.name]*len(assignment.get_task_captions()))
        # get assignment_names row and add it as the last row in the time_table - it should be extracted when loading the time_table
        assignments_names_df = pd.DataFrame([assignments_names], columns=time_table.columns)
        time_table = pd.concat([time_table, assignments_names_df], ignore_index=False)
        self.save_time_table(time_table)
        return time_table

    def find_available_soldier(self, time_frame, time_table, row_index, assignment_name):
        max_score = 0
        best_fit = None
        # print("find start again \n\n")
        for soldier in self.company.soldiers:
            if not soldier.is_in_base:
                continue

            for i in range(time_frame):
                time_table.iat[row_index + i, time_table.columns.get_loc(assignment_name)] = soldier.name  # Update the next column
            # if soldier.name == "לונטל ניר":
            #     import ipdb; ipdb.set_trace()
            table_score = self.get_table_score(time_table)
            if table_score > max_score:
                max_score = table_score
                best_fit = soldier
            # print(soldier.name, table_score)
        if not best_fit:
            import ipdb; ipdb.set_trace()
            a = 42
        return best_fit

    def get_table_score(self, time_table):
        score = 0
        # check propriery
        if self.is_same_soldier_used_twice_parallel(time_table):
            return 0
        # score for filling the table
        filling_cells_score = self.filling_cells_score(time_table)
        print(f"filling_cells_score: {filling_cells_score}")
        # score for letting soldiers rest a lot
        soldier_rest_score = self.soldier_rest_score(time_table)
        print(f"soldier_rest_score: {soldier_rest_score}")
        # score for not letting soldier do more than necessary
        assignments_replacements_score = self.assignments_replacements_score(time_table)
        print(f"assignments_replacements_score: {assignments_replacements_score}")
        # score for soldier constraints. Preferences and requirments.
        soldier_constraints_score = self.soldier_constraints_score(time_table)
        print(f"assignments_replacements_score: {soldier_constraints_score}")
        # score for assignment constraints. Requirements of the assignment.
        assignment_contraints_score = self.assignment_contraints_score(time_table)
        print(f"assignments_replacements_score: {assignments_replacements_score}")

        score  = filling_cells_score + soldier_rest_score + assignments_replacements_score + soldier_constraints_score + assignment_contraints_score
        print(f"score conclusion: {score}")
        return score

    def filling_cells_score(self, time_table):
        score = 0
        for row_index, (hour, row) in enumerate(time_table.iterrows()):
            for assignment_name in time_table.columns:
                if not pd.isna(row[assignment_name]):
                    score += 10
        return score

    def is_same_soldier_used_twice_parallel(self, time_table):
        for hour, row in time_table.iterrows():
            seen_soldiers = set()
            for assignment_name in time_table.columns:
                cell_value = row[assignment_name]
                # import ipdb; ipdb.set_trace()
                if isinstance(cell_value, str):
                    if cell_value in seen_soldiers:
                        return True
                    else:
                        seen_soldiers.add(cell_value)
        return False

    def soldier_rest_score(self, time_table):
        soldier_rest_score = 0
        for row_index, (hour, row) in enumerate(time_table.iterrows()):
            for assignment_name in time_table.columns:
                if self.soldier_finish_assignment(row, assignment_name, row_index, time_table):
                    soldier_next_assignment_time = self.soldier_next_assignment(row_index, time_table, row[assignment_name])
                    soldier_rest_time = soldier_next_assignment_time - row_index
                    soldier_rest_score += soldier_rest_time
        return soldier_rest_score

    def soldier_finish_assignment(self, row, assignment_name, row_index, time_table):
        return row_index + 1 < len(time_table) and \
            time_table.iat[row_index + 1, time_table.columns.get_loc(assignment_name)] != row[assignment_name]

    def soldier_next_assignment(self, last_row_index, time_table, soldier_name):
        for row_index, (hour, row) in enumerate(time_table.iterrows()):
            if row_index > last_row_index:
                for assignment_name in time_table.columns: 
                    if row[assignment_name] == soldier_name:
                        return row_index
        return len(time_table) - 1

    def assignments_replacements_score(self, time_table):
        assignments_replacements_score = 0
        for assignment_name in time_table.columns:
            assignment = self.company.find_assignment_by_name(assignment_name)
            # in case the assignment is easy we don't want people to replace it.
            if assignment.difficult == 0:
                continue

            column_index = time_table.columns.get_loc(assignment_name)
            time_frame = assignment.time_frame
            cur_soldier = time_table.iat[0, column_index]
            cur_soldier_appearances = 1
            # import ipdb; ipdb.set_trace()
            for same_soldier_index in range(1, len(time_table)): 
                if pd.isna(cur_soldier):
                    break

                if time_table.iat[same_soldier_index, time_table.columns.get_loc(assignment_name)] != cur_soldier:
                    assignments_replacements_score += time_frame - cur_soldier_appearances
                    cur_soldier = time_table.iat[same_soldier_index, column_index]
                    cur_soldier_appearances = 1
                else:
                    cur_soldier_appearances += 1
        return assignments_replacements_score

    def soldier_constraints_score(self, time_table):
        soldier_constraints_score = 0
        for row_index, (hour, row) in enumerate(time_table.iterrows()):
            for assignment_name in time_table.columns:
                cur_soldier = row[assignment_name]
                if pd.isna(cur_soldier):
                    break

                for contraint in self.company.find_soldier_by_name(row[assignment_name]).constraints:
                    soldier_constraints_score += self.find_constraint_score(row, assignment_name, time_table, contraint)
        return soldier_constraints_score

    def find_constraint_score(self, row, assignment_name, time_table, constraint):
        if constraint.assignment_name in assignment_name and constraint.preference == AssignmentPreference.PREFERRED:
            return 1
        constraint_score = 0
        if constraint.preference == AssignmentPreference.TOGETHER.value:
            # import ipdb; ipdb.set_trace()
            soldiers_on_the_same_assignment = [row[assignment] for assignment in time_table.columns]
            for partner in constraint.partner_names:
                if partner in soldiers_on_the_same_assignment:
                   constraint_score += 1
        return constraint_score 
    
    def assignment_contraints_score(self, time_table):
        constraint_score = 0
        for assignment in self.company.assignments:
            constraint_score += self.commander_level_score(time_table, assignment, assignment.commander_level)
        return constraint_score

    def commander_level_score(self, time_table, assignment, commander_level):
        commander_level_score = 0
        for assignment_name in time_table.columns:
            if assignment.name in assignment_name and COMMANDER_STR in assignment_name:
                for row_time, soldier_name in time_table[assignment_name].items():
                    if pd.isna(soldier_name):
                        break
                    soldier_job_description = self.company.find_soldier_by_name(soldier_name).job_description
                    # import ipdb; ipdb.set_trace()
                    commander_level_score += self.how_good_job_description_fit_commander_level(soldier_job_description, commander_level)
        return commander_level_score
    
    def how_good_job_description_fit_commander_level(self, soldier_job_description, commander_level_required):
        commander_level_table = {HIGH_LEVEL: 3, MID_LEVEL: 2, LOW_LEVEL: 1}
        soldier_level = self.find_soldier_level(soldier_job_description)
        if soldier_level is None:
            return 0
        if commander_level_table[soldier_level] == commander_level_table[commander_level_required]:
            return 10
        if commander_level_table[soldier_level] < commander_level_table[commander_level_required]:
            return commander_level_table[soldier_level]
        return 1
    
    def find_soldier_level(self, soldier_job_description):
        if type(soldier_job_description) is not str:
            return None
        # import ipdb; ipdb.set_trace()
        if HIGH_LEVEL in soldier_job_description:
            return HIGH_LEVEL
        if MID_LEVEL in soldier_job_description:
            return MID_LEVEL
        if LOW_LEVEL in soldier_job_description:
            return LOW_LEVEL
    
    def save_time_table(self, time_table):
        # extract the assignments_names row from the time_table
        assignments_names = time_table.iloc[-1]
        time_table = time_table.iloc[:-1]
        # reverse the time_table so the labels will make sense
        time_table = time_table.iloc[:, ::-1]
        # find critical information for storing via html
        shorten_time_table, time_table_spans, hours_row = self.rearrange_time_table_for_display(time_table)
        assignments_names_labels, assignments_names_spans = self.rearrange_assignments_names_for_display(assignments_names)
        with open(TIME_TABLE_PATH, "rt") as f:
                template = Template(f.read())
                html_time_table = template.render(
                    assignments_names_labels = assignments_names_labels,
                    assignments_names_spans = assignments_names_spans,
                    time_table_names=shorten_time_table,
                    time_table_spans=time_table_spans,
                    hours_row=hours_row
                )
                with open(OUTPUT_HTML_PATH_HTML, "wt") as output_file:
                    output_file.write(html_time_table)
        
        assignments_names_df = pd.DataFrame([assignments_names], columns=time_table.columns)
        time_table = pd.concat([time_table, assignments_names_df], ignore_index=False)
        time_table.to_csv(OUTPUT_HTML_PATH_CSV, index=True)
    
    def load_last_time_table(self):
        self.time_table = pd.read_csv(OUTPUT_HTML_PATH_CSV, index_col=0)
    
    def rearrange_time_table_for_display(self, time_table):
        def _add_soldier_and_row_span(soldiers, row_spans, current_soldier, current_row_span):
            soldiers.append(current_soldier)
            row_spans.append(current_row_span)
            
            # Add empty cells for line all cells on the same row. This is html requirement which avoids slip of cells to new lines.
            for _ in range(current_row_span-1):
                soldiers.append("Empty soldier")
                row_spans.append(1)

        # Initialize empty DataFrames to store results
        soldier_names_df = pd.DataFrame()
        row_span_df = pd.DataFrame()

        for col in time_table.columns:
            col_data = time_table[col]

            # Initialize variables to track soldiers and row spans
            soldiers = []
            row_spans = []

            current_soldier = col_data.iloc[0]  # Assume the first value is a soldier name
            current_row_span = 1

            # Iterate through the column data to identify soldiers and row spans
            for value in col_data[1:]:
                if value == current_soldier:
                    current_row_span += 1
                else:
                    _add_soldier_and_row_span(soldiers, row_spans, current_soldier, current_row_span)

                    current_soldier = value
                    current_row_span = 1
            _add_soldier_and_row_span(soldiers, row_spans, current_soldier, current_row_span)

            # Add the last soldier and row span
            soldiers.append(current_soldier)
            row_spans.append(current_row_span)

            # Create DataFrames from the collected data
            col_names_df = pd.DataFrame({col: soldiers})
            col_row_span_df = pd.DataFrame({col: row_spans})

            # Concatenate with the existing results
            soldier_names_df = pd.concat([soldier_names_df, col_names_df], axis=1)
            row_span_df = pd.concat([row_span_df, col_row_span_df], axis=1)
        
        hours_row = time_table.index.tolist()

        return soldier_names_df, row_span_df, hours_row
    
    def rearrange_assignments_names_for_display(self, assignments_names):
        assignments_names_labels = []
        assignments_names_spans = []
        current_row_span = 0
        current_assignment_name = assignments_names[0]
        for assignment_name in assignments_names:
            if assignment_name != current_assignment_name:
                assignments_names_labels.append(current_assignment_name)
                assignments_names_spans.append(current_row_span)
                current_assignment_name = assignment_name
                current_row_span = 1
            else:
                current_row_span += 1
        assignments_names_labels.append(current_assignment_name)
        assignments_names_spans.append(current_row_span)
        return assignments_names_labels, assignments_names_spans
    
    def augment_existing_time_table_with_empty_cells(self, hours_to_extend):
        # need to take the last row and understand the last filled row and add the next row accordingly
        start_time = self.find_right_date(self.time_table.index[-2]) + timedelta(hours=1)
        return pd.concat([self.time_table.iloc[:-1], self.get_empty_tasks_table(hours_to_extend, start_time)], axis=0)
    
    def find_right_date(self, required_date):
        current_time = datetime.now()
        start_time = datetime.strptime(required_date, '%H %A').replace(year=current_time.year, month=current_time.month, day=current_time.day)
        
        # Find the closest required_date to the current datetime - we assume it's in the
        while start_time.strftime('%A') != 'Sunday' or start_time.hour != 23:
            start_time += timedelta(hours=1)
        return start_time
    
    def find_assignment_difficult(self, assignment_name):
        return self.company.find_assignment_by_name(assignment_name).difficult

    
if __name__ == "__main__":
    from company import load_company
    company = load_company()
# company.soldiers[0].add_constraint(SoldierConstraint(importance=2, preference=AssignmentPreference.TOGETHER, partner_names=["Soldier1", "Soldier2"]))
    schedule = Schedule(company)
    schedule.load_last_time_table()
    print(schedule.find_solution())