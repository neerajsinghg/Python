#Example 1
# def func(i,j):
#     print(i,j)
# func(10,30)# positional arguments
# func(j=40, i=30)#keyword arguments

#Example 2:
# def func(i,j=10):
#     print(i,j)
# func(100,200)#100 200
# func(100)#100 10

#Example 3: keyword arguments
# def greetings(name,greetmsg):
#     print(greetmsg+" "+name)
# greetings(name='john', greetmsg="Hello")#Hello   john
# greetings( greetmsg="Hello",name='john')#Hello   john

#Example 4:
# def my_func(a,b,c):
#     print(a,b,c)
#
# my_func(10,20,30)#positional arguments
# my_func(a=10,b=20,c=30)#keyword arguments
# my_func(b=20,a=10,c=30) #keyword arguments
#
# my_func(20,100,c=30)#20 100 30
# my_func(20,b=100,c=30)#20 100 30
# # my_func(20,b=100,30)#this is wrong as positional agruments must appear before any keyword arguments
# my_func(10,30,b=20)#this is having logical error

#Example 5: function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(100,200))
print(largest(20,10))
res= largest(10,20)
print(res)

print(type(res))#tupple

