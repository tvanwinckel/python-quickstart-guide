# Python Quickstart Guide

## Intro and overview

What is Python?

...

This will be a basic introduction to the Python language, looking into how to get started.

- Getting started
- Variables
- Conditionals
- Creating and running Python modules
- Classes & objects
- ...

---

## Getting Started

The latest Python releases can be found at <https://www.python.org/downloads/> for all major operating systems. On OSX you can use homebrew to install with the following formula: `brew install python`. Most Linux distro will come with python pre installed.

Once installed verify you are on python 3: `python --version`

### Hello ~~World~~ Console

When Python is installed you should have access to its console. The console can be open by typing 'python' in your terminal. Once the console has been opened you can play around with it. To exit the console use the function 'exit()'.

```python
Python 3.9.2 (default, Feb 19 2021, 21:58:43)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World!")
Hello World!
>>> exit()
```

---

## Variables

Variables are simply data stored in a 'keyword'. You do not have to define a type, Python will handle this for you. Be careful as everything can be a variable.

### Basic variable types

```python
int = 1
float = 1.001
complex = 1j

str = "MyString"
str = 'AnotherString'

bool = True
bool = False

# comment
```

#### Working with strings

Python offers out of the box string manipulation tools:

```python
word = "programming"
sentence = "This is a sentence."

```

### Collection variables

There are a few different collection types: sequences, mappings and sets.

- Sequences containing: list and tuple
- Mappings containing: dict
- Sets containing: set

#### Sequences

While both list and tuple might look the same at first glace, they are not. A tuple is used to store certain data in a structured way, not meant to be edited. Therefor a tuple is and should be immutable. On the other hand a list is used to store multiple items (for example tuples). The list can be edited when more data is added or removed, making it mutable.

```python
list = [1, 2, 3]
list = ["1", "2", "3"]

tuple = (1, 2, 3)
tuple = ("1", "2", "3")
```

Note that both lists and tuples can be constructed out of mixture of items with different type:

```python
list = [1, 2, "three", (10, 20)]
tuple = (1, "two", 3)
```

##### Working with lists and tuples

Get data from a list:

```python
list = ["one", "two", "three"]

list[0] -> "one"
list[2] -> "three"
```

Add data to a list:

```python
# add one item to the list.
list = [1, 2, 3]

list.append(4)
>>> [1, 2, 3, 4]

# add a list to the list.
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_1.extend(list_2)
>>> [1, 2, 3, 4, 5 ,6]
```

Remove data from a list:

```python
list = [1, 2, 3]

# remove all items
list.clear()
>>> []

# remove an item by index
list.pop(1)
>>> [1, 3]

# remove an item by value
list.remove('1')
>>> [2, 3]
```

Get data from a tuple:

```python
tuple = ("python", 3)

tuple[0] -> "python"
tuple[1] -> 3
```

### Mappings

A dictionary 'dict', is a structure of key-value pairs.

```python
dictionary = {
    "language": "Python",
    "version": 3
}
```

#### Working with dicts

Get the value of a key:

```python
dictionary["language"] -> "Python"
dictionary["version"] -> 3
```

Add a new key to the dict:

```python
dictionary["newKey"] = "AnyValueYouWant"
```

Remove a key from the dict:

```python
dictionary.pop("language")
dictionary.pop("language", None)

>>> dictionary = {
    "version": 3
}
```

The `None` variable is not required when popping a key. If the key would not exist when popping a 'KeyError' will be thrown is None is not provided.

### Sets

In a set every item can only exist once. It is however possible to construct a set with 'duplicates', in this case Python will only the first entry and ignore all other ones.

```python
set = {"Windows", "Linux", "MacOs"}

set_with_duplicates = {"Windows", "Linux", "Linux", "MacOs"}
```

```python
set_with_duplicates = {"Windows", "Linux", "Linux", "MacOs"}

print(set)
>>> {"Windows", "Linux", "MacOs"}
print(set_with_duplicates)
>>> {"Windows", "Linux", "MacOs"}
```

---

## Conditionals

### if-else

If can be use as a standalone check.

```python
if True:
    print("Python IF condition.")

if 10 > 1:
    print("Greather than.")
```

Or you can use if to check a certain condition. When that condition is not met you can let it be handled by an else clause.

```python
if condition:
    print("Condition is met -> IF.")
else:
    print("Condition is not met -> ELSE.")
```

### if-elif-else

When you have multiple condition you could write separate if statements for them or combine them all into one by using **elif**. 

```python
if first_condition:
    print("First condition was met.")
elif second_condition:
    print("Second condition was met.")
else:
    print("None of the other conditions where met.")
```

The example shows only one elif statement but you could use as many as needed.

### for-loop

```python
items = [1, 2, "three", "four", 5]

for item in items:
    print(f"Print item with value: {item}")
```

### while-loop

```python
loop_condition = True

while loop_condition:
    print("Entered while-loop.")
    loop_condition = False
```

---

## Functions

Functions in Python are defined by the `def` keyword followed by the name of the function ending with with a semi colon `:`. The `pass` keyword indicates that the function is not implemented. If you fail to add pass to the function and leave it open, Python will expect an implementation and will throw an error at execution.

```python
def my_function_name():
    pass
```

Creating a function that accepts arguments can be done as follows:

```python
def my_function_name(argument_1, argument_2, argument_3):
    pass

# Create a function with a default argument value"
def my_function_name(argument_1, argument_2, argument_3 = "default_value"):
    pass

# Create a function with a argument type hinting"
def my_function_name(argument_1: int, argument_2: str, argument_3: str = "default_value"):
    pass
```

Functions can also return a value if wanted:

```python
def create_string(language: str, version: int):
     return f"This is {language} version {version}"

# it is also possible to use type hinting for a functions return type
def create_string(language: str, version: int) -> str:
     return f"This is {language} version {version}"
```

Example of calling a function:

```python
l = "python"
v = 3

def create_string(language: str, version: int):
    return f"This is {language} version {version}"


return_value = create_string(l, v)
print(return_value)
>>> "This is python version 3"
```

---

## Creating and running Python modules

### Python modules

- Create a Python file / module
- Use a single file as a single script
- Run the script

### Venv


### Pip


### Importing other modules

Import python, local and remote modules

---

## Classes / Objects

A class or object in Python is created by using the `class` keyword. By default a class is provided with a set 'special' fuctions. These functions can be overridden to tailor them to your needs, for example the constructor or init function.

```python
class Language:
    pass

l = Language()
```

An example of a class being constructed with two parameters. Unlike many other languages, Python does not provide a way for constructor overloading therefore you could could choose to make one or more of these parameters set to a default value.

```python
class Language:
    def __init__(name: str, version: int, unused_variable: str = None):
        self.name = name
        self.version = version

l = Language("Python", 3)
print(l.name)
print(l.version)
>>> "Python"
>>> 3
```

As is the case with many OOP languages, Python allows you to use inheritance while creating objects:

```python
class Python(Language):
    def __init__()
        super.__init__("Python", 3)

p = Python()
print(p.name)
print(p.version)
>>> "Python"
>>> 3
```

While looking at older Python code, you might encounter code that was originally targetted for Python2. When they switched from version 2 to 3 a few changes where made in the background to how objects are created. One of the most visual differences you will come across with will be the class declarations signature.

```python
# python 2 class declaration
class Language(object):
    pass

# python 3 class declaration
class Language:
    pass
```
