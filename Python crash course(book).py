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


# Exercise 2-3
person_name = "Prakash kakad"
message = (f"Hello {person_name},would you like to learn some Python today?")
print(message)

# Exercise 3-4
'''2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.'''
person_name = "Prakash Kakad"
print("Lowercase:", person_name.lower())
print("Uppercase:", person_name.upper())
print("titlecase:", person_name.title())


'''2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the
following, including the quotation marks:'''

person_name = "Albert Einstein"
print(f"{person_name} once said, “A person who never made a mistake never tried anything new.”")



''' 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.'''

famous_person = "Prakash kakad"
message = print(f"Life is very Baeutiful just see it properly & take a feel of It,Wrote By {famous_person}")
print(message)


'''2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each
 character combination, "\t" and "\n", at least once.Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),rstrip(), and strip().'''

person_name = "                               Prakash"
print(person_name)
p1 =person_name.lstrip()
print(p1)

p2 =person_name.rstrip()
print(p2)

p3 =person_name.strip()
print(p3)

