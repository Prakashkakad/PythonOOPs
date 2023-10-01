'''available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:

    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")'''
'''5-8. Hello Admin: Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user 
after they log in to a website. Loop through the list, and print a greeting to 
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin, 
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.'''

# usernames = ["Prakash","Sahil","admin","Partik","Akash","Rahul"]
# for username in usernames:
#
#     if username.lower() == "admin":
#         print("Hello admin, would you like to see a status report")
#
#     else:
#         print(f"Hello {username}, thank you for logging in again.")


'''No Users: Add an if test to hello_admin.py to make sure the list of users is 
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct 
message is printed.'''

# usernames = []
# for username in usernames:
#
#     if username.lower() == "admin":
#         print("Hello admin, would you like to see a status report")
#
#     else:
#         print(f"We need to find some users!")
# print("Welcome")


# usernames = []  # Empty list of users
#
# # Check if the list of users is empty
# if not usernames:
#     print("We need to find some users!")
# else:
#     for user in usernames:
#         if user == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print("Hello " + user + ", thank you for logging in again.")

'''5-10. Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or 
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already 
been used. If it has, print a message that the person will need to enter a 
new username. If a username has not been used, print a message saying 
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used, 
'JOHN' should not be accepted.
'''
# current_users = ["Prakash","Sahil","admin","Partik","Vice"]
# new_users =["Prakash","Sahil","admins","winner","fighter"]
#
# # Convert all current usernames to lowercase for case-insensitive comparison
# current_users_lower = [user.lower() for user in current_users]
#
# # Check for unique usernames in new_users
# for user in new_users:
#     if user.lower() in current_users_lower:
#         print(f"The username '{user}' is not available. Please choose a new username.")
#     else:
#         print(f"The username '{user}' is available.")

'''5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
7th 8th 9th", and each result should be on a separate line.
'''
# numbers = list(range(1, 10))
#
# for number in numbers:
#     if number == 1:
#         ordinal = str(number) + "st"
#     elif number == 2:
#         ordinal = str(number) + "nd"
#     elif number == 3:
#         ordinal = str(number) + "rd"
#     else:
#         ordinal = str(number) + "th"
#
#     print(ordinal)
'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each 
piece of information stored in your dictionary.'''

# person ={'first_name':'Prakash' ,'last_name':'kakad','age':20,'city':'Nashik'}
# #
# print("Hello,My name is " + person['first_name'] + " "+ person['last_name'] +"and age is "+ str(person['age']) +".He Lives in " + person['city'])

# person = {'first_name': 'Prakash', 'last_name': 'Kakad', 'age': 20, 'city': 'Nashik'}
#
# print("Hello, my name is " + person['first_name'] + " " + person['last_name'] +
#       " and my age is " + str(person['age']) + ". I live in " + person['city'] + ".")

'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program.'''
# friends = {'Prakash' : 19 ,'Sahil' : 5 , 'admin' : 2,'Pratik' : 1,'Vice' :23}
# print("Prakash and his favorite number is" + str(friends['Prakash']),
#       "Sahil and his favorite number is" + str(friends['Sahil']),
#       "admin and his favorite number is" + str(friends['admin']),
#       "Pratik and his favorite number is" + str(friends['Pratik']),
#       "Vice and his favorite number is" + str(friends['Vice'])
#     )

# friends = {'Prakash': 19, 'Sahil': 5, 'admin': 2, 'Pratik': 1, 'Vice': 23}
#
# for username, favorite_number in friends.items():
#     print(f"{username} has a favorite number of {favorite_number}.")

'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output'''

glossary = {
    'Variable': 'A storage location in a program that holds data, which can be changed during the execution of the program.',
    'Function': 'A reusable block of code that performs a specific task when called in a program.',
    'Loop': 'A control structure that allows a set of instructions to be executed repeatedly based on a condition.',
    'List': 'A data structure that holds an ordered collection of elements, which can be of different data types.',
    'Conditional Statement': 'A programming construct that allows you to make decisions in your code based on conditions.'
}

# for word, meaning in glossary.items():
#     print(f"{word}:")
#     print(meaning + "\n")
# fdhg

'''People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person.
'''
# Om = {
#     'Name':'Om Sonwane',
#     'Roll':'23',
#     'Age':'20'
# }
#
# Karan ={
#     'Name':'Karan Borade',
#     'Roll':'19',
#     'Age':'23'
#
# }
#
# friends =[Om,Karan]
# for friend in friends:
#     print("Name:",friend['Name'])
#     print("Age:",friend['Age'])
#     print("Roll no:",friend['Roll'])

'''6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through your list 
and as you do print everything you know about each pet.'''

# cat ={
#     'Name':'Cat',
#     'Owner Name':'Prakash kakad'
#
# }
#
# dog={
#     'Name':'Dog',
#     'Owner Name':'Pratik kakad'
# }
#
# Pets =[cat,dog]
# for Pet in Pets:
#     print("Name of Pet :",Pet['Name'])
#     print("Name of Owner:",Pet['Owner Name'])




'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person. To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places. Loop through the dictionary, and print 
each person’s name and their favorite places.'''
# Create the favorite places dictionary
# favorite_places = {
#     'Alice': ['Paris', 'New York', 'Tokyo'],
#     'Bob': ['London', 'Sydney', 'Barcelona'],
#     'Charlie': ['Rome', 'San Francisco', 'Rio de Janeiro']
# }
#
# # Loop through the dictionary and print each person's name and their favorite places
# for person, places in favorite_places.items():
#     print(f"{person}'s favorite places:")
#     for place in places:
#         print(f"- {place}")
#     print()


'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number. Then print each person’s 
name along with their favorite numbers.'''
# favorite_numbers = {
#     'Alice': [7, 11, 19],
#     'Bob': [3, 8],
#     'Charlie': [42, 13, 5],
#     'David': [2]
# }
#
# for person, numbers in favorite_numbers.items():
#     print(f"{person}'s favorite numbers are: {', '.join(map(str, numbers))}")

'''7-1. Rental Car: Write a program that asks the user what kind of rental car they 
would like. Print a message about that car, such as “Let me see if I can find you 
a Subaru.”'''

# car_choice = input('What kind of rental car would you like? ')
# print(f'Let me see if I can find you a {car_choice}.')

'''7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.'''

# Ask = input("How Many People Are You ???\n:")
# Ask = int(Ask)
#
# if Ask >=8:
#     print("You Should Wait for Table for becoming Empty")
# else:
#     print("You can Have a Sit And Have a Great Dinner")



# try:
#     group_size = int(input("How many people are in your dinner group? "))
#     if group_size > 0:
#         if group_size >= 8:
#             print("I'm sorry, you'll have to wait for a table.")
#         else:
#             print("Your table is ready. Enjoy your meal!")
#     else:
#         print("Please enter a valid positive number.")
# except ValueError:
#     print("Please enter a valid number for the group size.")

# '''7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.'''
#
# number =int(input("Please Enter a Number \n :"))
#
# if (number % 10 == 0):
#     print("Number is Multiple of 10")
# else:
#     print("Number is not Multiple of 10")


# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")


'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza.'''

# print("Enter 'quite' when you have done pizza Topping")
#
# while True:
#     Topping = input("Enter Pizza Toppings:"
#                     )
#
#     if Topping.lower() == "quite":
#         break
#     print(f"Your {Topping} Will Be Added to Pizza.")
# print("Your Pizza is ready")

'''7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket.'''

# while True:
#     try:
#         age = int(input("Enter Your Age:"))
#         if (age < 0) :
#             print("Enter Your Correct Age")
#         if (age == 0):
#             break
#         if ( age < 3):
#             print("the ticket is free")
#
#         elif(3 <= age <= 12):
#             print("the ticket is $10")
#
#         else:
#             print("the ticket is $15")
#
#     except ValueError:
#         print("Please enter a valid age as a number.")
#
#     print("Thank you for using the ticket price calculator!")


'''
. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value'''

# Using a Conditional Test in the While Statement:
# age = -1  # Initialize age to a value that doesn't meet any condition
#
# while age != 0:
#     age = int(input("Enter your age (or type '0' to exit): "))
#
#     if age < 3:
#         print("Your ticket is free.")
#     elif 3 <= age <= 12:
#         print("Your ticket costs $10.")
#     else:
#         print("Your ticket costs $15.")

# Using an Active Variable to Control Loop Duration:
# active = True

# while active:
#     age = int(input("Enter your age (or type '0' to exit): "))
#
#     if age == 0:
#         active = False
#     elif age < 3:
#         print("Your ticket is free.")
#     elif 3 <= age <= 12:
#         print("Your ticket costs $10.")
#     else:
#         print("Your ticket costs $15.")
# Using a Break Statement to Exit the Loop:
# while True:
#     age = int(input("Enter your age (or type '0' to exit): "))
#
#     if age == 0:
#         break
#     elif age < 3:
#         print("Your ticket is free.")
#     elif 3 <= age <= 12:
#         print("Your ticket costs $10.")
#     else:
#         print("Your ticket costs $15.")

'''8-12. Sandwiches: Write a function that accepts a list of items a person wants 
on a sandwich. The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the sandwich that is being ordered.
Call the function three times, using a different number of arguments each time.'''

# Sandwiches_order = ["cheese","butter","saltey","tomato"]
# finish_sandwich =[]
#
# print(input("Which Sandwich Order:"))
#
# for sandwich in Sandwiches_order:
#     print("I made Your " + sandwich +".!!!")
#     finish_sandwich.append(sandwich)
#
# print("/nfinish Sandwiches:")
# for Sandwich in finish_sandwich:
#     print(Sandwich)

''' User Profile: Start with a copy of user_profile.py from page 153. Build 
a profile of yourself by calling build_profile(), using your first and last names 
and three other key-value pairs that describe you.'''
# def build_profile(first_name, last_name, **additional_info):
#     profile = {
#         'first_name': first_name,
#         'last_name': last_name
#     }
#     for key, value in additional_info.items():
#         profile[key] = value
#     return profile
#
# # Build a profile for yourself
# my_profile = build_profile(
#     first_name='YourFirstName',
#     last_name='YourLastName',
#     age=25,
#     location='YourCity',
#     occupation='YourOccupation'
# )

# print(my_profile)


'''7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order, such 
as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches. After all the sandwiches have been made, print a 
message listing each sandwich that was made'''

# Sandwiches_order = ["Ham and Cheese", "Turkey", "Vegetarian", "Roast Beef"]
# Finish_Sandwiches =[]
#
# while Sandwiches_order:
#     current_Snadwich =Sandwiches_order.pop(0)
#     print(f"I made your {current_Snadwich} sandwich.")
#     Finish_Sandwiches.append(current_Snadwich)
#
#     print("\nList of finished sandwiches:")
#     for sandwich in Finish_Sandwiches:
#         print(sandwich)


'''7-10. Dream Vacation: Write a program that polls users about their dream 
vacation. Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll.'''
#
# Dream_Vacation ={}
#
# while True:
#     name =input("what  is your Name")
#     Dream_destination =input("If you could visit one place in the world, where would you go? ")
#
#     Dream_Vacation[name] = Dream_destination
#     another_response = input("Would you like to let another person respond? (yes/no)")
#     if another_response.lower() != 'yes':
#         break
#
#  # Print the results of the poll
# print("\n--- Dream Vacation Poll Results ---")
# for name, destination in Dream_Vacation.items():
#     print(f"{name} dreams of visiting {destination}.")


'''8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
 Call the function, and make sure the message displays correctly.'''

# def display_message():
#
#     print(f"Learn in this Chapter About Function And Arugment ")
#
# display_message()


# def favorite_book(title):
#     print(f"One of my favorite books is {title}.")
#
# # Call the function with a book title
# favorite_book("Alice in Wonderland")

'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print 
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.'''


# def make_shirt(size, message):
#     print(f"Creating a {size} shirt with the message: '{message}'")
#
# # Call the function using positional arguments
# make_shirt("Medium", "Hello, World!")
#
# # Call the function using keyword arguments
# make_shirt(size="Large", message="Python Lover")


'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message.'''

# def make_shirt(size="Large", message="I love Python"):
#     print(f"Creating a {size} shirt with the message: '{message}'")
#
# # Create a large shirt with the default message
# make_shirt()
#
# # Create a medium shirt with the default message
# make_shirt("Medium")
#
# # Create a shirt of any size with a different message
# make_shirt("Small", "Hello, World!")


'''8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value 
that’s returned.'''

# def city_country(country,city):
#     formatted_string=f'{country},{city}'
#     print(formatted_string)
#
#
# # Call the function with at least three city-country pairs
# city1 = city_country("Santiago", "Chile")
# city2 = city_country("Paris", "France")
# city3 = city_country("Tokyo", "Japan")
#
#
# print(city1)
# print(city2)
# print(city3)

'''8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Add an optional parameter to make_album() that allows you to store the 
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. 
Make at least one new 
function call that includes the number of tracks on an album.'''


#
# def make_album(artist,title,tracks=None):
#     album = {"artist":artist,"title":title}
#     if album:
#         album["tracks"]=tracks
#     return album
#
# #create a  different artist
# album1 =make_album("taylor swift","No way out")
# album2 =make_album("Arijit singh","Tere mere kahaani")
# album3 = make_album("Prakash kakad","Study")
#
#
# # Create an album dictionary with specifying number of tracks
# album4 = make_album("Imagine Dragons", "Evolve", 12)
# print(album1)
# print(album2)
# print(album3)
# print(album4)


'''def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

while True:
    print("Enter album information or 'q' to quit.")
    artist = input("Enter artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Enter album title: ")
    if title.lower() == 'q':
        break

    album_info = make_album(artist, title)
    print("Album information:")
    print(album_info)
'''


'''8-9. Magicians: Make a list of magician’s names. Pass the list to a function 
called show_magicians(), which prints the name of each magician in the list.'''

# def show_magicians(magician_names):
#     for magician in magician_names:
#         print(magician)
#
#
# magician_names = ["Prakash Kakad","Pratik Kakad","Sahil Kakad"]
# show_magicians(magician_names)

'''8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to 
see that the list has actually been modified.'''

# def show_magicians(magician_names):
#     for magician in magician_names:
#         print(magician)
#
# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i] = "the Great " + magician_names[i]
#
# # List of magician names
# magician_names_list = ["Prakash Kakad","Pratik Kakad","Sahil Kakad"]
#
# # Call make_great to modify the magician names
# make_great(magician_names_list)
#
# # Call the function to show magicians
# show_magicians(magician_names_list)


'''8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the 
function make_great() with a copy of the list of magicians’ names. Because the 
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original 
names and one list with the Great added to each magician’s name'''

# def show_magicians(magician_names):
#     for magician in magician_names:
#         print(magician)
#
# def make_great(magician_names):
#     modified_magician_names = []
#     for magician in magician_names:
#         modified_magician_names.append("the Great " + magician)
#     return modified_magician_names
#
# # List of magician names
# original_magician_names = ["Prakash ","Pratik","Pranav"]
#
#
# # Create a new list with the updated magician names
# great_magician_names = make_great(original_magician_names[:])  # Passing a copy to keep the original list unchanged
#
# # Call the function to show original magicians
# print("Original Magicians:")
# show_magicians(original_magician_names)
#
# # Call the function to show magicians with "the Great" added
# print("\nMagicians with 'the Great' added:")
# show_magicians(great_magician_names)

'''-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#     def describe_restaurant(self):
#         print(f"Restaurant Name:{self.restaurant_name}")
#         print(f"cuisine type : {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"The restaurant {self.restaurant_name} is now open.")
#     def set_number_served(self,number):
#         self.number_served= number
#
#     def increment_number_served(self,increment):
#         self.number_served +=increment
# # Create an instance of the Restaurant class
# restaurant =  Restaurant("Mirache","chinise")
#
# # Print the individual attributes
# print("Restaurant Name:", restaurant.restaurant_name)
# print("Cuisine Type:", restaurant.cuisine_type)
# #
# # # Call the describe_restaurant() and open_restaurant() methods
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
#
# '''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance'''
#
# # Create three instances of the Restaurant class
# restaurant1 = Restaurant("Restaurant A", "Mexican")
# restaurant2 = Restaurant("Restaurant B", "Chinese")
# restaurant3 = Restaurant("Restaurant C", "Indian")
#
# # Call describe_restaurant() for each instance
# restaurant1.describe_restaurant()
# print()  # Add a newline for separation
# restaurant2.describe_restaurant()
# print()
# restaurant3.describe_restaurant()
#
#
#
# '''9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number you like that could represent
# how many customers were served in, say, a day of business.'''
#
#
#
#
#
# # Create an instance of the Restaurant class
# restaurant = Restaurant("My Restaurant", "Italian")
#
# # Print the initial number of customers served
# print(f"Number of customers served: {restaurant.number_served}")
#
# # Change the value and print it again
# restaurant.number_served = 50
# print(f"Updated number of customers served: {restaurant.number_served}")
#
# # Use the set_number_served method to set the number of customers served
# restaurant.set_number_served(100)
# print(f"Updated number of customers served: {restaurant.number_served}")
#
# # Use the increment_number_served method to increment the number of customers served
# restaurant.increment_number_served(30)
# print(f"Updated number of customers served: {restaurant.number_served}")

'''9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write 
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0.
'''

class User:
    def __init__(self,first_name,last_name,username,email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.login_attempts=0
        self.email=email

    def describe_user(self):
        print(f"Hello my name is {self.first_name} {self.last_name}.")
        print(f"My E-mail id :{self.email} And My Username is :{self.username}")

    def greeting(self):
        print(f"Welcome to party {self.first_name}!!!!!!!!!!!!!!!!!!!!!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts=0


# Create an instance of the User class
user1 = User("John", "Doe", "johndoe", "john@example.com")

# Call increment_login_attempts multiple times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the value of login_attempts
print(f"Login attempts: {user1.login_attempts}")

# Call reset_login_attempts
user1.reset_login_attempts()

# Print the value of login_attempts after resetting
print(f"Login attempts after reset: {user1.login_attempts}")
# In this modified User class, we added the login_attempts attribute to track the number of login attempts.
# We also added the increment_login_attempts() method to increment the login attempts and
# the reset_login_attempts() method to reset the login attempts to 0. We then create an instance of the User class and
# demonstrate the usage of these methods.





