'''x = {1,2,3}
print(dir(x))
print(x.__init__())'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = person("sahil" ,19)
print(p.__dict__)

print(help(person))