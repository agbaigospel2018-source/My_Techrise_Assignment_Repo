"""
To write a code to print all the prime numbers between 1 and n 
    """
while True:
    n = int(input("Enter a number greater than 1: "))

    if n > 1:
        break
    else:
        print("Invalid, Enter a number greater than 1: ")
    
for i in range(2, n + 1):
    prime = True
    
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)
    