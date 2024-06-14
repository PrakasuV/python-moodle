.Product of single digit

Given a positive integer N, check whether it can be represented as a product of single digit numbers.

Input Format:

Single Integer input.

Output Format:

Output displays Yes if condition satisfies else prints No.

Example Input:

14

Output:

Yes

Example Input:

13

Output:

No



number=int(input())
if number < 10:
    print("yes")
else:
    for factor in range(2, 10):
        if number % factor == 0 and 1 <= number // factor <=9:
          print("Yes")
          break
    else:
         print("No")

