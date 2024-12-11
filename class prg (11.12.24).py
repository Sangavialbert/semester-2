#public variable (id)
class Student:
    id=123
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)
s=Student("Ria")
s.display()
print(s.id)



#private variable (__id)
class Student:
    __id=123
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)
s=Student("Ria")
s.display()
print(s.id)




#getting input from user
class Student:
    id=int(input())
    def _init_(self,name):
        self.__name=name
    def display(self):
        print("Name:",self.__name)
NAME=input()
s=Student(NAME)
s.display()
print(s.id)




#how to access private variables,syntax-(object_classname_varaible)
class Employee:
    def __init__(slef,name,salary):
        self.name=name
        self.__salary=salary
emp=Employee('Jessica',10000)
print('Name:',emp.name)
print('Salary:',emp._Employee__salary)















        
