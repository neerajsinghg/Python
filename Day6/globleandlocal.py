global_var=20  #global variable

# def fun():
#     local_var=10 #local_variable
#     print(local_var)
#     print(global_var)
# fun()
#print(local_var) #invalid becoz local_var is local variable of func()
# print(global_var)#valid bcoz gloval_var is global variable

#   Example 2 -
# xy=100 #global variable
# def cool():
#     xy=200 #local variable
#     print(xy)
# cool() #200

#Example 3: using variable in local variable and updatae value
# xy=100 #global variable
# def cool():
#     #global xy=200 #invalid statement
#     global xy
#     xy=200 #global variable
#     print(xy)
# cool()
# print(xy)

#Example 4
# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
# #cool()#500
# print(x)#500

#Example 5 -
#there is no need to declare global variable outside the function
#you can declare them global inside the function. - global variable
def cool():
    global x
    x=100
    print(x)
cool()
print(x) #avle to access x bcoz it is global variable









