from datetime import datetime

class DateUtils:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

    @classmethod
    def from_timestamp(cls, timestamp):
        dt = datetime.fromtimestamp(timestamp)
        return cls(dt.year, dt.month, dt.day)

# Example usage
date1 = DateUtils.from_string('2023-07-10')
print(date1.year, date1.month, date1.day)  # Output: 2023 7 10

timestamp = 1678790000  # Example timestamp
date2 = DateUtils.from_timestamp(timestamp)
print(date2.year, date2.month, date2.day)  # Output: 2023 3 13 (assuming the timestamp corresponds to this date)
