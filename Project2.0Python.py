print("ALLAH is greatest  ")
#
# def RemoveDup(li):
#     emptylist = []
#     for i in li:
#         if i not in emptylist:
#             emptylist.append(i)
#     return emptylist
#
#
# result=RemoveDup(['a', 'b', 'c', 'a', 'b', 'ab', 'ba'])
#
# print(result)

# string1 = "capital first and last letter in string"
#
# fistcapital =string1.title()
# split1 = fistcapital.split()
#
# emptystr = ""
#
# for i in split1:
#
#     emptystr = emptystr+i[:-1]+i[-1].upper() + " "
#
# print(emptystr)

#
# def fun(*args,**kwargs):
#     for i in args:
#         print(i)
#
#     for key, values in kwargs.items():
#         print(key, values)
#
#
#
#
# fun(['ali','hassan','add','everything'])
# fun({1 :'one', 2 : 'two'})
# Find the Factorial in python
#
# num = 4
# init = 1
#
# for i in range(1,num+1):
#     init = init*i
# print(init)
#
# num = int(input("Please enter numbers "))
#
#
# if num > 0 :
#     print("Number is positive  ")
# elif num == 0:
#     print(" number is zero ")
# else:
#     print("Number is negative  ")

# list = [1,0,1,2,3,-2,-23,-234,23,0,29,200]
#
# for i in list:
#     if i > 0:
#         print("only positive number is list  ", i)
#         print()
#     if i < 0 :
#         print("only negative number in list ", i)

# set1 = {1,2,3,4,5,6,7,8,9}
#
# set2 = {1,2,3,4,5,6,7,8,9}
#
# print(set1.difference_update(set2))
# num = [1,2,3,4,5,6,7,8,9,10]
# # n=3
# # newlist = [i for i in num if i%2==0 ]
# #
# # print(newlist)

# add=lambda x  : x +15
#
#
# print(add(10))
#
#
#
# mul = lambda x,y : x*y
#
# print(mul(2,3))


# stri = ['ali','hassan','janab']
#
# print(stri[:-1])


# a=lambda x:x*x
# print(a(5))


# list1 = [-23, -100, 90, -80, 70, -68, -61, 43, 45, 54]
#
# result = list(filter(lambda x: (x < 0), list1))
#
# print(result)
#
# lst1 = [22, 100, 19, 13, 11, 1, 4, 66]
#
# result = list(filter(lambda x: (x % 2 == 0, x % 2 == 1), lst1))
#
# print(result)


# str1="aqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
#
# lst = list(filter(lambda x: True if x.lower() in "aeiou" else False, str1))
# print(lst)

# str1 = "Winter Olympics in 2022 will take place in Beijing China"
#
# lst = list(filter(lambda x: True if x in "0123456789" else False, str1))

# l = list(filter(lambda x: True if x in "0123456789" else False, str1))

# l[2] = 121
# print(l)
# list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# res = list(map(lambda x : x*2, list1))
#
# print(res)


# list1 = [2,2]
# tot = 1
# for i in list1:
#     tot = tot*i
# print(tot)

# kilomters = 10
#
# miles = kilomters*0.621371
#
# print(miles)
#
# miles = 6.21371
#
# kilometers = miles/0.621371
#

#
# lst = [10,123,12,109,90,87,251,111110]


# max = lst[0]
#
#
# for x in lst:
#     if x > max:
#         max = x
# print(max)


# number1 = 11
#
# for i in range(number1) :
#
#     if i%number1== 0:
#         print("Number is not prime")
#         break
#     else:
#         print("prime")
# number = 4
#
# for i in range(2, number):
#     if number % i == 0:
#         print("Number is not prime")
#         break
#     else:
#         print("Number is prime")
#         break
# gi = 122
# sum = 0
#
# while gi >0:
#     sum =sum + int(gi%10)
#     gi = int(gi/10)
#
# print(sum)

# string1 = "121"
#
# a1 = string1[::-1]
#
# if a1==string1:
#     print("number is polidrem")
# else:
#     print('no')

#
# number = 121
# tem = number
#
# remainser = 0
# while number > 0:
#     dig = number%10
#     remainser = remainser*10+dig
#     number = number//10
#
# if remainser==tem:
#     print("Number is polidrim ")
#
# else:
#     print('not')


# list1 = [1, 2, 3,4]
#
# res = 1
#
# for i in list1:
#     res = res*i
# print(res)

# list1 = [12, 232, 13,4,21,312,921,1]
# list1.sort()
# print(list1[0])

# list1 = [12, 232, 13, 4, 21, 312, 921, 1,0,-912]
# min = list1[ 0 ]
#
# for i in list1:
#     if i < min:
#         min = i
# print(min)


# list1 = ['abc', 'xyz', 'aba', '1221','aba','aba']
#
# count = 0
#
#
# for i in list1:
#     if len(i) > 1 and i[0] == i[-1]:
#       count = count+1
# print(count)


# list1 = [1, 2, 3, 12, 3, 41, 1, 3, 4, 22,1,2,3,4,5,5]
#
# duplicate_list = []
#
# for element in list1:
#     if element not in duplicate_list:
#         duplicate_list.append(element)
#
#
# duplicate_list.sort()
# print(duplicate_list)


# list1 = [12,211,1,2,3,4,5]
#
# l = list1
#
# print(l[1])


# list1 = ["al", 'ali', 'hassan', 'loger list','ab','cd']
# n = 3
# emptylist = []
#
# for element in list1:
#     if len(element) >= n:
#         emptylist.append(element)
# print(emptylist)

#
# def pyfunction(l1,l2):
#
#     if l1 in l2:
#         print(True)
#     else:
#         print(False)
#
#
#
#
#
#
# list1 = [1,2,3,4,56,7,8,9,0]
# list2 = [2,34,5,6,7,8,9,0,5]
# pyfunction(list1,list2)

# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
#
# for i,x in enumerate(list1):
#     if i not in (0,4,5):
#         print(x)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# emptylist = []
#
# for i in list1:
#     if i % 2 != 0:
#         emptylist.append(i)
#
# print(emptylist)


# for i in list1:
#     if i % 2==0:
#         print("Even number is  ", i)
#     else:
#         print("odd number is ", i)

# import random
#
# list1 = [1,2,3,4,5,6,7]
#
#
# random.shuffle(list1)
# print(list1)
# lis = []
# for i in range(1,20):
#     i = i*2
#     lis.append(i)
# print(lis[5:-5])


# list1 = [1,3,4,5,67,8,9]
# list2 = [2,3,5,6,71,8,1]
# lst3 = []
#
# if list1 not in list2:
#     lst3.append(list1)
#
# print(lst3)
# emptylist = []
# for i in range(1,31):
#     i = i**2
#     emptylist.append(i)
# print(emptylist)
# print()
# print(emptylist[:6])
# print(emptylist[-5:])
#
# import itertools
#
# print(list(itertools.permutations([1,2,3,4])))


# list1 = ['ali',1,2,3,4,'ahmad','talal']

# for i in range(len(list1)):
#     print(list1[i])

# ls = ['ali', 'hassan', 'ali', 'ahmad']
# print(ls)
# print(type(ls))
# st = str(ls)
# print(st.upper())


# firstlist = [1, 2, 3, 4]
# secondlist = [9, 8, 7, 6]
#
#
# for i in firstlist:
#     secondlist.append(i)
# print(secondlist)
# import random
# firstlist = [1, 2, 3, 4]
#
# print(random.choices(firstlist))


#
# list1 = [2,3,4,4]
#
# el = []
#
# for element in list1:
#
#     el.count(element)
#
# print(element)

# import collections
#
# list1 = [12,34,1,1,1,12,31,23,3,3,3,312,3,1]
#
# res = list(collections.Counter(list1))
#
# print(res)



# freq = {}
#
# for element in my_list:
#     if element in freq:
#         freq[element] = freq[element] +1
#     else:
#         freq[element] = 1
#
# for x,y in freq.items():
#     print(x,y)
#
#
#
# print(type(freq))




# my_list1 = [1, 1,1, 1, 51]
# my_list2 = [12, 13,11, 13, 51]
#
# s1 = set(my_list1)
# s2 = set(my_list2)
#
# print(s1.intersection(s2))

#
# def change_pos(my_list):
#     print(my_list)
#     for i in range(1)
#
# #       for i in range(0,len(my_list),2):
# #
# #            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
# #
# #            return my_list
#

#
# print(change_pos(my_list))




# my_list=[0,1,2,3,4,5]
#
# print(my_list[1:-2])

# print(f“{2+2}+{10%3})

# print(f"{2+2} + {10%3}")


# num = int(input("Please enter number of check factorial "))
# # fac = 1
# # for i in range(1,num+1):
# #     fac = fac*i
# # print(fac)




# res=lambda x : x+15
#
# print(res(15))
#
# res1 = lambda x,y : x*y
#
# print(res1(2,3))

