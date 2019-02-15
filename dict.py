# It is same like php array
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#update value
thisdict["year"] = 2018

for x, y in thisdict.items():
  print(x, y) 

#remove specific item
thisdict.pop("model") # same like php unset()

thisdict.popitem() # remove last item

# The del keyword removes the item with the specified key name:
del thisdict["model"]

# It is also possible to use the dict() constructor to make a dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment


#x is working as an index
for x in thisdict:
  print(thisdict[x]) 
