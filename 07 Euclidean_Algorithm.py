a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a = a % b
    a, b = b, a

print("GCD =", a)
