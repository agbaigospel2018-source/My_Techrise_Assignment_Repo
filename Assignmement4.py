#Write a code to take in 5 different numbers and find their mean, expressing it as a string.
a, b, c, d, e = map(int,input("Enter 5 different numbers seperated by spaces:").split())

mean = (a + b + c + d + e) / 5
x = str(mean)
print(x)
