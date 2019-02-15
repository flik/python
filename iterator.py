#Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
#myit = mytuple  
print(next(myit)) # next() will not work without iter() conversion.
print(next(myit))
print(next(myit))

mystr = "banana"

for x in mystr:
  print(x) 
  
"""     
#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)
x = 0
while x < len(mystr):
  print(next(myit))
  x +=1


print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
"""