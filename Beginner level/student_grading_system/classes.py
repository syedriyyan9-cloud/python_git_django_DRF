"""

Contains all the classes that are to be used inside main.py for student 
grading system.

"""

class Student:
    """contains student's name and roll number"""

    def __init__(self):
        """initialize attributes"""
        self.name = input('Enter student\'s name: ')
        self.roll_num = int(input('Enter student\'s roll number: '))

class Subject:
    """contains student's subjects name, credit hour, grade point"""
    
    def __init__(self):
        """initialize subject name, credit hour, grade point"""
        self.subject_name = []
        self.subject_credit_hour = []
        self.subject_grade_point = []
        while True:
            self.subject_name.append(input('Enter Subject name: '))
            self.subject_credit_hour.append(
                input('Enter Subject credit hours: '))
            self.subject_grade_point.append(
                input('Enter Grade Point(A,B,C...): '))
            choice = input('Add more subjects? press \'n\' for no: ')
            if choice.lower() == 'n':
                break

class Record:
    """contains objects of student and subject class as student record"""
    
    def __init__(self):
        """Contains students info related to student"""
        self.student = Student()
        self.subject = Subject()