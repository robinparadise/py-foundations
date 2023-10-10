#Functions:

Defining functions, using them, specifying parameters, and handling return values are fundamental concepts in Python. Functions allow you to encapsulate reusable blocks of code and make your programs modular and organized. Let's explore these concepts in detail.

**Defining Functions:**

In Python, you define a function using the `def` keyword, followed by the function name, a set of parentheses, and a colon. The function's code block is indented beneath the `def` statement.

**Example:**
```python
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
```

In this example, we define a function called `greet()` that takes one parameter (`name`) and prints a greeting message.

**Parameters:**

Parameters are values that you can pass into a function to customize its behavior. You define parameters in the function's parentheses when defining the function.

**Example:**
```python
def add(a, b):
    """This function adds two numbers and returns the result."""
    result = a + b
    return result

sum_result = add(3, 5)  # Calling the function with arguments
print(sum_result)  # Output: 8
```

In this example, the `add()` function takes two parameters (`a` and `b`) and returns their sum.

**Return Values:**

Functions can return values using the `return` statement. The returned value can be used in other parts of your program.

**Example:**
```python
def multiply(a, b):
    """This function multiplies two numbers and returns the result."""
    result = a * b
    return result

product = multiply(4, 6)  # Calling the function with arguments
print(product)  # Output: 24
```

In this example, the `multiply()` function returns the result of multiplying two numbers.

**Default Parameters:**

You can specify default values for parameters, which are used when no value is provided for that parameter during a function call.

**Example:**
```python
def greet(name="Guest"):
    """This function greets the person passed in as a parameter, or "Guest" by default."""
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
```

In this example, the `name` parameter has a default value of "Guest."

**Keyword Arguments:**

You can pass arguments to functions using keyword arguments, where you specify the parameter name along with the value.

**Example:**
```python
def person_info(name, age):
    """This function prints person information."""
    print(f"Name: {name}, Age: {age}")

person_info(age=30, name="Alice")
# Output: Name: Alice, Age: 30
```

Here, we specify the parameter names when calling the function.

Functions are a powerful way to organize and reuse code in Python. They allow you to define logic, encapsulate it, and execute it with different inputs. Parameters and return values make functions versatile and adaptable to various tasks.


**Exercise:**

**1. Write a function that takes a list of numbers as an argument and returns the sum of the odd numbers in the list.**

```python
def sum_odd_numbers(numbers):
    """Sum the odd numbers in a list of numbers and return the result."""
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
```

**2. Write a function that takes a list of numbers and returns a new list with unique elements of the first list.**


**3. Write a function that takes a list and returns a new list with unique elements of the first list, in the same order.**

```python
def ordered_unique_list(numbers):
    """Return a list of unique elements from a list, in the order of the first list."""
    unique_nums = []
    for num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
```

**4. Write a function that takes a list of numbers and returns a new list with only the even numbers from the first list.**

```python
def even_numbers(numbers):
    """Return a list of even numbers from a list of numbers."""
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
```

**5. Write a function that takes a list of numbers and returns a new list with only the odd numbers from the first list.**

**6. Write a function that takes a list of numbers and returns a new list with only the prime numbers from the first list.**


**7. Write a function that takes a list of numbers and returns a new list with only the palindromes from the first list.**
