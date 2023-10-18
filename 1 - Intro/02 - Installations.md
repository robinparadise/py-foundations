# VSCode & Python & Window

**Running Python from Visual Studio Code:**

0. **Install Python:**
   If you haven't already installed Python on your Windows machine, you can download the latest version from the [official Python website](https://www.python.org/downloads/windows/). Make sure to check the "Add Python x.x to PATH" option during installation. This will automatically add Python to your system's PATH.

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

# Long Paths Window:

In Windows 10, there is a way to enable the use of file paths longer than 260 characters, which is the default limit imposed by the Windows operating system. You can do this by enabling "LongPathsEnabled" in the Windows Registry. Here's how you can do it:

**Note: Modifying the Windows Registry can be risky if not done correctly. Please follow these instructions carefully, and consider backing up your Registry before making any changes.**

1. **Open the Registry Editor:**
   Press `Win + R`, type `regedit`, and press Enter. This will open the Windows Registry Editor.

2. **Navigate to the correct key:**
   In the Registry Editor, navigate to the following key:

   ```
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
   ```

3. **Create or modify a DWORD value:**
   Right-click on the right side of the Registry Editor window and select "New" > "DWORD (32-bit) Value." Name it `LongPathsEnabled` (without the quotes).

4. **Change the value data:**
   Double-click on the `LongPathsEnabled` entry you just created and set its value data to `1`. This will enable long file paths.

5. **Click "OK" and close the Registry Editor.**

6. **Restart your computer:**
   Changes to the Registry often require a system restart to take effect. Reboot your computer for the changes to become active.

After making these changes, you should be able to use file paths longer than 260 characters without issues.

# Pip

In Windows, you can use the "pip" command to manage Python packages and install external libraries for your Python projects. Here are the basic steps to use "pip" in Windows:

1. **Install Python**:
   If you haven't already installed Python, you can download the latest version from the official Python website (https://www.python.org/downloads/windows/). Make sure to add Python to your system PATH during installation.

2. **Open Command Prompt**:
   To use pip, you need to open the Command Prompt. You can do this by searching for "cmd" or "Command Prompt" in the Start menu.

3. **Check Python and pip Installation**:
   To check if Python and pip are correctly installed, run the following commands:

   ```
   python --version
   pip --version
   ```

   These commands should display the installed Python version and pip version.

4. **Install a Package**:
   To install a Python package using pip, you can use the following command:

   ```
   pip install package_name
   ```

   Replace "package_name" with the name of the package you want to install. For example, to install the requests library, you would run:

   ```
   pip install requests
   ```

5. **Upgrade pip (if necessary)**:
   It's a good practice to keep pip itself up to date. You can upgrade pip using the following command:

   ```
   python -m pip install --upgrade pip
   ```

6. **List Installed Packages**:
   To list the packages you've installed, you can use the following command:

   ```
   pip list
   ```

7. **Uninstall a Package**:
   To uninstall a package, you can use the following command:

   ```
   pip uninstall package_name
   ```

   Replace "package_name" with the name of the package you want to uninstall.

8. **Search for Packages**:
   To search for packages available on the Python Package Index (PyPI), you can use the following command:

   ```
   pip search package_name
   ```

   Replace "package_name" with the name of the package you want to search for.

9. **More pip Commands**:
   You can find more information on pip and its commands by using the following command:

   ```
   pip --help
   ```

This should help you get started with using pip in Windows for managing Python packages. Make sure your Python installation and pip are up to date to ensure compatibility and access to the latest packages.

# GitHub

Here's how you can set up and use VSCode with GitHub:

1. **Install Visual Studio Code**:
   If you haven't already installed Visual Studio Code, you can download it from the official website (https://code.visualstudio.com/). Install VSCode for your specific platform (Windows, macOS, or Linux).

2. **Install Git**:
   Git is necessary for version control, and it's often included when you install Visual Studio Code. However, if it's not installed, you can download it from the official Git website (https://git-scm.com/).

3. **Sign Up for GitHub**:
   If you don't have a GitHub account, you'll need to sign up for one at https://github.com. GitHub offers both free and paid plans, depending on your needs.

4. **GitHub Authentication**:
   To work with your GitHub repositories in VSCode, you need to authenticate your GitHub account. You can do this in VSCode by following these steps:
   
   - Open VSCode.
   - Click on the gear icon (⚙️) at the bottom left to open the settings.
   - In the search bar, type "GitHub" and choose "GitHub: Sign In."
   - Follow the prompts to sign in to your GitHub account.

5. **Open a Project or Create a New One**:
   You can open an existing project that's already associated with a GitHub repository or create a new one.

6. **Initialize a Git Repository**:
   If your project isn't already a Git repository, you can initialize it by following these steps:
   
   - Open your project in VSCode.
   - Open the integrated terminal in VSCode.
   - Use the `git init` command to initialize a Git repository.

7. **Create or Clone a GitHub Repository**:
   You can create a new repository on GitHub or clone an existing one. To clone a repository, click the "Clone Repository" button in VSCode and provide the URL of the GitHub repository you want to clone.

8. **Make Changes and Commit**:
   Edit your code in VSCode, and when you're ready to save your changes, you can use the integrated Git features. Open the Source Control tab on the left sidebar to stage your changes, write a commit message, and commit your changes.

9. **Push to GitHub**:
   After committing your changes, you can push them to your GitHub repository by clicking the "..." button in the Source Control tab and selecting "Push."

10. **Pull from GitHub**:
    You can pull changes from your GitHub repository into your local project by using the "Pull" button in the Source Control tab.

11. **Branching and Merging**:
    You can create and manage branches, as well as merge changes, directly in VSCode with Git. Use the Source Control tab to switch branches, create new branches, and merge branches.

12. **GitHub Integration Features**:
    VSCode also provides GitHub integration features for creating pull requests, reviewing code, and collaborating with others. You can find these features in the Source Control tab and the GitHub pane.

By following these steps, you can easily use Visual Studio Code with GitHub for efficient code development and collaboration.