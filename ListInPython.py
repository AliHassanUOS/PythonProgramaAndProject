# list1 = [1,2,3,4,'aLI']
# print(id(list1))
# print(list1)
# print('After changing')
# list1[2] = 100
# print(list1)
# print(id(list1))

# list1 = [1,2,3,4,5,'abc']
# leng = len(list1)
#
# for i in range(leng):
#     print("Index Number of list", i , "element in list", list1[i])

# lis1 =[1,3,4,5,6,'ali',12.3,-12]
# leng = len(lis1)
# i = 0
# while i < leng:
#     print(lis1[i],end='-')
#     i = i+1
# list1 = [1, 2, 34, 5, 6, 7, 8, 9]
# for i in list1:
#     print(i)
#
# list1.append(100)
#
# print("After append list")
#
# for i in list1:
#     print(i)


# Taking input from user

# How to want to take input from user , firstly you take empty list
# emptylist = []
#
# userinput = int(input("Enter number you add in list"))
#
# for i in range(userinput):
#     emptylist.append(input('Enter number'))
#
# print(emptylist)
# print(type(emptylist))
#
# list1 = [1,3,4,5,6,7,8]
# print(list1)
# list1.insert(2,'Subscribe')
# print(list1)
# print()


# pop1 = [1,2,3,'aLI']
# print(pop1)
# pop1.pop()
# print(pop1)


# remove1= ['ali',1,2,3,'ali']
# print(remove1)
# remove1.remove('ali')
# print(remove1)


# index() method


# count1 = [1,2,3,4,1,1,1,3,4,1,2,3,4]
#
#
# print(count1.count(1))


# clear1= [1,2,3,4,5,5,6]
# # print(clear1)
# # afterclear=clear1.clear()
# # print(afterclear)


# Slicing in List
# SlicingList = [12,31,23,4,1,23,4,56,7,3]
#
# # print(SlicingList[0:6:2])
# # print(SlicingList[-5:-2])
# print(SlicingList[:3:])

# a = [1,3,4,'SAME']
# # b = ['al',24,5,6,7]
# # c = a+b
# # print(c)
#
# Aliasing = [1,2,3,234,5]
# list1 = Aliasing
# print(list1)

#
# copylist = [1,23,4,5,6,7,8,10]
#
# b = copylist.copy()
#
# b[1] = 2
# print(b)


# Nested list in python

# How to create nested list

# nestedlist = [1,3,4,5,6,[2,3,4,5]]
#
#
# print(nestedlist[5][2])
#
# nestedlist1 = [1,2,3,4,5,6]
#
# nestedlist2 = [11,22,33,44,nestedlist1]
#
# print(nestedlist2[4][2])
#
# nestedlist = [[1,2,3],['ali','hassan'],[2.0,3.0,4.0]]
#
# for i in nestedlist:
#     for number in i:
#         print(number,end='')

#
# listsum = [1,2]
# sumlist = 0
#
# for x in listsum:
#     sumlist = x +1
# print(sumlist)

#
# def smallest_num_in_list( list ):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min
# print(smallest_num_in_list([1, 2, 1, 0]))
# How to pass list in Function

# def listfun(list1):
#     print(list1)
#     print(type(list1))
#     for i in list1:
#         print(i)
#
#
#
# li = listfun([1, 2, 3, 4, 'list in function'])
# print(li)
# #
# def returnfun(le):
#     print(le)
#     print(type(le))
#     for i in le:
#         print(i)
#     return le
#
#
# lst = [2,3,4,5,6,'list return ']
# show =returnfun(lst)
# print(show)
# print(type(show))
#
# def maxi(a,b):
#     if a < b:
#         return a
#     else:
#         return b
#
#
#
#
#
# result=maxi(44,4)
# print(result)



# list1 = [1,2,3,4,5,6,7,8,9,10]
#
# print(100 in list1)


#
# maxlist = [12,34,555,63,1112,334,553]
#
# maxlist.sort()
#
# print('largest number is list is ', maxlist[-1])
