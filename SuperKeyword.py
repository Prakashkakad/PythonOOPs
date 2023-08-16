class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Progrommer:
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang


Pratik  = Employee("Pratik kakad","123")
Prakash = Progrommer("Prakash",133,"Python")