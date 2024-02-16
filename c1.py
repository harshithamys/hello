C1
import random

class Employee:
    def __init__(self, name, place, department):
        self.EID = self.EID()
        self.name = name
        self.place = place
        self.department = department

    def EID(self):
        EID = random.randint(1000, 9999)
        return EID

    def display(self):
        print(self.EID, self.name, self.place, self.department)

n = int(input('Enter number of employees: '))
e = []

for i in range(n):
    name = input('Enter name: ')
    place = input('Enter place: ')
    department = input('Enter department: ')
    emp = Employee(name, place, department)
    e.append(emp)

for emp in e:
    emp.display()