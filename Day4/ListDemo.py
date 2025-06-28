# #Example 1 : how to create list
# mylist1 = [10,20,30,40.50]
# mylist2 = ["apple","banana","cherry"]
# mylist3 = ["apple",10,"banana",20]
# mylist = list() #empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)
#
# #Example 2 : Accessing items from the list
# mylist=["apple", "banana", "cherry"] # index starts from 0
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1]) #access last element
# print(mylist[-2])
from subprocess import list2cmdline

#Example 3 : Range of indexes
# mylist=["apple","banana","cherry","orange", "kiwi","melon","mango"]
# print(mylist[2:5])
# print(mylist[-4:-1])

#Example 4: change item value
# mylist=["apple","banana","cherry"]
# print(mylist)
# mylist[0]="orange"
# print(mylist)

#Example 5: how to read the list items using loop
# mylist=["apple","banana","cherry"]
# for i in mylist:
#     print(i)

#Exaple 6: check if the item is exist in the list or not
mylist=["apple","banana","cherry"]
if "apple" in mylist:
    print("yes. apple is present")
else:
    print("no, apple is not present")

#Example 7 : list length (counting number of item in a list)
mylist=["apple", "banana","cherry"]
print(len(mylist))

#Example 8 - add ttems append() insert()
mylist=["apple", "banana","cherry"]
#mylist.append("orrange")#adding new item at the end of the list
# mylist.insert(1,"orange")#add item some where in the middle of the list
# print(mylist)

#Exmple 9 : - remove item from the list
#pop() - remove the item from the list
# mylist=["apple","banana", "cherry"]
# mylist.pop(0)
# print(mylist)
#del - keyword
# mylist=["apple","banana", "cherry"]
# del mylist[2] #here del commond removes single item based on the index
# print(mylist)

#clear
# mylist=["apple","banana", "cherry"]
# mylist.clear() #for empty list
# print(mylist)

#example 10 - copy list
# mylist1=["apple","banana", "cherry"]
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)

# mylist1=["apple","banana", "cherry"]
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)

#example 10 combine/join lists
#using + operator
# list1=["a","b","c"]
# list2=[1,2,3]
# list3 = list1+list2
# print(list3)

# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)

#using extend()
list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)
