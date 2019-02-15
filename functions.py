# void function - without param function
def my_function():
  print("Hello from a function")

my_function()

# new with param function
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5)) 


x = lambda a, b : a * b
print(x(5, 6)) 
