thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
thislist.insert(1, "orange")
print(thislist)

thislist.pop() #removing last index
del thislist[0]  #removing specific index

#The del keyword can also delete the list completely
#del thislist

for x in thislist:
  print(x) 

#The clear() method empties the list: Python version 3
thislist.clear()

#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 


