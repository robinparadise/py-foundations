# Functional Programming (FP)

Functional Programming (FP) is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It encourages immutability, first-class functions, and declarative code. To master functional programming, let's delve into key concepts:

### 1. **First-Class Functions:**
   - In functional programming, functions are first-class citizens. This means functions can be:
      - Assigned to variables
      - Passed as arguments to other functions
      - Returned as values from other functions

   Example:
   ```python
   def square(x):
       return x ** 2

   # Assigning function to a variable
   square_function = square

   # Passing function as an argument
   def apply(func, value):
       return func(value)

   result = apply(square, 5)  # Returns 25
   ```

### 2. **Pure Functions:**
   - Pure functions have no side effects and always produce the same output for the same input.
   - They don't rely on external state or modify any external state.

   Example:
   ```python
   # Impure function (modifies external state)
   def impure_add(x, y):
       global total
       total += x + y
       return total

   # Pure function
   def pure_add(x, y):
       return x + y
   ```

### 3. **Immutability:**
   - In functional programming, data is immutable, meaning it cannot be changed once created.
   - Instead of modifying existing data, you create new data.

   Example:
   ```python
   # Mutable approach
   data = [1, 2, 3]
   data.append(4)  # Modifies the original list

   # Immutable approach
   data = [1, 2, 3]
   new_data = data + [4]  # Creates a new list
   ```

### 4. **Higher-Order Functions:**
   - Higher-order functions take one or more functions as arguments or return a function as a result.
   - They allow for composing functions and building abstractions.

   Example:
   ```python
   def multiply_by(factor):
       def multiplier(x):
           return x * factor
       return multiplier

   double = multiply_by(2)
   result = double(5)  # Returns 10
   ```

### 5. **Map, Filter, and Reduce:**
   - These are common higher-order functions used in functional programming.
      - **Map:** Applies a function to all items in an iterable.
      - **Filter:** Filters items in an iterable based on a given condition.
      - **Reduce:** Applies a function cumulatively to items in an iterable.

   Example:
   ```python
   numbers = [1, 2, 3, 4, 5]

   # Map
   squared = list(map(lambda x: x ** 2, numbers))

   # Filter
   evens = list(filter(lambda x: x % 2 == 0, numbers))

   # Reduce
   from functools import reduce
   product = reduce(lambda x, y: x * y, numbers)
   ```

### 6. **Recursion:**
   - Functional programming often relies on recursion instead of iterative loops.
   - Recursion is a technique where a function calls itself to solve smaller instances of a problem.

   Example:
   ```python
   def factorial(n):
       if n == 0 or n == 1:
           return 1
       else:
           return n * factorial(n - 1)
   ```

### 7. **Closures:**
   - Closures occur when a function remembers the environment in which it was created.
   - This is particularly useful for creating partially applied functions or maintaining state.

   Example:
   ```python
   def outer_function(x):
       def inner_function(y):
           return x + y
       return inner_function

   add_five = outer_function(5)
   result = add_five(3)  # Returns 8
   ```

### 8. **Lambda Functions:**
   - Lambda functions, or anonymous functions, are often used for short-lived operations.
   - They are defined using the `lambda` keyword.

   Example:
   ```python
   square = lambda x: x ** 2
   result = square(4)  # Returns 16
   ```

### 9. **Lazy Evaluation:**
   - Lazy evaluation delays the evaluation of an expression until its value is actually needed.
   - It can improve efficiency by avoiding unnecessary computations.

   Example:
   ```python
   from itertools import cycle, islice

   natural_numbers = cycle(range(1, 1000))
   filtered_numbers = islice(filter(lambda x: x % 3 == 0, natural_numbers), 10)
   ```

### 10. **Monads:**
   - Monads are a design pattern in functional programming used to handle computations with side effects.
   - They provide a way to compose functions while encapsulating state or side effects.

   Example:
   ```python
   class Monad:
       def __init__(self, value):
           self.value = value

       def bind(self, func):
           return func(self.value)

   result = Monad(5).bind(lambda x: Monad(x * 2)).bind(lambda x: Monad(x + 1)).value
   # Result is 11
   ```
1. **List Monad:**
  + Represents a sequence of values and allows for chaining computations on each element.
  + Libraries: Python's built-in list comprehensions can be used for monad-like behavior with lists.

  Example 1:
  ```python
  numbers = [1, 2, 3, 4]

  doubled = [x * 2 for x in numbers]
  squared = [x ** 2 for x in doubled]

  print(squared)
  ```
2. **Dict Monad:**

  Example 2:
  ```python
  # Sample dictionary of student grades
  grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

  # Double and square the grades using dictionary comprehensions
  doubled_squared_grades = {name: (grade * 2) ** 2 for name, grade in grades.items()}

  print(doubled_squared_grades)
  ```

  In this example:

  - `grade * 2` doubles each grade.
  - `(grade * 2) ** 2` squares the doubled grade.
  - The result is a new dictionary where each student's grade has been doubled and squared.

