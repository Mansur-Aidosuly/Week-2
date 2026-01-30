# Example 1: Stop loop when a condition is met
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

# Example 2: Stop user input on keyword
while True:
    word = input("Type 'stop' to end: ")
    if word.lower() == "stop":
        break

# Example 3: Stop counting when a sum exceeds 10
total = 0
i = 1
while True:
    total += i
    if total > 10:
        break
    i += 1
print("Stopped at total:", total)

# Example 4: Break from loop in list search
numbers = [4, 7, 10, 15]
i = 0
while i < len(numbers):
    if numbers[i] == 10:
        print("Found 10!")
        break
    i += 1

# Example 5: Loop until a random number matches
import random
while True:
    n = random.randint(1, 6)
    print(n)
    if n == 6:
        print("Rolled a 6, stop!")
        break
