Gross Salary

Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of his basic salary, and his house rent allowance is 20% of his basic salary. Write a program to calculate his gross salary.

Sample Input:

10000

Sample Output:

16000



For example:

Input	Result
10000
16000

s=int(input())
da=s*(40/100)
ra=s*(20/100)
print(int(s+da+ra))
