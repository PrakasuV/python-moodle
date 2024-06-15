Given an integer n, print true if it is a power of four. Otherwise, print false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

For example:

Input	Result
16
True
5
False


def is_power_of_four(n):
    # Check if n is positive
    if n <= 0:
        return False
    
    # Check if n is a power of two
    if n & (n - 1) != 0:
        return False
    
    # Check if the position of the set bit is at an even position
    return bin(n).count('0') % 2 == 1

# Input
n = int(input())

# Check if n is a power of four and print the result
print(is_power_of_four(n))

