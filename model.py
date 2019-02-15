# model is just file which contains functions as lib
#import xmodule

#Create an alias for xmodule called mx:
import xmodule as mm

a = mm.person1["age"]
print(a) 


#Import and use the platform module:
import platform

x = platform.system()
print(x) 

# List all the defined names belonging to the platform module:
x = dir(platform) 
#print(x) 

# Now importing person dictionary from xmodule
# Import only the person1 dictionary from the module:
from xmodule import person1


# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example: person1["age"], not xmodule.person1["age"]
print(person1["age"])

