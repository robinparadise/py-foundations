# OOP

Object-Oriented Programming (OOP) is a powerful paradigm that provides a way to structure and organize code by representing real-world entities as objects. To master OOP, it's crucial to understand several key concepts and principles. Let's delve deep into each of them:

### 1. **Class:**
   - **Definition:** A class is a blueprint or a template for creating objects. It defines the properties (attributes) and behaviors (methods) that all objects of that type will have.
   - **Example:**
     ```python
     class Dog:
         def __init__(self, name, age):
             self.name = name
             self.age = age
         def bark(self):
             print("Woof!")
     ```

### 2. **Object:**
   - **Definition:** An object is an instance of a class. It is a concrete entity created from the class blueprint, with its own unique state (attributes) and behavior (methods).
   - **Example:**
     ```python
     my_dog = Dog("Buddy", 3)
     ```

### 3. **Attributes:**
   - **Definition:** Attributes are the properties or characteristics of an object. They store information about the object's state.
   - **Example:**
     ```python
     print(my_dog.name)  # Accessing the 'name' attribute
     ```

### 4. **Methods:**
   - **Definition:** Methods are functions that are part of a class. They define the behavior of objects of that class.
   - **Example:**
     ```python
     my_dog.bark()  # Calling the 'bark' method
     ```

### 5. **Constructor (`__init__` method):**
   - **Definition:** The constructor is a special method called when an object is created. It initializes the object's attributes.
   - **Example:**
     ```python
     def __init__(self, name, age):
         self.name = name
         self.age = age
     ```

### 6. **Encapsulation:**
   - **Definition:** Encapsulation is the bundling of data (attributes) and methods that operate on that data into a single unit (class). It hides the internal details of how an object works.
   - **Example:**
     ```python
     class BankAccount:
         def __init__(self, balance):
             self.__balance = balance  # Private attribute
         def get_balance(self):
             return self.__balance
     ```

### 7. **Inheritance:**
   - **Definition:** Inheritance is a mechanism that allows a class (subclass/derived class) to inherit properties and behaviors from another class (superclass/base class). It promotes code reuse.
   - **Example:**
     ```python
     class Animal:
         def __init__(self, species):
             self.species = species

     class Dog(Animal):
         def __init__(self, name, age):
             super().__init__("Dog")
             self.name = name
             self.age = age
     ```

### 8. **Polymorphism:**
   - **Definition:** Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables the same method to behave differently for different classes.
   - **Example:**
     ```python
     class Animal:
         def __init__(self, species):
             self.species = species

         def make_sound(self):
             print("Some generic animal sound")

     class Dog(Animal):
         def __init__(self, name, age):
             super().__init__("Dog")
             self.name = name
             self.age = age

         def bark(self):
             print("Woof!")

         def make_sound(self):  # Overriding the make_sound method
             self.bark()

     class Cat(Animal):
         def __init__(self, name):
             super().__init__("Cat")
             self.name = name

         def make_sound(self):  # Implementing the make_sound method
             print("Meow!")

     def animal_sound(animal):
         animal.make_sound()

     dog = Dog("Buddy", 3)
     cat = Cat("Whiskers")

     animal_sound(dog)  # Calls the 'bark' method
     animal_sound(cat)  # Calls the 'make_sound' method

     ```

### 9. **Abstraction:**
   - **Definition:** Abstraction involves simplifying complex systems by modeling classes based on essential properties and behaviors. It hides the unnecessary details.
   - **Example:**
     ```python
     from abc import ABC, abstractmethod

     class Shape(ABC):
         @abstractmethod
         def area(self):
             pass

     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius

         def area(self):
             return 3.14 * self.radius ** 2

     class Rectangle(Shape):
         def __init__(self, length, width):
             self.length = length
             self.width = width

         def area(self):
             return self.length * self.width

     # Creating instances of the concrete classes
     circle = Circle(5)
     rectangle = Rectangle(4, 6)

     # Using the abstraction to calculate area without knowing the specific shape
     shapes = [circle, rectangle]

     for shape in shapes:
         print(f"Area: {shape.area()}")

     ```

### 10. **Composition:**
   - **Definition:** Composition is a design principle where a class contains objects of other classes. It is an alternative to inheritance and allows for more flexibility in combining behaviors.
   - **Example:**
     ```python
     class Engine:
         def start(self):
             print("Engine started")

     class Car:
         def __init__(self):
             self.engine = Engine()
         def start(self):
             print("Car starting...")
             self.engine.start()
     # Creating an instance of the Car class
     my_car = Car()

     # Calling the start method of the Car class
     my_car.start()

     # Output:
     # Car starting...
     # Engine started

     ```

### 11. **Association:**
   - **Definition:** Association represents a relationship between two or more classes. It can be one-to-one, one-to-many, or many-to-many.
   - **Example:**
     ```python
     class Player:
         def __init__(self, name, skill_level):
             self.name = name
             self.skill_level = skill_level

     class Team:
         def __init__(self, name):
             self.name = name
             self.players = []

         def add_player(self, player):
             """Add a player to the team."""
             self.players.append(player)
             print(f"{player.name} added to {self.name}")

         def remove_player(self, player_name):
             """Remove a player from the team."""
             for player in self.players:
                 if player.name == player_name:
                     self.players.remove(player)
                     print(f"{player_name} removed from {self.name}")
                     return
             print(f"{player_name} not found in {self.name}")

         def get_average_skill_level(self):
             """Calculate and return the average skill level of the team."""
             if not self.players:
                 return 0
             total_skill = sum(player.skill_level for player in self.players)
             return total_skill / len(self.players)

     # Creating instances of the Player class
     player1 = Player("Alice", 85)
     player2 = Player("Bob", 92)
     player3 = Player("Charlie", 78)

     # Creating an instance of the Team class
     team = Team("Red Team")

     # Adding players to the team
     team.add_player(player1)
     team.add_player(player2)
     team.add_player(player3)

     # Removing a player from the team
     team.remove_player("Alice")

     # Calculating and displaying the average skill level of the team
     average_skill = team.get_average_skill_level()
     print(f"Average Skill Level of {team.name}: {average_skill}")

     ```

### 12. **Static and Class Methods:**
   - **Definition:** Static methods belong to a class rather than an instance, while class methods take the class itself as an argument.
   - **Example:**
     ```python
     class MathOperations:
         PI = 3.14  # Class attribute

         @staticmethod
         def add(x, y):
             """Static method to add two numbers."""
             return x + y

         @classmethod
         def multiply_with_pi(cls, x):
             """Class method to multiply a number with the class attribute PI."""
             return x * cls.PI

     # Example Usage:

     # Using the static method
     result_addition = MathOperations.add(5, 3)
     print(f"Addition Result: {result_addition}")

     # Using the class method
     result_multiplication = MathOperations.multiply_with_pi(5)
     print(f"Multiplication Result with PI: {result_multiplication}")

     ```

     In summary, static and class methods provide ways to define methods that are associated with a class rather than an instance. Static methods are independent of the class state, while class methods can interact with class-level attributes using the cls reference.


### 13. **Special methods in Python:**
Also known as "magic methods" or "dunder methods" (due to the double underscores, i.e., "dunder"), provide a way for classes to define or customize certain behaviors. These methods are invoked by the interpreter in specific situations and allow you to define how instances of your class should behave in various contexts. Here are some commonly used special methods:

### `__init__`:
```python
def __init__(self, parameters):
    pass
```
- This method is called when an object is created. It initializes the object's attributes.

### `__str__`:
```python
def __str__(self):
    pass
```
- This method returns a human-readable string representation of the object. It is called by the built-in `str()` function and `print()`.

### `__repr__`:
```python
def __repr__(self):
    pass
```
- This method returns an unambiguous string representation of the object. It is used by the built-in `repr()` function and can be called in the interpreter.

### `__len__`:
```python
def __len__(self):
    pass
```
- This method returns the length of the object. It is called by the built-in `len()` function.

### `__getitem__` and `__setitem__`:
```python
def __getitem__(self, key):
    pass

def __setitem__(self, key, value):
    pass
```
- These methods allow you to define how objects of your class behave when accessed or modified using square bracket notation (`obj[key]`).

### `__del__`:
```python
def __del__(self):
    pass
```
- This method is called when an object is about to be destroyed. It can be used for cleanup tasks.

### `__call__`:
```python
def __call__(self, parameters):
    pass
```
- This method enables instances of a class to be called as functions. It is invoked when you use parentheses with an instance (`obj()`).

### `__eq__` and `__ne__`:
```python
def __eq__(self, other):
    pass

def __ne__(self, other):
    pass
```
- These methods define the equality and inequality comparisons between objects.

### `__lt__`, `__le__`, `__gt__`, `__ge__`:
```python
def __lt__(self, other):
    pass

def __le__(self, other):
    pass

def __gt__(self, other):
    pass

def __ge__(self, other):
    pass
```
- These methods define the less than, less than or equal, greater than, and greater than or equal comparisons between objects.

### Example Usage:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, index):
        return str(self.value)[index]

    def __setitem__(self, index, char):
        value_str = list(str(self.value))
        value_str[index] = char
        self.value = "".join(value_str)

    def __delitem__(self, index):
        value_str = list(str(self.value))
        del value_str[index]
        self.value = "".join(value_str)

    def __call__(self, new_value):
        self.value = new_value
        print(f"MyClass instance called with new value: {self.value}")

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

# Example Usage:

obj1 = MyClass(42)
obj2 = MyClass(42)

print(str(obj1))          # Calls __str__: Output: MyClass instance with value: 42
print(repr(obj1))         # Calls __repr__: Output: MyClass(42)
print(len(obj1))          # Calls __len__: Output: 2 (length of "42")

print(obj1[1])            # Calls __getitem__: Output: '2'
obj1[1] = '5'             # Calls __setitem__
print(str(obj1))          # Output: MyClass instance with value: 45

del obj1[0]               # Calls __delitem__
print(str(obj1))          # Output: MyClass instance with value: 5

obj1(99)                  # Calls __call__: Output: MyClass instance called with new value: 99
print(obj1 == obj2)       # Calls __eq__: Output: False
print(obj1 != obj2)       # Calls __ne__: Output: True

```


# Exercises

### Exercise 1: Shapes
Create a hierarchy of geometric shapes using classes such as `Shape`, `Circle`, `Rectangle`, and `Triangle`. Implement methods to calculate the 'area' and 'perimeter' for each shape.

### Exercise 2: Zoo Management
Build a zoo management system with classes like `Animal`, `Mammal`, `Bird`, and specific animal classes. Use polymorphism to handle different types of animals.

### Exercise 3: E-commerce System
Develop an e-commerce system with classes for `Product`, `Customer`, `Order`, and `ShoppingCart`. Implement methods for placing orders, adding products to the cart, and calculating the total price.
```python

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
```

### Exercise 4: Social Media Platform
Build a simple social media platform with classes for `User`, `Post`, and `Comment`. Implement features such as posting, commenting, and tracking user activities.

