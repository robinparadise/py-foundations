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

```python
def unique_list(numbers):
    """Return a list of unique elements from a list."""
    unique_nums = []
    for num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
```

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

```python
def odd_numbers(numbers):
    """Return a list of odd numbers from a list of numbers."""
    odds = []
    for num in numbers:
        if num % 2 != 0:
            odds.append(num)
    return odds
```

**6. Write a function that takes a list of numbers and returns a new list with only the prime numbers from the first list.**

```python
def prime_numbers(numbers):
    """Return a list of prime numbers from a list of numbers."""
    primes = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
```

**7. Write a function that takes a list of numbers and returns a new list with only the palindromes from the first list.**

```python
def palindromes(numbers):
    """Return a list of palindromes from a list of numbers."""
    palindromes = []
    for num in numbers:
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    return palindromes
```
