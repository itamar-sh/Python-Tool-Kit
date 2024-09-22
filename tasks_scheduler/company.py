import json
import pandas as pd
from soldier import Soldier
from schedule import Schedule
from assignment import Assignment
from constraints import SoldierConstraint, AssignmentPreferenceEncoder


class Company:
    def __init__(self, soldiers, assignments) -> None:
        self.soldiers = soldiers
        self.assignments = assignments

    def add_soldier(self, soldier):
        self.soldiers.append(soldier)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def find_assignment_by_name(self, assignment_name):
        for assignment in self.assignments:
            if assignment.name in assignment_name:
                return assignment

    def find_soldier_by_name(self, soldier_name):
        for soldier in self.soldiers:
            if soldier_name == soldier.name:
                return soldier

def load_company():
    soldiers_path = "/home/itamars/PycharmProjects/tasks_scheduler/soldiers2.csv"
    assignments_path = "/home/itamars/PycharmProjects/tasks_scheduler/assignments2.csv"

    soldiers_df = pd.read_csv(soldiers_path)  # Set header=None to ignore the header row
    company = Company([], [])
    for soldier_row in soldiers_df.itertuples(index=False):
        new_soldier = Soldier(soldier_row.name, soldier_row.in_base, soldier_row.job_description)
        for c in json.loads(soldier_row.constraints):
            new_soldier.add_constraint(SoldierConstraint(**c))
        company.add_soldier(new_soldier)

    assignments_df = pd.read_csv(assignments_path)
    for assignment_row in assignments_df.itertuples(index=False):
        company.add_assignment(Assignment(
            assignment_row.name,
            assignment_row.time_frame,
            assignment_row.num_of_members,
            assignment_row.commander_level,
            assignment_row.num_of_commanders,
            assignment_row.difficulty
        ))
    return company


def save_company(company):
    soldiers_path = "/home/itamars/PycharmProjects/tasks_scheduler/soldiers3.csv"
    assignments_path = "/home/itamars/PycharmProjects/tasks_scheduler/assignments2.csv"

    soldiers_dict = dict()
    names = []
    in_base = []
    constraints = []
    for soldier in company.soldiers:
        names.append(soldier.name)
        in_base.append(soldier.is_in_base)
        constraints.append(json.dumps([c.__dict__ for c in soldier.constraints], cls=AssignmentPreferenceEncoder))
    soldiers_dict["name"] = names
    soldiers_dict["in_base"] = in_base
    soldiers_dict["constraints"] = constraints
    pd.DataFrame(soldiers_dict).to_csv(soldiers_path, index=False)  # Set index=False to exclude the index column in the CSV

    assignment_dict = dict()
    names = []
    time_frames = []
    nums_of_poeple = []
    for assignment in company.assignments:
        names.append(assignment.name)
        time_frames.append(assignment.time_frame)
        nums_of_poeple.append(assignment.num_of_members)
    assignment_dict["name"] = names
    assignment_dict["time_frame"] = time_frames
    assignment_dict["num_of_members"] = nums_of_poeple
    pd.DataFrame(assignment_dict).to_csv(assignments_path, index=False)  # Set index=False to exclude the index column in the CSV


if __name__ == "__main__":
    company = load_company()
    # company.soldiers[0].add_constraint(SoldierConstraint(importance=2, preference=AssignmentPreference.TOGETHER, partner_names=["Soldier1", "Soldier2"]))
    schedule = Schedule(company)
    print(schedule.find_solution())
    # save_company(company)
