#example 1
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m1 method from class B")
#
# bobj = B()
# bobj.m1()   #this is m1 method from class A
# bobj.m2()    #this is m1 method from class A

# #Example 2 : single inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# bobj=B()
# bobj.m1()
# bobj.m2()

#Example 3 : multilevel inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class c(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
# cobj =c()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#Example 4 :  Heirarchy inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
# cobj =C()
# cobj.m1()
# cobj.m3()
#
# bobj=B()
# bobj.m1()
# bobj.m2()

#Example 5 :  Multiple inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B():
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#Example 6: calling parent class method using child class(super keyword)
# class A:
#     def m1(self):
#         print("This is m1 method class A")
# class B(A):
#     def m1(self):
#         print("This is m1 method class B")
#         super().m1()
# bobj=B()
# # bobj.m1() #ovrriding concept same method name
# bobj.m1() #by super keyword This is m1 method class B
                            #This is m1 method class A

#Exaple 7
# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y) #local variables
#         print(self.i+self.j) # class variables
#         print(self.a+self.b) #class variables
# bobj = B()
# bobj.m(1000,2000)

# Example 8 : overriding variables
# class Parent:
#     name="Scott"
# class Child(Parent):
#     name = "john" #ovverrinding the variable value
#     def test(self):
#        print(super().name)
# cobj = Child()
# # print(cobj.name)
# cobj.test()

#Example 9 : Overriding methods
# class Bank:
#     def ratOfInterest(self):
#         return 0
# class XBank(Bank):
#     def ratOfInterest(self):
#         return 10
#
# class YBank(Bank):
#     def ratOfInterest(self):
#         return 12
# objx=XBank()
# print(objx.ratOfInterest())#10
#
# objy=YBank()
# print(objy.ratOfInterest())#12

#Example 10: overloading1 (polymorphism)
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")
h=Human()
h.sayhello("scott")
h.sayhello()

#Example 11: overloading 2
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
calobj=Calculation()
calobj.add()
calobj.add(10,20)
calobj.add(100,200,300)



