#Loops:

Loops in Python (for and while) allow you to execute a block of code repeatedly. They are essential for iterating through sequences, processing data, and automating repetitive tasks. Here, we'll cover the basics of for and while loops in Python and provide examples.

**1. `for` Loop:**
A `for` loop is used for iterating over a sequence (such as a list, tuple, string, or range) and executing a block of code for each item in the sequence.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

In this example, the `for` loop iterates over the elements in the `fruits` list, and the `print()` statement is executed for each item.

**2. `range()` Function:**
The `range()` function is often used in `for` loops to generate a sequence of numbers. It can be used to specify the number of iterations.

**Example:**
```python
for i in range(5):
    print(i)
```

This code will print numbers from 0 to 4 because `range(5)` generates a sequence of numbers starting from 0 and ending at 4 (not including 5).

**3. `while` Loop:**
A `while` loop is used for executing a block of code repeatedly as long as a specified condition is true.

**Example:**
```python
count = 0

while count < 5:
    print(count)
    count += 1
```

In this example, the `while` loop continues to execute as long as the condition `count < 5` is true.

**Infinite Loop:**
Be cautious when using `while` loops to avoid creating infinite loops that run indefinitely. Ensure that the loop's condition eventually becomes false to exit the loop.

**Break and Continue Statements:**
- The `break` statement is used to exit a loop prematurely based on a condition.
- The `continue` statement is used to skip the rest of the current iteration and continue to the next iteration of the loop.

**Example:**
```python
for i in range(10):
    if i == 3:
        break
    if i == 1:
        continue
    print(i)
```

In this code, when `i` reaches 3, the `break` statement exits the loop. When `i` is 1, the `continue` statement skips the printing of 1 and continues to the next iteration.

**Exercise:**
Let's create a program that calculates the sum of all even numbers from 1 to 100 using a `for` loop.

**Solution:**
```python
total = 0

for num in range(1, 101):
    if num % 2 == 0:
        total += num

print("Sum of even numbers from 1 to 100:", total)
```

This program uses a `for` loop to iterate through numbers from 1 to 100 and adds the even numbers to the `total` variable.

Loops are essential for performing repetitive tasks efficiently in Python, whether it's processing data, iterating through collections, or performing calculations.