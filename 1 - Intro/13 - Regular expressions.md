# Regular Expressions

Python is a popular programming language that lets you write code to perform various tasks. Regular expressions, often called "regex," are a powerful tool used in Python and many other programming languages to find and manipulate text patterns.


**Regular Expressions (Regex)**: Regular expressions are like special search patterns that help you find and manipulate text in strings. You can use them to:

- Search for specific words or patterns within text.
- Validate data (like checking if an email address is correctly formatted).
- Replace or modify text based on patterns.

In Python, you use the `re` module to work with regular expressions. It provides functions to search, match, and manipulate text based on these patterns. Regular expressions can be quite powerful, but they may look a bit cryptic at first. With practice, you'll become more comfortable using them to solve various text-related tasks in Python.

Sure, let's dive into regular expressions (regex) in Python in detail, along with examples.

**re Module:** In Python, you can work with regular expressions using the `re` module.

Here are some common regex metacharacters:

1. `.` (dot): Matches any character except a newline.
2. `*`: Matches 0 or more repetitions of the preceding character or group.
3. `+`: Matches 1 or more repetitions of the preceding character or group.
4. `?`: Matches 0 or 1 repetition of the preceding character or group.
5. `^`: Matches the start of a string.
6. `$`: Matches the end of a string.
7. `[]`: Defines a character class, matching any one of the characters inside the brackets.
8. `|`: Acts like a logical OR, matching either the expression before or after it.
9. `()`: Groups characters to apply operators to the entire group.
10. `\`: Escapes a metacharacter, allowing you to match it as a literal character.

**Example 1: Basic Pattern Matching**
```python
import re

text = "Hello, my email is john@example.com"
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
else:
    print("No email found.")
```
This code searches for an email address pattern in the given text.

- `\w+` matches one or more word characters (letters, digits, or underscores).
- `@` matches the "@" character literally.
- `\w+` matches one or more word characters (the domain name).
- `\.` matches the dot (.) character literally.
- `\w+` matches one or more word characters (the top-level domain).

**Example 2: Extracting Multiple Matches**
```python
import re

text = "Apples are red, bananas are yellow, and grapes are green."
pattern = r'\w+'
matches = re.findall(pattern, text)

print(matches)
```
This code extracts all words from the text and prints a list of matches.

- `\w+` matches one or more word characters.

**Example 3: Replacing Text**
```python
import re

text = "Hello, my name is Alice. Hello, my name is Bob."
pattern = r'Hello'
replacement = "Hi"
new_text = re.sub(pattern, replacement, text)

print(new_text)
```
This code replaces all occurrences of "Hello" with "Hi" in the text.

**Example 4: Character Classes**
```python
import re

text = "The code is 1A-BC9D."
pattern = r'\d[A-Z]-\w\w\d'
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
else:
    print("Pattern not found.")
```
This code searches for a pattern that matches a digit, followed by a capital letter, a hyphen, two word characters, and another digit.

- `\d` matches a digit.
- `[A-Z]` matches any uppercase letter.
- `-` matches the hyphen character literally.
- `\w\w` matches two word characters.
- `\d` matches another digit.

Certainly, here are some regular expression exercises along with solutions in Python:

**Exercise 1: Find All Email Addresses**
Write a Python program that finds and prints all email addresses in a given text.

```python
import re

text = "Contact us at info@example.com or support@company.co.uk for assistance. For more information, email admin@12345.org."

pattern = r'\S+@\S+'
matches = re.findall(pattern, text)

for match in matches:
    print(match)
```

**Solution 1:**

This code uses the pattern `\S+@\S+` to find and print all email addresses. `\S+` matches one or more non-whitespace characters, and `@` is a literal character.

**Exercise 2: Extract Dates**
Write a Python program to extract all dates in the format "dd/mm/yyyy" from a given text.

```python
import re

text = "The meeting is scheduled for 23/10/2023. Please submit your report by 15/11/2023."

pattern = r'\d{2}/\d{2}/\d{4}'
matches = re.findall(pattern, text)

for match in matches:
    print(match)
```

**Solution 2:**

This code uses the pattern `\d{2}/\d{2}/\d{4}` to find and print all dates in the "dd/mm/yyyy" format. `\d{2}` matches two digits, and `\d{4}` matches four digits.

**Exercise 3: Remove HTML Tags**
Write a Python program to remove all HTML tags from an HTML document.

```python
import re

html = "<p>This is a <strong>sample</strong> HTML <em>text</em>.</p>"
pattern = r'<.*?>'

text = re.sub(pattern, '', html)
print(text)
```

**Solution 3:**

This code uses the pattern `<.*?>` to find and remove all HTML tags in the given HTML document.

**Exercise 4: Validate Phone Numbers**
Write a Python program to validate a list of phone numbers. The valid format is "xxx-xxx-xxxx," where x is a digit.

```python
import re

phone_numbers = ["123-456-7890", "555-5555-555", "12-3456-7890"]

pattern = r'\d{3}-\d{3}-\d{4}'

for number in phone_numbers:
    if re.match(pattern, number):
        print(f"{number} is a valid phone number.")
    else:
        print(f"{number} is not a valid phone number.")
```

**Solution 4:**

This code uses the pattern `\d{3}-\d{3}-\d{4}` to validate the phone numbers. It checks if each number in the list matches the specified format.

Certainly, here are five regular expression exercises for beginners to advance without solutions. These exercises cover different scenarios:

# Exercises
Create a new git project "py-rexp" and create a module called utils/rexp.py and implement every functions below:

**Exercise 1: Match URLs**
Write a Python program to extract and print all URLs from a given text. URLs usually start with "http://" or "https://" and can include letters, digits, and special characters.

```python
import re

text = "Visit our website at https://www.example.com or http://example.net."
pattern = r'.*' # fix code here
matches = re.findall(pattern, text)

for match in matches:
    print(match)
```


**Exercise 2: Validate Email Addresses**
Create a Python program that validates a list of email addresses. Valid email addresses typically have the format "username@domain.com" or "username@subdomain.domain.com".

```python
import re

email_addresses = [
  "username@domain.com",
  "username@subdomain.domain.com",
  "username",
  "username@domain",
  "username@domain.",
  "@domain.com",
  "username@.com",
  "username@domaincom",
]

pattern = r'.*' # fix code here

for email in email_addresses:
  if re.match(pattern, email):
    print(f"{email} is a valid email address.")
  else:
    print(f"{email} is not a valid email address.")
```

**Exercise 3: Extract Phone Numbers**
Write a Python program to extract and print all phone numbers in a given text. Phone numbers can have various formats, including (123) 456-7890, 123-456-7890, or 123.456.7890.

```python
import re

text = "Call us at (123) 456-7890 or (123) 456-7891."
pattern = r'.*' # fix code here
matches = re.findall(pattern, text)

for match in matches:
    print(match)
```

**Exercise 4: Find Word Occurrences**
Develop a Python program that counts the number of occurrences of a specific word in a text. Allow the user to input the word and the text, and then print the count of occurrences.

```python
import re

word = input("Enter a word: ")
text = input("Enter a text: ")

pattern = r'.*' # fix code here
matches = re.findall(pattern, text)

print(f"The word '{word}' occurs {len(matches)} times in the text.")
```

**Exercise 5: Remove Punctuation**
Create a Python program that removes all punctuation from a text, leaving only the words. Punctuation includes characters like ".", ",", "!", and "?".

```python
import re

text = "Let's try, Mike. Isn't this fun? Yes, it is!"

# write code here
```
