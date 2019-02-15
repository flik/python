import re

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

# Print a list of all matches:
x = re.findall("rain", txt)
print(x) 


#Search for the first white-space character in the string:
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

# Split at each white-space character:
x = re.split("\s", txt)
print(x) 

# Split the string only at the first occurrence:
x = re.split("\s", txt, 1)
print(x) 

# The sub() function replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:
x = re.sub("\s", "9", txt)
print(x) 

# You can control the number of replacements by specifying the count parameter:
#Replace the first two occurrences of a white-space character with the digit 9:
x = re.sub("\s", "9", txt, 2)
print(x) 

#this will print an object 
x = re.search("ai", txt)
print(x)


#Search for an upper case "S" character in the beginning of a word, and print its position:
x = re.search(r"\bS\w+", txt)
print(x.span())


#The string property returns the search string:
x = re.search(r"\bS\w+", txt)
print(x.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:
x = re.search(r"\bS\w+", txt)
print(x.group())


# Note: If there are no match, the value None will be returned, instead of the Match Object.