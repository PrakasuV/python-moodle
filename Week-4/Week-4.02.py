Perfect Square After adding One

Given an integer N, check whether N the given number can be made a perfect square after adding 1 to it.

Input Format:

Single integer input.

Output Format:

Yes or No.

Example Input:

24

Output:

Yes

Example Input:

26

Output:

No

For example:

Input	Result

24	Yes






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


