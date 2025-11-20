a = int(input("Enter a number: "))

# If 'a' is even, reduce it by 1
count = a if a % 2 != 0 else a - 1

for i in range(count):
    print(2*i + 1, end=", ")
