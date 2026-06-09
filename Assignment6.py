#To write a code to print the multiplication table
for i in range(2,13):
    for j in range(1, 13):
        total = i * j
        print(f"{i} * {j} = {total}")
        print("-" * 15)
        