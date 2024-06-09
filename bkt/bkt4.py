# 1)
kho = {
    "hp": 20,
    "dell": 50,
    "macbook": 12,
    "asus": 30
}
# print(kho["macbook"])

# x = str(input("may: "))
# print(kho["x"])

# 2)
#1
# kho["toshiba"]=10
# print(kho)

#2
# a = str(input("ten may: "))
# b = int(input("so may: "))
# kho[a]=b
# print(kho)

#3
# kho["dell"]=60
# kho["macbook"]=2
# print(kho)

#4
# print(kho["asus"]+kho["dell"]+kho["hp"]+kho["macbook"])

#3)1.2.3
gia = {
    "hp": 600,
    "dell": 650,
    "macbook": 1200,
    "asus": 400
}
# print(gia["asus"])
# a = str(input("ten may: "))
# print("gia", gia[a])

#4)
#1.
# print(gia[asus]*5)

#2.
# c = str(input("ten may: "))
# d = int(input("so may: "))
# print(gia[c]*d)

#3.
# kho[c] -= d
# print(kho)

#5)1.2.
tong = {

}
tong["hp"] = kho["hp"]* gia["hp"]
tong["dell"] = kho["dell"]* gia["dell"]
tong["macbook"] = kho["macbook"]* gia["macbook"]
tong["asus"] = kho["asus"]* gia["asus"]
# print(tong)
# print(("tong cong "), tong["hp"] + tong["dell"] + tong["macbook"] + tong["asus"])

#6)1.2.
character = {
     "name":"Light",
     "age":17,
     "strength":8,
     "hp":100,
     "backpack":"shield ,bread_loaf",
     "gold":100,
     "level":2
}
character["gold"] += 50
character["backpack"] += " ,flintstone"
print(character)

#7)1.2.
skill_1 = {
   "name":"Tackle",
   "minimun_level":1,
   "damage":5,
   "hitrate":0.3
}
skill_2 = {
   "name":"Quick_Attack",
   "minimun_level":2,
   "damage":3,
   "hitrate":0.5
}
skill_3 = {
   "name":"Strong_kick",
   "minimun_level":4,
   "damage":9,
   "hitrate":0.2
}
skill_list = [skill_1, skill_2, skill_3]

for x,y,z,t in skill_list:
    print(x,y)