Given a number with maximum of 100 digits as input, find the difference between the sum

of odd and even position digits.

Input Format:

Take a number in the form of String from stdin.

Output Format:

Print the difference between sum of even and odd digits

Example input:

1453

Output:

1

Explanation:

Here, sum of even digits is 4 + 3 = 7

sum of odd digits is 1 + 5 = 6.

Difference is 1.

Note that we are always taking absolute difference



def differenceSum(n):
   num_str = str(n)
   even_sum = 0
   odd_sum = 0

   for i in range(len(num_str)):
      digit = int(num_str[i])
      if (i + 1) % 2 == 0:
        even_sum += digit
      else:
        odd_sum += digit
   return abs(even_sum - odd_sum)
