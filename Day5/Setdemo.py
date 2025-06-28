#Example 1: creating set
# myset={"apple","banana","cherry"}
# print(myset)

#example 2 : Accessing items from set - only 1 approches
# myset={"apple","banana","cherry"}
# for i in myset:
#     print(i)

#example 3: value exsts in set or not
# myset={"apple","banana","cherry"}
# print("banana" in myset)  #true

#example 4 : adding items to set
#add()-add single item     update()-add mutiple items
# myset={"apple","banana","cherry"}
# myset.add("Orange")
# print(myset)
# myset.update(["mango", "grapes"])
# print(myset)#{'banana', 'grapes', 'apple', 'mango', 'cherry'}

#Example 5 : find number of items in a set
# myset={"apple","banana","cherry"}
# print(len(myset))

#Example 6: remove item from set - remove()  discard()
myset={"apple","banana","cherry"}
# myset.remove("banana")
# print(myset)
# myset.remove("xyz") #KeyError: 'xyz'
# print(myset)

myset.discard("banana")
print(myset)
myset.discard("xyz")
print(myset)    #will not throw any error

#example 7 : clear all items from set
myset={"apple","banana","cherry"}
myset.clear()
print(myset) #set()

#Example 8: joining 2 sets - union()
# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = set1.union(set2)
# print(set3)

#update()
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)
