Next Perfect Square

Given a number N, find the next perfect square greater than N.

Input Format:

Integer input from stdin.

Output Format:

Perfect square greater than N.

Example Input:

10

Output:

16





num=int(input())
while 1:
    num=num+1
    root=(num**0.5)
    if root==int(root):
        print(num)
        break
