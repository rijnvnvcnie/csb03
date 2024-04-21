# phan 1
# 1.
# a = input("fist name: ")
# b = input("last name: ")
# print("Your full name is", a+" "+b)

#2.
# a = input("your school: ")
# print(a.upper())

#3.
# a = int(input("number: "))
# print( a**2 )

#4.
# from turtle import *
# pen
# shape(circle(100))
# mainloop()

#phan 2
#1.
# for i in range(3, 13):
#     print(i)

#2.
# a = int(input("number: "))
# for i in range(a+1):
#     print(i)

#3.
# a = int(input("number: "))
# b = 0
# while b < a+1:
#     if b%2 != 0:
#         print(b)
#     b += 1   

#phan 3
#1
# a = int(input("Input a number: "))
# if a < 13:
#     print("nho hon 13")
# elif a == 13:
#     print("bang 13")
# else:
#     print("lon hon 13")

#2.
# a = int(input("Input a number: "))
# if a%2 == 0:
#     print(a, "la so chan")
# else:
#     print(a, "la so le")

#3
# a = int(input("Input a month: "))
# if a == 1 or 3 or 5 or 7 or 8 or 10 or 12:
#     print("This month has 31 days")
# elif a == 2:
#     print("This month has 28 or 29 days")
# elif a == 4 or 6 or 9 or 11:
#      print("This month has 31 days")
# else:
#     print("It is not a month")

#phan 4
#1 and 2 and 3.
a = input("Username: ")
b = input("Password: ")
e = input("Email: ")
if "@" in e:
 if "." in e:
  if len(e) >= 8:
   print("Registered successfully.")
   c = input("Username: ")
   d = input("Password: ")
   f = input("Email: ")
   if b != d:
      print("Passwords not match. Please input again")
      print(d = input("Repeat password:"))
      if a == c and b==d and e == f:
       print("You are logged in, admin.")
      else:
       print("Wrong username or email.")
   else:
    print("Invalid password. Please input again.")
  else:
     print("Wrong username or email.")
 else:
   print("Invalid password. Please input again.")
else:
   print("Invalid password. Please input again.")
 
 
