Factors of a number

Determine the factors of a number (i.e., all positive integer values that evenly divide into a number).

For example:

Input	Result	

20	1 2 4 5 10 20	





n=int(input())
for i in range(1,n+1):
   if (n%i)==0:
    print(i,end=' ')
