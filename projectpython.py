# def sum(num1, num2):
#     return num1 + num2
# def sub(num1, num2):
#     return num1 - num2
# def mul(num1, num2):
#     return num1 * num2
#
# def divi(num1, num2):
#     return num1 / num2
#
# print("Please select operation -\n"
#       "1. Add\n"
#       "2. Subtract\n"
#       "3. Multiply\n"
#       "4. Divide\n"
#       "5. sin\n"
#       )
# select = int(input("Select operations form 1, 2, 3, 4 :"))
# num1 = int(input("Enter number 1 "))
# num2 = int(input('Enter number 2 '))
# if select== 1 :
#     print(num1, "+",num2, "=", sum(num1,num2) )
# elif select==2:
#     print(num1, "-", num2, "=", sub(num1, num2))
# elif select==3:
#     print(num1, "*", num2, "=", mul(num1, num2))
# elif select==4:
#     print(num1, "//", num2, "=", divi(num1, num2))
# else:
#     print("Wrong input ")

# Bank ATM Machine project in python

#
# print("************************************* Welcome to HBL bank *****************************************************")
# print("Please select operation -\n"
#       "1. CashWithDrawal\n"
#       "2. Add money\n"
#       "3. Transfer money\n"
#       "4. Bill Payment\n"
#       )
#
# name = input("Please Enter your name  ")
# password = int(input('Please enter 4 digit password  '))
#
# balance = 1000000
# select = int(input("Select operations form 1, 2, 3,4 :"))
#
# while password == 1234:
#     print("Welcome dear Customer ", name, "Your current balance is ", balance)
#     if select == 1:
#         ammount = int(input("Enter money you want withdraw "))
#
#         if ammount < balance:
#             currentammout = balance - ammount
#             print("Transaction completed, Your current balance is  ", currentammout)
#         else:
#             print("Your entered amount is greater then your Current amount , Your current amount is ", balance)
#         break
#     elif select == 2:
#         print("Welcome dear Customer ", name, "Your current balance is ", balance)
#         addmoney = int(input("Please Enter amount that you want to add  "))
#         if addmoney>0:
#             addinbank = balance+addmoney
#             print("You added money successfully, Your current balance is  ", addinbank)
#         else:
#             print("Please enter amount greater then 0 ")
#             break
#     elif select == 3:
#         transfermoney = int(input("Please enter amount that you want to transfer  "))
#         if transfermoney < balance:
#             MoneyHasTranfered = balance - transfermoney
#             print("Money transferred successfully, Your current balance is  ", MoneyHasTranfered)
#         else:
#             print("You enter wrong amount  ")
#             break
#     elif select == 4:
#         Paybill = int(input("Please enter amount of bill   "))
#         if Paybill < balance:
#             BillPayment = balance - Paybill
#             print("Bill paid successfully, Your current balance is  ", BillPayment)
#         else:
#             print('Enter current amount')
#             break
#     else:
#         print("Please Choice correct number ")
#         break
#

######################################### Gussing number in Python #####################################################

# import random
# numbertaking = random.randint(1,99)
#
# guessnumber = int(input("Please enter number in range of 1,99  "))
# attempt = 0
# while  :
#     attempt = attempt+1
#     if guessnumber < numbertaking:
#         print(" Your entered number is too less ")
#         print('computer guess number is  ', numbertaking)
#         guessnumber = int(input("Please enter number in range of 1,99  "))
#     elif guessnumber > numbertaking:
#         print(' Your entered number is too greater ')
#         print('computer guess number is  ', numbertaking)
#         guessnumber = int(input("Please enter number in range of 1,99  "))
#     else:
#        print('You got it')
#     break
# print(f" Your guessed attempt count is {attempt}
# import random
# acualnumber = random.randint(1,100)
# attempt = 0
#
# while True:
#     attempt = attempt+1
#     print(f"actual number is {acualnumber}")
#     guess = int(input("Please Guess the number  "))
#     if guess < acualnumber:
#         print("You entered less number ")
#     elif guess > acualnumber:
#         print("You entered high number ")
#
#     else:
#         print(F" Your total attempt for guessing nunber is {attempt}")
#         break
# import random
# userinput = int(input("Please enter the lenght of password   "))
#
# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#
# p ="".join(random.sample(s,userinput))
#
# print(p)

# li=[10, 20, 33, 46, 55,12,2,5555]
# for i in li:
#     if i%5==0:
#         print(i)
#

# for i in range(10):
#     for j in range(i):
#         print(j, end="")
#     print("")
#
#
#
# UserNumber = int(input("Please Enter the number "))
# tem = UserNumber
# reversenumber = 0
#
# while UserNumber > 0:
#     rem = UserNumber % 10
#     reversenumber = (reversenumber*10)+rem
#     UserNumber = UserNumber//10
#
# print(reversenumber)


# for i in range(10):
# #     for j in range(i):
# #         print(j, end="")
# #     print("")
# Ask for enter the number from the use
# number = int(input("Enter the integer number: "))
#
# # Initiate value to null
# revs_number = 0
#
# # reverse the integer number using the while loop
#
# while (number > 0):
#     # Logic
#     remainder = number % 10
#     revs_number = (revs_number * 10) + remainder
#     number = number // 10
#
# # Display the result
# print("The reverse number is : {}".format(revs_number))


# Password = int(input("Please Enter your password "))
# email = input("Please enter your Email ")
# Psave = Password
# Esave = email
# print()
#
# print("Welcome to python login system   ")
# username = input("Please enter your name  ")
# print(f"Hi {username} how are you ")
# enterpass = int(input("Please Enter your password for login "))
# usermail = input("Enter your email for login  ")
# if enterpass== Psave and usermail==Esave:
#     print("Login Successfully  ")
# else:
#     print("Wrong password ")
#
#






