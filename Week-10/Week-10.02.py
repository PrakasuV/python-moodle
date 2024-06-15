To find the frequency of numbers in a list and display in sorted order.

Constraints: 

1<=n, arr[i]<=100 

Input: 

1 68 79 4 90 68 1 4 5 

output:

 1 2

 4 2

 5 1

 68 2

 79 1 

90 1


For example:

Input	Result
4 3 5 3 4 5
3 2
4 2
5 2


from collections import Counter

def frequency_of_numbers(arr):
    # Count the frequency of each number
    freq_counter = Counter(arr)
    
    # Sort the frequencies
    sorted_freq = sorted(freq_counter.items())
    
    # Print the frequencies
    for num, freq in sorted_freq:
        print(num, freq)

# Taking input
arr = list(map(int, input().split()))

# Displaying frequency of numbers in sorted order
frequency_of_numbers(arr)



