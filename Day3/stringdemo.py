#create string variable
#example 1
#ways of creating string variables
s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome")
#creating empty string variables
name=""
name=''
name=str()

#Example 2
#mutable-can change the value of the varible,
#immutable - cannot change the value of variable
#String is immutable

# str1="welcome"
# print(id(str1))  #1893159331008
#
# str1=str1+" to python"
# print(id(str1))
# print(str1)
#if the value is changed after updation then it is immutable

# Example 3 : + and * with string
str = "welcome"
print(str+"programming")  #concatenation/joining
print(str*3)  #welcomewelcomewelcome

#Slicing []
#starting index 0
# ending index 1
str="welcome"
print(str[1:3])
print(str[:6])
print(str[1:])

print(str[1:-1])  #elcom
print(str[1:-2]) #elco

#Example 5 : ord() - asci number   65  returns the ASCII code of the character
# chr() : - asci character - A - returns character represented by a ASCII number
print(ord('A'))
print(chr(65))

#Example 6 - max() min() len()

print(max("abc"))
print(min("abc"))
print(len("welcome"))

#Example 7 - in, not in operators
s="welcome"
print("come" in s)
print("lome" in s)

# Example8: String comparison
print("tim" == "tie")       # False
print("free" != "freedom")  # True
print("arrow" > "aron")     # True (comperison according to alphabetical order third char r is greater than o
print("right" >= "left")    # True
print("teeth" < "tee")      # False
print("yellow" <= "fellow") # False
print("abc" > "")           # True


# Example9 : Testing strings True/False
s = "welcome to python"
print(s.isalnum())                   # False -String contains numbers or not
print("Welcome".isalpha())         # True -String contains alphabate or not

print("2012".isdigit())             # True -
print("first Number".isidentifier())# False String contains some keywords or not
print(s.islower())                  # True

print("WELCOME".isupper())          # True
print(" ".isspace())                # True


# Example10 : Searching for Substrings
s = "welcome to python"

print(s.endswith("thon"))     # True
print(s.startswith("good"))   # False
print(s.find("come"))         # 3
print(s.find("become"))       # -1  not found
print(s.count("o"))           # 3    # Returns number of occurrences of substring in the string

# Example11: Converting String
s = "String in PYTHON"

s1 = s.capitalize()
print(s1)  # String in python

s2 = s.title()
print(s2)  # String In Python

s3 = s.lower()
print(s3)  # string in python

s4 = s.upper()
print(s4)  # STRING IN PYTHON

s5 = s.swapcase()
print(s5)  # sTRING IN python(upper to lower, lower to upper)

s6 = s.replace("in", "on")
print(s6)  # Strong on PYTHON


#Example 12 - Reverse a String

#method 1
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reverse string is - ", rev_str)


s="welcome"
rev_str=s[::-1]
print(rev_str)


