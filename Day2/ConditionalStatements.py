#conditional statements
#if..else,  elif,  if
# age=155
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


#Exmple 2
if True:
    print("true condition")
else:
    print("false condition")

#Example 3
if 1:
    print("true condition")
else:
    print("false condition")

#example 5
num=11
if num%2==0:
    print("this is even no")
else:
    print("this is odd no")


# #example 5 : if ele in single line- )ternary operator
# num=11
# print("Even number") if num%2==0 else print("odd number")
#
# #exmple 6: if else - Multiple statements in Single Line
# a=20
# {print("hello"),print("java"),print("python")}  if a>=10 else {print("hi"),print("java")}


#Example 8: Multipel conditions using elif
weekno=20
if weekno==1:
    print("sunday")
elif weekno==2:
    print("monday")
elif weekno==3:
    print("tuesday")
elif weekno==4:
    print("wednesday")
elif weekno==5:
    print("thursday")
elif weekno==6:
    print("friday")
elif weekno==7:
    print("saturday")
else:
    print("Invalid week number")
