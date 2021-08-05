#prime number

#Check number is prime or not

num = 20

# define flag as variable
flag = False
# wirte condition here
if num > 1:
    for i in range(2,num):
      if (num % i) ==0:
          flag = True
          break
#check  Flag is ture
if flag:
    print(num, "Is not a prime number")
else:
    print(num, "Is a prime number")




