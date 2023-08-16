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
with open('data.txt') as file:
    while (chunk := file.read(10000)):
        print(chunk, end='')

