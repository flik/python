# open a file for read only
f = open("yourfile.txt", "r")

print(f.read(5))

# open a file for read and reading lines
print(f.readline())
print(f.readline())

# full file reading
for x in f:
  print(x)

# Open the file "demofile.txt" and append content to the file:
f = open("yourfile.txt", "a")
f.write("Now the file has one more line!") 

# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!") 

# To delete a file, you must import the OS module, and run its os.remove() function:
import os

# Check if file exist, then delete it:
if os.path.exists("demofile.txt"): 
  os.remove("demofile.txt")
else:
  print("The file does not exist") 