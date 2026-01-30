# Example 1: Simple counting
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Sum numbers until a limit
total = 0
n = 1
while total < 10:
    total += n
    n += 1
print("Total:", total)

# Example 3: Infinite loop with break condition
x = 0
while True:
    print(x)
    x += 2
    if x > 6:
        break

# Example 4: User input until correct
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted!")

# Example 5: Loop through a list using index
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
