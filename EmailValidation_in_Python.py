
# email=input("Enter Your Email :")#g@g.in
# k,j,d=0,0,0
# if len(email) >=6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@")==1):
#             if (email[-4]==".") ^ (email[-3]=="."):
#                 for i in email:
#                     if i==i.isspace():
#                         k=1
#                     elif i.isalpha():
#                         if i ==i.upper():  #w-- W==W
#                             j==1
#                         elif i.isdigit():
#                             continue
#                         elif i == "_"or i=="." or i=="@":
#                             continue
#                         else:
#                             d=1
#                 if k==1 or j==1 or d==1:
#                     print("Wrong Email Due to Lower and Upper case")
#             else:
#                 print("Wrong Email Due to (.)")
#         else:
#             print("Wrong Email due Symbol related to @ ")
#     else:
#         print("Wrong Email due to character is not proper")
# else:
#     print("Wrong Email ")
#
# email = input("Enter Your Email: ")  # Example: g@g.in
# k, j, d = 0, 0, 0
#
# if len(email) >= 6:
#     if email[0].isalpha():
#         if "@" in email and email.count("@") == 1:
#             if email[-4] == "." or email[-3] == ".":
#                 for i in email:
#                     if i.isspace():
#                         k = 1
#                     elif i.isalpha():
#                         if i == i.upper():
#                             j = 1
#                         elif i.isdigit():
#                             continue
#                         elif i == "_" or i == "." or i == "@":
#                             continue
#                         else:
#                             d = 1
#                 if k == 1 or j == 1 or d == 1:
#                     print("Wrong Email Due to Lower and Upper case")
#             else:
#                 print("Wrong Email Due to (.)")
#         else:
#             print("Wrong Email due Symbol related to @")


email = input("Enter Your Email: ")  # Example: prakashkakad812@gmail.com
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if email[-4] == "." or email[-3] == ".":
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 0 or d == 1:
                    print("Wrong Email Due to Lower and Upper case")
                else:
                    print("Valid Email")
            else:
                print("Wrong Email Due to (.)")
        else:
            print("Wrong Email due Symbol related to @")
    else:
        print("Wrong Email Due to starting with a non-alphabetic character")
else:
    print("Wrong Email due to length less than 6 characters")
