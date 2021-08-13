# Python Quickstart Guide

## Intro and overview

> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python supports modules and packages, which encourages program modularity and code reuse.

The goal of this document is go offer you an easy and quick way to get started with the Python programming language. Following topics will be covered:

- Getting Started
- Basic Concepts
- Control Flow
- Collections
- Loops
- Strings
- Functions
- Modules
- Date and time
- Working with files
- Classes
- Testing
- Sources

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

### Running a python script

Running a Python file can be easily done by using the `python` command.

```bash
> python my-python-file.py
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
- `*` multiplication
- `/` division
- `%` modulus
- `**` exponentiation

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

The `print()` function is used to output text, numbers, or other printable information to the console.

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

Lists are ordered collections of items that allow for easy use of a set of data. List values are placed in between square brackets `[ ]`, separated by commas. Empty lists do not contain any values within the square brackets.
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

A tuple is used to store certain data in a structured way, not meant to be edited. Therefore a tuple is and should be immutable. On the other hand a list is used to store multiple items (for example tuples). The list can be edited when more data is added or removed, making it mutable.

```python
tuple = (1, 2, 3)
tuple = ("1", "2", "3")

# getting data from a tuple
tuple = ("python", 3)

tuple[0] -> "python"
tuple[1] -> 3
```

In a set every item can only exist once. It is however possible to construct a set with 'duplicates', in this case Python will only use the first entry and ignore all the other ones.

```python
systems = {"Windows", "Linux", "MacOs"}
system_duplicates = {"Windows", "Linux", "Linux", "MacOs"}

print(systems)
>>> {"Windows", "Linux", "MacOs"}
print(system_duplicates)
>>> {"Windows", "Linux", "MacOs"}
```

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

String, refering to a sequence of characters, can be any length and can include any character such as letters, numbers, symbols, and whitespace (spaces, tabs, new lines).

Strings are immutable in Python. This means that once a string has been defined, it can’t be changed. There are no mutating methods for strings. This is unlike data types like lists, which can be modified once they are created.

Python strings can be indexed using the same notation as lists, since strings are lists of characters. A single character can be accessed with bracket notation `[index]`, or a substring can be accessed using slicing `[start:end]`. Indexing with negative numbers counts from the end of the string.

```python
string = "python"

string[0]   -> p
string[3]   -> i
string[-1]  -> n
```

Strings can also easily be combined with the `+` operator.

```python
first = "Hello "
second = "World!"

print(first + second)
>>> "Hello world!"
```

The keyword `in` can be used to check if a string contains a specific character or substring. A `True` or `False` is returned depending if a match was found or not.

```python
string = "Programming with Python"

print("P" in string)
>>> True
print("Programming" in string)
>>> True
print("x" in string)
>>> False
```

### String methods

As is the case with other Python datatypes, strings also come with a set of build-in methods.

The `.len()` function can be used to determine the length of an object. In this case when you pass a string to it, it will return the length of the string.

```python
string = "python"

print(len(string))
>>> 6
```

The string method `.lower()` returns a string with all uppercase characters converted into lowercase. While the method `.upper()` returns a string with all characters converted to uppercase.

```python
string = "PythoN"

print(string.lower())
>>> "python"
print(string.upper())
>>> "PYTHON"
```

`.split()` will spit a string into a list of items. If no arguments are given the method will split on whitespace by default. When an argument is passed, that argument will be used as the delimiter on which to split the string.

```python
string = "Programming with Python"

print(string.split())
>>> ["Programming", "with", "Python"]

print(string.split("i"))
>>> ["Programm", "ng w", "th Python"]
```

The `.join()` method concatenates a list of strig together to create a new string joined with a chosen delimiter.

```python
list_of_strings = ["Programming", "with", "Python"]

result = "-".join(list_of_strings)
print(result)
>>> = "Programming-with-Python"
```

`.strip()` can be used to remove characters from the beginning and end of a string. A string argument can be passed to the method, specifying the set of characters to be stripped. When no argument is given, whitespaces are removed by default.

```python
string = "   Programming with Python   "

print(string.strip())
>>> "Programming with Python"
```

### f-string

f-strings are a simplified notation to insert a variable into a string by using a placeholder. A string is marked as an f-string by prefixing the string with `f`. Placeholders are defined in the string by using curly brackets `{ }`.

```python
language = "Python"
version = 3

result = f"We are programming in {language} with version {version}."
print(result)
>>> "We are programming in Python with version 3."
```

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

It is also possible to set a default value for function variables.

```python
def print_full_name(first_name: str = "John", last_name :str = "Doe") -> str:
    return first_name + " " + last_name 

print(print_full_name("Nyctophilopython", "oenpelliensis"))
>>> "Nyctophilopython oenpelliensis"
pritn(print_full_name())
>>> "John Doe"
```

---

## Modules

In Python, files that end with the `.py` extension and containing Python code that can be imported inside another Python program are called modules. Modules allow you to organize related functions and/or classes in the same file. By default Python already offers a wide selection of built in modules that can be imported in your own code.

You can import and use the content of another file/module using the `import` keyword. Modules can be imported in three different ways: `import <MODULE>`, `from <MODULE> import <FUNCTION/CLASS`, or `from module import *`. The last one is not encouraged.

```python
# option one
import module
module.function()
 
# option two
from module import function
function()
```

The `as` keyword can be used to give an alternative name to a module or function.

```python
from calculation-module import floating-point-calculator as cal

cal.add(1, 5)
```

### Pip

Even though Python comes with an extensive library of included packages and modules, it is possible that you miss a certain package or module to fit your needs.
Pip is the standard package manager for Python. It allows you to install and manage additional packages throught the `pip` command.

```bash
> pip help

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible 
                              dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.
```

Note: when you have an existing project, you can use the `freeze` command to extract all your dependencies to a file. This will allow others to import your project and its dependencies much easier. In most cases the file being used will be called `requirements.txt`.

```bash
# extracting your dependencies to the requirements file
> pip freeze > requirements.txt

# importing dependencies from the requirements file
> pip install -r requirements.txt
```

### Venv

`venv` is a Python module included in the Python standard library and the prefered way to create and manage virual environments. `venv` allows you to manage separate package isntallations for different projects. In essence it will create a isolated Python installation and will install packages into that virtual installation. If you where to switch projects, you can simply create a new virtual environmetn and not have to worry about breaking the packages installed int he other environments.

```bash
# setting up a venv for your python project.
python3 -m venv env
```

---

## Date and time

Python provides a module named datetime to deal with dates and times. It allows you to set date, time or both date and time using the `date()`, `time()` and `datetime()` functions respectively, after importing the datetime module.

```python
import datetime

date = datetime.date(year=2021, month=8, day=18)
print(date) 
>>> 2019-02-16
 
time = datetime.time(hour=13, minute=48, second=5)
print(time) 
>>> 13:48:05
 
timestamp= datetime.datetime(year=2019, month=2, day=16, hour=13, minute=48, second=5)
print (timestamp) 
>>> 2019-01-02 13:48:05
```

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

The `__repr__()` method is used to tell what the string representation of the class should be. It can only have one parameter (`self`) and it should return a string.

```python
class Language:
    def __repr__(self)
        return "The is a language object."

l = Language()
print(l)
>>> "The is a language object."
```

The built-in `dir()` function returns a list of all the attributes in the current scope. With an object as argument, `dir()` tries to return all valid object attributes.

```python
class Language:
    def get_name_and_version(self, name, version):
        return f"This is {name} version {version}"

print(dir(Language))
>>> ['__doc__', '__init__', '__module__', 'get_name_and_version']
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

---

## Testing

Testing your code increases your confidence that the code behaves as you expect and ensures that changes to your code won’t cause regressions. Python comes with a built in test and testrunner library: `unittest`. Another popular choise is `pytest`.

### Unittest

To use `unittest`you have to follow the following rules:

- Test are put into classes as methods.
- A series of special assertion methods in the `unittest.TestCase` class instead of the built-in assert statement.

```python
from unittest import TestCase

class ExampleUnittest(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
```

A few other assertion methods for unittest are: `.assertEqual()`, `.assertTrue()`, `.assertFalse()`, `.assertIs()`, `.assertIsNone()`, `.assertIn()`

Running a `unittest` test can be done through the python command itself:

```bash
> python -m unittest test
```

### Pytest

Pytest is an external library and therefore will require you to install it firt. This can be done by using pip.

```bash
> pip install pytest
```

`pytest` also supports execution of `unittest` test cases.
Pytest test cases are a series of functions in a Python file starting with the `test_`prefix. Some other advantages are:

- Support for the built-in `assert` statement instead of using special `self.assert` methods.
- Additional features like fixtures and parameterization.
- Ability to rerun from the last failing test.
- Plugins to extend the functionality.

```python
def test_always_passes():
    assert True

def test_always_fails():
    assert False
```

Running a `pytest` test can be done with the following command:

```bash
> pytest test.py
```

---

## Sources

- [Official Python website](https://www.python.org/)
- [Official pip website](https://pypi.org/project/pip/)
- [Official Python venv website](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [RealPython pip guide](https://realpython.com/what-is-pip/)
- [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Pytest website](https://docs.pytest.org/en/latest/)
