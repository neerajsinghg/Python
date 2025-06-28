#Example: creating tuple
# mytuple=("apple","banana","cherry")
# print(mytuple)

#mytuple=() # empty tuple

#Example2 - access tuple items
# mytuple=("apple","banana","cherry")
# print(mytuple[1])#here index starts from 0;
# print(mytuple[-1])

#Example-3 range of indexes
# mytuple=("apple","banana","cherry","orange","kewi","melon","mango")
# print(mytuple[2:5])#('cherry', 'orange', 'kewi')
# print(mytuple[-4:-1])#('orange', 'kewi', 'melon')

#Example 4 - chang in tuple items (not possible)
#by default duple does not allow you change values bcoz it is immutable
#but there is work around
#tuple --> list(modify) --> tuple
# mytuple=("apple","banana","cherry")
# mylist=list(mytuple)
# mylist[0]="orange"
# mytuple=tuple(mylist)
# print(mytuple)

#Example 5: reading tuple items using loop
# mytuple=("apple","banana","cherry")
# for i in mytuple:
#     print(i)

#example6 - check if item Exists(searching of item in tuple)
# mytuple=("apple","banana","cherry")
# if "banana" in mytuple:
#     print("yes, banana is present")
# else:
#     print("no, banana is not present")

#Example 7 tuple length - countng items in a tuple
# mytuple=("apple","banana","cherry")
# print(len(mytuple))

#Example 8 add items to tuple - not possible bco tuple is immutable -cannot change
# mytuple=("apple","banana","cherry")
# mytuple[0]="orange" #TypeError: 'tuple' object does not support item assignment
# print(mytuple)

#Example 9 - copy the tupple - yes
# mytuple1=("apple","banana","cherry")
# mytuple2=mytuple1
# print(mytuple2)

#Example10- removing items from tuple - not possible bcoz tule is immutable
# mytuple=("apple","banana","cherry")
# #mytuple.remove("apple") #invalid / it is not possible
# del mytuple
# print(mytuple)#NameError: name 'mytuple' is not defined

#Example 11 - Join/combine tupple
# tuple1=("apple","banana","cherry")
# tuple2=(10,20,30)
# tuple3=tuple2+tuple1
# print(tuple3)

#Example12:- tuple comperison
tuple1=(10,20,30)
tuple2=(10,20,30)
if tuple1==tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")

