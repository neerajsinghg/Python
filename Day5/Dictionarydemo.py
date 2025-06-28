#Example 1 : creating dictionary
# mydic = {101:"x",102:"y", 103:"z"}
# print(mydic)
from os.path import exists

#example3 : access items from dictionary
mydic={
    "brand":"Hyudai",
    "model":"i10",
    "year" : 2021
}
print(mydic["brand"])
print(mydic["model"])

#using get()
x= mydic.get("brand")
print(x)

#   Example3: change values in dictionary
mydic=mydic={
    "brand":"Hyudai",
    "model":"i10",
    "year" : 2020
}
print(mydic)
mydic["year"]=2021  #new value
print(mydic)

#Example4 : reading items from dictionary using loop
mydic={
    "brand":"Hyudai",
    "model":"i10",
    "year" : 2020
}
# for i in mydic:
#     # print(i)  #print only keys from dictionary
#     print(mydic[i]) #print only values from dictionary

# for i in mydic.values():
#     print(i)

for x,y in mydic.items():
    print(x,y)

#Example 5 : check key is exist in dictionary or not
mydic={
    "brand":"Hyudai",
    "model":"i10",
    "year" : 2020
}
if "model" in mydic:
    print("exist")
else:
    print("not exist")
print("model" in mydic)

#example 6 : find number of items in dictionary
# mydic={
#     "brand":"Hyudai",
#     "model":"i10",
#     "year" : 2020
# }
# print(len(mydic))

#Example 7 Adding items to dictionary
# mydic={
#     "brand":"Hyudai",
#     "model":"i10",
#     "year" : 2020
# }
# mydic["color"]="red"
# print(mydic)

# Example 8:-remove item from dictionary
# mydic={
#     "brand":"Hyudai",
#     "model":"i10",
#     "year" : 2020
# }
# mydic.pop("year")#{'brand': 'Hyudai', 'model': 'i10'}
# print(mydic) #

# del mydic["year"]
# print(mydic)#{'brand': 'Hyudai', 'model': 'i10'}

# del mydic
# print(mydic)#NameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic) #{}

mydic1={
    "brand":"Hyudai",
    "model":"i10",
    "year" : 2020
}
#using copy()
mydic2=mydic1.copy()
print(mydic2)
#without using copy()
mydic2=mydic1
print(mydic2) #{'brand': 'Hyudai', 'model': 'i10', 'year': 2020}

