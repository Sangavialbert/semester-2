class Company:
    def Company_info(self):
        print("ABC Company")

class Employee1(Company):
    def employee1_info(self):
        print("Name:Gokul   Salary:50,000    Batchno:123")

class Employee2(Company):
    def employee2_info(self):
        print("Name:Lavanya    Salary:55,000    Batchno:456")

class display(Employee1,Company):
     def display1(self):
        print("Employee details displayed")

a=display()
a.Company_info()
a.employee1_info()
        
