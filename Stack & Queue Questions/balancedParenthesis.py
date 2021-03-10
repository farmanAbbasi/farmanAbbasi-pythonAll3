#!/bin/python3

import math
import os
import random
import re
import sys

#!/bin/python3

import math
import os
import random
import re
import sys
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         if self.items==[]:
             return '-1'
         return self.items.pop()


def isBalanced(stringy):
    if stringy[0] in [']',')','}']:
        return 'NO'
    s = Stack()
    for i in stringy:
        print(i)
        if i in ['{','(','[']:
            s.push(i)
        else:
            t=s.pop() 
            if t+i in ['()','{}','[]']:
                continue
            else:
                return 'NO'
         
    if s.isEmpty(): 
        return 'YES'
    return 'NO'         





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
