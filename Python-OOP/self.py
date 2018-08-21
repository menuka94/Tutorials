class Employee:
    def employee_details(self):
        self.name = "Harry"
        print("Name =", self.name)
        age = 30
        print("Age =", age)

    def print_employee_details(self):
        print("method 2")
        print("Name:", self.name)
        print("Age:", age)  # throws error


employee = Employee()

employee.employee_details()
employee.print_employee_details()
# the python interpreter converts this line into
# Employee.employee_details(employee)
