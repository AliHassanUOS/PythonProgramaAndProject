print("Allah")


#
# createset = {1,2,3,4,5,6,7,8,9,0,0,10,11}
# sum = 0
# for i in createset:
#
#     sum = sum+i
#
# print(sum)

# createset = {1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11}
# # createset.discard(11123)
# # createset.pop()
# # createset.update({"Ali","Alia"})
# print(createset)

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44}
# set2 = {22, 33, 44, 55, 66, 77, 88, 99, 00, 1, 2, 3, 4, 5, 6, 78}
# ans = set1.union(set2)
# ans1 = set1.intersection(set2)
# ans2 = set1.difference(set2)
# ans3 = set1.symmetric_difference(set2)
#
#
# print(f"Union of 2 sets is {ans}")
# print(f"intersection of 2 sets is {ans1}")
# print(f"difference of 2 sets is {ans2}")
# print(f"Symmetric_difference of 2 sets is {ans3}")
# print(len(set1)
# How to remove space in string


# def remove(string):
#     return string.replace(" ", "")
#
#
# # Driver Program
# string = "Remove space asd "
# print(remove(string))

# string = "remove space asd"
# res = string.replace(" ", "")
# print(res)
# string = "remove Character at even indexes"

# newlist = ""
# for key,value in enumerate(string):
#      if key%2==0:
#          newlist = newlist+str(value)
# print(str(newlist))


# string = "12345asd6"
#
# if string.isnumeric()==True:
#     print(f"Yes string contain only numbers {string}")
# else:
#     print("Not Ture")

# string = "Python"
# n = 3
# newstr = ""
# for key,values in enumerate(string):
#     if key!=n:
#         newstr = newstr+str(values)
#
# print(newstr)
# string = "Python"
# res= string.replace("Py", "ha")
# print(res)

# string = "Separate,comma,with,dot,"
# res = string.replace(",", ".")
#
# print(res)
# def countfrequecnyword(string):
#     res_dic = {}
#     for element in string:
#
#         if element in res_dic:
#             res_dic[element] += 1
#         else:
#             res_dic[element] = 1
#     print(res_dic, end=" ")
#
#
# string = "fFFFFind the frequecny of repeated wordsssss"
# countfrequecnyword(string)

# list = [111,2,32,4,5,6,7,8]
# max = list[0]
# for i in list:
#     if i > max:
#         i = max
#
# print(max)


# list = [12, 3, 0,1, 2, 31, 21, 231, 23, 12, 312]
#
# min = list[0]
#
# for i in list:
#     if i < min:
#         min = i
# print(min)


#
# for key,value in enumerate(list):
#     print(f"key {key} and values {value}")


# list = [12, 12, 12, 12, 3, 3, 1, 21, 3, 0, 1, 2, 31, 21, 231, 23, 12, 312]

# newlist = []
#
# for element in list:
#
#     if element not in newlist:
#         newlist.append(element)
#
# print(newlist)


# list = [1,2,12, 12, 3, 3]
# k=1
# count = 0
# for i in list:
#     if i >k:
#         count = count+1
# print(count)
# li1 = [10, 15, 20, 25, 30, 35, 40]
#
# li2 = [25, 40, 35]
#
# list1 = set(li1)
#
# list2 = set(li2)
#
# ans=list1.symmetric_difference(list2)
# print(ans)

# li1 = [10, 15, 20, 25, 30, 35, 40]
# li2 = [25, 40, 35]
# newlist = []
#
# for i in li1:
#     if i not in li1 or i not in li2:
#         newlist.append(i)
#
# print(newlist)
# li1 = [1, 2, 3, 4, 5,6]
# li2 = [5, 6, 7, 8, 9]
#
# list1 = set(li1)
# list2 = set(li2)
#
#
# res=list1.intersection(list2)
# print(res)

# li1 = [1, 2, 3, 4, 5, 6,6,2,1,23]
#
# res= set(li1)
# print(res)

# di = {1:"Ali", 2:"hASSAN", 3:"Adeel", 4: "kamran"}
# for key,val in enumerate(di):
#     print(key,di[val])
# di = {1:"Ali", 2:"hASSAN", 3:"Adeel", 4: "kamran"}
#
# res=11 in di
# print(res)
#
#
# list = [1, 2, 3, -1, -1, -2, -3, 12, 1, 2, 3, 21, 0, 0, 0, 0, 0, 203, 1]
# sum1 = 0
# sum_1 = 0
# sum0 = 0
# for i in list:
#     if i >=1:
#         sum1 = sum1+1
#     elif i <0:
#         sum_1 = sum_1+1
#     else:
#         sum0 = sum0+1
#
# print(f"Total number that are greater the 1 {sum1}")
# print(f"Total number that are less the 1 {sum_1}")
# print(f"Total number that are equal to 0 {sum0}")


# table = int(input("Please enter the number for find table "))
# for i in range(1,11):
#     ans = table*i
#     print(f"{table} by the {i} = {ans}")

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i in list:
#     res= i*3
#     print(res, end=" ")


# res = lambda x, y: x * y ** 3
#
# print(res(2, 2))
# def FindMaxInThreeNum(a,b,c):
#
#     if a>b:
#         return a
#     elif b > c:
#         return b
#     elif c > a and c >b:
#
#         return c
# res=FindMaxInThreeNum(1001,200,30)
# print(f"Most greater number is  {res}")

#
# a =1
# b = 10
# c =0
# max = 0
#
# if a<b and a<c:
#     max = a
#     print(f"Most greater number is a {a}")
#
# elif b < a and b < c:
#     max = b
#     print(f"Most great number is b {b}")
# elif c < a and c<b:
#     max = c
#     print(f"most greater number is c {c}")

# findday = int(input("Please enter the number of month  "))

# if findday == 1 or 2 or 3 or 4:
#     print("Total number in  this month is ",31)
#
# sum = 0
# for i in range(1,11):
#     sum = sum+i
#     print(sum)

#
# usernum = int(input("Enter number to check table "))
# for i in range(1,11):
#     res= usernum*i
#     print(f"{usernum} by {i} = {res} ")


# total = 0
# for i in range(1,110):
#     if i%2!=0:
#         print(f"First 100 even number is {i}")
#         total = total+1
# print(f"Total number is {total}")
#
# fac = int(input("Please enter enter to find factorial "))

# res= 1
# for i in range(1,fac+1):
#     res = res*i
# print(f"Factorial for {fac} is == {res}")

# primenumber = 21
#
# if primenumber > 1:
#
#     for i in range(2,primenumber+1):
#         if primenumber%i==0:
#               print("Not Prime ",primenumber)
#               break
#         else:
#               print("prime number True", primenumber)
#               break
# else:
#     print(f"not prime number {primenumber} ,  please enter greater then 1 ")

# lower = 1
# upper = 100
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


# for i in range(0,6):
#
#     for num in range(i):
#         print("*", end=" ")
#     print('')
#
# string = "AliHassan"
# newstring = ""
# for i in string:
#     newstring = i+newstring
#
# print(newstring)

# from datetime import date
#
# res= date.today()
#
# print(res)


# a = [2, 3, 4, 5]
# try:
#     print(a[1])
#     print(a[2])
#     print(a[10])
# except:
#     print("Error occour")

# print("Other code can run Now , important code")
# fac = 1
# try:
#     usernum = int(input("Enter number to find factorial "))
#     for i in range(1, usernum+1):
#         fac = fac * i
#     print(fac)
#
# except Exception as e:
#     print(e)

# finally:
#     print("After error occur  ")
#     a = 3
#     b = 3

#     print(f"Total of {a+b}")


# lst = [i for i in range(1, 20) if i % 2 != 0]
# print(lst)


# lst = [60, 120, 123, 123, 41, 45, 48, 1, 2, 3, 12, 331, 121]
#
# lst = list(filter(lambda x: x > 60 or x < 40 , lst))
# print(lst)


# a = 10
# b = 101
# c = 100
# sum = 0
#
# if a==b or b==c:
#     print(sum)
# elif c==a:
#     print(sum)
# else:
#     sum = a+b+c
#     print(sum)

# a = 10
# b = 1
# sum = a+b
#
# if 15 <= sum <= 20:
#     print("20")
# else:
#     print(sum)

# x = 4
# y = 3
#
# res= (x+y) * (x+y)
# print(res)


# flag = 10
# sum = 0
#
# while flag != 0:
#     user = int(input("Enter your Grocery items price "))
#     sum = sum + user
#
#     flag -= 1
#
# print(f"Total Price is {sum}")

#
# prompt = "Tell me something cool: "
# prompt += "\nEnter 'quit' to end the program"
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# price = "Enter the price of items  "
# price += "\nEnter '0' to quit the program  "
# flag = True
# total = 0
# while flag:
#     sum = int(input(price))
#     total = total+sum
#
#     if sum== 0 :
#         flag = False
# print(total)


# while True:
#     password1 = input("Enter your Password ")
#     password2 = input("Confirm Your Password")
#
#     if password1 == password2:
#         print("logged in Successfully ")
#         break
#     else:
#         print("Both password does not match ! Please try again ")

# num = int(input("Please enter number to find is number prime or not "))
# flag = False
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
# if flag:
#     print("Not a prime number ")
# else:
#     print("Prime number confirm ")


# def maxfun(a,b):
#
#     if a > b:
#         return a
#     else:
#         return b
#
# res=maxfun(20,10)
# res1=maxfun(1,10)
# print(f"a is greater {res}")
# print(f"b is greater {res1}")


# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "fizebazz"
#     elif num % 3 == 0:
#         return "baz"
#     elif num % 5 == 0:
#         return "fiz"
#
#     else:
#         return num
#
#
# num = int(input("Enter numbers "))
#
# res = fizz_buzz(num)
# print(res)


# def driver_speed_check(speed):
#     if speed < 70:
#         return "Ok"
#     else:
#         determitpoint = speed > 70 % 5
#         print(determitpoint)
# speed = int(input("Enter speed "))
# res=driver_speed_check(speed)
# print(res)
# def speed_check(speed):
#     if speed <= 70:
#         return "OK"
#     else:
#         speed1 = (speed-70)//5
#
#         if speed1 <= 12:
#             return print(f"Point: {speed1}")
#
#         else:
#             return print("License suspended")
#
# enter = speed_check(int(input("Enter speed: ")))
# print(enter)


# def ShowNumber(limit):
#     for i in range(0, limit + 1):
#         if i % 2 == 0:
#             print(f"{i} is even")
#         else:
#             print(f"{i} is odd")
# ShowNumber(10)
# def Numlimit(limit):
#     for i in range(1, limit + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             print(i)
# Numlimit(20)
