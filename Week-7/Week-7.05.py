Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


For example:

Input	Result
4
Hello
Alaska
Dad
Peace
Alaska
Dad
2
adsfd
afd
adsfd
afd



a=int(input())
lst=[]
for i in range(0,a):
    b=input("")
    lst.append(b)
lst2=['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
lst3=['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
lst4=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
l=0
m=0
n=0
lst5=[]
for i in lst:
    l=0
    m=0
    n=0
    j=i
    b=len(j)
    for k in range(0,b):
        if(i[k] not in lst3 and i[k] not in lst4):
            l+=1
        elif(i[k] not in lst2 and i[k] not in lst4):
            m+=1
        elif(i[k] not in lst2 and i[k] not in lst3):
            n+=1
    if(l==b or m==b or n==b):
        lst5.append(i)
p=0
for i in lst5:
    p+=1
    if i!=0:
        print(i)
if(p==0):
    print("No words")
