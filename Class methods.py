# class Employee:
#     company = "WOWinfotech"
#     def show(self):
#         print(f"The name is {self.name}and Company name is {self.company}")
#
#     @classmethod
#     def Changecompany(cls,newCompany):
#         cls.company = newCompany
#
# e1= Employee()
# e1 = "Prakash"
# e1.show()
# e1.Changecompany("ESDS")
# e1.show()


'''class Employee:
    company = "WOWinfotech"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name} and Company name is {self.company}")

    @classmethod
    def changecompany(cls, newcompany):
        cls.company = newcompany


e1 = Employee("Prakash")
e1.show()
e1.changecompany("ESDS")
e1.show()'''

class  Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1 = Employee("Prakash",15000)
print(e1.name)
print(e1.salary)

string = "sahil-18000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)




