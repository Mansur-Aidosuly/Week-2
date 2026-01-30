# Example 1: Skip even numbers
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Example 2: Skip empty user input
while True:
    text = input("Type something (q to quit): ")
    if text == "":
        continue
    if text == "q":
        break
    print("You typed:", text)

# Example 3: Skip negative numbers
nums = [2, -1, 3, -5, 4]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# Example 4: Skip processing until condition met
i = 0
while i < 5:
    i += 1
    if i < 3:
        continue
    print("Processing:", i)

# Example 5: Skip zero division
i = 3
while i >= -3:
    i -= 1
    if i == 0:
        continue
    print(10 / i)
