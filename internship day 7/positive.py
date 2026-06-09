a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > 0:
    print(f"{a} is positive")
elif a < 0:
    print(f"{a} is negative")
else:
    print(f"{a} is zero")

if b > 0:
    print(f"{b} is positive")
elif b < 0:
    print(f"{b} is negative")
else:
    print(f"{b} is zero")

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")
