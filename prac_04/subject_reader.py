"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    display_subjects(data)


def load_data(filename):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_lists = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        subject_lists.append(parts)
    input_file.close()
    return subject_lists

def display_subjects(subjects):
    """Display details of each subject"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")



main()
