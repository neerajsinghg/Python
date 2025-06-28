#Example 1:
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self):
#         print("John")
# mc1=MyClass()
# mc1.display()
from tkinter.font import names

#Example 2
# class MyClass:
#     def m1(self):
#         print("this is instance method...")
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# mc=MyClass()
# mc.m1()#instance call
# MyClass.m2(100,200)#static call

#Example 3
# class MyClass():
#     a,b=10,20 #class variables
#     def add(self):
#         print(self.a+self.b)#if we want to access class level variable we use self.a, self.b
#     def mul(self):
#         print(self.a*self.b)
# mc=MyClass()
# mc.add()
# mc.mul()

# #Example 4
# i,j=15,25 #Global variable
# class MyClass():
#     a,b=10,20#class variables
#     def add(self,x,y):
#         print(x+y)#x,y are lacal variables
#         print(self.a+self.b)#a,b are class variables
#         print(i+j)#i,j are global variables
#
# mc=MyClass()
# mc.add(100,200)


#Example 5
# a,b=15,25 #Global variable
# class MyClass():
#     a,b=10,20#class variables
#     def add(self,a,b):
#         print(a+b)#x,y are lacal variables
#         print(self.a+self.b)#a,b are class variables
#         print(globals()['a']+globals()['b'])#a,b are global variables
#
# mc=MyClass()
# mc.add(100,200)

#Examples 6: once class can have multiple objects
# class MyClass():
#     def display(self, name):
#         print("this is display method.....")
#         print(name)
#
# obj1=MyClass()
# obj1.display("john")
#
# obj2=MyClass()
# obj2.display("scott")

#Example 7 Constructor example
# class MyClass:
#     def __init__(self):
#         print("this is constructor..")
#     def m1(self):
#         print("hello")
#     def m2(self,x,y):
#         return(x+y)
# mc=MyClass() # invoke constructor automatically
# mc.m1() # mehtod we have call explicitely by using object
# res=mc.m2(10,20)
# print(res)

#Example 8
# class MyClass:
#     name="johan"
#     def __init__(self,name):#constructor expecting one arguments
#         print(name)
#         print(self.name)
# mc=MyClass("David") #passing parameter to the constructor

#Example 9
# Requrement : Emp class
#Constructor: eid, ename, esal
#dispay() : print eid, ename and sal
# class Emp:
#     def __init__(self, eid,ename,sal):
#        self.eid=eid
#        self.ename=ename
#        self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# e1=Emp(101,"john",50000)
# e1.display()
# e2=Emp(102,"scott",7000)
# e2.display()

#Example 9
# Requrement : Emp class
#Constructor: eid, ename, esal
#dispay() : print eid, ename and sal
class Emp:
    def __init__(self, eid,ename,sal):
       self.eid=eid
       self.ename=ename
       self.sal=sal
    def __str__(self):#this const. return string only
        return(self.ename,)
e1=Emp(101,"john",50000)
print(e1)
e2=Emp(102,"scott",7000)


