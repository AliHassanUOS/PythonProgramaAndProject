print("Allah")

# num = 6
#
# for element in range(num,-1,-1):
#     for i in range(1,element+1):
#         print("*", end=" ")
#     print(" ")
# userinput = int(input("Please enter number "))
# count = 0
# for element in range(1,userinput+1):
#
#      count = count+element
# print(count)


# userinput = int(input("Please enter the number that you want to print table "))

# for i in range(1,10+1):
#     re = userinput*i
#     print(f"table of {userinput} X {i} = {re}")


# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# for elemet in list1:
#
#     if elemet > 180:
#         break
#     if elemet % 5 == 0:
#         print(elemet)


# number = 9876
# remainder = 0
#
# while number > 0:
#     res = number%10
#     remainder = (remainder*10)+res
#     number = number//10
#
# print(remainder)

# list1 = [10, 20, 30, 40, 50]
#
# print(list1[::-1])
# for element in range(-10,0,1):
#     print(f"{element}")


# for element in range(1,20):
#     print(element)
#
# print("Done")

# primenumber = 29
#
# for i in range(2,primenumber):
#     if i%primenumber==0:
#         print("Number is not prime number")
#
#     else:
#         print("number is prime")
#         break
# num  = 29
# for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#        else:
#           print(num,"is a prime number")
# num = 5
# mul = 1
# for i in range(1,num+1):
#     mul = mul*i
#
# print(mul)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
#
# for elemet in my_list[1::2]:
#     print(elemet)


# userinput = 6
#
# for i in range(1,userinput+1):
#     print(i*i*i)


#
#
# for row in range(6):
#     for column in range(row):
#         print(row, end=" ")
#     print(" ")

# def createfun(a,b):
#     print(a,b)
#     print(type(a))
#     print(type(b))


# def fun1(*args):
#
#     for i in args:
#         print(i)
# fun1(1)

# def calculation(a,b):
#     return a+b ,a-b, a*b, a**b, a/b, a//b
# res = calculation(10,10)
#
# print(res)

# find the largest number in list
# list1 = [3, 1, 2, 3, 45, 24, 31, 2, 341, 21, 2, 4, 563, 121, 23, 41, 13, 11]
#
# max = list1[0]
# for i in list1:
#     if i > max:
#         max= i
#
# print(max)

# lam=lambda x:x+5+10
#
# print(lam(10))

# lst = [i for i in range(1,101) if i%9==0 ]
# print(lst)
#
# userinput = 9
#
# for i in range(1,11):
#     res = userinput*i
#     # print(res)


# newlist = []
# for i in range(1,20):
#     if (i%2==0 and i%3==0) or i%4==0:
#         newlist.append(i)
#
# print(newlist)

# How many character in Human word


# sum=0
# for i in range(1,101):
#     sum = sum+i
#     print(sum)


# factorial = int(input("Please enter the number for checking factorial"))
#
# res =1
# for element in range(1,factorial+1):
#     res = element*res
#
# print(res)


# def factorial(fac):
#
#
#     res = 1
#     for element in range(1,fac+1):
#         res = res*element
#     print(res)


#
#
#
#
#
# fac = int(input("Please enter the number for find factorial "))
#
# factorial(fac)
#
#
# def add_it_up(num):
#     sum = 0
#
#     for element in range(1, num + 1):
#         sum = sum + element
#     return sum


# userinput = int(input("Please enter the number "))
#
# res=add_it_up(userinput)
#
# print(res)


# How to remove duplication in following list

# words = ["one", "one", "two", "three", "three", "two"]
#
# newlis = []
#
# for i in words:
#     if i not in newlis:
#         newlis.append(i)
#
# print(newlis)

# sum  = 0
# for i in range(2,101):
#     sum = sum+i
#
# print(sum)

# a = 4
# b= 8
# c = 120
# d = 1
#
#
# if (a > b) and (a > c) and (a > d):
#     largets = a
# elif (b > a) and (b > c) and (b > d):
#     largets  = b
#
# elif (c > a) and (c > b) and (c > d):
#     largets = c
# else:
#     largets = d
#
# print(f"largest number is {largets}")


# list1 = [11112, 31, 23, 12, 21, 312, 3, 41, 2, 12, 31, 234, 1]
#
# max = list1[0]
#
# for element in list1:
#     if element > max:
#         max = elemen4
#
#
# i = 0
# while i < 6:
#         i += 1
#         if i == 16:
#             continue
#         print(i)
#


# num = 0
# total = 0
#
#
#
# while num <= 100:
#
#     total = total+num
#     num = num+1
#
# print(total)


# lst = [100, 100, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# i=0
#
# while i < len(lst):
#     if lst[i]==100:
#         print("The index of 100 is ", i)
#     i= i+1
#
# list = [100, 100, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# # length = len(list)
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1


# string = "firstletter"
#
# str1 = string[:2]
# str2 = string[2:]
# str1 = str1[::-1]
#
# newstring = str1+str2
# print(newstring)


# newstring = "change the string"
#
# newstring = newstring.split()
#
# s2 = newstring[:2]
# # print(s2)
#
# answer = newstring[2]
#
# si = answer[::-1]
#
# ans = s2.append(si)
# print(ans)


# list = "ali hassan"
#
# i = 0
# while i < len(list):
#     print(list[i], end=",")
#     i = i + 1


# newch = "ffind the frequency of words in string"
#
# frequency = {}
#
# for element in newch:
#     if element in frequency:
#         frequency[element] = frequency[element]+1
#     else:
#         frequency[element] = 1
#
#
#
# print(frequency)


# newstring = "find the maximum occourance in stringnnnnn"
#
# d = {}
# for i in newstring:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#
#
# print(d)
# res = max(d,key=d.get)
# res1 = min(d,key=d.get)
#
# print(res)
# print(res1)


# newstring = "CapitaP FirsL and LasT CharacteT In StrinG"
#
# newstring = newstring[2].upper()
#
# aftersplit = newstring.split()
# res = ""
#
# for element in aftersplit:
#     res += element[:-1] + element[-1].lower()+ " "
# print(res)
# new = "HHHHow to remove duplication in stringggg"
# res = []
# for i in new:
#     if i not in res:
#         res.append(i)


# new = "find the sum of 1231 in strin8"
# alldigit = 0
# for i in new:
#     if i.isdigit()== True:
#         newvariable = int(i)
#
#         alldigit = alldigit+newvariable
# print(alldigit)

#
# new = "count ALL the 5pecial% charact3r in 5tring"
# lowercase,uppercase,digit,specialCharacter = 0, 0 , 0,0
#
# for i in new:
#     if i.islower()==True:
#         lowercase  = lowercase+1
#     elif i.isupper()==True:
#         uppercase= uppercase+1
#     elif i.isdigit()==True:
#         digit = digit+1
#     else:
#         specialCharacter = specialCharacter+1
#
# print(lowercase)
# print(uppercase)
# print(digit)
# print(specialCharacter)

# new = "SWAP THE string case"
#
# newstring = ""
# for i in new:
#     if i.isupper()==True:
#         newstring = newstring+i.lower()
#     elif i.islower()==True:
#         newstring = newstring+i.upper()
#     else:
#         pass
#
# print(newstring)

# aLsit = [100, 200, 300, 400, 500]
# newlist = aLsit[:3]
# afternewlist = newlist[::-1]
# finallist = aLsit[3:]
# res = afternewlist+finallist
#
# print(res)

# aList = [1, 2, 3, 4, 5, 6, 7]
#
# # aList = [x * x for x in aList]
# # print(aList)
# res = 1
# for x in aList:
#     res = x * x
#
#     print(res, end=" ")
# list1 = [10, 20, 30, 40]
#
# list2 = [100, 200, 300, 400]
#
# list2 = list2[::-1]
#
# print(f"{list1}  {list2}")
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#
#
#
# newlist = list(filter(None,list1))
#
# print(newlist)

# number = 12
# res = 0
# while number > 0:
#     rem = number % 10
#     res = (res*10)+rem
#     number = number//10

# print(res)

# find the sum of all digits


# number = 12
#
# sum= 0
# while number > 0:
#     res = number%10
#     sum = sum+int(res)
#     number = number//10
#
# print(sum)

#
# userinput = "numbe3 1 is number3 is 3"
#
# sum= 0
# for element in userinput:
#     if element.isdigit()==True:
#         sum= sum+int(element)
#
# print(sum)

#  range for 1 to 100 entries in list


# first = 1
# last = 100
# emptylist = []
#
# for i in range(first, last):
#     emptylist.append(i)
#
#
# print(emptylist)


# list = [12,3,12,12,31,2,312,12,31,2,31,2,12,3]
#
# list.sort()
# print(list[-1])

userinput = int(input("Please enter the total numbers that you wants to enter in list"))

ans =0
for element in range(userinput):
      res=int(input("Please enter your numbers"))
      ans = ans+res

print(ans)

