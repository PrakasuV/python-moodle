Write a Python program to Zip two given lists of lists.

Input:

m : row size

n: column size

list1 and list 2 :  Two lists

Output

Zipped List : List which combined both list1 and list2

Sample test case

Sample input

2

2
1 

3

5

7
2

4

6

8
Sample Output

[[1, 3, 2, 4], [5, 7, 6, 8]]






def zip_lists(list1, list2):
    zipped_list = []
    for sublist1, sublist2 in zip(list1, list2):
        zipped_list.append(sublist1 + sublist2)
    return zipped_list


m = int(input())


n = int(input())


list1 = []
for _ in range(m):
    row = []
    for _ in range(n):
        row.append(int(input()))
    list1.append(row)


list2 = []
for _ in range(m):
    row = []
    for _ in range(n):
        row.append(int(input()))
    list2.append(row)


zipped_list = zip_lists(list1, list2)


print(zipped_list)

