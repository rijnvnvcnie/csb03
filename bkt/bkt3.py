# 1.1
# so = int(input("nhap so: "))

# def tinh():
#     if so%2 == 0:
#      return True
#     else:
#      return False
# if tinh():
#   print("la so chan")
# else:
#   print("la so le")

# 1.2
# so = int(input("ban kinh: "))
# def cal_area():
#     dt = 3.14*so**2
#     print("dien tich hinh tron: ",dt)
# cal_area()

# 1.3,1.4
# ki_tu = str(input("dao nguoc: "))
# def reverse_str():
#     txt = ki_tu[::-1]
#     if ki_tu == txt:
#         print("This is a palindrome.")
#     else:
#         print(txt)
# reverse_str()

#2.1
# so = int(input("nhap so: "))
# def giaithua():
#     a = 1
#     b = 0
#     while b < so:
#      b += 1
#      a = a*b
#     print(a)
# giaithua()

# 2.2
# so = (input("nhap so: ").split(" "))
# def bedenlon(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     print(so)

# bedenlon(so)

# 2.3
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


#3.1
# so = int(input("nhap so: "))
# a=so-17
# def tinh17():
#     if so < 17:
#         c = a*2
#         print(c)
#     else:
#         b = abs(a)
#         print(b)
# tinh17()