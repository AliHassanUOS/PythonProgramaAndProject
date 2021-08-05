# usernumber = int(input("Enter number for checking is prime or not  "))
#
#
# if usernumber > 1:
#
#     for i in range(2,usernumber):
#         if usernumber%i ==0:
#             print(f"{usernumber} is not prime number")
#             break
#     else:
#         print(f"{usernumber} is prime number ")
# else:
#     print('Please enter grater number then 1')


# newstring = "aliaslginasd95"
# middlestring = int(len(newstring)/2)
# threemiddlestring = newstring[middlestring-1:middlestring+2]
# print(threemiddlestring)

# s1 = "America"
# s2 = "Japan"
#
# fistword = s1[:1]+ s2[:1]
# lastword = s1[len(s1)-1] +s2[len(s2)-1]
#
# result = fistword+lastword
# print(result)


# str1 = "ALIhassan"
# lowercase = []
# uppercase = []
#
# for i in str1:
#     if i.islower():
#         lowercase.append(i)
#     else:
#         uppercase.append(i)
# newlist = ''.join(lowercase + uppercase)
# print(newlist)
#
# str1 = "hiALL12"
#
# lowercase = 0
# uppercase = 0
# digit = 0
# special = 0
# for find1 in str1:
#     if find1.islower():
#         lowercase = lowercase+1
#     elif find1.isupper():
#         uppercase = uppercase+1
#     elif find1.isdigit():
#         digit = digit+1
#     else:
#         special = special+1
# print(f"total lower case letter is {lowercase}")
# print(f"total upper case letter is {uppercase}")
# print(f"total number of digit {digit}")

# string1 = "alihasssans     alijasssss                    sssss"
# newstr = string1[-1]
# count = 0
# for i in string1:
#     if i==newstr:
#         count = count+1
# print(count)
#
#
#


# userinput = input("Please enter input ")
#
# sum=0
# for i in userinput:
#     sum = sum+1
# print(sum)


# userinput = input("Please enter input  ")
# sum = 0
# n=0
# for i in userinput:
#     if i.isdigit() == True:
#         n = int(i)
#         sum = sum+n
# print(f"sum of digit is {sum}")
# str1 = "hi all how are you"
# print(f"string before removing i'th Character ")
# new = ''
# for i in range(len(str1)):
#     if i!=8:
#         new = new + str1[i]
# print(new)

# str1= "h"
# sum = 0
# for i in str1:
#     sum = sum+1
# print(sum)
# string1 = "This is a python language"
# string1 = string1.split()
# for i in string1:
#     if len(i)%2==0:
#         print(i)


# str1 = " is a datawqwqdd Emma scientist who knows Python. "
#
# h = str1.find('Emma')
# print(f"last occourance of {h} ")
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# print(f"Original String is {str_list}")
#
# for i in str_list:
#     if i != None:
#         print(i)
#
# str1 = 'I am 25 years and 10 months old'
#
# for i in str1:
#     if i.isdigit():
#         print(i)
#
# test_str = "al ihassanas   dwqw3qej   askjd  sds"
# leng = len(test_str)//2
# res = ''
# for i in range(len(test_str)):
#     if i >= leng:
#         res = res+test_str[i].upper()
#     else:
#         res = res+test_str[i].lower()
# print(res

#
# str1 = "hello friends chai pee loo"
# str1 = str1.title()
# spli = str1.split()
# res= ""
# for i in spli:
#     res = res+i[:-1]+i[-1].upper()+""
#
# # print(res)
#
# str1 = "asds"
#
# flag_1 = False
# flag_2 = False
#
# for i in str1:
#
#     if i.isdigit():
#         flag_1 = True
#     if i.isalpha():
#         flag_2 = True
# print(flag_1)
# print(flag_2)

# str1 = "string has any special Character  "
#
# specialChar = '[@_!#$%^&*()<>?/\|}{~:]'
#
# for i in str1:
#     if i == specialChar:
#         print("String is not accepted  ")
#     else:
#         print("String is accepted  ")

# str = "hlo geeks for geeks is computer science portal"
# str = str.split()
# k = 7
# res = []
# for i in str:
#       if len(i) >= k:
#           res.append(i)
#
# print(res)
#

#
# str1 = "geek"
# i = 2
# for j in str1:


# How to take factorial in Python
#
# num = int(input("Please enter number for check factorial  "))
# f = 1
#
# for i in range(1,num+1):
#     f = f*i
# print(f)


# str1 = "google"
#
# dict = {}
#
# for i in str1:
#     keys = dict.keys()
#     if i in keys:
#         dict[i] = dict[i] +1
#     else:
#         dict[i] = dict[i]  +1
# print(dict)

# print("print numbers between 2000 to 3200  ")
# emptylist = []
# for i in range(10, 50):
#     if (i % 7 == 0) and (i % 5 != 0):
#         emptylist.append(i)
# print(emptylist)

#
# print("Print Factorial  ")
#
# num = 5
# fac = 1
# for i in range(1,num+1):
#     fac = fac*i
# print(fac)


# print("Print dictionary  ")
#
# num = int(input("Please enter number   "))
# di = dict()
# for i in range(1, num+1):
#    di[i] = i*i
# print(di)

#
# num = int(input("Please enter number "))
#
# li = []
#
# for i in range(num):
#     li.append(i)
#
# print(li)
# tu = tuple(li)
# print(tu)

#
# print("Check number is prime or not  ")
#
# num = int(input("Please enter number for checking prime or Not  "))
#
#
# for i in range(2,num):
#     if num%i == 0:
#         print("number is not prime ",num)
#         break
#
#     else:
#         print("Number is prime ",num)

# print("If else Practice program ")
# print()
# print()
#
# salary = int(input("Please enter your salary "))
# yearofex = int(input("Please enter year of experience "))
#
# if yearofex > 5 :
#     print("Your current salary is  ", salary)
#     print("your have year of service greater then 5 year so you get bones  ")
#     print("bones is  ", 0.5*salary)
# else:
#     print("Your salary is ", salary ,'not have any bones ')

# list1 = ['code with harry ', 'T-series', 'amit', 'ali code', 'second']
#
# for i in enumerate(list1):
#     print(i)

# str1 = "geeks"
#
# s1 = str1[::-1]
#
#
# if str1==s1:
#     print("yes this string is polideom ")
# else:
#     print('not')

# str = "geeks quiz practice code"
# s = str.split(' ')
# print(s[::-1])


# test_str = "GeeksForGeeks"
#
# # Printing original string
# print("The original string is : " + test_str)
#
# # Removing char at pos 3
# # using loop
# new_str = ""
#
# for i in range(len(test_str)):
#     if i != 2:
#         new_str = new_str + test_str[i]
#
# # Printing string after removal
# print("The string after removal of i'th character : " + new_str)
# print("Print even length Character   ")
#
#
# def EvenNumChar(sr):
#     sr = sr.split(' ')
#     emplist = []
#     for word in sr:
#         if len(word) % 2 == 0:
#             emplist.append(word)
#     print(emplist)
#
#
# sr = "I am Ali Hassan"
# EvenNumChar(sr)



