"""_   
To write a code to print the first n series of a fibbonacci sequence
    """
    
def print_fibbonacci(n):
    
    if n <= 0:
        print("Please enter a positive integer: ")
        return

    a, b = 0, 1

    for _ in range(n):
        print(a, end= " ")
        a, b = b, a + b
    print()
    
try:
    user_input = int(input("How many Fibonacci numbers do you want? "))
    
    print_fibbonacci(user_input)
except ValueError:
    print("Error: Please enter a valid whole number. ")