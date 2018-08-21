class Student:
    def student_details(self):
        self.name = "Hermione"

    @staticmethod
    def welcome_message():
        print("Welcome to Hogwarts")


student = Student()
student.student_details()
print(student.name)
student.welcome_message()
