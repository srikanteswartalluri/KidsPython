"""
Task1:
1. take your name as input
2. find the length of your name
3. print the length
ex: John
length is : 4
"""
#
# name = input("Enter your name: ")
# age = 10
# print(type(age))
# print(name)
# print(type(name))
#
# length = len(name)
# print("Length of my name is {}".format(length))
#


"""
Task2:
1. take two names as input
2. Print the longer name
ex: Name1: Tarun
Name2: Srikanteswararao
Srikanteswararao is longer
"""
#
# name1 = input("Enter name1: ")
# name2 = input("Enter name2: ")
#
# length1 = len(name1)
# length2 = len(name2)
#
# if length1 > length2:
#     print("{} is longer".format(name1))
# else:
#     print("{} is longer".format(name2))



"""
Task3:
1. take three names as input
2. Print the longest name
ex: Name1: Tarun
Name2: Srikanteswararao
Name3: Siddu
Srikanteswararao is the longest
"""

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")
name3 = input("Enter name3: ")

length1 = len(name1)
length2 = len(name2)
length3 = len(name3)

if length1 > length2:
    if length1 > length3:
        print("{} is the longest".format(name1))
elif length2 > length3:
    print("{} is the longest".format(name2))
else:
    print("{} is the longest".format(name3))
