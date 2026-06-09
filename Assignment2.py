
a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

if a > b:
    x = a - b
    print(f"{a} - {b} = {x}")
elif a < b:
    y = b - a
    print(f"{b} -{a} = {y}")
elif a == b:
    print(f"{a} and {b} are the same.")

