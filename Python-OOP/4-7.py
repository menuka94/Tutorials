class Employee:
    # class attribute
    number_of_working_hours = 40


employeeOne = Employee()
employeeTwo = Employee()
print(employeeOne.number_of_working_hours)  # prints 40
print(employeeTwo.number_of_working_hours)  # prints 40

Employee.number_of_working_hours = 45
print(employeeOne.number_of_working_hours)  # prints 45
print(employeeTwo.number_of_working_hours)  # prints 45

employeeOne.name = "John"
print(employeeOne.name)  # prints John
print(employeeTwo.name)  # throws error: AttributeError: 'Employee' object has no attribute 'name'

employeeOne.number_of_working_hours = 40
print(employeeOne.number_of_working_hours)  # prints 40
print(employeeTwo.number_of_working_hours)  # prints 45

# python first checks instance attributes, then class attributes
