"""Simple Loops"""
fruits = ['pomme', 34, 'orange']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# for fruit in fruits:
#     print(fruit)

"""List comprehension"""
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
# print (S, V, M, sep="\n")
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
# [0, 4, 16, 36, 64]

"""Dictionnary"""
ls_dict = [{"name":"poppo","age":34}, {"name":"dadada","age":24}]
# print(ls_dict[1])
# print(ls_dict[1]["name"])

"""List manipulation"""
contact = ["Vanessa", "Hugo", "Michael"]
count = len(contact)
last_one = contact[len(contact)-1]
last_one_alt = contact[-1]
# print(last_one)

contact = ["Vanessa", "Hugo", "Michael"]
contact.insert(0,"Jules")
contact.append("Marion")
# print(contact)

contact = ["Vanessa", "Hugo", "Michael", "Léo"]
# contact.pop(len(contact)-1) # delete last element
# contact.pop(0) # delete first element
contact.pop(-2)
print(contact)