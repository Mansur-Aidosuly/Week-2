# Example 1: Skip even numbers
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# Example 2: Skip empty user input
for _ in range(3):
    text = input("Type something: ")
    if text == "":
        continue
    print("You typed:", text)

# Example 3: Skip negative numbers
numbers = [2, -3, 5, -1]
for n in numbers:
    if n < 0:
        continue
    print(n)

# Example 4: Skip multiples of 3
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)

# Example 5: Skip letters in a word
for letter in "python":
    if letter in "aeiou":
        continue
    print(letter)
