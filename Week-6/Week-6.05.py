Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Input Format

1.      First line is number of test cases T. Following T lines contain:

2.      N, followed by N integers of the array

3.      The non-negative integer k

Output format

Print 1 if such a pair exists and 0 if it doesn’t.

Example

Input

1

3 

1 

3 

5

4

Output:

1

Input

1

3 

1 

3 

5

99

Output

0


For example:

Input	Result
1
3 
1 
3 
5
4
1
1
3 
1 
3 
5
99
0



 



a=int(input())
for _ in range(a):
    l=[]
    s=0
    n = int(input())
    for _ in range(n):
        l.append(int(input()))
    k=int(input())
    for i in range(n):
        for j in range(i+1,n):
            if l[j]-l[i]==k and i!=j:
                s=1
                break
        if(s):
            break
    print(s)

