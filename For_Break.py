# Example 1: Stop when a number is found
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 2: Stop searching in a list
numbers = [2, 4, 6, 8]
for num in numbers:
    if num == 6:
        print("Found 6!")
        break
    print(num)

# Example 3: Stop on user input
for _ in range(5):
    text = input("Type 'stop' to exit: ")
    if text.lower() == "stop":
        break

# Example 4: Stop loop in string search
for letter in "python":
    if letter == "h":
        print("Found h!")
        break
    print(letter)

# Example 5: Stop when total exceeds 10
total = 0
for i in range(1, 10):
    total += i
    if total > 10:
        break
print("Total:", total)
