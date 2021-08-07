# Python Quickstart Guide

## Intro and overview

> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python supports modules and packages, which encourages program modularity and code reuse. 

The goal of this document is go offer you an easy and quick way to get started with the Python programming language. Following topics will be covered:

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

## Basic Concepts

### Variables and commets

A variable is used to store data. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers and the underscore character.

```python
language_name = "python"
version = 3
easy_to_use = True

# comments
```

### Operations

Python supports different types of arithmetic operations that can be performed on numbers, variables, or some combination. The primary arithmetic operators are:

- `+` addition
- `-` subtraction
- `*` subtraction
- `/` subtraction
- `%` subtraction
- `**` subtraction

A couple of examples: 

```python
result = 10 + 5
result = 10 - 5
result = 10 * 5
result = 10 / 5
```

These operators can also be paired with a `=` to perform a direct AND operation, for example:

```python
result = 0
result += 10

# this would be the same as:
result = 0
result = result + 10
```

### Variables

There are three number types in Python: integers, decimals and complex. An integer can be a positive number, a negative number or the number 0 so long as there is no decimal portion. The number 0 represents an integer value but the same number written as 0.0 would represent a floating point number.

```python
int = 1
float = 1.001
complex = 1j
```

A string is a sequence of characters (letters, numbers, whitespace or punctuation) enclosed by quotation marks. It can be enclosed using either the double quotation mark `"` or the single quotation mark `'`. If a string has to be broken into multiple lines, the backslash character `\` can be used to indicate that the string continues on the next line. 
Python supports the joining (concatenation) of strings together using the `+` operator. If the parameters passed to `+` have different types, then Python will report an error condition.

```python
language = "Python"
version = " 3"

long_string = "This is a sting \
broken up over multiple lines."

concat = language + version
```

### Print function

The print() function is used to output text, numbers, or other printable information to the console.

```python
hw = "Hello World!"
print(hw)

print(101)
```

---

## Control Flow

### if

The `if` statement is used to determine the execution of code based on the evaluation of a Boolean expression. When the if statement expression evaluates to True, then the indented code following the statement is executed. Otherwise the if statement is skipped.

```python
value = 10

if value > 1:
    print("The condition was True")

if value > 101:
    print("The condition was False, code is not executed")
```

### else

The `else` statement provides alternate code to execute if the expression in an if statement evaluates to False.

```python
value = 10

if value > 1:
    print("The condition was True")
else:
    print("The condition was False")
```

### elif

The `elif` statement allows for continued checks to be performed after an initial if statement. An elif statement differs from the else statement because another expression is provided to be checked, just as with the initial if statement.

```python
value = "python"

if value == "cat":
    print("The condition was cat")
elif value == "python":
    print("The condition was python")
elif value == "dog":
    print("The condition was dog")
else:
    print("default fallback")
```

### Operators

Pyton supports three control operators: or, and and not.

The `or` operator combines two Boolean expressions and evaluates to True if at least one of the expressions returns True.

```python
True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
```

The `and` operator performs a boolean comparison between two Boolean values, variables, or expressions. If both sides of the operator evaluate to True then the and operator returns True. A non-Boolean value will always evaluate to True when used with the and operator.

```python
True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
```

The `not` operator is used in a Boolean expression in order to evaluate the expression to its inverse value.

```python
not True        # Evaluates to False
not False       # Evaluates to True
"Yes" and 100   # Evaluates to True
```

---

## Collections

Python supports a few different collection types: sequences, mappings and sets.

- Sequences containing: list and tuple
- Mappings containing: dict
- Sets containing: set

In this guide we will take a look at lists and dictionaries and provide an example for the other two.

### Lists

Lists are ordered collections of items that allow for easy use of a set of data. List values are placed in between square brackets [ ], separated by commas. Empty lists do not contain any values within the square brackets.
They are a versatile data type that can contain multiple different data types within the same square brackets. The possible data types within a list include numbers, strings, other objects, and even other lists.

```python
numbers = [1, 2, 3, 4]
strings = ["one", "two", "three", "four"]
mixed = [1, "two", 3.0, False]
list_of_lists[[1, 2], ["one", "two"]]
empty_list = []
```

List elements are ordered by index, indices start at 0 and increment by one. To access a list element by index, square bracket notation is used: `list[index]`.

```python
systems = ["Windows", "Linux", "MacOs"]
 
systems[0]   # "Windows"
systems[2]   # "MacOs"
```

Lists also come with whole set of built-in methods to perfom a set of actions on the list.

You can add values to the end of a list using the `.append()` method. This will place the item end of the list.

```python
systems = ["Windows", "Linux"]
systems.append("MacOs")

print(systems)
>>> ["Windows", "Linux", "MacOs"]
```

The method `.insert()` allows us to add an element to a specific index in a list.

```python
systems = ["Windows", "Linux", "MacOs"]
systems.insert(2, "Android")

print(systems)
>>> ["Windows", "Linux", "Android", "MacOs"]
```

The `.remove()` method is used to remove an element from a list by passing in the value of the element to be removed as an argument. In the case where two or more elements in the list have the same value, the first occurrence of the element is removed.

```python
systems = ["Windows", "Linux", "MacOs"]
systems.remove("Windows")

print(systems)
>>> ["Linux", "MacOs"]
```

The `len()` function can be used to determine the number of items found in the list it accepts as an argument.

```python
systems = ["Windows", "Linux", "MacOs"]
size = systems.len()

print(size)
>>> 3
```

The `.count()` method searches a list for whatever search term it receives as an argument, then returns the number of matching entries found.

```python
systems = ["Windows", "Linux", "MacOs", "Linux"]
counted = systems.count("Linux")

print(counted)
>>> 2
```

The `.extend()` method allows you to add an other list to a list. The added list items will be added to the back of the original list.

```python
systems = ["Windows", "Linux", "MacOs", "Linux"]
mobile_systems = ["Android", "iOS"]

systems.extend(mobile_systems)
print(systems)
>>> ["Windows", "Linux", "MacOs", "Linux", "Android", "iOS"]

# an alternative method would be to use the + operator
all_systems = systems + mobile_systems
print(all_systems)
>>> ["Windows", "Linux", "MacOs", "Linux", "Android", "iOS"]
```

### Dictionaries

A Python dictionary is an unordered collection of items. It contains data as a set of key-value pairs. A dictionaly contains zero or more key-value items separated by commas `,`. Keys must always be an immutable data type, such as strings, numbers, or tuples.

```python
dictionary = {"language": "Python", "version": 3}
```

Values in a dictionary can be accessed by using the key within square brackets next to the dictionary variable. Values can be written by placing key within square brackets next to the dictionary and using the assignment operator `=`. If the key already exists, the old value will be overwritten otherwise a new key will be added to the dictionary.

```python
dictionary = {"language": "Python", "version": 3}

print(dictionary["version"])
>>> 3

dictionary["easy_to_use"] = True
print(dictionary["easy_to_use"])
>>> True
```

As is the case for lists, Python provides a set of build-in functions for dictionaries too.

The `.update()` function makes it easy to merge two given dictionaries. If both dictionaries have the a common key, the key of the dictionary calling the update function will be overwritten.

```python
dict_1 = {"colour": "blue", "shape": "circle"}
dict_2 = {"colour": "red", "number": 101}

dict_1.update(dict_2)
print(dict_1)
>>> {"colour": "red", "shape": "circle", "number": 101}
```

A `.get()` method is provided to access a dictionary value if it exists.

```python
dictionary = {"language": "Python", "version": 3}

print(dictionary.get("language"))
>>> "Python"

print(dictionary.get("NON-EXISTING-KEY"))
>>> None

print(dictionary.get("NON-EXISTING-KEY", "default value"))
>>> "default value"
```

Dictionaries can remove key-value pairs with the `.pop()` method. The method takes a key as argument and removes it from the dictionary.

```python
dictionary = {"language": "Python", "version": 3}

dictionary.pop("version")
print(dictionary)
>>> {"language": "Python"}
```

### Examples of Tuple and Set

TODO

---

## Loops

### While loops

A `while` loop will repeatedly execute a code block as long as a condition evaluates to True. The condition of a while loop is always checked first before the block of code runs. If the condition is not met initially, then the code block will never run.

```python
# this loop wil run 5 times

counter = 0
while counter < 5:
    counter += 1
```

### For loops

A `for` loop can be used to iterate over a list of items and perform a set of actions on each item.

```python
numbers = [0, 1, 2, 3, 4]

for number in numbers:
    print(number)

>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
```

A `for` loop can be used to perform an action a specific number of times in a row. The `range()` function can be used to create a list that can be used to specify the number of iterations in a for loop.

```python
for i in range(3):
    print(i)

>>> 0
>>> 1
>>> 2
```

In a loop, the `break` keyword ends the loop, regardless of the iteration number it was in. Once break executes, the code outside the loop will continue to execute.

```python
numbers = [0, 1, 2, 3, 4]

for number in numbers:
    if number == 2
        break
    print(number)

>>> 0
>>> 1
```

When the `continue` keyword is used inside a loop the remaining code inside the loop code block is skippend and we begin the next loop iteration.

```python
numbers = [0, 1, 2, 3, 4]

for number in numbers:
    if number == 2:
        continue
    print(number)

>>> 0
>>> 1
>>> 3
>>> 4
```

### List Comprehension

Python list comprehensions provide a concise way for creating lists. It consists of brackets containing an expression followed by a for-clause, then zero or more for- or if-clauses: `[EXPRESSION for ITEM in LIST <if CONDITIONAL>]`. A list comprehension always returns a list.

```python
# the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]
 
print(result)
>>> [0, 4, 16, 36, 64]
```

---

## Strings

---

## Functions

Certain tasks need to be performed multiple times. Instead of rewriting the same code in multiple places, a function can be defined using the `def` keyword. Function definitions may include parameters for data input to the function. 
Parameters in Python are variables — placeholders for the actual values the function needs. When the function is called, these values are passed in as arguments. They behave identically to a function’s local variables. And are initialized with the values passed into the function when it was called. Like local variables, parameters cannot be referenced from outside the scope of the function.


```python
def add_one_to(argument):
    return argument + 1

# calling the function
result = add_one_to(10)
print(result)
>>> 11
```

Python uses indentation (a tab) to identify blocks of code. Code within the same block should be indented at the same level. All code under a function declaration should be indented to the same level to identify it as part of the function. There can be additional indentation within a function to handle other statements such as `for` and `if` so long as the lines are not indented less than the first line of the function code.

Functions can have multiple parameters. To define a function with multiple parameters, parameter names are placed behind eachother, separated by commas in the functions definition.

```python
def print_full_name(first_name, last_name):
    return first_name + " " + last_name
```

On rare occasions you might want a function to return more than one result. Therefore functions are able to return multiple values using one return statement. All values that should be returned are listed after the return keyword and are separated by commas.

```python
coordinate = (51.22902493206556, 4.412085947717211)

def split_coordinate(coordinate):
    return coordinate[0], coordinate[1]
```

Python does not require to define a type in a functions definition nor does it require you to define the functions return type. While this might not always be needed as a function is small and readable. It might be useful for larger functions or some day in the future. Therefore you are able to suggest a type to each function argument by using a colon followed by a type: `:<TYPE>`. And suggest a function return type by using the arrow operator `-> <TYPE>`.

```python
def print_full_name(first_name: str, last_name :str) -> str:
    return first_name + " " + last_name 
```

### TODO -> default values

--- 

## Modules

---

## Working with files

A file-object is created when a file is opened with the `open()` function. You can associate this file object with a variable when you open a file using the `with` and `as` keywords. For example:

```python
with open('example.txt') as file_object:
```

### Reading from a file

After a file is opened, call the `.read()` method of the file object to return the all content as a string.

```python
with open('example.txt') as file_object:
    text_string = file_object.read()
print(text_string)
```

Instead of reading the entire content of a file, you can read a single line at a time. Use `.readlines()` to return a list of strings, each representing an individual line in the file. 

```python
with open('example.txt') as file_object:
    text_string = file_object.readlines()
print(text_string)
>>> ["line 1", "line 2", ...]
```

To read only one line instead of multiple lines in a file, use the method `.readline()`. Every next `.readline()` will extract the next line in the file if it exists.

### Writing to a file

By default, a file is opened for reading only. A second argument `r` is passed to it as a default value. To write to a file, the file should be opened with write permission via the `w` argument. After that the `.write()` method can be used to write to the file. If the file already exists, all prior content will be overwritten.

```python
with open('example.txt', 'r') as file_object:
    file_object.write("Data to be writte to the file.")
```

To avoid overwriting all data in a file you can use the `a` argument while opening the file. This allows you to append data to the end of the file. If a file doesn't exist, it will be created.

```python
with open('example.txt', 'a') as file_object:
    file_object.write("Data to be appended to the end of the file.")
```

### Parsing a JSON file to a dictionary

The JSON format is used to store key value pairs and looks a lot like Python's dictionary datatype. Python’s json module allows for reading this data format and parsing it to a dictionary. The `json.load()` function takes a file object as an argument and returns the data in a dictionary format.

```python
import json

with open('file.json') as json_file:
  python_dict = json.load(json_file)
```

---

## Classes

A class is a 'template' for a datatype and can be defined using the `class` keyword. In Python a class always needs to be instantiated before use.

```python
class Language:
    # this is an empty class
    pass

python = Language()
```

### Initialising a class

By default classes come with a set 'special' function. These functions can be overridden to tailor them to your needs, an example is the constructor function `__init__()`.

```python
class Language:
    def __init__(self, name: str):
        self.name

python = Language("Python")
java = ("Java")
```

### Class variables

Class variables are defined outside of all methods and have the same value for every instance of the class.

```python
class Language:
    type = "Programming"

l = Language()
print(l.type)
>>> "Programming"
```

### Class methods

Methods are functions that are defined as part of a class. It is common practice that the first argument of any mehtod that is part of a class is the actual object calling the method. This argument is usually called `self`.

```python
class Language:
    def get_name_and_version(self, name, version):
        return f"This is {name} version {version}"

l = Language()
print(l.get_name_and_version("Python", 3)
>>> "This is Python version 3"
```

### Inheritance

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

### Special functions

Repr()

Dir()

While looking at older Python code, you might encounter code that was originally targetted for Python2. When they switched from version 2 to 3 a few changes where made in the background to how objects are created. One of the most visual differences you will come across with will be the class declarations signature.

```python
# python 2 class declaration
class Language(object):
    pass

# python 3 class declaration
class Language:
    pass
```

---

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

Get data from a tuple:

```python
tuple = ("python", 3)

tuple[0] -> "python"
tuple[1] -> 3
```

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



## Sources

- https://www.python.org/