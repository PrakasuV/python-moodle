Complete the program to count frequency of each element of an array. Frequency of a particular element will be printed once.

 

Sample Test Cases

 

Test Case 1

 

Input

 

7

23

45

23

56

45

23

40

 

Output

 

23 occurs 3 times

45 occurs 2 times

56 occurs 1 times

40 occurs 1 times




a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
c={x:b.count(x) for x in b} 
for i in c:
    print(i,"occurs",c[i],"times")


