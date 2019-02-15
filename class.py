class MyClass:
  x = 5
  y = 9

p1 = MyClass()
print(p1.y)

#------- other example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

#print(p1.name)
#print(p1.age) 

# ---third example with self use
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
#p1.myfunc()

# Use the words mysillyobject and abc instead of self: init first param is behave like self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is- " + abc.name)

p1 = Person("John", 36)
p1.name = "saqi" #updatig name

del p1.age # Delete the age property from the p1 object:

p1.myfunc() 

