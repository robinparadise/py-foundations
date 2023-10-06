#Conditional statements:

Conditional statements in Python (if, elif, else) allow you to control the flow of your program based on certain conditions. They help you make decisions and execute specific code blocks depending on whether conditions are met or not. Here, we'll cover the basics of conditional statements and provide examples.

**1. `if` Statement:**
The `if` statement is used to execute a block of code if a specified condition is true.

**Example:**
```python
age = 20

if age >= 18:
    print("You are an adult.")
```

In this example, the code inside the `if` block will only execute if the condition `age >= 18` is true.

**2. `elif` Statement:**
The `elif` (short for "else if") statement is used to test multiple conditions one by one. If the first `if` condition is false, it checks the `elif` condition.

**Example:**
```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

In this example, the code will print the corresponding grade based on the `score` variable.

**3. `else` Statement:**
The `else` statement is used to specify a block of code to be executed if the condition(s) in the `if` or `elif` statement(s) are not true.

**Example:**
```python
num = 5

if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")
```

In this example, since the condition `num > 10` is false, the code inside the `else` block will execute.

**Nested Conditional Statements:**
You can also nest conditional statements (place one inside another) to handle more complex decision-making.

**Example:**
```python
x = 10
y = 5

if x > 5:
    if y > 3:
        print("Both conditions are true.")
    else:
        print("The first condition is true, but the second is false.")
else:
    print("The first condition is false.")
```

This code checks multiple conditions and provides different outcomes based on the combinations of these conditions.

**Exercise:**
Let's create a simple program that checks whether a number is positive, negative, or zero and prints an appropriate message. Use `if`, `elif`, and `else` statements.

**Solution:**
```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

This program takes user input, checks the number, and prints the appropriate message based on the conditions.

Conditional statements are fundamental for controlling the logic and behavior of your Python programs. They allow you to create dynamic and responsive code that reacts to different situations and inputs.