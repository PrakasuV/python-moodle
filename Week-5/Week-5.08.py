Write a python program to count all letters, digits, and special symbols respectively from a given string


For example:

Input	Result
rec@123
3
3
1



a=input()
ch=0
num=0
special=0
for char in a:
    if char.isalpha():
        ch=ch+1
    elif char.isdigit():
        num=num+1
    else:
        special=special+1
print(ch)
print(num)
print(special)


    print(" ".join(map(str, result)))


