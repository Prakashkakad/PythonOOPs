# class student:
#     def __init__(self):
#         self.__name = "Harry"
#
# a = student()
# print(a.name)

class student:
    def __init__(self):
        self.__name = "Harry"

a = student()
print(a._student__name)  # This will print "Harry"


print(a.__dir__())





