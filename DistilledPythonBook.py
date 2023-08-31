# principal: int = 1000  # Initial amount
# rate = 0.05            # Interest rate
# numyears = 5           # Number of years
# year = 1
#
# while year <= numyears:
#     principal = principal * (1 + rate)
#     print(year, principal)
#     year += 1
#
#
# print(f'{year:>3d} {principal:0.2f}')
# suffix =input("Please Enter file name")
# if suffix == '.htm':
#     content = 'text/html'
# elif suffix == '.jpg':
#     content = 'image/jpeg'
#
# elif suffix == '.png':
#     content = 'image/png'
# else:
#     raise RuntimeError(f'Unknown content type {suffix!r}')
#
# x = 0
# while (x := x + 1) < 10: # Prints 1, 2, 3, ..., 9
#     print(x)

# x = 0
# while x < 10:
#     if x == 5:
#         break # Stops the loop. Moves to Done below
#         print(x)
#     x += 1
#     print('Done')


# x = 0
# while x < 10:
#     x += 1
#     if x == 5:
#         continue  # Skips the remaining code in this iteration and proceeds to the next iteration.
#     print(x)
# print('Done')

# print('''Content-type: text/html
# <h1> Hello World </h1>
# Click <a href="http://www.python.org">here</a>.
# ''')
#
# print(
# 'Content-type: text/html\n'
# '\n'
# '<h1> Hello World </h1>\n'
# 'Clock <a href="http://www.python.org">here</a>\n'
# )
# with open('data.txt') as file:
#     for line in file:
#         print(line, end='')

# file = open('data.txt')
# for line in file:
#     print(line, end='HELLO') # end='' omits the extra newline
# file.close()
# with open('data.txt') as file:
#     while (chunk := file.read(10)):
#         print(chunk, end='')

#
# names = [ 'Dawan', 'Paul', 'Tara', 'Prakash' ]
# # print(names)
# #
# a = names[-1]
# print(a)
#
# a = names.append("sham")
# print (names)
# names[2] ='Pratik'
# print(names)
# a = names.insert(1,'pranav')
# print(names)
#
# for name in names:
#     print(name)
#
#
# letter = list('Prakash')
# print(letter)
#
#
# family = ["Prakash"["Pratik",["Mom"]]]
# print(family)
#
# a = [1, 'Dave', 3.14, ['Mark', 7, 9, [100, 101]], 10]
# print(a)

# import sys
# if len(sys.argv) != 2:
#         raise SystemExit(f'Usage: {sys.argv[0]} filename')
# rows = []
# with open(sys.argv[1], 'rt') as file:
#     for line in file:
#         rows.append(line.split(','))
# # rows is a list of this form
# # [
# # ['SYM', '123', '456.78']
# # ...
# # ]
# total = sum([ int(row[1]) * float(row[2]) for row in rows ])
# print(f'Total cost: {total:0.2f}')
#  Tuple---------------------------------------------
# opertion =tuple(aa,50,91.02)
#
# print(opertion[1])
# names1 = { 'IBM', 'MSFT', 'AA' }
# names2 = set(['IBM', 'MSFT', 'HPE', 'IBM', 'CAT'])
# # print(names2)
# # print(names1)
#
# # a = names1 | names2
# # print(a)
#
# # b = names1 &                            names2
# # print(b)
# #
# # c= names1 - names2
# # print(c)
# #
# #
# # d = names1 ^ names2
# # print (d)
#
# names1.add('DIS')
# print(names1)
#
# names1.update({'Prakash','Pratik','sahil','sohiel','saurabh','vishal'})
# print(names1)
#
# names1.remove('sahil')
# print(names1)
#
# names1.discard('sahiel')
# print(names1)

'''----------------------------------------------------------Dictionary------------------------------------------'''
'''s = {
'name' : 'GOOG',
'shares' : 100,
'price' : 490.10
}

name = s['name']
cost = s['shares'] * s['price']

print(name)
print(cost)

'''#_____________________________________________________ #Iteration in python  _______________________#

message = 'Hello World'
# Print out the individual characters in message
for c in message:
    print(c)

names = ("Prakash" ,"SahiL","Pratik")
for name in names:
    print(name)


# prices = { 'GOOG' : 490.10, 'IBM' : 91.50, 'AAPL' : 123.15 }
# # Print out all of the members of a dictionary
# for key in prices:
#     print(key, '=', prices[key])


# Print all of the lines in a file
# with open('foo.txt') as file:
#     for line in file:
#         print(line, end='')

 #
 # portfolio = []
 # with open ('portfolio') as file:
 #     for line in file:
 #         row = line.split(',')
 #         try:
 #             name = row[0]
 #             shares = int(row[1])
 #             price = float(row[2])
 #         except ValueError as err:
 #             print('Bad row',row)
 #             print('Reason',err)

 Magic