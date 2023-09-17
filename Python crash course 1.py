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

for word, meaning in glossary.items():
    print(f"{word}:")
    print(meaning + "\n")
