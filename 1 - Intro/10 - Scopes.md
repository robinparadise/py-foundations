In Python, the scope and lifetime of variables are crucial concepts that determine where and for how long a variable is accessible within your program. Understanding these concepts is essential for writing clean and bug-free code. Here's an overview:

**1. Scope of Variables:**

The scope of a variable defines where in your code the variable is accessible. In Python, variables can have one of the following scopes:

- **Local Scope**: Variables defined inside a function have local scope. They are only accessible within that function and are not visible outside of it.

**Example:**
```python
def my_function():
    x = 10  # x is a local variable
    print(x)

my_function()
print(x)  # Raises a NameError because x is not defined in this scope
```

- **Enclosing (Non-local) Scope**: Variables defined in an enclosing function's scope can be accessed by nested functions.

**Example:**
```python
def outer_function():
    y = 20  # y is in the enclosing scope

    def inner_function():
        print(y)  # y is accessible within the inner function

    inner_function()

outer_function()
```

- **Global Scope**: Variables defined at the top level of a module or script have global scope. They are accessible from any part of the code within that module or script.

**Example:**
```python
global_var = 30  # global_var is a global variable

def my_function():
    print(global_var)  # global_var is accessible within the function

my_function()
print(global_var)  # global_var is accessible outside the function
```

**2. Lifetime of Variables:**

The lifetime of a variable is the duration during which the variable exists and holds a value in memory. It depends on its scope:

- **Local Variables**: Local variables have a lifetime limited to the execution of the function in which they are defined. They are created when the function is called and destroyed when the function exits.

**Example:**
```python
def my_function():
    local_var = 42  # local_var is created when the function is called
    print(local_var)
    
my_function()
# At this point, local_var is no longer accessible
```

- **Global Variables**: Global variables persist throughout the execution of the program. They are created when the program starts and exist until the program terminates.

**Example:**
```python
global_var = 100  # global_var exists throughout the program's execution

def my_function():
    print(global_var)

my_function()
# global_var is accessible within and outside the function
```

**3. Shadowing:**

Shadowing occurs when a local variable within a function has the same name as a variable in a higher scope. In such cases, the local variable takes precedence, and it "shadows" or hides the variable in the higher scope.

**Example:**
```python
x = 5  # Global variable

def my_function():
    x = 10  # Local variable, shadows the global x
    print(x)

my_function()
print(x)  # Accesses the global x
```

In this example, the local variable `x` within the function shadows the global variable `x` temporarily.

Understanding the scope and lifetime of variables is crucial for avoiding unexpected behavior in your code and ensuring that variables are used in the intended way. It's important to use variable names that don't conflict with variables in different scopes to minimize confusion.

**Advance Exercise:**

**1.** What is the output of the following code?

```python
def my_function():
    print("Hello from a function")

my_function()
```

- [ ] `Hello from a function`
- [ ] `Hello from a function, Hello from a function`
- [ ] `Hello from a function, Hello from main`
- [ ] `Hello from main, Hello from a function`
```

**2.** What is the output of the following code?

```python
def my_function():
    print("Hello from a function")

print("Hello from main")
my_function()
```

- [ ] `Hello from a function`
- [ ] `Hello from a function, Hello from a function`
- [ ] `Hello from a function, Hello from main`
- [ ] `Hello from main, Hello from a function`
```

**3.** Advance exercise of Shadowing in Python

```python
x = 5

def my_function():
    x = 3
    print(x)

my_function()
print(x)
```

- [ ] `3, 5`
- [ ] `5, 3`
- [ ] `3, 3`
- [ ] `5, 5`
```

**4.** Fix the following code?

```python
var = 100
def func():
  print(var)
  var = 200

func()
```

