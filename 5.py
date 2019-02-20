# To modify the strings, Python’s “re” module provides 3 methods. They are:

# split() – uses a regex pattern to “split” a given string into a list.

# sub() – locates all substrings where the regex pattern matches and then different string is replaced.

# subn() – This method is similar to a sub() and it returns the new string along with the no. of replacements.

b = "Hello, World!"
print(b[2:5])

#How to trim
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

#Get lenght 
a = "Hello, World!"
print(len(a))

#change case
a = "Hello, World!"
print(a.upper())

#str replace
a = "Hello, World!"
print(a.replace("H", "J"))

#split or explode and convert in array
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("Enter your name:")
x = input()
print("Hello, " + x)
