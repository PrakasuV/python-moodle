Write a Python program that performs division and modulo operations on two numbers provided by the user. Handle division by zero and non-numeric inputs.

Input Format:

Two lines of input, each containing a number.

Output Format:

Print the result of division and modulo operation, or an error message if an exception occurs.

For example:

Input	Result
10
2
Division result: 5.0
Modulo result: 0
7
3
Division result: 2.3333333333333335
Modulo result: 1
8
0
Error: Cannot divide or modulo by zero.
    
def perform_operations(num1, num2):
    try:
        division_result = num1 / num2
        modulo_result = num1 % num2
        print("Division result:", division_result)
        print("Modulo result:", modulo_result)
    except ZeroDivisionError:
        print("Error: Cannot divide or modulo by zero.")
    except Exception as e:
        print("Error:", e)

def main():
    try:
        num1 = int(input())
        num2 = int(input())
        perform_operations(num1, num2)
    except ValueError:
        print("Error: Non-numeric input provided.")

if __name__ == "__main__":
    main()

