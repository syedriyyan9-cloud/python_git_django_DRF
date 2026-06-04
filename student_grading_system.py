"""

A basic project to practice what i have learned so far

[Main Loop: while True]
    │
    ├──► Choice 1: Add Student 
    │
    ├──► Choice 2: View All   
    │
    ├──► Choice 3: GPA 
    │
    └──► Choice 4: Exit        

"""

import sys

# create functions for adding, viewing, GPA calculations and displaying

# so what info relating to student do we need:
# name, roll number, subjects: grade points, credit hours
# dictionary overview
# {name: name, rollno: roll number, subjects: list(subject's names),
#  grade_points: list(subject grade points), credit_hours: list(credit_hours)}

# add students name and roll number
def student_name_roll() -> dict:
    """Returns dictionary containing students name, and roll number"""
    student_info = {}
    student_info['name'] = input("Student's name: ")
    student_info['rollno'] = input("Student's roll number: ")
    return student_info

# add students subjects, credit hours, grade points
def student_subject_info() -> list:
    """Returns a list containing tuples 
    storing subject name, credit hours and grade points"""
    subjects = []
    while True:
        subject_name = input("Subject's name: ")
        subject_grade_point = input("Subject's grade points (A+,A,B...F): ")
        subject_credit_hour = int(input("Subject's credit hours: "))
        subject_tuple = (subject_name,subject_grade_point,subject_credit_hour)
        subjects.append(subject_tuple)
        choice = input("Press q to stop adding subjects, press n to continue: ")
        if choice.lower() == 'q':
            break
    return subjects

# add subjects, credit hours and grade points to students dictionary
def add_student() -> dict:
    """returns a dict containing student's info."""
    student_info = student_name_roll()
    subjects = student_subject_info()
    # subject_names = []
    # subject_grade_points = []
    # subject_credit_hours = []
    # for subject in subjects:
    #     subject_names.append(subject[0])
    #     subject_grade_points.append(subject[1])
    #     subject_credit_hours.append(subject[2])
    student_info['subjects'] = subjects
    # student_info['grade_points'] = subject_grade_points
    # student_info['credit_hours'] = subject_credit_hours
    return student_info

# displays the students info
def view_students(dictionary) -> None:
    """Displays all the students records, Returns None"""
    for key, value in dictionary.items():
        print(f'{key}: {value}')

def calculate_gpa():
    """Returns Calculated Gpa of the student"""
    # get the student by name or by roll number
    # then get that student's subjects
    # then calculate GPA 
    # then return it.

def display():
    counter = 1
    all_students = {}
    print("Enter number of option you want to pick")
    while True:
        print('-----------------------------')
        print("1. Add Student")
        print("2. View All Students")
        print("3. Calculate Student GPA")
        print("4. Exit")
        choice = int(input())
        match choice:
            case 1:
                all_students[counter] = add_student()
                counter += 1
            case 2:
                view_students(all_students)
            case 3:

                break
            case 4:
                sys.exit()


if __name__ =='__main__':
    display()