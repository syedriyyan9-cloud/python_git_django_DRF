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

def view_students():
    pass

def calculate_gpa():
    pass

def display():
    pass


if __name__ =='__main__':
    print(add_student())