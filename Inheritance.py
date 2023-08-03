class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id



    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")

class SoftwareDeveloper(Employee):
    def showWork(self):
        print("The Software developer developed the product")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Rahul", 412)
e2.showDetails()
e2.showLanguage()
e3 =SoftwareDeveloper("Ram", 420)
e3.showDetails()
e3.showWork()
