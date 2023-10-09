# VSCode & Python & Window

To add Python to your Windows PATH and run Python from Visual Studio Code, follow these steps:

**Adding Python to Windows PATH:**

1. **Install Python:**
   If you haven't already installed Python on your Windows machine, you can download the latest version from the [official Python website](https://www.python.org/downloads/windows/). Make sure to check the "Add Python x.x to PATH" option during installation. This will automatically add Python to your system's PATH.

   If you've already installed Python without adding it to PATH, you can modify your PATH manually. Here's how:

2. **Open the Start menu and search for "Environment Variables."**
   
3. **Click on "Edit the system environment variables."**

4. **In the System Properties window, click the "Environment Variables" button.**

5. **In the "System Variables" section, scroll down and find the "Path" variable, then click "Edit."**

6. **Click "New" and add the path to your Python installation. The default path is usually something like `C:\Users\<Your Username>\AppData\Local\Programs\Python\<Python Version>`, but it may vary based on your installation path. Be sure to use the actual path where Python is installed on your system.**

7. **Click "OK" to close all the dialog boxes.**

Now, Python is added to your system's PATH, and you can run it from any command prompt or terminal window.

**Running Python from Visual Studio Code:**

1. **Install Visual Studio Code:**
   If you haven't already installed Visual Studio Code, you can download it from the [official website](https://code.visualstudio.com/).

2. **Install the Python extension:**
   Open Visual Studio Code, go to the Extensions view by clicking on the square icon on the sidebar or using the shortcut `Ctrl+Shift+X`. Search for "Python" and install the official Python extension by Microsoft.
   This extension adds Python language support and various tools for Python development.
      - Install python extension
      - Install Code Runner

3. **Select a Python Interpreter:**
   After installing the Python extension, you need to select a Python interpreter for your project. An interpreter is responsible for running your Python code. To do this:
   - Open your Python project folder in VS Code (File -> Open Folder).
   - Create a virtual environment (optional but recommended for project isolation). You can do this from the terminal in VS Code using `python -m venv venv` (replace `venv` with your desired environment name).
   - Once your virtual environment is created, you can select it as your Python interpreter. Click on the Python version in the bottom status bar or use the command palette (`Ctrl+Shift+P`) and search for "Python: Select Interpreter." Choose the interpreter from the list, which should be located in your project's virtual environment.

4. **Create or open a Python file:**
   Create a new Python file by clicking "File" > "New File" and then save it with a `.py` extension (e.g., `hello.py`). You can also open an existing Python file.

5. **Write Python code:**
   Write your Python code in the editor.

6. **Run Python code:**
   To run Python code in Visual Studio Code, you can use the following methods:

   - **Press `F5`** to run the entire script.
   - **Right-click** in the editor and select "Run Python File in Terminal."
   - **Use the integrated terminal**: Open the integrated terminal in VS Code (View > Terminal or `Ctrl+~`), navigate to the directory containing your Python file, and then use the `python` command followed by your script's filename (e.g., `python hello.py`).

Visual Studio Code will use the Python interpreter you have installed and added to the PATH to execute your Python code.

#Your first Python program

Your first Python program is typically a simple "Hello, World!" program, which is a tradition in programming and serves as a basic introduction to the language. Here's how you can create and run your first Python program:

1. **Install Python**: If you haven't already, you'll need to install Python on your computer. You can download the latest version of Python from the official website (https://www.python.org/downloads/) and follow the installation instructions for your specific operating system.

2. **Choose a Text Editor or Integrated Development Environment (IDE)**: You can write Python code in any plain text editor, but using an IDE designed for Python can enhance your development experience. Some popular Python IDEs include Visual Studio Code, PyCharm, and IDLE (which comes bundled with Python).

3. **Write the Code**:

```python
# This is a simple Python program that prints "Hello, World!" to the console.
print("Hello, World!")
```

This code consists of a single line that uses the `print()` function to display the text "Hello, World!".

4. **Save the File**: Save the code in a file with a ".py" extension. For example, you can save it as "hello.py".

5. **Run the Program**:
   
   - Open a terminal or command prompt, navigate to the directory where you saved the file, and run the program by typing `python hello.py` and pressing Enter. You should see "Hello, World!" displayed on the screen.

That's it! You've successfully created and run your first Python program. This basic example demonstrates how to use the `print()` function to display output in Python, which is a fundamental concept in programming. You can build on this knowledge to explore more advanced Python programming topics and projects.

