# studen = ['bach','khoa','khoi','ngoc','huy','tai']
# number = [1,2,4,6,8,10]
# studen.remove('huy')
# studen.pop(4)
# del studen[5]
# studen.clear()
# i = 0
# while i < len(studen):
#   print(studen[i])
#   i += 1
# newlist = studen + number
# print(newlist)
# mytuples = ('hieu','lam','ngoc','khoa')

# mylist = list(mytuples)

# myList = list(input("an gi").split(","))
# for i in myList:
#      print(i)
# a = input("bỏ món ăn nào: ")
# myList.remove(a)
# for i in myList:
#      print(i)

input_str = input("Nhap vao cac so cua list: ")
user_list = input_str.split()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

def totalNums(x):
    sum = 0
    for i in x:
        sum += i
    return sum

print(totalNums(user_list))