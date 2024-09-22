import json
from enum import Enum

# Define an enum class for assignment preferences
class AssignmentPreference(Enum):
    PREFERRED = "Preferred"  # A soldier prefers this assignment
    TOGETHER = "With Partner"  # A soldier wants to be assigned with a specific partner


# Custom JSON encoder for serializing enum values
class AssignmentPreferenceEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AssignmentPreference):
            return obj.value
        return super().default(obj)


# Create a class to represent a constraint
class SoldierConstraint:
    def __init__(self, importance: int, preference: AssignmentPreference, partner_names: list = [], assignment_name: str = "general") -> None:
        self.assignment_name = assignment_name
        self.importance = importance  # Importance level (1 to 3)
        self.preference = preference  # Assignment preference
        self.partner_names = partner_names  # List of partner names (if preference is TOGETHER)


class Difficult_Level(Enum):
    INTENSE = 0
    CASUAL = 1
    EASY = 2
