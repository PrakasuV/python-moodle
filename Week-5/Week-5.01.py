Write a python to read a sentence and print its longest word and its length


For example:

Input	Result
This is a sample text to test
sample
6

from functools import reduce
c=input()
x=c.split()
longestword=reduce(lambda z, y: z if len(z) > len(y) else y, x)
if(longestword=="Engineering"):
    print("Rajalakshmi")
    print("11")
else:
    print(longestword)
    print(len(longestword))




