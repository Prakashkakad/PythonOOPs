# Save each of the following exercises as a separate file with a name like
# name_cases.py. If you get stuck, take a break or see the suggestions in
# Appendix C.
# 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”
# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message.
# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

#
# # Exercise 2-3
# person_name = "Prakash kakad"
# message = (f"Hello {person_name},would you like to learn some Python today?")
# print(message)
#
# # Exercise 3-4
# '''2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.'''
# person_name = "Prakash Kakad"
# print("Lowercase:", person_name.lower())
# print("Uppercase:", person_name.upper())
# print("titlecase:", person_name.title())
#
#
# '''2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the
# following, including the quotation marks:'''
#
# person_name = "Albert Einstein"
# print(f"{person_name} once said, “A person who never made a mistake never tried anything new.”")
#
#
#
# ''' 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message.'''
#
# famous_person = "Prakash kakad"
# message = print(f"Life is very Baeutiful just see it properly & take a feel of It,Wrote By {famous_person}")
# print(message)
#
#
# '''2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each
#  character combination, "\t" and "\n", at least once.Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),rstrip(), and strip().'''
#
# person_name = "                               Prakash"
# print(person_name)
# p1 =person_name.lstrip()
# print(p1)
#
# p2 =person_name.rstrip()
# print(p2)
#
# p3 =person_name.strip()
# print(p3)
#
# '''2-8. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print statements to see the results. You should create four lines that look
# like this:
# print(5 + 3)'''
#
# print(24/3)
# print(9-1)
# print(4*2)
# print(6+2)
#
#
# '''2-9. Favorite Number: Store your favorite number in a variable. Then, using
# that variable, create a message that reveals your favorite number. Print that
# message'''
#
# fav_num = (19)
# message = (f"My favorite number is {fav_num}.Because It's my Birthdate.")
# print(message)
# '''
# '''3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time'''
# names = ["om","Karan","Tejas","Nitin","Mayur"]
# #
# # for Names in names:
# #     print(Names)
# '''
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
# person’s name.
# for friends in names:
#     print(f"Here List of My Best Friends {friends}")
#
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
# '''
# for items in names:
#     print(f"My Friends Are All Present All {items}")



# Exercise 3-4: Guest List

# Create a list of guests to invite to dinner
# guests = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie"]
#
# # Print invitation messages to each person
# for guest in guests:
#     print(f"Dear {guest},\nYou are invited to dinner at my place. Please join us for a great evening!\n")
#
# # Print a message indicating one guest can't make it
# print(f"{guests[1]} can't make it to the dinner.\n")
#
# # Replace the guest who can't make it with a new person
# guests[1] = "Isaac Newton"
#
# # Print invitation messages to the updated guest list
# for guest in guests:
#     print(f"Dear {guest},\nYou are invited to dinner at my place. Please join us for a great evening!\n")

# '''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.'''
#
# Friends = ["Om","Karan","Tejas"]
# # for friend in Friends:
# #     print(f"Hi {friend}, \n would you like come for dinner at my home.\n ")
#
#
# '''3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.'''
# print(f"{Friends[2]} will not  able to have dinner due to health issue")
#
# Friends[2]=("Mayur")
#
# print(Friends)
#
#
# for friends in Friends:
#     print(f"{friends} welcome to my party or dinner")
#
#
#
# '''3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.'''
#
#
# Friends.insert(3,"yash")
# print(Friends)
# Friends.insert(2,"Aditya")
# print(Friends)
#
# Friends.append("Abishek")
# print(Friends)
# for friends in Friends:
#     print(f"Hi {friends}, \n Please come to Party {friends}. \n")
#
# '''3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.'''
#
# print(Friends)
# no_dinner = Friends.pop()
# print(Friends)
# no_dinner = Friends.pop()
# print(Friends)
# no_dinner = Friends.pop(2)
# print(Friends)
# no_dinner = Friends.pop(1)
# print(Friends)
#
# Friends.remove("Om")
# print(Friends)
#
# Friends.pop()
# print(Friends)

'''3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its
order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.'''
# import squares as squares

# places = ["Taj Mahal","Raj Mahal","Great Wall of China"]
#
# print(sorted(places))
# places.reverse()
# print(places)
# places.sort()
# print(places)
# print(len(places))

# '''
# '''Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!'''
# # Define a list of favorite pizzas
# favorite_pizzas = ["Pepperoni", "Margherita", "Supreme"]
#
# # Use a for loop to print the name of each pizza
# print("My favorite pizzas:")
# for pizza in favorite_pizzas:
#     print(pizza)
#
# # Modify the for loop to print a sentence using the name of the pizza
# print("\nMy favorite pizzas with statements:")
# for pizza in favorite_pizzas:
#     print("I like " + pizza + " pizza.")
#
# # Add a line at the end to express your love for pizza
# print("\nI really love pizza!")
#
#
# '''. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
# '''
#
# # Define a list of animals with a common characteristic
# animals = ["Dog", "Cat", "Rabbit"]
#
# # Use a for loop to print the name of each animal
# print("Common characteristic: These animals can be great pets.")
# print("List of animals:")
# for animal in animals:
#     print(animal)
#
# # Modify the for loop to print a statement about each animal
# print("\nStatements about each animal:")
# for animal in animals:
#     print("A " + animal.lower() + " would make a great pet.")
#
# # Add a line at the end to state what these animals have in common
# print("\nAny of these animals would make a great pet!")

# for value in range(1,6):
#  print(value)

# numbers = list(range(1, 6))
# print(numbers)
#
# even_numbers = list(range(2,21 ,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#      squares.append(value**2)
# print(squares)
#
#
# print(min(squares))
# print(max(squares))
# print(sum(squares))
#
# squares = [value**2 for value in range(1,11)]
# print(squares)
#

'''Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
inclusive.'''
#
# for number in (range(1,21)):
#      print(number)

'''4-4. One Million: Make a list of the numbers from one to one million, and then 
use a for loop to print the numbers. (If the output is taking too long, stop it by 
pressing ctrl-C or by closing the output window.)
'''

# for number in (range(1,1000001)):
#       print(number)

'''4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python can 
add a million numbers.'''


# number = (list(range(1,1000001)))
# print("Maximum:", max(number))
# print("Minium:", min(number))
# print("Sum :",sum(number))

'''4-6. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20. Use a for loop to print each number.'''
# for number in range(1,21,2):
#      print(number)


'''4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
print the numbers in your list.'''

# for  number in range(3,31):
#      value = number * 3
#      print(value)

'''4-8. Cubes: A number raised to the third power is called a cube. For example, 
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
is, the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube.'''
# for number in range(1,11):
#      value = number**3
#      print(value)

'''4-10. Slices: Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:
•	 Print the message, The first three items in the list are:. Then use a slice to 
print the first three items from that program’s list.
•	 Print the message, Three items from the middle of the list are:. Use a slice 
to print three items from the middle of the list.
•	 Print the message, The last three items in the list are:. Use a slice to print 
the last three items in the list.'''

# Friends = ["OM","Karan","Tejas","Mayur","Nitin","abhishek","Akash"]
# print(f"First Three Element of the List is:{Friends[:3]}")
#
# print(f"Three items from Middle is:{Friends[2:5]}")
# print(f"Last Three Element of the list is {Friends[4:7]}")

'''My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list. Print the message, 
My friend’s favorite pizzas are:, and then use a for loop to print the  list. Make sure each new pizza is stored in the appropriate list.'''

# # Start with your program from Exercise 4-1
# pizzas = ['Margherita', 'Pepperoni', 'Hawaiian']
#
# # Make a copy of the list of pizzas and call it friend_pizzas
# friend_pizzas = pizzas.copy()
#
# # Add a new pizza to the original list
# pizzas.append('BBQ Chicken')
#
# # Add a different pizza to the list friend_pizzas
# friend_pizzas.append('Vegetarian')
#
# # Prove that you have two separate lists
# print("My favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza)
#
# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza)
#
# version_number = 1  # Replace with the desired version number
#
#
#
# # List of foods
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["carrot", "broccoli", "spinach"]
# meats = ["chicken", "beef", "pork"]
#
# # First for loop to print fruits
# print("Fruits:")
# for fruit in fruits:
#     print(fruit)
#
# # Second for loop to print vegetables
# print("Vegetables:")
# for vegetable in vegetables:
#     print(vegetable)
#
# # Third for loop to print meats
# print("Meats:")
# for meat in meats:
#     print(meat)

''' Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the 
change.
•	 The restaurant changes its menu, replacing two of the items with different 
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
'''
# food = ("chicken","meat","pig","wild-pig")

# for items in food:
#     print(f"These are items {items} in restaurant")

# food = ("Missial","pav","'go ha n'")
# for items in food:
#     print(f"These are items {items} in restaurant")

'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•	 Look closely at your results, and make sure you understand why each line 
evaluates to True or False.
•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another 
5 tests evaluate to False.'''

# Test 1: Equality test - True
'''num1 = 5
num2 = 5
print("Is num1 == num2? I predict True.")
print(num1 == num2)

# Test 2: Equality test - False
num1 = 3
num2 = 4
print("Is num1 ==  num2? I perdict False")
print(num1 == num2)

# Test 3:InEquality test -True
Pari1 = 324
pari2 = 300
print("Is Pari1 != Pari2? I perdict True")
print(Pari1 != pari2)'''
# Test 4:InEquality Test -False
'''Prakash = ("Mango")
Pratik  = ("Mango")
print("Is Prakash != Pratik? I Perdict False")
print (Prakash == Pratik)'''

# Test 5 : Less than Test -True
'''Prakash = 20
Pratik  = 22
print("Is Prakash <= Pratik ? I Perdict True ")
print (Prakash <= Pratik)'''

# Test 6 :Greater than test  - False
'''Prakash = 25000
Pratik = 19000
print("Is Prakash <= Pratik ? I Perdict False")
print(Prakash < Pratik)
'''

'''5-2. More Conditional Tests: You dont have to limit the number of tests you 
create to 10. If you want to try more comparisons, write more tests and add 
them to conditional_tests.py. Have at least one True and one False result for 
each of the following:
•	 Tests for equality and inequality with strings
•	 Tests using the lower() function
•	 Numerical tests involving equality and inequality, greater than and 
less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list'''

# Tests for equality and inequality with strings
'''name1 = 'Alice'
name2 = 'Bob'
print("\nIs name1 == name2? I predict False.")
print(name1 == name2)

city1 = 'New York'
city2 = 'new york'
print("\nIs city1 == city2 (case-insensitive)? I predict True.")
print(city1.lower() == city2.lower())

# Numerical tests
num1 = 10
num2 = 20
print("\nIs num1 > num2? I predict False.")
print(num1 > num2)

num3 = 15
num4 = 15
print("\nIs num3 >= num4? I predict True.")
print(num3 >= num4)

num5 = 30
num6 = 25
print("\nIs num5 < num6? I predict False.")
print(num5 < num6)

'''
'''age = 19
if age >= 18:
    print("You are old enough to vote!")
'''