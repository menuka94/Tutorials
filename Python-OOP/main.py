class Employee:
    name = "Ben"
    designation = "Sales Execution"
    salesMadeThisWeek = 6

    def has_achieved_target(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")


employeeOne = Employee()
print(employeeOne.name)
print(employeeOne.hasAchievedTarget())
