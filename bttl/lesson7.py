# f = open("c:/Users/ntmtr/OneDrive/Desktop/jsp03/bttl/names.txt","r")
# print(f.read())

# f = open("bttl/ten_ban.txt")
# f.write("nguyen van a")
# f.write("10a ")
# f.write("le quy don")
# print(f.write())

import os
f = open("c:/Users/ntmtr/OneDrive/Desktop/jsp03/bttl/names.txt","r")


a = input("ten: ")
if os.path.exists("bttl/names.txt"):
    print('file exists')
else:
    print("file does not exist")