# Python Standard Library:

The Python Standard Library is a comprehensive collection of modules that come bundled with Python and provide a wide range of functionalities for various tasks. These modules are readily available, so you don't need to install them separately. Here are some examples of how to work with the Python Standard Library for common tasks:

**1. File Handling (`os` and `shutil` modules):**
   
   - `os` Module: The `os` module provides functions for interacting with the operating system, such as navigating directories, creating folders, and deleting files.

**Example** (Listing files in a directory):
```python
import os

current_directory = os.getcwd()
file_list = os.listdir(current_directory)

for file in file_list:
   print(file)
```

   - `shutil` Module: The `shutil` module provides higher-level file operations, including copying, moving, and removing files and directories.

**Example** (Copying a file):
```python
import shutil

source_file = "source.txt"
destination = "destination_folder/"

shutil.copy(source_file, destination)
```

**2. Working with Dates and Times (`datetime` module):**
   
   The `datetime` module allows you to work with dates and times, including date formatting, arithmetic, and more.

**Example** (Displaying the current date and time):
```python
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
```

**3. Regular Expressions (`re` module):**

   The `re` module provides support for working with regular expressions, which are powerful tools for pattern matching and text manipulation.

**Example** (Matching email addresses in a text):
```python
import re

text = "Emails: alice@example.com, bob@gmail.com, carol@yahoo.com"
pattern = r'\S+@\S+'
emails = re.findall(pattern, text)

for email in emails:
    print(email)
```

**4. Command-Line Arguments (`sys` module):**

   The `sys` module allows you to interact with the Python interpreter and access command-line arguments passed to your script.

**Example** (Accessing command-line arguments):
```python
import sys

script_name = sys.argv[0]
arguments = sys.argv[1:]

print(f"Script Name: {script_name}")
print(f"Arguments: {arguments}")
```

**5. JSON Serialization (`json` module):**

   The `json` module allows you to work with JSON data, including parsing JSON strings and serializing Python data to JSON format.

**Example** (Parsing JSON data):
```python
import json

json_data = '{"name": "Alice", "age": 30}'
python_data = json.loads(json_data)

print(python_data["name"])  # Output: Alice
```

**6. Working with Command Execution (`subprocess` module):**

   The `subprocess` module allows you to run and interact with external commands or processes from your Python script.

**Example** (Running an external command):
```python
import subprocess

command = "ls -l"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

print(result.stdout.decode())  # List files and directories
```

These are just a few examples of the many modules available in the Python Standard Library. The Standard Library is a valuable resource for Python developers, as it simplifies a wide range of common tasks and allows you to write more efficient and productive code. Explore the official Python documentation for a comprehensive list of modules and their functionalities.