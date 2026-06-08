"""
Scraped eveything as that was not the right design.

oop would shine here so I would use that, so entities are students, subjects.

Different objects for different entities then another object for records obj

so different module for classes and a main file for running the project
"""

from classes import Record
import sys

def display() -> None:
    """Displays info related to student. return None"""
    student_record = {}
    grade_points = {'A':4,'B':3,'C':2,'D':1,'F':0}
    print("Welcome to student grading system")
    while True:
        print("---------------------------")
        print("1. Add Student")
        print("2. View Student Record")
        print("3. View All Records")
        print("4. Calculate GPA")
        print("5. Exit")
        user_input = int(input("Enter your choice: "))
        match user_input:
            case 1: 
                student = Record()
                student_record[student.student.roll_num] = student
            case 2:
                user_input = int(input("Enter Students roll number: "))
                student = student_record.get(user_input, "Student not found")
                print(f"Student's Name: {student.student.name}")
                print(f"Student's Roll Number: {student.student.roll_num}")
                print(f"Student's Subjects: {student.subject.subject_name}")
                print("Student's Credit Hours: "
                        f"{student.subject.subject_credit_hour}")
                print("Student's Grade Points: "
                        f"{student.subject.subject_grade_point}")
            case 3:
                for value in student_record.values():
                    print(f"All Student Record: ")
                    print(f"Student's Name: {value.student.name}")
                    print(f"Student's Roll Number: {value.student.roll_num}")
                    print(f"Student's Subjects: {value.subject.subject_name}")
                    print("Student's Credit Hours: "
                          f"{value.subject.subject_credit_hour}")
                    print("Student's Grade Points: "
                          f"{value.subject.subject_grade_point}")
            case 4:
                user_input = int(input("Enter student's roll number: "))
                student = student_record.get(user_input, None)
                total_quality_point = 0
                # calculate gpa
                student_grade = student.subject.subject_grade_point
                student_credit_hour = student.subject.subject_credit_hour
                for index, grade in enumerate(student_grade):
                    grade_point = grade_points.get(grade.upper(), None)
                    credit_hour = student_credit_hour[index]
                    total_quality_point += grade_point * credit_hour
                gpa = total_quality_point/sum(student_credit_hour)
                print(f"Student's GPA is: {gpa}")
            case 5:
                print("Thank You for Using Grading System.")
                sys.exit()

if __name__ == "__main__":
    display()