class Soldier:
    def __init__(self, name, is_in_base, job_description) -> None:
        self.name = name
        self.is_in_base = is_in_base
        self.constraints = []
        self.job_description = job_description

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
