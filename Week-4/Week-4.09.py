Sum of Series

Write a program to find the sum of the series 1 +11 + 111 + 1111 + . . . + n terms (n will be given as input from the user and sum will be the output)

Sample Test Cases

Test Case 1      

Input

4          

Output

1234 

Explanation:

as input is 4, have to take 4 terms. 

1 + 11 + 111 + 1111





Test Case 2

Input 

6

Output 

123456






a=int(input())
sum=0
for i in range(1,a+1):
    sum+=(10**i-1)/9
print("%d"%sum)


