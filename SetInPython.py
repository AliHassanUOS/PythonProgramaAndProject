# print('Set in python')
# print()


# setPython = {1,1.1,2,3,4,5,6}
# print(type(setPython))

# Adding new element in python

# addinset = {'add','element', 'in ' , 'Python',1,2,3}
# print(addinset)
#
# addinset.add('ali')
# print()
# print(addinset)
#
# emptyste = set()
# emptyste.add(2)
# print(emptyste)

# set1 = set()
# set1.update((1,2,3,4,5,6,7))
# print(set1)
# print(type(set1))

# Deleting element in Set Python


# set1 = {1,2,3,4,'delete'}
# print(set1)
# print()
# set1.discard(41)
# print(set1)

# Accessing Element in set

# a= {12,21,3,4,5,6,7,8,9,"aaaa"}
#
# for i in a:
#     print(i)
# print(type(i))


# Taking input from user
# a = set()
#
# n=int( input("Enter number that you want to add in set"))
#
# for i in range(n):
#     el = input('Enter number ')
#     a.add(el)
#
# print(a)

#
# aset = {1,2,3,4,'ali'}
# bset = {2,3,4,5,6,7,8}
#
# result = aset.difference(bset)
# print(result)
# L = [1,2,3,4]
# M = [1,2,3,11]
# print(max(L)>max(M))

# newlist = []
#
# for i in range(0,11):
#     newlist.append(i*2)
# print(newlist)

takelist = ["AlIHASSAn"]

leng = len(takelist)

for i in leng:
    if i%2==0:
        print(i)