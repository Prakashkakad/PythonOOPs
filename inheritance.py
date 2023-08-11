class Employees:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetaiis(self):
        print(f"The name of Employee {self.id} is {self.name}")
class progmmer(Employees):
    def showlangauge(self):
        print (f" The default  Language is Python")


class company(progmmer):
    def tellcompany(self):
        print(f"The name of company I work is Wowinfoteach")



e1 = company("Pratik Gunjal", 791)
e1.showDetaiis()
e1.showlangauge()
e1.tellcompany()
# e2 = progmmer("Harry Bro",729 )
# e2.showDetaiis()
# e2.showlangauge()

