print("ALLAH")

# class calculator(object):
#     def __init__(self, a, b):
#         self.num1 = a
#         self.num2 = b
#
#     def add(self):
#         sum = self.num1 + self.num2
#         print(f"addition of number is {sum}")
#
#     def sub(self):
#         sub = self.num1 - self.num2
#         print(f"Subtraction of numbers is {sub}")
#
#
# obj = calculator(10, 20)
# obj.add()
# obj.sub()

#################################### Constructor in python ###########################################


# class name
# class person(object):
#     # constructor with parameter
#     def __init__(self, name, age):
#         self.name = name  # Instance variable
#         self.age = age  # Instance variable
#     # instance method declare
#     def ShowDetail(self, edu):
#         self.edu = edu  # instance variable
#         print(f"person name is {self.name} and age is {self.age} education is {self.edu}")
#
# # Create object/instance of class
# obj = person("ali", 23)
# pe = person("hassan", 21)
# # instance function calling using object of class
# # obj.ShowDetail('Graduation ')
# pe.ShowDetail('Masters ')

#
# class CarSpeedTest(object):
#     def __init__(self):
#
#         self.speed = int(input("Please enter speed  "))
#
#     def CheckSpeed(self):
#
#         if self.speed < 70:
#             print("Your Speed is Ok")
#         else:
#             token = (self.speed - 70) // 5
#             if token < 12:
#                 print("Don't up your speed otherwise your license will be banned, Your have number of token", token)
#             else:
#                 print("Your license has been rejected, You have number  of token ", token)
#
# obj = CarSpeedTest()
#
# obj.CheckSpeed()


# class CarSpeedTest(object):
#
#     def __init__(self,speed):
#         self.speed = 100
#
#     def get_value(self, speed):
#         return speed
#
#
#     def CheckSpeed(self):
#         if self.get_value()< 70:
#             print("Your Speed is Ok")
#         else:
#             token = (self.get_value() - 70) // 5
#             if token < 12:
#                 print("Don't up your speed otherwise your license will be banned, Your have number of token", token)
#             else:
#                 print("Your license has been rejected, You have number  of token ", token)
#
#
# obj = CarSpeedTest(100)
# obj.CheckSpeed()


# Class Method example in python


# class  person:
#     age = 19
#     name = "hassan"  # Class Variable or static variable
#
#     @classmethod # Decorator
#     def person_detail(cls, city): # Class method
#
#         cls.city = city
#         print(f"person name is {cls.name} age is {cls.age} and city is {cls.city}")
#
#
# obj = person()
# obj.person_detail("bhawalpur ")

# Create a class in python that perform two activities, first one is find even and odd number in list and second one is add all the items in list


# class listfunction(object):  # create a class
#
#     # create constructor means __init__(self) function
#     def __init__(self):
#         self.lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # instance variable of the class
#
#     def Find_Even_odd(self):  # Instance method
#         total = 0  # class variable
#         for i in self.lst:
#             if (i % 2 == 0):
#                 print(f"Even numbers in list are {i}")
#             else:
#                 print(f"Odd numbers in list are {i}")
#             total = total + 1
#         print()
#         print(f"Total numbers in list are {total}")
#
#     def SumOfList(self):  # second Instance method
#         sum = 0
#         for i in self.lst:
#             sum = sum + i
#         print(f"sum of list is {sum}")
#
#     def TablePrint(self):
#         user = int(input("Enter number for print table  "))
#         for i in range(1,11):
#             res = user*i
#             print(f" {user} by {i} = {res} ")


# obj = listfunction()
# obj.Find_Even_odd()
# obj.SumOfList()
# obj.TablePrint()
# Tab=obj.TablePrint()


#########################################################3 Single Inheritance in python####3333333#############################################################################3

# class listfunction(object):  # create a class
#
#     # create constructor means __init__(self) function
#     def __init__(self):
#         self.lst = [1, 2, 3, 4]  # instance variable of the class
#
#     def Find_Even_odd(self):  # Instance method
#         total = 0  # class variable
#         for i in self.lst:
#             if (i % 2 == 0):
#                 print(f"Even numbers in list are {i}")
#             else:
#                 print(f"Odd numbers in list are {i}")
#             total = total + 1
#         print()
#         print(f"Total numbers in list are {total}")
#
#     def SumOfList(self):  # second Instance method
#         sum = 0
#         for i in self.lst:
#             sum = sum + i
#         return sum
#
#     def TablePrint(self):
#         user = int(input("Enter number for print table  "))
#         for i in range(1, 11):
#             res = user * i
#             print(f" {user} by {i} = {res} ")
#


# class ExtraFeatureInList(listfunction):  # Make a New class and inherit it by Parent class ( list Function )
#
#
#     def __init__(self):
#         self.list = [2,3,4,5,6,7]
#
#     # def RemoveDuplication(self):  # Child class instance method
#
#
#     def show(self):
#         print(self.list)
#
#
# newlist = []  # Function variable
#
# for element in self.lst:
#     if element not in newlist:
#         newlist.append(element)
#
# print(f"After removed duplicated element {newlist}")


#########################################################3 Multilevel Inheritance in python####3333333####################################################################

# class parent(object):
#     def __init__(self, n, un):  # parent class constructor
#         self.num = n  # instance variable
#         self.unum = un
#
#     def parentmethod(self):
#         print("I am instance method of parent class ")
#
#     def sumofallinterger(self):
#         sum = 0
#         while self.unum > 0:
#             res = self.unum % 10
#             sum = sum + int(res)
#             self.unum = self.unum // 10
#         print(sum)

#
# class child(parent):
#     def __init__(self, n, un):  # Child class constructor
#         super().__init__(n, un)  # Call parent class constructor using super () method
#         self.name = "ali hassan"  # child class instance method
#
#     def childmethod(self):
#         print("My name is child class  method and my instance variable name is ", self.name)
#
#     def numberreverse(self):  # child class instance method for reverse the number
#         res = 0
#         while self.num > 0:
#             remainder = self.num % 10
#             res = res * 10 + remainder
#             self.num = self.num // 10
#         print(res)
#
#
# class grandson(child):
#
#     def __init__(self, n, un):
#         super().__init__(n, un)
#         print("grand son class constructor ")
#
#
# instance = grandson(12, 19)
#
# instance.sumofallinterger()


########################################## Duck Typing in polymorphism in python ###############################################
# class monkey:
#
#     def eat(self):
#         print("Monkey eats banana")
#
#
# class dog:
#
#     def eat(self):
#         print("Dog eats meat ")
#
#
# class horse:
#
#     def eat(self):
#         print("horse eats gras")
#
#
# class cat:
#     def walk(self):
#         print("cat walks beautifully ")
#
# def myfunction(obj):
#    if hasattr(obj,"eat"):
#        obj.eat()
#
#
#
#
# h = cat()
#
# myfunction(h)


########################################## strong Typing in polymorphism in python ###############################################
# class monkey:
#
#     def eat(self):
#         print("Monkey eats banana")
#
#
# class dog:
#
#     def eat(self):
#         print("Dog eats meat ")
#
#
# class horse:
#
#     def eat(self):
#         print("horse eats gras")
#
#
# class cat:
#     def walk(self):
#         print("cat walks beautifully ")
#
# def myfunction(obj):
#    if hasattr(obj,"eat"):
#        obj.eat()
#
#
#
#
# h = cat()
#
# myfunction(h)


############################## Method overriding in python (Polymorphism) ###############################################

# class methodoverriding(object):  # create class named as methodoverriding
#
#     def __init__(self):  # parent class constructor
#         self.a = 10  # instance variable
#         self.b = 10  # instance variable
#
#     def sum(self):  # instance method within methodoverriding class
#
#         res = self.a + self.b  # access instance variable with method using self keyword
#
#         # print(res)  # print the result of instance variable
#
#
# class overriding(methodoverriding):  # create a class named as overriding and use  inheritance concept
#
#     def __init__(self):  # Child class constructor
#         super().__init__()  # called parent class constructor
#         self.c = 100  # instance variable declare
#         self.d = 10  # instance variable declare
#
#     def sum(self):  # instance method declare in child class
#         super().sum()  # method overriding perform here using super() method
#         ans = self.d + self.a
#         print(ans)

# obj = overriding()  # create object/instance of child class
# obj.sum()   # calling child class method using object/instance

############################################# Date and time module in python ###############################################
# from time import time,ctime,localtime
#
# locatl = localtime()
# print(f"year {locatl.tm_year}")
# print(f"month {locatl.tm_mon}")
# print(f"hours {locatl.tm_hour}")
# print(f"mint {locatl.tm_min}")


# from datetime import datetime
#
# from datetime import datetime
# d1 = datetime.today()
# d2 = datetime(2021,10,1)
#
# print(d1<d2)
