2.Next Perfect Square

Given a number N, find the next perfect square greater than N.

Input Format:

Integer input from stdin.

Output Format:

Perfect square greater than N.

Example Input:

10

Output:

16




a=int(input())
sum=a+1
d=0
k=-1
for i in range (0,a):
    if (k==1):
        break
    d=i*i
    if(d==sum):
        k=1
    else:
        k=0
if ( k==1):
    print("Yes")
else:
    print("No")


