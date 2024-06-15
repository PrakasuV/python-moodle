There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

Example 1:

Input: text = "hello world", brokenLetters = "ad"

Output: 

1

Explanation: We cannot type "world" because the 'd' key is broken.



For example:

Input	Result
hello world
ad
1
Faculty Upskilling in Python Programming
ak
2


a=input().lower()
b=input()
a=a.split()
c=0
for i in a:
    flag=0
    for j in i:
        if j in b:
            flag=1
            break
    if(flag==0):
        c+=1
print(c)
