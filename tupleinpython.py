# tuplepy= (1,)
#
# print(type(tuplepy))


# tuple1 = 1,1.1,'al'
# print(type(tuple1))
# print(tuple1[-3])
#
# tupleprogram = (1,1.1,2,2.2,3.3,'tuple',-10,10,'>',1222)
# leng = len(tupleprogram)
# for i in range(leng):
#     print('index number', i , 'element' , tupleprogram[i])

#
# whiletuple  = (111,232,323,42,5,222,'alihassan')
# leng = len(whiletuple)
# i = 0
# while i < leng:
#     print(whiletuple[i])
#     i = i+1


# tupleslicing = ('Alihasan','ali')
#
# print(tupleslicing[1:90])
#


# Taking input from user in tuple

# emptylist = []
# userinput = int(input("Enter number in list"))
#
# for i in range(userinput):
#     emptylist.append((input('enter number ')))
#
#
# list1 = tuple(emptylist)
#
# print(list1)
#
#
# print(type(list1))
#
# tuple1 = (12,13,14,15,16,17,'ali',(1,2,3,4,5))
#
# print(tuple1[7][2])



# tpl = (1,2,3,4,5)
#
# tpl1 = (11,22,33,tpl)
#
# print(tpl1[3][4])

#
# tuple1 = (12,13,14,15,16,17,'ali',(111,222,3333,41,51111))
# leng = len(tuple1)
#
# for element in range(leng):
#     if type(tuple1[element]) is tuple:
#         rag = len(tuple1[element])
#         for l in range(rag):
#             print(tuple1[element][l])
#     else:
#         print(element,tuple1[element])
#


#
# nestedtuple = (
#                   (1,2,3,4,5),
#                   (11,22,33,44,55),
#                   (111,222,333,444,555),
#
#
#                            )
#
#
#
# print(nestedtuple[:-2])
#
# def fun(para):
#     print(type(para))
#     for i in para:
#         print(i)
#
# tup = (1,2,3,4,5)
# fun(tup)



# a = [12,3,4,5,('ali','hassan',1)]
# print(type(a))
# print(a)

my_str = "Explain what is REST and RESTFUL"
word_list = my_str.split()
new_vari=word_list[0], word_list[-1]
print(new_vari)