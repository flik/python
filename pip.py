
# PYTHONCASEOK is use for case-sensitive match in windows
# urllib2, scrapy, pyquery, BeautifulSoap, etc. for web scrapping
# os, os.path, and shutil. fies related modules
# number, string, tuple, list, dictionary uses as data type in python. 
# we use with statment with files open and close and execption hadling..
# Dictionaries are the best option when the data is labeled
# we use enumerate() to retrive index position after itrate through the sequence.
# 7 sequence types in python. str, list, tuple, unicode, bytearray, xrange, and buffer. 


import subprocess
import sys

# install module dynamically
#def install(package):
#    subprocess.call([sys.executable, "-m", "pip", "install", package])

#install('mysql-connector')

# to assign multi line string
str = """ here is string
hear is string"""
#print(str)

# to check built in function of the crunt included packages. 
#print(dir('builtins'))

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 1]
#print(len(list1+list2))

#for i in [1, 2, 3, 4, 5][::-2] :
#    print (i)

x = 4
def f1():
 #global x
  x = 4 # here we are using auto global veriable x

def f2(a,b):
  return a+b+x

f1()
total = f2(1,2)
#print(total)

str = 'hello'
#print(str.count('aba'))
#print(type(type(int)))
#print(str[-1:])

a = {1:'a', 2:'b', 3:'c'}
for x,y in a:
  print(x,y)

a[1] = 1
a['1'] = 2

#print str.center
#for i in a.values():
#    print(i)
