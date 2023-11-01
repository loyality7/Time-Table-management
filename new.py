import pandas as pd
import numpy as np
import random

# Constants
years = ["Year 1", "Year 2", "Year 3"]
groups = ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8"]
sections = ["Section A", "Section B"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_hours = 6

# Subjects and their hours
subjects = ["sub1", "sub2", "sub3", "sub4", "sub5", "sub6"]
lab_lib_subjects = ["Lab", "Lib"]
subject_hours = {subject: 4 for subject in subjects}
lab_lib_hours = 2

# Create a list of lecturers
lecturers = [f"lect{i}" for i in range(1, 81)]

# Create a dictionary to track which lecturers are assigned to subjects
lecturer_assignment = {}

# Function to generate and display the simplified timetable for a specific day
def generate_day_timetable(year, group, section, day):
    if year in years and group in groups and section in sections and day in days:
        timetable = []

        day_subjects = subjects.copy()
        day_lecturers = lecturers.copy()

        for hour in range(1, day_hours + 1):
            if hour <= lab_lib_hours:
                subject = random.choice(lab_lib_subjects)
                lecturer = ""
            else:
                if day_subjects:
                    subject = random.choice(day_subjects)
                    day_subjects.remove(subject)

                    # Check if lecturers for the subject are already assigned
                    if subject not in lecturer_assignment:
                        lecturer_assignment[subject] = []
                    possible_lecturers = [l for l in day_lecturers if l not in lecturer_assignment[subject]]

                    if possible_lecturers:
                        lecturer = random.choice(possible_lecturers)
                        lecturer_assignment[subject].append(lecturer)
                    else:
                        lecturer = ""
                else:
                    subject = random.choice(lab_lib_subjects)
                    lecturer = ""

            timetable.append([year, group, section, day, hour, subject, lecturer])

        df = pd.DataFrame(timetable, columns=["Year", "Group", "Section", "Day", "Hour", "Subject", "Lecturer"])
        print(f"Simplified Timetable for Year {year}, Group {group}, Section {section}, Day {day}:\n")
        print(df)

    else:
        print("Timetable not found for the selected options.")

# Choose options
year = input("Choose a year (1 for Year 1, 2 for Year 2, 3 for Year 3): ")
group = input("Enter the group (1 to 8): ")
section = input("Enter the section (A for Section 1, B for Section 2): ")
day = input("Choose a day (1 for Monday, 2 for Tuesday, etc.): ")

# Convert input to corresponding values
year = years[int(year) - 1] if 1 <= int(year) <= 3 else None
group = groups[int(group) - 1] if 1 <= int(group) <= 8 else None
section = sections[0] if section.lower() == "1" else sections[1] if section.lower() == "2" else None
day = days[int(day) - 1] if 1 <= int(day) <= 7 else None

if year and group and section and day:
    generate_day_timetable(year, group, section, day)
else:
    print("Invalid input. Please check your selections.")
