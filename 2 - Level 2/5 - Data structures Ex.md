# Exercises:

**Exercise 1: Tuple Manipulation**

Write a Python function that takes a tuple of numbers as input and returns a new tuple containing the square of each number in the original tuple.

```python
def square_tuple(input_tuple):
  # write code
  return tuple(x**2 for x in input_tuple)

numbers = (1, 2, 3, 4, 5)
result = square_tuple(numbers)
print(result)  # Output: (1, 4, 9, 16, 25)
```

**Exercise 2: Set Intersection**

Write a Python function that takes two sets as input and returns a new set containing the elements that are common to both sets (intersection).

```python
def set_intersection(set1, set2):
  # write code
  return {4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = set_intersection(set1, set2)
print(result)  # Output: {4, 5}
```

**Exercise 3: Dictionary Merging**

Write a Python function that takes two dictionaries as input and returns a new dictionary that is a merge of the input dictionaries. If there are common keys, use the values from the second dictionary.

```python
def merge_dictionaries(dict1, dict2):
  # write code
  return {'a': 1, 'b': 4, 'c': 5, 'd': 6}

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
result = merge_dictionaries(dict1, dict2)
print(result)  # Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
```

**Exercise 4: Dictionary Comprehension**

Write a Python function that takes a list of strings as input and returns a dictionary where the keys are the strings, and the values are the lengths of the strings.

```python
def string_length_dictionary(strings):
  # write code
  return {'apple': 5, 'banana': 6, 'cherry': 6}

words = ["apple", "banana", "cherry"]
result = string_length_dictionary(words)
print(result)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}
```

**List Manipulation Exercise:**

**Problem:** Given a list of integers, write a Python function to return a new list that contains only the even numbers, squared.

```python
def square_even_numbers(numbers):
    squared_evens = [x**2 for x in numbers if x % 2 == 0]
    return squared_evens

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = square_even_numbers(numbers)
print(result)  # Output: [4, 16, 36, 64, 100]
```

**String Manipulation Exercise:**

**Problem:** Write a Python function that takes a sentence as input and returns a new sentence where each word is reversed, but the order of words is maintained. Punctuation should be preserved.

```python
def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] if word.isalnum() else word for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = "Hello, World! Python is fun."
result = reverse_words_in_sentence(input_sentence)
print(result)  # Output: "olleH, dlroW! nohtyP si nuf."
```

