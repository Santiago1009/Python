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
        self.student = Student(name, age, tuition, career)

    def display_info(self):
        """Display info from the student class"""
        print("Student name: ", self.student.name)
