"""Wrapping classes in Python"""

# We need a base class


class Student:
    """Model for student"""

    def __init__(self, name, age, tuition, career) -> None:
        self.name = name
        self.age = age
        self.tuition = tuition
        self.career = career


class StudentWrap(Student):
    """Wrapping class student"""

    def __init__(self, name, age, tuition, career) -> None:
        # It may show a warning for avoiding the super()__init__() method
        self.student = Student(name, age, tuition, career)

    def display_info(self):
        """Display info from the student class"""
        print("Student's name: ", self.student.name)
        print("Student's age: ", self.student.age)
        print("Student's tuition: ", self.student.tuition)
        print("Student's career: ", self.student.career)
