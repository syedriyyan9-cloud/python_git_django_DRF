"""
Scraped eveything as that was not the right design.

oop would shine here so I would use that, so entities are students, subjects.

Different objects for different entities then another object for records obj

so different module for classes and a main file for running the project
"""

from classes import Record
import sys
import csv

def user_choice(s: str) -> int:
    """takes user input and returns it in int"""
    try:
        user_value = int(input(s))
    except ValueError:
        print("Enter correctly using numbers")
    except TypeError:
        print("Enter correct value")
    else:
        print("---------------------------")
        return user_value

def view_student_records(value: Record) -> None:
    """Takes in Record object and prints its values. Returns None"""
    print(f"Student's Name: {value.student.name}")
    print(f"Student's Roll Number: {value.student.roll_num}")
    print(f"Student's Subjects: {value.subject.subject_name}")
    print("Student's Credit Hours: "
            f"{value.subject.subject_credit_hour}")
    print("Student's Grade Points: "
            f"{value.subject.subject_grade_point}")
    print("-----------------------")
    return None

def calculate_gpa(student: Record) -> float:
    """Takes in Record object and returns gpa in float data type"""
    grade_points = {'A':4,'B':3,'C':2,'D':1,'F':0}
    total_quality_point = 0
    student_grade = student.subject.subject_grade_point
    student_credit_hour = student.subject.subject_credit_hour
    for index, grade in enumerate(student_grade):
        grade_point = grade_points.get(grade.upper(), None)
        credit_hour = student_credit_hour[index]
        total_quality_point += grade_point * credit_hour
    gpa = total_quality_point/sum(student_credit_hour)
    print("---------------------------")
    return gpa

def given_choices() -> None:
    """displays choices we have give to user. Returns None"""
    print("1. Add Student")
    print("2. View Student Record")
    print("3. View All Records")
    print("4. Calculate GPA")
    print("5. Exit")
    print("---------------------------")
    return None    

def store_record(d: dict) -> None:
    """Saves a record to a file. Returns none"""
    # file_path = 'file.txt'
    file_path = 'file.csv'
    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        file.write(d)
        
def load_records():
    """Loads the records saved in file"""
    student_record = {}
    # file_path = 'file.txt'
    file_path = 'file.csv'
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        pass
            


def display() -> None:
    """Displays info related to student. return None"""
    student_record = {}
    print("Welcome to student grading system")
    #load saved student records
    while True:
        given_choices()
        user_input = user_choice("Enter your Choice: ")
        match user_input:
            case 1: 
                student = Record()
                student_record[student.student.roll_num] = student
                store_record(f"{student.student.name}, {student.student.roll_num}, " 
                             f"{student.subject.subject_name}, " 
                             f"{student.subject.subject_credit_hour}, "
                             f"{student.subject.subject_grade_point}")
            case 2:
                user_input = user_choice("Enter student's roll number: ")
                student = student_record.get(user_input, "Student not found")
                view_student_records(student)
            case 3:
                print(f"All Student Record: ")
                for value in student_record.values():
                    view_student_records(value)
            case 4:
                user_input = user_choice("Enter student's roll number: ")
                student = student_record.get(user_input, None)
                print(f"Student's GPA is: {calculate_gpa(student)}")
            case 5:
                print("Thank You for Using Grading System.")
                sys.exit()

if __name__ == "__main__":
    display()