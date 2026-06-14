"""

Contains all the classes that are to be used inside main.py for student 
grading system.

"""

class Student:
    """contains student's name and roll number"""

    def __init__(self, name: str = '', roll: int = 0) -> None:
        """initialize student name and roll number. Returns None"""
        if name and roll:
            self.name = name
            self.roll_num = roll
        else:
            self.name = input('Enter student\'s name: ')
            self.roll_num = int(input('Enter student\'s roll number: '))

class Subject:
    """contains student's subjects name, credit hour, grade point"""
    
    def __init__(self, subjects: list = None, credit_hours: list = None, grade_points: list = None) -> None:
        """initialize subject name, credit hour, grade point. Returns None"""
        if subjects is not None and credit_hours is not None and grade_points is not None:
            self.subject_name = subjects
            self.subject_credit_hour = credit_hours
            self.subject_grade_point = grade_points
        else:
            self.subject_name = []
            self.subject_credit_hour = []
            self.subject_grade_point = []
            while True:
                self.subject_name.append(input('Enter Subject name: '))
                self.subject_credit_hour.append(
                    int(input('Enter Subject credit hours: ')))
                self.subject_grade_point.append(
                    input('Enter Grade Point(A,B,C...): '))
                choice = input('Add more subjects? press \'n\' for no: ')
                if choice.lower() == 'n':
                    break

class Record:
    """contains objects of student and subject class as student record"""
    
    def __init__(self, name:str = '', roll: int = 0, subjects: list = None, credit_hours: list = None, grade_points: list = None):
        """Contains students info related to student"""
        self.student = Student(name, roll)
        self.subject = Subject(subjects, credit_hours, grade_points)