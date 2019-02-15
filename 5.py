
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
