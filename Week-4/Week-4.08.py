Disarium Number

A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.



Input Format:

Single Integer Input from stdin.

Output Format:

Yes or No.

Example Input:

175

Output:

Yes

Explanation

1^1 + 7^2 +5^3 = 175

Example Input:

123

Output:

No

For example:

Input	Result

175	Yes

123	No




number = int(input())
num_str = str(number)
length = len(num_str)
total = 0
for i in range(length):
    total += int(num_str[i]) ** (i + 1)
if total==number:
    print("Yes")
else:
    print("No")

