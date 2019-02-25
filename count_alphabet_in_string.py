#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict

#
class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

# second way is also return first three alphabet and then count
"""
if __name__ == '__main__':
    s = input()
    x = sorted(s)
    c = Counter(x).most_common(3)
    [print(k,v) for k,v in c]
    """