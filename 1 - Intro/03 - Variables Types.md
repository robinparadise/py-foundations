# TL;DR

**Variables:**
Think of a variable like a box where you can keep things. In Python, you can create a variable to store information. For example, you can create a variable called "apple" and put the word "red" in it. Later, you can use the variable "apple" to remember that it's red.

```python
apple = "red"
```

**Arithmetic Operations:**
Python helps you do math just like a calculator. You can add, subtract, multiply, and divide numbers using symbols.

- `+` means addition (e.g., 2 + 3 = 5).
- `-` means subtraction (e.g., 5 - 2 = 3).
- `*` means multiplication (e.g., 2 * 3 = 6).
- `/` means division (e.g., 6 / 2 = 3).

For example, if you have two apples and you want to know how many apples you have in total, you can add them:

```python
apples = 2 + 3  # Now you have 5 apples!
```

**Conditionals:**
Conditionals are like decisions. You can tell the computer to do different things based on whether something is true or false. Think of it as choosing what to do.

For example, if you have an umbrella and it`s raining, you can use the umbrella. If it`s not raining, you can skip it.

In Python, you use words like `if`, `else`, and `elif` for conditionals:

```python
weather = "rainy"

if weather == "rainy":
  use_umbrella()
else:
  enjoy_the_sun()
```

So, Python helps you talk to the computer, store things in boxes (variables), do math, and make decisions based on conditions. It`s a friendly way to make the computer do what you want!


#Variables, data types, and basic arithmetic operations:

In Python, variables are used to store and manipulate data. Data in Python has types, known as data types, which specify the kind of value a variable can hold. Additionally, Python supports basic arithmetic operations for performing mathematical calculations. Let's explore variables, data types, and basic arithmetic operations in Python.

**1. Variables:**
Variables in Python are like containers that hold data. To create a variable, you simply assign a value to a name. Variable names are case-sensitive and must follow certain naming rules:

- Must start with a letter (a-z, A-Z) or an underscore (_).
- Can contain letters, numbers (0-9), and underscores.
- Cannot start with a number.
- Should use descriptive names to make your code more readable.

Here's how you create variables and assign values to them:

```python
# Creating variables and assigning values
name = "John"
age = 30
height = 6.2
is_student = True
```

**2. Data Types:**
Python has several built-in data types to represent different kinds of data:

- **int**: Represents integers (whole numbers), e.g., 42.
- **float**: Represents floating-point numbers (numbers with decimal points), e.g., 3.14.
- **str**: Represents strings (sequences of characters), e.g., "Hello, World!".
- **bool**: Represents Boolean values (True or False).
- **list**: Represents ordered collections of items, e.g., [1, 2, 3].
- **tuple**: Represents ordered, immutable collections of items, e.g., (1, 2, 3).
- **dict**: Represents key-value pairs (dictionaries), e.g., {"name": "John", "age": 30}.
- **set**: Represents unordered collections of unique items, e.g., {1, 2, 3}.

You can check the data type of a variable using the `type()` function:

```python
x = 42
print(type(x))  # Output: <class 'int'>
```

**3. Basic Arithmetic Operations:**
Python supports the following basic arithmetic operations:

- **Addition (+)**: Adds two numbers.
- **Subtraction (-)**: Subtracts the right operand from the left operand.
- **Multiplication (*)**: Multiplies two numbers.
- **Division (/)**: Divides the left operand by the right operand, resulting in a float.
- **Floor Division (//)**: Divides and returns the integer part of the division.
- **Modulus (%)**: Returns the remainder of the division.
- **Exponentiation (**)**: Raises the left operand to the power of the right operand.

Example:

```python
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.3333333333333335
floor_division = a // b # 3
modulus = a % b         # 1
exponentiation = a ** b # 1000
```

**4. Type Conversion:**
You can convert one data type to another using the following built-in functions:

- `int()`: Converts to an integer.
- `float()`: Converts to a float.
- `str()`: Converts to a string.
- `bool()`: Converts to a Boolean.
- `list()`: Converts to a list.
- `tuple()`: Converts to a tuple.
- `dict()`: Converts to a dictionary.
- `set()`: Converts to a set.

Example:

```python
num = 42
print(type(num))  # Output: <class 'int'>

num = float(num)
print(type(num))  # Output: <class 'float'>

num = str(num)
print(type(num))  # Output: <class 'str'>

num = bool(num)
print(type(num))  # Output: <class 'bool'>

num = list(num)
print(type(num))  # Output: <class 'list'>

num = tuple(num)
print(type(num))  # Output: <class 'tuple'>

num = dict(num)
print(type(num))  # Output: <class 'dict'>

num = set(num)
print(type(num))  # Output: <class 'set'>
```


#Exercises:

**1. Integers (`int`):**
Integers represent whole numbers.

**Example:**
```python
age = 30
```

**Exercise 1:**
Calculate the sum of two integers, `num1` and `num2`, and store the result in a variable `total`. Print `total`.

**Solution 1:**
```python
num1 = 15
num2 = 20
total = num1 + num2
print(total)  # Output: 35
```

**2. Floating-Point Numbers (`float`):**
Floats represent numbers with decimal points.

**Example:**
```python
pi = 3.14159
```

**Exercise 2:**
Calculate the area of a circle with radius `radius` using the formula `area = pi * (radius ** 2)`. Print `area`.

**Solution 2:**
```python
radius = 5.0
pi = 3.14159
area = pi * (radius ** 2)
print(area)  # Output: 78.53975
```

**3. Strings (`str`):**
Strings represent sequences of characters.

**Example:**
```python
name = "Alice"
```

**Exercise 3:**
Create a greeting by combining the `name` variable with a greeting message and store it in a variable `greeting`. Print `greeting`.

**Solution 3:**
```python
name = "Alice"
greeting = "Hello, " + name
print(greeting)  # Output: Hello, Alice
```

**4. Booleans (`bool`):**
Booleans represent true or false values.

**Example:**
```python
is_student = True
```

**Exercise 4:**
Check if a variable `is_adult` is `False`. If it is, print "You are not an adult." Otherwise, print "You are an adult."

**Solution 4:**
```python
is_adult = False
if not is_adult:
   print("You are not an adult.")
else:
   print("You are an adult.")
# Output: You are not an adult.
```

**5. Lists (`list`):**
Lists represent ordered collections of items.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
```

**Exercise 5:**
Add "orange" to the `fruits` list. Print the modified list.

**Solution 5:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

**6. Lists (`list`):**
Lists represent ordered collections of items.

**Example:**
```python
numbers = [1, 2, 3, 4, 5]
```

**Exercise 6:**
Calculate the sum of all the numbers in the `numbers` list. Print the sum.

**Solution 6:**
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15
```

**7. Tuples (`tuple`):**
Tuples represent ordered, immutable collections of items.

**Example:**
```python
coordinates = (3, 4)
```

**Exercise 7:**
Calculate the Euclidean distance between two points, `(x1, y1)` and `(x2, y2)`, using the formula `distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)`. Print the distance.

**Solution 7:**
```python
import math

point1 = (1, 2)
point2 = (4, 6)
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print(distance)  # Output: 5.0
```

**8. Dictionaries (`dict`):**
Dictionaries represent key-value pairs.

**Example:**
```python
student = {"name": "Alice", "age": 25, "grade": "A"}
```

**Exercise 8:**
Add a new key-value pair to the `student` dictionary to represent the student`s city. Print the modified dictionary.

**Solution 8:**
```python
student = {"name": "Alice", "age": 25, "grade": "A"}
student["city"] = "New York"
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'city': 'New York'}
```

**9. Sets (`set`):**
Sets represent unordered collections of unique items.

**Example:**
```python
unique_numbers = {1, 2, 3, 4, 5}
```

**Exercise 9:**
Create a set `even_numbers` containing even numbers from 1 to 10. Print `even_numbers`.

**Solution 9:**
```python
even_numbers = set(range(2, 11, 2))
print(even_numbers)  # Output: {2, 4, 6, 8, 10}
```

**Exercise 10:**
Create a set `odd_numbers` containing odd numbers from 1 to 10. Print `odd_numbers`.

**Solution 10:**
```python
odd_numbers = set(range(1, 10, 2))
print(odd_numbers)  # Output: {1, 3, 5, 7, 9}
```

**Exercise 11:**
Usage of set, intersection, union, difference, symmetric_difference.

**Solution 11:**
```python
# set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)  # Output: {1, 2, 3, 4, 5}
print(set2)  # Output: {4, 5, 6, 7, 8}

# intersection
intersection = set1 & set2
print(intersection)  # Output: {4, 5}

# union
union = set1 | set2
print(union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# difference
difference = set1 - set2
print(difference)  # Output: {1, 2, 3}

# symmetric_difference
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # Output: {1, 2, 3, 6, 7, 8}
```
