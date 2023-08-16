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


class Employee:
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
e1.show()
