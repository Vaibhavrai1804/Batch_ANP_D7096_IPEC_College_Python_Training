class Employee:
    #member variable i.e class varibale 
    company='XYZ'

    #Instance method
    def display(self):
        self.company="ABC"
        print("Company Name:",self.company)
        print("Company Name:",Employee.company)
emp=Employee()
emp.display()