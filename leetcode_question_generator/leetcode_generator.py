import csv
from random import shuffle

def process_data_to_csv(input_file_name, output_file_name):
    with open(input_file_name) as input_file, open(output_file_name, 'w', newline='') as output_file:
        lines = input_file.readlines()
        writer = csv.writer(output_file)
        writer.writerow(["Question Name", "Difficulty"])

        rows = []
        for line_index in range(0, len(lines)-4, 4):
            question_name = lines[line_index].strip()
            difficulty = lines[line_index+3].strip()
            rows.append([question_name, difficulty])
        shuffle(rows)
        writer.writerows(rows)

input_file_path = "/home/itamars/q150"
output_file_path = "leetcode_top_150_most_common_interview_questions.csv"
process_data_to_csv(input_file_path, output_file_path)
