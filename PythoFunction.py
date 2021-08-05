# Create a function that add 3 number
# def AddNumber():
#     a = 10
#     b = 10
#     c = 10
#     d = a + b + c
#     print(d)
#
#
# # Calling Function Here
# AddNumber()
# # Function that takes parameters
# def subtract(c):
#     a = 10
#     b = 20
#     d = a + b + c
#     print(d)
# subtract(10)
#############################
# Calculator in Python
# def add():
#     add1 = int(input("Enter Number for add"))
#     add2 = int(input("Enter Number for add"))
#     add = add1 + add2
#     print(add)
#
#
# add()
#
# def sub():
#     add1 = int(input("Enter Number for add"))
#     add2 = int(input("Enter Number for add"))
#     add = add1 - add2
#     print(add)
#
#
# sub()
#
# def mul():
#     add1 = int(input("Enter Number for add"))
#     add2 = int(input("Enter Number for add"))
#     add = add1 * add2
#     print(add)
#
#
# mul()
#
#
# def div():
#     add1 = int(input("Enter Number for add"))
#     add2 = int(input("Enter Number for add"))
#     add = add1 / add2
#     print(add)
#
#
# div()

# def fun(y):
#     x = 10
#     return y + x
#
#
# sum = fun(20)
# print(sum)


# def fun(y):
#     x = 90
#     return x + y
#
#
# sum = fun(10)
# print(sum)


# def outerfun():
#     def innerfun():
#         print("Inner function")
#     print("Outer function")
#     innerfun()
# outerfun()

# def outerfun():
#     def innerfun():
#         a = 10
#         b= 11
#         return a*b
#     return innerfun()
# print(outerfun())

# def greeting(first, last):
#   # nested helper function
#   def getFullName():
#     return first + " " + last
#
#   print("Hi, " + getFullName() + "!")
#
# greeting(2, 4)

#
# def person(name, age):
#     print(name)
#     print(type(name))
#     print(age)
#     print(type(age))
#
#
# person("STR", 23)


# def func(args):
#     for items in args:
#         print(items)
#         # print(type(items))
#     # for i , data in kwargs:
#     #     print(i,data)
#     #     print(type(i))
#
#
#
#
# ar = ['Ali', 'ahmad', 'amna', 'hadia','arslan','a','as']
# # kw = {1: 'Aali', 2 : 'Hassan'}
# func(ar)


# Decorator
# from array import *
#
#
# def array1(arr):
#     for i in arr:
#         print(i)
#     return i
#
#
# arr = array('i', [1, 2, 3, 45, 6, 3, 4])
# newarr = array1(arr)
# print(newarr)

# from math import *
#
# a=factorial(4)
# print(a)


# def user(a,b):
#     return a+b ,a-b
#
# u1 = int(input("Enter number"))
# u2 = int(input("Enter number"))
# all = user(u1,u2)
# print(type(all))
# print(all)

# def fun():
#     a = int(input('Enter Num'))
#     b = int(input('Enter Num'))
#     sum= a +b
#     sub = a-b
#     print(sum)
#     print(sub)
# fun()

# class cal:
#
#     def __init__(self,a,b,c):
#         self.a =a
#         self.b = b
#         self.c = c
#
#     def maximum(self):
#
#         if self.a > self.b and self.a > self.c:
#             return self.a
#         elif self.b > self.a and self.b > self.c:
#             return self.b
#         else:
#             return self.c
#
# object = cal(23,12,341)

class cal:

    def mini(self,lst):
        try:
            smallest = lst[0]
            for i in lst:
                if i < smallest:
                    smallest = i
            return smallest

        except:
            print("Please enter correct output")


obj = cal()