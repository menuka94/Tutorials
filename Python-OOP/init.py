class Student:
    def __init__(self, name):
        self.name = name

    def display_student_details(self):
        print(self.name)


ron = Student("Ron")
hermione = Student("Hermione")

ron.display_student_details()
hermione.display_student_details()
