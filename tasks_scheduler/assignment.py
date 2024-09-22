class Assignment:
    def __init__(self, name, time_frame = 4, num_of_members=1, commander_level = "חייל רגיל", num_of_commanders = 0, difficult = 1) -> None:
        self.name = name
        self.num_of_members = num_of_members
        self.time_frame = time_frame
        self.commander_level = commander_level
        self.num_of_commanders = num_of_commanders
        self.difficult = difficult

    def get_task_captions(self):
        captions = []
        num_of_members_left = self.num_of_members
        if self.commander_level != "חייל רגיל":
            captions.append(f"מפקד {self.name}")
            num_of_members_left -= 1
            if self.num_of_commanders:
                for i in range(1, self.num_of_commanders):
                    captions.append(f"מפקד {i+1} {self.name}")
                    num_of_members_left -= 1
        captions.extend([f"{self.name} {i+1}" for i in range(num_of_members_left)])
        return captions
