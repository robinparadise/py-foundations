#Lists:

In Python, lists are ordered collections of items that allow you to store and manipulate data. Lists are versatile and can contain elements of different data types, including integers, strings, floats, and even other lists. Here, we'll cover basic list operations and common list manipulations.

**1. Creating Lists:**
You can create lists by enclosing a comma-separated sequence of items within square brackets `[]`.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.14, True]
```

**2. Accessing Elements:**
You can access individual elements in a list using indexing. Lists in Python are zero-indexed, which means the first element has an index of 0.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]  # "apple"
second_fruit = fruits[1]  # "banana"
```

**3. Modifying Elements:**
You can change the value of an element in a list by assigning a new value to its index.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
# fruits is now ["apple", "orange", "cherry"]
```

**4. Adding Elements:**
   - `append()`: Adds an element to the end of the list.
   - `insert()`: Inserts an element at a specific position in the list.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# fruits is now ["apple", "banana", "cherry", "orange"]

fruits.insert(1, "grape")
# fruits is now ["apple", "grape", "banana", "cherry", "orange"]
```

**5. Removing Elements:**
   - `remove()`: Removes the first occurrence of a specified value.
   - `pop()`: Removes an element at a specific index (default is the last element) and returns it.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# fruits is now ["apple", "cherry"]

removed_fruit = fruits.pop(0)
# removed_fruit is "apple" and fruits is now ["cherry"]
```

**6. List Slicing:**
You can extract a portion of a list using slicing. Slicing allows you to specify a range of indices to create a new list.

**Example:**
```python
numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]  # [2, 3, 4]
```

**7. List Concatenation:**
You can concatenate (combine) two or more lists using the `+` operator.

**Example:**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # [1, 2, 3, 4, 5, 6]
```

**8. List Length:**
You can find the length (number of elements) of a list using the `len()` function.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
length = len(fruits)  # 3
```

These basic list operations are fundamental for working with lists in Python. You can use these operations to manipulate and extract data from lists efficiently.

**Exercises:**

**1. Create a list of your favorite foods and assign it to a variable.**

```python
# Example:
favorite_foods = ["pizza", "ice cream", "cheeseburgers"]
```

**2. Add a food to the beginning and end of the list.**

```python
# Example:
favorite_foods = ["pizza", "ice cream", "cheeseburgers"]
favorite_foods.insert(0, "pasta")
favorite_foods.append("sushi")
```

**3. Print the list and make sure the new items were added.**

```python
# Example:
print(favorite_foods)  # Output: ["pasta", "pizza", "ice cream", "cheeseburgers", "sushi"]
```

**4. Print the second item in the list.**

```python
# Example:
print(favorite_foods[1])  # Output: pizza
```

**5. Print the last item in the list.**

```python
# Example:
print(favorite_foods[-1])  # Output: sushi
```


**6. Change the second item in the list to something new.**

```python
# Example:
favorite_foods[1] = "cake"
```


**7. Remove the last item from the list & print the new list.**

```python
# Example:
favorite_foods.pop()
print(favorite_foods)  # Output: ["pasta", "cake", "ice cream", "cheeseburgers"]
```

**8. Create a list of numbers from 1 to 10.**

```python
# Example:
numbers = list(range(1, 11))
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```

**9. Print the numbers 1 to 5.**

```python
# Example:
print(numbers[:5])  # Output: [1, 2, 3, 4, 5]
```


**10. Print the even numbers from the list.**

```python
# Example:
print(numbers[1::2])  # Output: [2, 4, 6, 8, 10]
```


**11. Print the odd numbers from the list.**

```python
# Example:
print(numbers[::2])  # Output: [1, 3, 5, 7, 9]
```

**12. Print the multiples of 5 from the list.**

```python
# Example:
print(numbers[4::5])  # Output: [5, 10]
```




