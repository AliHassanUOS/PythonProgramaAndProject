# print("Dictionary in python")
# print()

#
#
# print(dic[2])


#
# print(dic)

# dic = {1: 'ali', 2: 'hassan', 3: 'rubab', 4: 'ahmad'}
#
# print(11 not in dic)

# dic = {1: 'ali', 2: 'hassan', 3: 'rubab', 4: 'ahmad'}
# print(dic)
# print()
# dic.clear()
# print(dic)


# dic = {1: 'ali', 2: 'hassan', 3: 'rubab', 4: 'ahmad'}
#
#
# result=dic.items()
# lst = list(result)
# print(lst)
# print(type(lst))
# print(lst[2][1])

# dic = {1: 'ali', 2: 'hassan', 3: 'rubab', 4: 'ahmad'}
# # # dic [11] = 'aks'
# # # print(dic)
# # # print(dic[1])
# # # result = dic.items()
# # # print(result)
# # print(dic)
# # print()
# # dic.update({11:'new dictionary'})
# # print(dic)


# How to add 3 dictionary

# dic1 = {1: 'ali', 2 :'hassan'}
# dic2 = {3 :' ahmad', 4 : 'adeel'}
#
# dic3 = {}
#
# for i in (dic1, dic2):
#     dic3.update(i)
# print(dic3)
# print(type(dic3))


# print(dic.pop(7))
# print(dic.pop(8))
# print(dic.pop(6))
# print(dic)
#
# print(dic.popitem())
# print(dic.popitem())
# print(dic.popitem())
# print(dic.popitem())
# print(dic)

# dic = {1: 'ali', 2: 'hassan', 3: 'rubab', 4: 'ahmad'}
#
# val = {5 : 'ahmad', 6 : 'kamran', 7 :'adeel', 8 : 'junaid'}
# dic.update(val)
#
# for key in dic:
#     print(key ,dic[key])

# Taking input from user in dictionary
# emptydic = {}
#
# userinput = int(input("Enter values that you want to add in dictionary  :"))
#
# for i in range(userinput):
#     key = input("Enter key :")
#     val = input("Enter values :")
#     emptydic.update({key : val})
# print(emptydic)
#

# dic = {1: 'ali', 2: 'hassan', 3: 'rubab', 4: 'ahmad'}
# dic[5] = 'python'
#
# print(8 not in dic)
# n = int(input("Enter number that you want to enter  :"))
#
# d = dict()
#
# for x in range(1, n+1):
#     d[x] = x*x
#     print(d)
#

# Previousnumber = 0
#
# for i in range(0,10):
#     sum = Previousnumber+i
#     print("Current number is ", i, "Previous Number is ", Previousnumber, "Sum of number is ", sum)
#     Previousnumber=i

# def printEveIndexChar(str):
#   for i in range(0, len(str), 3):
#     print("index[",i,"]", str[i] )
#
# inputStr = "pynative"
# print("Orginal String is ", inputStr)
#
# print("Printing only even index chars")
# printEveIndexChar(inputStr)

list1 = [1,2,3,4,5,6,11,22,100]
list2 = [1,2,3,4,5,6,11,22,100]
if list1[0] == list2[-1]:
    print('True')
else:
    print('False')