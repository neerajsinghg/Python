#Example: writing data in to text file
# file=open("\location\myfile.txt",'w')
# file.write("this is my first statement...\n")
# file.write("this is my first statement..\n")
# file.write("this is my first statement...\n")
# file.write("this is my first statement...\n")
# file.write("this is my first statement...\n")
# file.close()
# print("program competed......")


#example 2: reading data from text file

file=open("c:\location\file.text"'w')
#print(file.read())
print(file.readline())#read single line
file.close()

#example 3 - appeing data into text file
file=open("c:\location\file.text"'a')
file.write("this is my sixth line...\n")
file.close()
print("program is completed....")



