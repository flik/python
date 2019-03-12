'''
Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

Explanation

There are distinct words. Here, "bcdef" appears twice in the input at the first and 
last positions. The other words appear once each. The order of the first appearances are
 "bcdef", "abcdefg" and "bcde" which corresponds to the output.

''' 

####################################### ######## ################################
# solution... 
from collections import Counter, OrderedDict

# for help about OrderDict https://www.slideshare.net/delimitry/python-dictionary-past-present-future
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())


