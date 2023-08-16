# class math:
#     def __init__(self,num):
#         self.num = num
#
#     def addtonum(selfself,n):
#         self.num = self.num +n
#
#     @staticmethod
#     def add(a+b):
#         return a + b
# #
# # print(a.add(7,2))
# result = math.add(1,2)
# print(result)
# -----------------------Error code

###corrected code

class Math:  # Class names are usually capitalized
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):  # Corrected method name
        self.num = self.num + n

    @staticmethod
    def add(a, b):  # Corrected the method signature and indentation
        return a + b

# Create an instance of the Math class
a = Math(5)

# Call the instance method add_to_num
a.add_to_num(3)

# Call the static method add
result = Math.add(7, 2)
print(result)
