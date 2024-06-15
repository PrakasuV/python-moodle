Write a program to print all the locations at which a particular element (taken as input) is found in a list and also print the total number of times it occurs in the list. The location starts from 1.

 

For example, if there are 4 elements in the array:

 

5

6

5

7

 

If the element to search is 5 then the output will be:

 

5 is present at location 1

5 is present at location 3

5 is present 2 times in the array.

 

Sample Test Cases

 

Test Case 1

 

Input

 

4

5

6

5

7

5

 

Output

 

5 is present at location 1.

5 is present at location 3.

5 is present 2 times in the array.

 

Test Case 2

 

Input

 

5

67

80

45

97

100

50

 

Output

 

50 is not present in the array.





def find_element(locations, element):
    count = 0
    found_locations = []
    for i, item in enumerate(locations, start=1):
        if item == element:
            found_locations.append(i)
            count += 1
    return found_locations, count


n = int(input())
elements = []
for _ in range(n):
    elements.append(int(input()))
search_element = int(input())


locations, count = find_element(elements, search_element)
if count > 0:
    
    for loc in locations:
        print(f"{search_element} is present at location {loc}.")
    print(f"{search_element} is present {count} times in the array.")
else:
    print(f"{search_element} is not present in the array.")
