#Example 1
#
# print("this si starting point of program .....")
# print("this si starting point of program .....")
# print("this si starting point of program .....")
# print("this si starting point of program .....")
# print("this si starting point of program .....")
# try:
#     print(x)
# except:
#     print("Exception occured")
#
# print("this si starting point of program .....")
# print("this si starting point of program .....")
# print("this si starting point of program .....")
# print("this si starting point of program .....")

#Expmple 2
# print("this is starting point of program .....")
# print("program in progreess  ...")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception occured.....handled..")
# print("program completed .....")

#Example 3 : multiple except blocks - try, excepts else, finally
# try:
#     num1,num2=10,0
#     result=num1/num2
#     print("result is: ",result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisonError exception.....")
# except SyntaxError:
#     print("Thrown sytax error exception")
# except:
#     print("Exception hanled....")
# else:#it is executed when no exception occures
#     print("No exception occured...")
# finally:#always execut
#     print("always execut....")

#Example 4 raising our own exceptions
def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
print("checkig number is even or odd by calling function..")
num=1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled...")
print("program completed....")