# Input and output (I/O):

Input and output (I/O) in Python refers to the process of getting data into a Python program (input) and sending data out of a Python program (output). In Python, you can perform input and output operations using a variety of functions and methods. Here, we'll cover some of the most common ways to handle I/O in Python.

**Input in Python:**

1. **Using `input()` Function:**
 The `input()` function allows you to get user input from the keyboard. It reads a line of text from the user and returns it as a string. Here's an example:

```python
name = input("Enter your name: ")
print("Hello, " + name)
```

 When you run this code, it will prompt you to enter your name, and then it will greet you using the entered name.

Convert to int or float:

```python
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

height = float(input("Enter your height (in meters): "))
print("Your height is " + str(height) + " meters.")
```

**Output in Python:**

1. **Using `print()` Function:**
 The `print()` function is used to display output in Python. You can pass one or more expressions or strings to `print()`, and it will print them to the console. For example:

```python
print("Hello, World!")
```

2. **Formatted Output:**
You can format the output using f-strings (Python 3.6+) or the `format()` method. This allows you to embed variables and values within strings:

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

3. **Writing to Files:**
Python allows you to write data to files using the `open()` function and file objects. Here's an example of writing to a text file:

```python
with open("output.txt", "w") as file:
  file.write("This is a line of text.\n")
  file.write("This is another line of text.\n")
```

This code creates a file named "output.txt" and writes two lines of text to it.

3.1. **Reading files:**
You can read data from files using the `read()` method of file objects. Here's an example:

```python
with open("output.txt", "r") as file:
  contents = file.read()
  print(contents)
```

3.2. **Reading by lines:**
You can also read files line by line using the `readline()` method of file objects. Here's an example:

```python
with open("output.txt", "r") as file:
  line = file.readline()
  while line:
    print(line)
    line = file.readline()
```

Different operating systems use different line endings. For example, Windows uses `\r\n` (carriage return followed by a newline) while Linux and macOS use `\n` (newline). Python automatically converts line endings to `\n` when reading files.

3.3. **Reading all lines:**
You can read all lines from a file into a list using the `readlines()` method of file objects. Here's an example:

```python
with open("output.txt", "r") as file:
  lines = file.readlines()
  print(lines)
```

Differences to note between `read()`, `readline()`, and `readlines()`:

- `read()` returns the entire contents of the file as a single string.
- `readline()` returns the next line of the file as a string.
- `readlines()` returns a list of lines from the file.

4. **Command-Line Arguments:**
 You can access command-line arguments passed to your Python script using the `sys.argv` list from the `sys` module. Here's an example:

```python
import sys

if len(sys.argv) > 1:
  print("Hello, " + sys.argv[1])
```

You can run this script from the command line and pass your name as an argument like this: `python script.py John`. It will greet you with "Hello, John."

4.2. **Standard Error (stderr):**
Python has two standard streams, stdout (standard output) and stderr (standard error). You can write error messages to stderr using `sys.stderr.write()`:

```python
import sys

sys.stdout.write("This is an error message.\n")
```

**Explanaition about standard output and standard error:**

- **Standard output (stdout):** This is the default stream that is used to write output to the console. For example, when you use the `print()` function, it writes to stdout.

- **Standard error (stderr):** This is the default stream that is used to write error messages to the console. For example, when you use `sys.stderr.write()`, it writes to stderr.

