print("Alhamdulillah  For everything ")

# string1 = "fdclfinddd"
#
# dictionary = {}
#
# for element in string1:
#     # keys = dictionary.keys()
#     if element  in dictionary:
#         dictionary[element] +=  1
#     else:
#         dictionary[element] = 1
#
#
# print(dictionary)


# di = {1:'ali',2:"ahmad"}
# print(di.pop(2))
# print(di)
# string = "string"
# re=string[:2]
# re1=string[-2:]
# print(re+re1)
# string1 = "abc"
# string2 = "xyz2223"
#
# new_a = string2[:3]
#
# # new_b = string1[:2] + string2[2:]
# #
# # c = new_a +''+ new_b
# # print(c)
# print(new_a)


# num = int(input("Please enter the number that you want to print "))
# previous = 0
# for element in range(1,10):
#     sum = previous+element
#     print(f"your current number is {previous} and previous number is {element} sum is : {sum}")
#     previous = element

# string = "onlyeveninterger"
# # leng = len(string)
# for i in range(len(string)):
#     if  i%2!=0:
#         print(string[i],end= "")


# string = "AliHassan"
# n = 3
#
# print(string[n:])


# list1 = [10, 20, 30, 40, 10]
# li1 = list1[0]
# li2= list1[-1]
#
# if li1==li2:
#     print(True)
# else:
#     print(False)

# li = [10, 20, 33, 46, 55,21,40]
#
# for items in li:
#     if items%5==0:
#         print(items)


# str = "Emma is good developer. Emma is a writer Emma Emma Emma Emma"
# str = str.split()
# count = 0
# for i in str:
#     if i == "Emma":
#         count += 1
# print(count)


# for i in range(4):
#     for j in range(i+2):
#         print(i, end=" ")
#     print("\n")


# num = 12
# tem = num
# remainder = 0
# while num > 0:
#     res = num % 10
#
#     remainder = (remainder*10)+res
#
#     num= num//10
#
#
# print(remainder)
#
#
# if tem==remainder:
#     print("reversed number is correct",remainder)
# else:
#     print('no reversed match',remainder)

# list1 =  [10, 20, 23, 11, 17]
# list2 = [13, 43, 24, 36, 12]
# li1 = []
# li2 = []
# for elemet in list1:
#     if elemet%2 !=0:
#         li1.append(elemet)
# for el in list2:
#     if el%2==0:
#         li2.append(el)
#
# res = li1+li2
#
# print(res)
#
# num = 291
#
# while (num > 0):
#     res = num % 10
#
#     num = num//10
#
#     print(res, end= "")
# print()
#
#
# number = 7536
# print("Given number", number)
# while (number > 0):
#     # get the last digit
#     digit = number % 10
#
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")
# str = "my name is James bond";
# print (str.title())
#


# list1 = []
# for i in range(1,31):
#     list1.append(i*2)
#
# print(list1)
# print(list1[:5]+list1[-5:])
# list1 = [1,23,4,5,6,7,8,9]
# list2 = [1,2,3,45,23,4,23,21]
#
# list3 = []
#
# for element in list1:
#     list3.append(element)
#
# for i in list2:
#     list3.append(i)
# print(list3)


# list1 = [1, 2, 4, 5, 6, 7]
# n= 3
# if n in list1:
#     print(True)
# else:
#     print(False)

# string = "aeiou"
# # word = "a"
# #
# # if word in string:
# #     print(True)
# # else:
# #     print(False)

#
# histogramOutPut = [50, 3, 8, 9, 1]
#
#
# for element in histogramOutPut:
#     output = ""
#     while (element > 0):
#         output = output + "*"
#         element  = element-1
#     print(output)

# int1 = 10
# int2 = 102
#
# sum = int1+int2
#
#
# if sum in range(16,20):
#     print(20)
# else:
#     print(sum)


# for element in range(1,9):
#     guess = int(input("Please Guess the numbers between 1 to 9:  "))
#     if guess==element:
#         print("Well Guessed ")
#         break

#
# for i in range(1,5):
#     for j in range(i):
#         print("$", end="")


# string = "w3SCHOooLLEARNING"
# newlist = []
#
# for i in string:
#     newlist.append(i.lower())
#
# new = str(newlist)
# print(newlist)
# print(type(newlist))
# userinput = input("Please enter number ")
#
# res = userinput[::-1]
#
# print(res)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count = 0

for i in numbers:
    if i%2==0:
        i = i+1

print(f"total even number is {i}")