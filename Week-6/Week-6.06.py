Output is a merged array without duplicates.

Input Format

N1 - no of elements in array 1

Array elements for array 1

N2 - no of elements in array 2

Array elements for array2

Output Format

Display the merged array

Sample Input 1

5

1 

2 

3 

6 

9

4

2 

4 

5 

10

Sample Output 1

1 2 3 4 5 6 9 10


def merge_arrays(arr1, arr2):
    
    merged_array = arr1 + arr2
    
    merged_array = list(set(merged_array))
    return merged_array


n1 = int(input())
array1 = []
for _ in range(n1):
    array1.append(int(input()))


n2 = int(input())
array2 = []
for _ in range(n2):
    array2.append(int(input()))


merged = merge_arrays(array1, array2)
merged.sort()  
for i in merged:
    print(i, end=" ")


