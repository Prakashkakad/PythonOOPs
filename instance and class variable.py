class Students:
    School_Name = "Stanford University" #Class Variable
    def __init__(self,name):
        self.name = name #Instance Variable
        self.fees = 75000  #Instance Variable
    def ShowDetails(self):
        print(f"The name of student is {self.name}.He is studying in {self.School_Name} and fees are {self.fees} ")

std1 = Students("pratik")
std1.fees = 175000
std1.ShowDetails()

student_2 = Students("Prakash")
student_2.fees =270000
student_2.ShowDetails()