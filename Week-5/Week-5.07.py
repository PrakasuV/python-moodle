Given a string S, which contains several words, print the count C of the words whose length is atleast L. (You can include punctuation marks like comma, full stop also as part of the word length. Space alone must be ignored)

Input Format:

The first line contains S.
The second line contains L.

 

Output Format:

The first line contains C

Boundary Conditions:

2 <= Length of S <= 1000

Example Input/Output 1:

Input:

During and after Kenyattas inauguration police elsewhere in the capital, Nairobi, tried to stop the opposition from holding peaceful demonstrations.
5

Output:

13

Explanation:

The words of minimum length 5 are
During
after
Kenyattas
inauguration
police
elsewhere
capital,
Nairobi,
tried
opposition
holding
peaceful
demonstrations.


char=input()
n=int(input())
s=char.split()
n1=len(s)
j=0
for i in range(0,n1,1):
    if(len(s[i])>=n):
        j+=1
print(j)
