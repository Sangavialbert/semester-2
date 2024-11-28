#QUESTION 1

rahman=Student('Rahman')
rahman.show()
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter ID")
        self.name=input("Enter the name")
        self.salary=int(input("Enter the salary"))
    def displayEmployeeInf(self):
        print("ID={self.id}\n Name={self.name} \nSalary={self.salary}")
    def getSalary(self):
        return self.salary
class Perks(Employee):
    def calculateSalary(self):
        self.sal=getSalary()
        self.basic=sal*70/100
        self.basic=sal*70/100
        self.hra=sal*15/100
        self.da=sal*14/100
        self.total=self.basic+self.hra+self.da
    def displayPerks(self):
        self.displayEmployeeInfo()
        print("Perks=",self.getSalary()+self.total)


p=Perks()
p.calculateSalary()
p.dispalyPerks()


#QUESTION 2

class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount

    def show(self):
        print("ID:",self.prodId)
        print("Name:",self.prodName)
        print("Count:",self.prodCount)
display=Inventory(101,"Mobile",10)
display.show()


#QUESTION 3

class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
class Display(Inventory):
    def show(self):
        print("ID:",self.prodId)
        print("Name:",self.prodName)
        print("Count:",self.prodCount)
display=Display(101,"Mobile",10)
display.show()














p
