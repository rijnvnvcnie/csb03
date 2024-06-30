#1
# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# print( a + b)

#2
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# x1 = (-b + (b**2-4*a*c)**(1/2))/2*a
# x2 = (-b - (b**2-4*a*c)**(1/2))/2*a
# print("x = ",x1," or x = ",x2)

#3
# a = str(input("input a text: "))
# def is_palindrome():
#     txt = a[::-1]
#     if a == txt:
#         print("This is a palindrome.")
#     else:
#         print("This is not a palindrome.")
# is_palindrome()

#4
# bill = []
# def goimon():
#     a = str(input("Please choose a dish: "))
#     if a in bill:
#         print("dish was already chosen")
#     else:
#         bill.append(a)
#     c()
# def c():
#     b = str(input("Chose anything? (y/n): "))
#     if b == "y":
#         goimon()
#     elif b == "n":
#         i = 0
#         while i < len(bill):
#             print(bill[i])
#             i += 1
#     else:
#         print("not understand")
#         c()
# c()

#5
# gia = {
#     "iphone12": 28000000,
#     "samsungn10": 16000000,
#     "oppo93": 7500000,
#     "vsmart":7400000,
#     "vivo": 4200000
# }
# a = str(input("Input name of a phone: "))
# print("Price: ", gia[a])

# tuvan = int(input("Input your budget:"))
# for i in gia:
#     if i >= a:
#         print(gia[i])

#6
# so = input("Input a number: ")
# print(len(so))

#7
# so = [5,1,8,92,-1,30]
# def bedenlon(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     print(so)
# bedenlon(so)

#8
# so = int(input("nhap so: "))
# def print_filbo():
#     num1 = 0
#     num2 = 1
#     next_number = num2 
#     c = 1
#     while  c <= so:
#      print(next_number, end=" ")
#      c += 1
#      num1, num2 = num2, next_number
#      next_number = num1 + num2
#     print()
# print_filbo()