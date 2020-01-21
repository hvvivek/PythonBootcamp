![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)

# TABLE OF CONTENTS

- [HELLO WORLD](#hello-world)
- [THE KOAN OF PYTHON](#the-koan-of-python)
- [IMPORTING MODULES](#importing-modules)
- [CODE COMMENTS](#code-comments)
- [VARIABLE TYPES](#variable-types)
- [DECLARING VARIABLES](#declaring-variables)
- [STRINGS](#strings)
  - [declaration](#declaration)
  - [length](#length)
  - [returning values](#returning-values)
  - [escaped characters](#escaped-characters)
  - [multiline strings](#multiline-strings)
  - [string concatenation](#string-concatenation)
  - [text transformations](#text-transformations)
  - [stripping](#stripping)
  - [splitting](#splitting)
  - [slicing](#slicing)
  - [searching](#searching)
  - [replacement](#replacement)
  - [string substitution](#string-substitution)
- [INTEGERS AND FLOATS](#integers-and-floats)
  - [declaration](#declaration-1)
  - [operators](#operators)
  - [conversion](#conversion)
  - [maximum sizes](#maximum-sizes)
  - [incrementing in place](#incrementing-in-place)
  - [rounding floats](#rounding-floats)
  - [order of operations](#order-of-operations)
- [LISTS](#lists)
  - [declaration](#declaration-2)
  - [length](#length-1)
  - [indexing / slicing](#indexing---slicing)
- [indexing multidimensional lists](#indexing-multidimensional-lists)
  - [list ordering](#list-ordering)
  - [adding / deleting / changing values](#adding---deleting---changing-values)
    - [changing values](#changing-values)
    - [adding values](#adding-values)
    - [deleting values](#deleting-values)
  - [unpacking](#unpacking)
- [TUPLES](#tuples)
  - [declaration](#declaration-3)
- [DICTS](#dicts)
  - [declaration](#declaration-4)
  - [pretty printing a dict](#pretty-printing-a-dict)
  - [indexing](#indexing)
  - [listing keys and values](#listing-keys-and-values)
  - [adding / removing / changing key values](#adding---removing---changing-key-values)
    - [adding / changing](#adding---changing)
    - [removing](#removing)
  - [json to dict](#json-to-dict)
- [BOOLEANS](#booleans)
  - [logical operators](#logical-operators)
  - [equality vs identity](#equality-vs-identity)
  - [logical combinations](#logical-combinations)
  - [in operator](#in-operator)
- [CONTROL FLOW](#control-flow)
  - [if statements](#if-statements)
  - [for](#for)
  - [while](#while)
- [FUNCTIONS](#functions)
  - [declaration](#declaration-5)
  - [parameters](#parameters)
  - [scope](#scope)
- [ADDITIONAL RESOURCES](#additional-resources)

# HELLO WORLD

Welcome to Python! Let's start where we always start with programming languages, "hello world". This simple statement demonstrates all of the elements of the Read, Evaluate, Print loop (**REPL**):

- **READ** - read in the statement below as typed by the user
- **EVALUATE** - run the 'print' method and take it's argument 'hello world' 
- **PRINT** - takes the result yielded by **EVALUATE** and prints it to the terminal
- **LOOP** - you can enter more statements to evaluate which will start the loop again 

```python
print('hello world!')
```

> NOTE: `print` is a built in function in Python that we can use to return text and values to our screen.

# THE KOAN OF PYTHON

Let's take a look at THE KOAN OF PYTHON (more about `import` later on):

```python
import this
```

# IMPORTING MODULES

Modules are pre-packaged bundles of code that provide us with useful functions, variables, and classes. Some modules come built-in with Python, while others come from packages that can be installed optionally

Here is the basic module import syntax:

```python
import os
import sys

os.getcwd() # returns current working directory
sys.platform # returns platform of machine
```

We can also import modules and alias them to other names:

```python
# numpy is a powerful matrix math package for Python
# that is almost always imported as the alias 'np'
import numpy as np
np.pi # returns value of pi
```

# CODE COMMENTS

Comments should  be used when it is not obvious what your code is doing. Compared to most other languages Python code is so easy to read / understand, so you can be sparing with your comments. Before you write comments to explain a complex / confusing piece of code, make sure your code cannot just be simplified first.

Here are the two types of comments:

```python
'''
this is a multiline comment
we can put as many lines of comment between these triple quotes as we want!
these comments are often used to document what a function or class does
'''

# this is a single line comment! 

# everything after the # is a comment
# everything before is evaluated
# all comments will be ignored by the interpreter!

print('hi') # this line will print 'this' to the standard output
```

# VARIABLE TYPES

Python has a few important and commonly used variable types, along with some more exotic types you don't see used quite as often.

This block of code loops through all the different variable types in Python and prints them out. Don't worry about understanding exactly how it loops yet, this code is simply for demonstration of Python builtin types:

```python
import builtins

for name in dir(builtins):
    if isinstance(getattr(builtins, name), type):
        print(name)
```

We are going to be concerned with the following types:

- **Booleans**: `True` or `False` values
- **Strings**: ordered collections of characters, ex. `"General Assembly"`
- **Integers/Floats**: numeric values, integer (ex. `5`) of floating point (ex. `3.14`)
- **Lists**: ordered collections of values that can be modified programatically
- **Tuples**: exactly like lists, but a Tuple cannot be changed one declared
- **Dicts**: collections of values that can be referenced by their names (called **keys**)
- **Functions**: blocks of code that received some value, execute some logic / calculation, and return a result
- **Classes**: blueprints for making objects which are simplified models of real world objects and their characteristics and behaviors

# DECLARING VARIABLES

We declare variables by name and set their value using the `=` assignment operator 

```python
my_first_var = 'Hello'
my_second_var = "Hi"
my_third_var = 2
my_fourth_var = True
my_fifth_var = 36.2
```

Python is a dynamically-typed language; this means that Python determines the type of the 
variable for you automatically given the context that the variable is declared in 
and the value passed to the variable

```python
print(type(my_first_var))
print(type(my_second_var))
print(type(my_third_var))
print(type(my_fourth_var))
print(type(my_fifth_var))
```

Variable naming conventions: all lowercase, starting with a letter or 
underscore, with underscores between words don't use special characters! 
don't use dashes!
[PEP-8 naming standards for Python](https://www.python.org/dev/peps/pep-0008/)

```python
my_var = 1
invalid-var = 1
0invalid_var = 1
invalid_var@ = 1
```

You can declare multiple variables at once:

```python
name, age, sex = 'Arjun', 33, 'M'
```

Overwriting a variable is as simply as reassigning it:

```python
my_var = 'Hello'
```

A re-assigned variable can be of any type; it is not constrained to be of the
same type as it was originally declared:

```python
print(type(my_var))
```

> ## TRY IT

Declare `name`, `sex`, and `age` variables with your own information:

```python

```

<details>
<summary>Solution</summary>

```python
name = 'Sandra'
sex = 'female'
age = 31

# or

name, sex, age = 'Sandra', 31, 'female'
```

</summary>
</details>

# STRINGS

Strings are ordered collections of characters which are enclosed in single or double quotation marks. Single letters, words, sentences, paragraphs, emojis, kanji... these are all represented as strings. 

## declaration

```python
my_string = 'this'
# or
my_string = "this"
```

## length

You can use a builtin function called `len` to calculate the length of variables:

```python
len(my_string)
```

## returning values

Once you make a string, or really any variable, you can see it's value in two different ways:

```python
my_string
# vs
print(my_string)
```

Are these different?

> ## TRY IT

Look at the contents of `my_string` by both viewing it using `print` or just entering it's name. What is the difference? Why?

```python
my_string = 'first line\nsecond line'
```

<details>
<summary>Solution</summary>

When you print `my_string`, Python converts the `'\n'` substring to a line break
ie printing will actually replace special placeholder characters called **escaped characters** (such as `'\n'`) with their text representation, whereas simply evaluating the name of the string will give the value
of the string, including the escaped characters

</details>


## escaped characters

These characters are called **escaped characters** because the `\` "escapes" / changes the normal meaning of the following letter(s), and they return a special designated string when printed, instead of just their
character contents.

Here are some common string **escape character**:
> NOTE: these work in many / most programming languages!

- `\n` - newline
- `\t` - tab
- `\'` - escaped single quote
  - allows you to use a `'` in the middle of a string which has starting and ending `'` characters without prematurely ending the string declaration
- `\"` - escaped double quote
  - same as escaped single quote but for string declared with `"` starting and ending characters

```python
print('first line\n\ttabbed second line\n\'I can use single quotes if I escape them\'')
```

You can get unicode characters outside of the standard alphanumeric characters by using
strings starting with "u" to indicate unicode, and `\u<unicode char number>` for unicode symbols references.

[Here are a ton of unicode character code mappings](http://unicode.org/charts/)

```python
ustring = u'I have to get to work, \u2602 or \u2600..\u2639'
print(ustring)
```

> ## TRY IT

Declare a string that prints the following string value (double quotation
marks and new lines included, but you can ignore the ''' characters):

```python
'''
"We may have all come on different ships, but we're in the same boat now."
     - MLK
'''

```

<details>
<summary>Solution</summary>

Notice how the escaped quote allows us to use the same type of quotation mark as those used to declare the string:

```python
quote = '"We may have come on different ships, but we\'re in the same boat now."\n\t- MLK'
# or
quote = "\"We may have come on different ships, but we're in the same boat now.\"\n\t- MLK"
```

</details>

> ## TRY IT

Replace the double quotes in the above string with special character \u2036 (open quotation), and \u2033 (closed
quotation)

<details>
<summary>Solution</summary>

```python
print u'\u2036We may have come on different ships, but we\'re in the same boat now.\u2033\n\t- MLK'
```

</details>

## multiline strings

Multiline strings are exactly the same as multiline comments, but you can in fact save their values in variable for later use:

```python
multiline_string = '''
my name is Arjun
and I'm a teacher at General Assembly
'''
# or
multiline_string = """
my name is Arjun
and I'm a teacher at General Assembly
"""
```

## string concatenation

Concatenation means adding two values together, in this case, joining to strings end to end.

A string can simply be added together using the `+` operator:

```python
str_1 = 'In the beginning, '
str_2 = 'there was Assembly'
str_3 = str_1 + str_2
print(str_3)
```

You can also use the `+=` operator as a shorthand way of saying incrementing an existing value by another value. In the case of strings, you end up concatenating a string value to a preexisting on:

```python

str_4 = "PROLOGUE: "
str_4 += str_3
print(str_4)
# vs the longer way
str_5 = "PROLUGUE: "
str_5 = str_5 + str_3
print(str_5)
```

In order to add non-string variables with strings, you must convert them to strings first using the builtin `str` function:
> NOTE: This is not always the most elegant way to combine variables and string (we'll learn better ways in the **STRING SUBSTITUTION** section below)

```python
# notice the difference in the value printed for these two statements
print(5)
print(str(5))

# now use str method to convert an integer to a string for concatenation
print('Here is a string plus a number: ' + str(5))
```

> ## TRY IT

Print a string that says `"my name is <name>, and I am <age> years old"` using the `name` and `age` vars
provided below:

```python
name = 'Jerermy'
age = 4

```

<details>
<summary>Solution</summary>

```python
name = 'Jerermy'
age = 4

print('my name is ' + name + ', and I am ' + str(age) + ' years old')
```

</details>

## text transformations

String comes pre-packaged with all kinds of handy methods that allow us to transform them. 
> NOTE: Notice that when we talk about calling a function by it's name such as `len` or `str`, we call them **functions** whereas when we use a function with the syntax `<my variable>.<function name>`, we call these **methods**. Methods are simply functions that belong to variables, and are specialized to be used with those variable. All functions are run by using parentheses where we put any required data called **arguments** to the function between the parentheses: `<function name>(<arguments>)`

```python
sentence = "I aim to become a Python hacker!"
sentence.upper()
sentence.lower()
sentence.capitalize()
```

Some methods allow you to chain one method after another. It runs the methods in order, outputting the resultant value. Method chaining is also possible with some but not all methods in other types:

```python
sentence = "i AIm tO BeCoMe a PytHOn HaCkEr!"
sentence.lower().capitalize()
```

## stripping

Stripping allows the removal of trailing space or characters around a string using the `strip` method. To remove spaces / characters from left and right sides, you can use `lstrip` or `rstrip`, respectively:

```python
padded = '\t    There are a lot of spaces and tabs around this string\'s contents    \t\t'
padded.strip()
padded.lstrip()
padded.rstrip()
```

All of the stripping methods optionally take an argument for what kind of character to strip. By default, this character is set to `' '` (a single space), so running `strip()` is the same as running `strip(' ')`

Let's try stripping a non-space character:

```python
num_padded = '00000why are there zeros surrounding this string?0000'
num_padded.strip('0')
```

## splitting

The `split` method allows a string can be split into a list of substrings. We have not talked abut list variables yet, but all you need to know for now is that they are a ordered set of comma-separated values inside of square brackets, ex. `['the', 'quick', 'brown', 'fox']`.


`split` also has a default "split-at" value of `' '`. Let's try using the default value and other values:

```python
sentence = "i AIm tO BeCoMe a PytHOn HaCkEr!"

# split at every space (default)
sentence.split()

# split at every 'a'
sentence.split('a')
```

A very easy way to split a string into a list of characters is using the `list` method, with the string as the argument:

```python
list(sentence)
```

> ## TRY IT

Take the `weird_string` below, remove the trailing spaces on the left and the trailing repetitions of the word 'end' from the right, then split it into words:

```python
weird_string = '\n\t   well~isn\'t~this~a~weird~string?endendend'
```

<details>
<summary>Solution</summary>

One of the key details in this solution the you can pass multi-character string to `rstrip` and it will strip using each character of the multi-character string!

```python
weird_string.lstrip().rstrip('end').split('~')
```

</details>

## slicing

Python provides a way to get parts of a string by specifying start and stop positions. This is called **slicing**, and later we will see that this syntax works on lists as well.

Slicing takes three positional arguments separated by ':' and placed within square brackets:

- starting index (inclusive) _default value: `0`_
- ending index (exclusive) _default value: the end of the string_
- skipping - how many positions to move forward between each retrieved value, starting at starting index until the ending index is reached _default value: `1`_

> NOTE: string indices, and counting in general in Python and other programming languages starts at `0`. For example, in this string `'hello'` the index of the letter `h` is `0`, not `1`!

```python
sentence[2:5]
sentence[:5]
sentence[5:]
sentence[:]
sentence[::2]
```

> ## TRY IT

Unscramble the message in `scrambled`.

- hint 1: the first letter of the hidden message is `y`
- hint 2: the message is embedded in scrambled at regular intervals

```python
scrambled = 'T{vSzXyJ^osatoCJuWZOurtwnDi cAIxMFhXkB\\caaoTpLVnvSqIppfe_TYDAc TrJrbamRuPvGPas[rGqWniqfduIahZ_YvVgHxWpVheXDYy_{dsIur{^ L[hQTrt`j^n`voaPKzpF IIOnWodrxpEcjehcThaTcbtoJZ`obH[aSZdEuVfT[eK]fptE TfcCs]t[RX]e\\hxcgtOairYORWcsNNekoB wqp^FmsHRkExGenyRlrGnUc\\pTrtgW{rHheUYOIUJnUREozScYjwH\\ae'
```

<details>
<summary>Solution</summary>

The first thing to do is start at the left and find the index of the first `y`, which is `6`, then try different skipping values until a meaningful message appears.

```python
scrambled[6::7]
```

If your curious how the message was made, here was the code that generated it:

```python
import random
hidden_message = 'you have managed to decode this sentence'
scrambled = ''
gap = 6
for i in hidden_message:
    for n in range(gap):
        scrambled += chr(random.randint(65, 123))
    scrambled += i

print(scrambled)
```

</details>

## searching

There are a few different ways that we can search within a string to see if a substring exists within it.

Let's consider this `paragraph`

```python
paragraph = '''In the works of Tarantino, a predominant concept is the distinction between
ground and figure. In a sense, Sartre suggests the use of rationalism to attack
colonialist perceptions of sexuality. Marx uses the term ‘subcapitalist
materialism’ to denote the rubicon, and subsequent futility, of conceptualist
class.
“Society is used in the service of class divisions,” says Derrida. Thus,
Sargeant[1] suggests that the works of Tarantino are
empowering. The main theme of Finnis’s[2] model of
rationalism is the role of the participant as artist.'''
```

To simply check for the presence of a substring, we can use the `in` operator:

```python
# this statement will evaluate to True or False
'Tarantino' in paragraph
```

To get the index of the first instance of a substring from the left, we can use the `find` method:

```python
paragraph.find('Tarantino')
```

To do the same from the right, we can use the `rfind` method:

```python
paragraph.rfind('Tarantino')
```

> ## TRY IT

One of the most important things you can learn as any kind of programmer is to learn how to read the documentation for the language and modules / packages that you plan to use. Let's take a look at the Python language documentation to learn more about the built in string method `find` and it's arguments. [Check out the docs here.](https://docs.python.org/2/library/stdtypes.html#str.find)

> NOTE: **functions** take two different kinds of arguments: 
> - **positional arguments**: 
>   - the first few arguments to a **function** need to be input into the function in a specific order. 
>   - For example, you may have a function called `whisperThanYell` that expects two string arguments, first the whispered string (which will be transformed to all lowercase) then second, the yelled string (which will be transformed to all uppercase). 
>   - If you ran `whisperThanYell('I\'ll tell you a secret', 'you better not tell')` you'd get back `"i'll tell you a secret, YOU BETTER NOT TELL"`, but if you ran `whisperThanYell('you better not tell', 'I\'ll tell you a secret')`, `you better not tell, "I'LL TELL YOU A SECRET"`. 
>   - Notice how these are two different outcomes, ie with positional arguments, order matters!
> - **keyword arguments**:
>   - some functions let you pass arguments using `<keyword>=<some value>` notation in the arguments list **AFTER** all of the positional arguments, and these are called keyword arguments
>   - these arguments can go in any order
> - either, both, or neither type of argument can be applicable to a given function, and any one of the arguments in particular can be required or optional

Now, let's find the index of the second `of` occurrence in `paragraph` using `find`:

```python
paragraph = '''In the works of Tarantino, a predominant concept is the distinction between
ground and figure. In a sense, Sartre suggests the use of rationalism to attack
colonialist perceptions of sexuality. Marx uses the term ‘subcapitalist
materialism’ to denote the rubicon, and subsequent futility, of conceptualist
class.
“Society is used in the service of class divisions,” says Derrida. Thus,
Sargeant[1] suggests that the works of Tarantino are
empowering. The main theme of Finnis’s[2] model of
rationalism is the role of the participant as artist.'''
```

<details>
<summary>Solution</summary>

First we find the index of the first `of` from the left, then we pass that index + 1 (so it doesn't match again), as the second optional `start` positional argument to `find`:

```python
first_index = paragraph.find('of')
paragraph.find('of', first_index + 1)
```

</details>

## replacement

Using the bulitin `replace` string method, we can replace characters or substring in an existing string. If we're clever, we can remove characters and substrings as well using the same method (think about it).

This time, you are going to read about the `replace` method and try to implement it yourself.
[Check out the docs here.](https://docs.python.org/2/library/stdtypes.html#str.replace)

> ## TRY IT

In `quote`, replace the first 'th' with 'the' and make the string all lowercase other than the first word.
- hint: [another string method...](https://docs.python.org/2/library/stdtypes.html#str.capitalize)

```python
quote = 'In th End, we will remember not the words of our Enemies, but the silence of our Friends.'
```

<details>
<summary>Solution</summary>

We can string the and `capitalize` and `replace` methods to return a string transformed by both. We have to be careful with `replace` because simply replacing `th` with `the` will turn the `the` before `silence` into `thee`. In order to change only the first `th` substring, we can either using the optional `count` positional argument to stop replacing after `1` instance, or we can cleverly notice that replacing `th ` gets around the issues of replacing `th`.

```python
quote.capitalize().replace('th', 'the', 1)
# or
quote.capitalize().replace('th ', 'the ')
```

</details>

## string substitution

Strings containing `{}` characters can have those characters replaced with variable value using the `format` string method. Inserting variable into strings in this way is called either **string substitution** or **interpolation**. A string with `{}` values is called a template string as it's the template from which string can be formatted by
inserting variable values.

By the way, _this_ is a more elegant way to combine variables into a string than concatenation and using the `str` function.

> NOTE: The `{}` can contain values that determine the index of the variable to be inserted, or it's name, or other cool magical stuff([see here for more info on these tricks](https://pyformat.info/)). Also, **Python3** supports yet another way to do **interpolation** using [**f-Strings**](https://cito.github.io/blog/f-strings/).

Let's insert some values into a template string by passing several positional values to the `format` method:

```python
print 'my name is {} and I am {} years old'.format('Arjun', 33)
```

We can specify the order that the positional arguments are inserted by putting integers inside the curly braces:

```python
print 'I want to substitute the {1} and {0} value in a different order'.format('second', 'first')
```

We can also name the insertion points and pass keyword arguments to `format` to replace named insertion points with their key-ed value:

```python
print 'Your name is {name}, today is {day_of_week} and we are in the {class_name} class' \
         .format(name='Sara', day_of_week='Saturday', class_name='Introduction to Python Bootcamp')
```

> ## TRY IT

Generate a **multiline** template string in the form of a short written letter that uses the values of the following variables, and sign your nickname in capital letters

- variables: `day_of_week`, `favorite_color`, `nickname`, and `salutation`
- hint: you need to declare these variable before using `format` if you are going to use positional arguments

<details>
<summary>Solution</summary>

You need to start by making a multiline string using `'''` or `"""`. Within that string, you can use empty `{}` if you plan on using positional arguments, but if you use keyword arguments, you can name and define their values right in the `format` method's arguments.

```python
my_string = \
'''Dear nobody,
I'm writing you this {day_of_week} to let you know that my favorite color is {favorite_color}.
That is all.
{salutation},
{nickname}'''.format(day_of_week='Saturday', favorite_color='black', salutation='Regards', nickname='Arjuan'.upper())

print(my_string)

# OR

day_of_week = 'Saturday'
favorite_color = 'black'
salutation = 'Regards'
nickname = 'Arjuan'

my_string = \
'''Dear nobody,
I'm writing you this {} to let you know that my favorite color is {}.
That is all.
{},
{}'''.format(day_of_week, favorite_color, salutation, nickname.upper())

print(my_string)
```

</details>

# INTEGERS AND FLOATS

Integer and Floats (floating point numbers) are some of the most commonly used numeric variable types. There are a few others but they are not used very often unless you are doing math with imaginary numbers, or math with very large or very small numbers (yes, a representation of infinity exists).

Any number with a decimal in it will be determined as a float:
- `3.14` is a float
- so is `8.` and `1.000000` even though we might think of these as basically integer values

## declaration

```python
my_int = 10
my_float = 1.6
type(my_int)
type(my_float)
```

## operators

Since we are talking about numbers, we expect to have all of the standard mathematical operators used with numeric computation. Here are the basic math operators in Python:

- `+`   addition
- `-`   subtraction
- `*`   multiplication
- `/`   division
- `**`  power
- `%`   remainder on division (modulus)

> NOTE: In **Python2**, when you divide integers by other integers, it will only return whole integer values (rounded down), but in **Python3** it will output a floating point result if a non-integer result is to be expected.

```python
my_int = 20

my_int / 3
my_int % 3
```

## conversion

You can easily convert Integers to Floats and vice versa.

To convert an Integer to a Float, you simply need to have a decimal place somewhere in the calculation:

```python
# notice how dividing / multiplying by 1. does not change the actual value of my_int
my_int = 256

type(my_int / 1.)
type(my_int * 1.)
```
To convert a Float to an Integer, you can use the `int` builtin function:

```python
my_float = 20

int(my_float)
type(int(my_float))
```

## maximum sizes

Since Python is a nice, friendly, high-level language, you don't have to worry about allocating memory and your variable values getting too large, unless you are dealing with very large or very small values. How large and how small?

```python
import sys

# the Maximum integer size for Python
sys.maxsize

# a bunch of information on maxiumum Float sizes
sys.float_info
```

> ## TRY IT

Let's play with these numbers at the extremities of what is allowed in Python:

1. What happens when you add `1` to `sys.maxsize`?
2. What happens when you multiply `sys.float_info[0]` (the max size) by `2`?

```python

```

<details>
<summary>Solution</summary>

```python
sys.maxsize + 1
```

1. Python creates a Long type integer, which has a larger maximum size and larger memory footprint.

```python
sys.float_info[0] * 2
```

2. Any value greater than the max float size is considered `inf`, the largest float value (`-inf` is the smallest float value).

</details>

## incrementing in place

You can combine the arithmetic operators with the assignment operator (`=`) to create an increment operator to modify numeric values in place. We saw this before when we were learning about string methods, as strings also support the `+=` operator, albeit for to a different purpose.

Let's try out some increment operators:

```python
my_int = 24

my_int += 2
print(my_int)

my_int -= 1
print(my_int)

my_int *= 6
print(my_int)

my_int /= 2
print(my_int)
```

## rounding floats

You can round Floats to their nearest Integer value using methods from the builtin `math` module.

- `math.ceil` - round up
- `math.floor` - round down

```python
# you must import this module to access it's methods
import math

math.ceil(3.14157)
math.floor(6.62607004)
```

You can round floats to a set number of decimal places using the builtin `round` function.

> NOTE: There are some significant issues with representing base 10 numbers as binary numbers, with binary being the representation that the computer actually stores. [These issues can show up in rounding amongst other places.](https://docs.python.org/2/tutorial/floatingpoint.html)

```python
# default number of decimal places is 0
round(3.14157) 

round(3.14157, 3)
```

## order of operations

Python arithmetic operators have a set order of operations that is similar but not exactly the same as what was taught in math class in school. You can use the parentheses operator `()` (not the same as the function call `()`) to set an order to avoid arbitrary miscalculations due to remembering the order or Python operations incorrectly.

**HIGHEST PRECEDENCE**

- `()`
- `**`
- `*`
- `/`
- `+`
- `-`

**LOWEST PRECEDENCE**

> ## TRY IT

Calculate the surface area of a square-based pyramid using the set `height`, `width`, and `length` variable values below.

[Here is the equation](https://www.google.com/search?q=surface+area+of+a+pyramid)

- hint: to perform a square root, you simply raise a value to the power 0.5 (`value ** 0.5`)

```python
height = 225
width = 200
length = 200

```

<details>
<summary>Solution</summary>

```python
# I shortened the variable names to make the equation easier to read
h = 225
w = 200
l = 200
area = l * w + l * ((w / 2) ** 2 + h ** 2) ** 0.5 + w * ((l / 2) ** 2 + h ** 2) ** 0.5

print(area) 
```
</details>

# LISTS

Lists are collections of values in a set order, and the values are **mutable** ie changeable, addable and deleteable. Lists is Python are **heterogenous** meaning all of the List values do not have to be of the same type.

Lists are declared as a collection or values separated by commas, between square brackets.

## declaration

A heterogeneous list:

```python
my_list = ["string", 20, True, 36.33, [0,1,2]]
```

Two-dimensional homogeneous (all of same type) list:

```python
tic_tac_toe_pos = [[0,1,1],
                   [1,2,0],
                   [0,2,0]]
# or
tic_tac_toe_pos = [[0, 1, 1], [1, 2, 0], [0, 2, 0]]
```

> ## TRY IT

How would we declare a 3-dimensional list? What does that even mean? &#128579;

Take the two 2-d lists below and put them together into a list called `list3`

```python
list1 = [['Irish Wolfhound', 'Great Dane'], ['Beagle', 'Collie'], ['Chihuahua', 'Toy Poodle']]
list2 = [['Tiger', 'Lion'], ['Jaguar', 'Bobcat'], ['Ocelot', 'Maine Coon']]

```

<details>
<summary>Solution</summary>

```python
list3 = [list1, list2]
```

Also a neat trick to print out this list or any python variable in a prettier format, is to use the `dumps` method from the `json` builtin module:

```
import json
print(json.dumps(list3, indent=2))
```

</details>

## length

Calculating the length from a list uses the same builtin function `len` as when we calculated string length:

```python
my_list = ["string", 20, True, 36.33, [0,1,2]]
len(my_list)
```

## indexing / slicing

Since lists have a set element order, you can select elements by index, or slice parts of them, just like with strings:

```python
my_list[0]
my_list[-2]
my_list[0:1]
my_list[::3]
```

## indexing multidimensional lists

Sometimes you end up with lists inside of lists. How do you index a value when it's in a list nested within another list? You simply index into the outer list, to select one of the inner lists, and then you index into that inner list!

For example, consider this tic-tac-toe board again:

```python
tic_tac_toe_pos = [[0,1,1],
                   [1,2,0],
                   [0,2,0]]
row0 = tic_tac_toe_pos[0]
row0_col2 = tic_tac_toe_pos[0][2]
```

> ## TRY IT

Index the `'Jaguar'` value from `list3`

```python
list1 = [['Irish Wolfhound', 'Great Dane'], ['Beagle', 'Collie'], ['Chihuahua', 'Toy Poodle']]
list2 = [['Tiger', 'Lion'], ['Jaguar', 'Bobcat'], ['Ocelot', 'Maine Coon']]
list3 = [list1, list2]
```

<details>
<summary>Solution</summary>

We know the outer most set of lists are dogs (index `0`) and cats (index `1`), so we start with `[1]`, now within the cats sublist, we want the middle-sized cat sub-sublist (index `1`), so we continue with `[1][1]`, and lastly, within the middle-sized cat sub-sublist, we select the `'Jaguar'` (index[0]) so we finally end up with `[1][1][0]`.

```python
list3[1][1][0]
```

</details>

## list ordering

When working with lists, there are some methods and tricks to manipulate the ordering of a list efficiently.

We can reverse a list using both the slice operator `[]` skip argument:

```python
my_list[::-1]
```

Or with the list `reverse` method:

```python
my_list.reverse()
```

Sorting a list can be done two ways:

- list `sort` method: sort a list in-place
  - sort the actual list itself
- `sorted` builtin function: return a sorted copy of the list
  - leave the original list alone


Returning a new sorted list:

```python
out_of_order = [0,6,2,7,8,3,1]

sorted(out_of_order)
print(out_of_order)
```

In-place list sorting:

```python
out_of_order = [0,6,2,7,8,3,1]

out_of_order.sort()
print(out_of_order)
```

## adding / deleting / changing values

We can add, delete, or change list values (otherwise known as mutating the list) using a variety of methods.

### changing values

We can use the index to change list values using the assignment `=` operator:

```python
print(my_list[3])
my_list[3] = 'changed'
print(my_list)
```

### adding values

We can add values at a certain index in a list using the `insert` list method:

```python
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
colors.insert(1, 'Red-Orange')
```
We can also add values to the end of the list using `append` and `extend` list methods"

- `append`: takes the value you pass it and adds it as the next index in the list
- `extend`: takes the value you pass it as an list, and adds the contents of that list to the end of the list

Let's use `append` to add a value to our `topics` list:

```python
topics = ['Statistics', 'Biology', 'Architecture', 'Microeconomics', 'Computational Complexity', 'Art', 'Composition']
topics.append('English')
```

Now let's use `extend` to add another two values to our `topics` list. Notice the difference in syntax for the arguments to each method:

```python
topics.extend(['French', 'Skiing'])
```

### deleting values

We can remove a list item both by it's value or by it's index using:

- `remove` list method: remove element by value
- `del` keyword: remove element by index
- `pop` list method: remove element by index and return it
  - this allows us to save the "popped" value in a variable if we choose

You can remove a list element by it's value:

```python
colors.remove('Red-Orange')
```

You can remove a list element by it's index:

```python
del colors[1]
print(colors)
```

And you can remove a list element by it's index and save the removed element:

```python
popped_color = colors.pop(-1)
print(popped_color, colors)
```

> ## TRY IT

What happens when you run this? Why?

```python
topics = ['Statistics', 'Biology', 'Architecture', 'Microeconomics', 'Computational Complexity', 'Art', 'Composition']
topics.extend('World History')
```

<details>
<summary>Solution</summary>

`extend` treats the argument (which is a string) as a list of characters, adding the contents of that list, letter
by letter, to the end of `topics`.

</details>

> ## TRY IT

Replace the colors `'Red'` and `'Orange'` from `colors` with `'Red-Orange'` and add `'Ultraviolet'` and add `'X-Ray'` to the end of the list:

```python
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
```

<details>
<summary>Solution</summary>

```python
colors.remove('Red')
colors.remove('Orange')
colors.insert(0, 'Red-Orange')
colors.extend(['Ultraviolet', 'X-Ray'])
```

</details>

## unpacking

You can get the values from a list and automatically declare multiple vars with those values simultaneously:

```python
topic1, topic2 =  topics[0:2]
print(topic1, topic2)
```

# TUPLES

Tuples are just like lists except they are a fixed length and their values are immutable. This makes them more computationally efficient at scale than lists, since the mutability of lists requires more computational resources under the hood than an immutable tuple.


## declaration

Tuples are declared as comma separated values between parentheses.

```python
my_tuple = ('Yes', 'No', 'Maybe')
```

Once declared, a tuple cannot be changes:

```python
# none of these will work since tuples are immutable and fixed length
my_tuple[0] = 'Oui'
my_tuple.append('Sort of')
```

We can see that tuples are more efficient than lists if we run the following to
see how long declaring either type takes when run each 10 million times:

```python
# timeit allows us to time our code, allowing us to 
# optimize our code for speed!
import timeit

timeit.timeit("x=(1,2,3,4,5,6,7,8)", number=10000000)
timeit.timeit("x=[1,2,3,4,5,6,7,8]", number=10000000)
```

It turns out that tuples also take far less low-level commands to store in physical memory. Keep in mind, the low level assembly language commands are the commands the machine uses to store bits and bytes, so efficiency at the level of computation can have big ramifications for efficiency at higher, more complex levels of computation such as in Python:

```python
# see how many operations each requires when the commands are disassembled into assembly
import dis
def a():
   x=(1,2,3,4,5,6,7,8)


def b():
   x=[1,2,3,4,5,6,7,8]


dis.dis(a)
dis.dis(b)
```

# DICTS

Dictionaries (dicts) store key-value pairs, where the key must be a string, and the value can be any variable type. Below vesion **Python3.6**, the keys are ambiguously ordered, unlike list indices, but in **Python3.6** and above, their order is based on the order they are put in the dictionary.

## declaration

Dicts use curly braces to enclose key value pairs, where the key is a quotation enclosed string, and the value is
written however the type you'd like to assign to the key is normally written. Instead of using `=` to assign values,
dicts use `:`, and the key value pairs are separated by commas.

Here's an example of a simple dict:
```python
simple_dict = {
    'food': 'sandwich',
    'amount': 1,
    'calories': 200,
    'eaten': False
}
```

And here is a more complex dict, where some of the key's values are dicts themselves:

```python
my_dict = {
   'first_name': 'Arjun',
   'last_name': 'Ray',
   'birthday': {
       'year': 1984,
       'month': 'September',
       'day': 11
   },
   'fav_colors': [
       'black',
       'red'
   ],
   'alive': True,
}
```

## pretty printing a dict

JSON (JavaScript Object Notation) is a nearly universal data format that uses key value pairs. Python dicts are
interconvertible to this data type which is essentially a string that other language can parse back into data objects.
Pythons `json` module methods also allow us to print out data structures in more readable ways

Let's use `json.dumps` again to print out `my_dict` in a more readable way:

```python
# without json.dumps
print(my_dict)

# with json.dumps
import json
print(json.dumps(my_dict, indent=4))
```

## indexing

Dictionary values are selected by their key name:

```python
my_dict['first_name']
my_dict['birthday']
```

Dictionaries can be nested inside of dictionaries, and we index into nested dicts the same general way we index into nested lists:

```python
my_dict['birthday']['year']
```

## listing keys and values

Dicts have methods for getting back a list of either their keys or values, called `keys` and `values`:

```python
my_dict.keys()
my_dict.values()
```

> ## TRY IT

Make a dictionary with a bunch of keys in non alphabetical order called `test`
look at output from `test.keys()`. what do you notice?

<details>
<summary>Solution</summary>

If you are on not on **Python3.6** or above, dictionaries have ambiguous key order. `test.keys()` likely outputs the keys in an order is
not the order you declared them in. If you are on **Python3.6** or above, the dictionary key order resembles the order that the dictionary was declared in:

```python
test = {
    'zebra': 3,
    'halo': False,
    'jersey': [34, 45, 545],
    'magnet': 4.6
}

test.keys()
```

</details>

## adding / removing / changing key values

You can change a pre-existing key value the same way you add a new key, using the key string within square brackets and the assignment operator to assign a new value.

### adding / changing

Changing a pre-existing key value:

```python
my_dict['alive'] = False
```

Adding a new key with a new value:

```python
my_dict['occupation'] = 'instructor'
```

### removing

Two methods are available for removing key-value pairs from a Dict:

- `del` operator: remove element by key
- `pop` list method: remove element by key and return it's value

You can remove a key-value pair using `del`:

```python
del my_dict['alive']
print(my_dict)
```

You can remove a key-value pair and save the value using `pop`:

```python
occupation = my_dict.pop('occupation')
print(occupation, my_dict)
```

> ## TRY IT

Rename the `alive` key in `my_dict` to `hungry`:

- hint: You aren't actually renaming the key. Think about the add / remove methods above

<details>
<summary>Solution</summary>

Remember that `pop` returns the value for the key-value pair that was removed, so we can grab out the value of `'alive'` while removing the key and immediately assign it to a new `'hungry'` key.

```python
my_dict['hungry'] = my_dict.pop('alive')
```

</details>

## json to dict

The JSON data format is used for all kinds of language-agnostic things these days. For example, JSON is the main data format that is used for sending and receiving data over the internet. In Python, you can easily load JSON data directly into a python dictionary as the two data structures are interconvertible.

Let's get a JSON string loaded into Python:

> NOTE: Notice how this is actually not a Dict, even though it has the same "shape"
it is in fact a long multi-line string with very strict (JSON) formatting.

```python
json_string = \
'''{
   "id": "0001",
   "type": "donut",
   "name": "Cake",
   "ppu": 0.55,
   "batters":
       {
           "batter":
               [
                   { "id": "1001", "type": "Regular" },
                   { "id": "1002", "type": "Chocolate" },
                   { "id": "1003", "type": "Blueberry" },
                   { "id": "1004", "type": "Devil's Food" }
               ]
       },
   "topping":
       [
           { "id": "5001", "type": "None" },
           { "id": "5002", "type": "Glazed" },
           { "id": "5005", "type": "Sugar" },
           { "id": "5007", "type": "Powdered Sugar" },
           { "id": "5006", "type": "Chocolate with Sprinkles" },
           { "id": "5003", "type": "Chocolate" },
           { "id": "5004", "type": "Maple" }
       ]
}'''
```

Now we can convert it to a Dict using the `loads` method from the aforementioned Python `json` module:

```python
import json
cake_dict = json.loads(json_string)
```

And now we can access data inside `cake_dict` just like we would any other Python Dict!

```python
print (cake_dict['batters']['batter'][0])
```

> ## TRY IT

Pretty print the `topping` key list within `cake_dict` with an indent of `5` using `json.dumps`:

```python
```

<details>
<summary>Solution</summary>

```python
print(json.dumps(cake_dict['topping'], indent=5))
```

</details>

# BOOLEANS

Booleans are simply `True` and `False` values and are an extremely important and powerful part of any programming language's logic. When you use a logical operator for a set of expressions, it will return a boolean value of `True` or `False`. For example, the expression `5 > 3` resolves to (basically turns into) `True`.

## logical operators

Python provides several standard operators for performing comparative and associative logic:

- `==` :          equal in value
- `is` :          identity
- `!=` :           not equal in value
- `<` :           less than
- `>` :           greater than
- `<=` :          less than or equal to
- `>=` :          greater than or equal to
- `and` :         and operator
- `or` :          or operator
- `not` :         inverse modifier
- `in` :          membership operator

Logical operators always compare **2** values against eachother and return a Boolean:

```python
5 < 6

3 in [3, 4, 6]
```

## equality vs identity

Equality `==` compares the values of the two statements, whereas identity `is` compares whether or not the two
statements refer to the same object:

```python
a = [1, 2, 3]
```

Assignment does not make a copy of `a`, but actually sets `b` to point to `a`:

```python
b = a
```

Both of these statements will be `True`:

```python
a == b
a is b
```

You can see that `a` and `b` are actually the same list as modifications of `a` modify `b` as well:

```python
a.insert(0, 'first')
print(a, b)
```

To make a copy of a list, you can use the `list` method with a list as it's argument:

```python
c = list(a)
```

While the `a` and `c` have equality, they don't share identity:

```python
c == a
c is a
```

This point is further emphasized by the fact that modifications of `a` are not reflected in `c`:

```python
a.remove('first')
print(a, c)
```

> ## TRY IT

Make the following comparisons:

1. 4 is greater than 5
2. 5 is not equal to 4
3. 5 is greater than or equal to 4 and 4 is greater than or equal to 6
4. list `a` shares identity with list `b` or list `a` shares identity with list `c`

```python

```

<details>
<summary>Solution</summary>

1
```python
4 > 5
```

2
```python
5 != 4
# or
not 5 == 4
```

3
```python
5 >= 4 and 4 >= 6
```

4
```python
a is b or a is c
```

</details>

## logical combinations

Statements joined with `and` are all required to be `True` to return `True`, otherwise they return `False`. One way to think of it is that one bad `False` spoils the bunch.

Let's see what happens when we combine Boolean values with `and` associative logic:

```python
True and True
True and False
False and False
True and True and True and True and False
```

Statements joined with `or` require any of the statements to be `True` to return `True`, otherwise they return `False`.

Let's see what happens when we combine Boolean values with `or` associative logic:

```python
True or False
False or False
False or False or False or False or True
```

So what happens if you combine `and` and `or`? what if you use `not` as well?
The following precedence is followed for logical operators:

HIGHEST PRECEDENCE

- `not`
- `and`
- `or`

LOWEST PRECEDENCE

[more info on logical operator precedence](https://docs.python.org/2/reference/expressions.html#operator-precedence)

Let's test out some of these combinations, using parentheses to emphasize the natural order or precedence for the logic:

```python
True and False or False

# equivalent to
(True and False) or False
```

```python
not True and False or False

# equivalent to
(not (True and False)) or False
```

## in operator

The `in` operator can be used to check if a value exists within a collection variable (such as a dict, list, tuple, and it works with strings as well).

```python
'hello' in 'hello world'
5 in [1, 2, 3, 4, 5]
'5' in [1, 2, 3, 4, 5]
'5' not in [1, 2, 3, 4, 5]
'my_key' in {'first_key': 0, 'my_key': 1}
```

> ## TRY IT

Try running this clever Python easter egg and explain why it works:

```python
import this
love = this
this is love
love is True
love is False
love is not True or False
love is love
```

<details>
<summary>Solution</summary>

When you assign `love` to `this`, `love` is not pointing to `this`, so they share identity, thus `love is this` returns `True`, however the type of `love` is a string (try `type(love)`) so it is neither `True` nor `False`, which
is why `love is True` and `love is False` returns `False`, and `love is not True or False` (equivalent to `love is not(True or False)`) returns `True`. The last statement is a simply identity so of course it returns `True`.

</details>

# CONTROL FLOW

Control flow is a way of breaking up the flow of execution in a program based on logical conditions.

The main control flow statements are `for`, `if`/`elif`/`else`, and `while`. 

## if statements

`if` statements allow us to evaluate whether a logic statement is `True`, and if so, it will run the indented code block, ie:

```python
if some_logic_statement_is_True:
   # do something
```

Notice how one of these blocks will **always** run because `5 > 4` will always be `True`, and one of these blocks will **never** run becasue `5 < 4` will always be `False`:

```python
if 5 > 4:
   print('5 is greater than 4')
   print('great')

if 5 < 4:
   print('5 is less than 4')
```

> ## TRY IT

Try running the statement below. Why doesn't it work?

```python
if 5 > 4:
print('5 is greater than 4')
```

<details>
<summary>Solution</summary>

Conditional blocks such as `if` statements require the block below the condition to be indented.

</details>

You can chain multiple conditions using `elif` (else if) statements after an `if`. the program will try each condition
until it reaches one that evaluated to `True`, and only run the indented code block for that condition. If it passes
through all `if` and `elif` conditions without a True evaluation, it will run the indented code block within the
`else` statement, if it is provided.

```python
my_val = 20
if my_val > 10:
   print('greater than 10')
elif my_val < 0:
   print('is negative')
elif my_val == 0:
   print('is 0')
else:
   print('neither greater than 10 nor negative')
```

> ## TRY IT

Write an `if`/`elif`/`else` block that will check if a string var called `my_val2`:

1. if it contains the letter `'a'`, print `'contains the letter a'`
2. or else if it is greater than `5` characters long, print `'is greater than 5 characters long'`
3. or else --> print `'oh well'`

```python
my_val2 = 'hello my name is'

```

<details>
<summary>Solution</summary>

One important thing to notice is that only one of these blocks will ever run, so even though `my_val2` both contains the letter `'a'` and is longer than `5`, only the first condition will run:

```python
my_val2 = 'hello my name is'

if 'a' in my_val2:
   print('contains the letter a')
elif len(my_val2) > 5:
   print('is greater than 5 characters long')
else:
   print('oh well')
```

</details>

> ## TRY IT

Reverse the order of the first two conditions in the above solution. What happens? Why?

```python

```

<details>
<summary>Solution</summary>

Now only the new first condition will run, so we'll never see `'contains the letter a'` unless the first condition is false for this variable:

```python
if len(my_val2) > 5:
   print('is greater than 5 characters long')
elif 'a' in my_val2:
   print('contains the letter a')
else:
   print('oh well)
```

If we wanted both of the first condition blocks to potentially run, we could write two `if` blocks such as:

```python
if len(my_val2) > 5:
   print('is greater than 5 characters long')

# it's good code style to put a space between your `if` blocks
if 'a' in my_val2:
   print('contains the letter a')
```

</details>

## for

For loops are used when you have a known number of loops you want to perform. You can use for loops to iterate through all of the elements in an iterable variable type, types that include lists, dicts, strings, and ranges.

> NOTE: A range is actually just two values, a **start**, and a **stop** value within a range, such as `4` and `10`. When the range is actually declared, all you write is:
> ```python
> my_range = range(<start>, <stop>)
> ```
> When the range is actually used, Python automatically expands the range into a list, starting at the **start** value (inclusive) and ending _before_ the **stop** value (exclusive) so that `my_range` would turn into `[4,5,6,7,8,9]` when it was then used for something after it's declaration. Storing ranges in this way takes up less memory as the ranges are only expanded into list if and when they are used, as opposed to lists which take up their full amount of memory right when they are declared whether or not they end up being used.

For loops always start with a `for` keyword, and then there is an expression that describes how you want to handle receiving each element in your iteration within the block of the `for` loop then a `:`. Notice below that the block is simply the indented region immediately following the `for` line, all of whose lines will be run for each iteration of the loop. The block will have each element available within it for each iteration, named as whatever you called it in the expression.

Let's look at an example of how to use `for` loops on a list. Out iteration expression is `item in our_list` which tells the for loop that you want to iterate through elements in `our_list` and within the block of the `for` loop, have access to that element as the local variable (only available inside the block) called `item`. See how this works:

```python
our_list = ['hi', 'there', 'how', 'are', 'you?']
for item in our_list:
   print(item)
```

You can use for loops to iterate through values in a range:

```python
for n in range(0,200):
   print(n)
```

Sometimes you also want to get the index of the element you are on during iteration, not just the value. For that, you can use the `enumerate` built in function which turns an iterable variable into a list of `(<index>, <value>)` pairs, allowing you to capture them both as named local variable in the `for` block and use them:

```python
for index, item in enumerate(our_list):
   print('index of item: {}\nvalue of item: {}\n'.format(index, item))
```

> ## TRY IT

How might we iterate through the first `4` items in a list of length `8`?

<details>
<summary>Solution</summary>

You could use a range and be clever by slicing the range on usage:

```python
eight_list = range(0,8)
for val in eight_list[0:4]:
    print(val)
```

Or, you could use the `break` keyword which allows you to break out of a for loop at any time:

```python
my_list = ['hello', 'how', 'are', 'you', 'doing', 'today?', 'I\'m', 'well']
for idx, val in enumerate(my_list):
    if idx > 3:
        break
    else:
        print(val)
```

</details>

It is possible to iterate through the keys in a dict using the `in` operator:

```python
our_dict = {
   'robots': 0,
   'ninjas': 1
}

# iterate through keys in dict
for key in our_dict:
   print(key)
```

You can iterate through the keys and values in a dict by using the dict method `iteritems()` which returns a list of `(<key>, <value>)` pairs from a list, allowing you to iterate through them, very much like `enumerate` for lists:

```python
# iterate through keys and values in dict
for key, value in our_dict.iteritems():
   print('key: {}\nvalue: {}\n'.format(key, value))
```

You may have notices that string act pretty much like lists, and indeed, you can iterate through a string's characters:

```python
# iterate through string
for char in 'hello':
   print char
```

Importantly, you can always break out a `for` loop by using the `break` keyword:

```python
for i in range(0, 10000000):
   print(i)
   if i == 100:
       break
```

Similarly, you can skip particular iterations by using the `continue` keyword, which forces the `for` loop to go to the next iteration without running any more lines of code in the current iteration:

```python
for i in range(0,10):
   if i % 2 == 0:
       continue
   print(i)
```

> ## TRY IT

This is a famous programming interview question called FizzBuzz that was designed to filter out "the 99.5% of
programming job candidates who can't seem to program their way out of a wet paper bag". Give it a shot!
write a program that prints the numbers from `1` to `100`, but for multiples of `3` print `“Fizz”` instead of the number
and for the multiples of `5` print `“Buzz”`. For numbers which are multiples of both `3` and `5` print `“FizzBuzz”`:

```python

```

<details>
<summary>Solution</summary>

The most important thing to realize here is that only one conditional block will run in an `if`, `elif`, `else` chain, so the order you put the conditions in can be important. In this case, if you were to check `i % 3 == 0` or `i % 5 == 0` before `i % 15 == 0`, you would never see `"Fizzbuzz"` for numbers divisible by `15` since one of the other two conditions would have been true before it every reached the `i % 15 == 0` condition. Therefore, the `i % 15 == 0` condition has to be checked first in each iteration. It's also important to note that `i % 15 == 0` is a stand in for `i % 5 == 0 and i % 3 == 0` since any number divisible by `5` and `3` must be divisible by `15`:

```python
for i in range(1,101):
   if i % 15 == 0:
       print('FizzBuzz')
   elif i % 3 == 0:
       print('Fizz')
   elif i % 5 == 0:
       print('Buzz')
   else:
       print(i)
```

</details>

## while

`while` loops should be used when you want to wait for some process that takes an unknown amount of time to finish. If you know how many loop iterations you will have, such as in the case of iterating over a enumerable variable, consider using a `for` loop instead. `while` loops keep looping as long as the condition following the `while` statement remains `True`. `while` loops can also be ended using the `break` keyword and loops can be continued using the `continue` keyword.

Let's create a process that takes a random amount of time to finish:

```python
import time
import random

milliseconds = 0
# here is the random number of milliseconds this process will run for
# between 20 and 200 milliseconds
max_milliseconds = random.randint(20, 200)

while milliseconds <= max_milliseconds:
   print('{} milliseconds elapsed'.format(milliseconds))

   # this method will pause the the program for 1 millisecond
   time.sleep(0.1)
   milliseconds += 1
```

# FUNCTIONS

Functions define blocks of code which take in arguments, perform some logical operations on those argument and then return something. To declare a function, we use the `def` keyword followed by the name of the function, then a `()` containing comma separated parameters (sometimes none), then `:`.

Parameters are all of the variables the function needs to execute as defined between the `()`. When a function is run, the actual values passed in for each parameter name are called the arguments.

As we have seen, functions must be called using '<function name>(<function arguments>)' in order to run it. A function block execution finishes when it reaches the end of it's indented code block, or it hits a `return` statement, which ends function execution and returns a value. Functions that reach their end without hitting a `return` keyword automatically return the `undefined` value.

## declaration

A `return` keyword can be useful to return data to the line where a function is run from, allowing us to save the value in a variable. In the example below, `my_func` is declared using `def my_func(name, age):`, and then it returns the value of a template string which has interpolated the parameter values for `name` and `age`. When the function is run using the argument `"Arjun"` for the `name` parameter and `33` for the `age` parameter, we save the returned string as `info_str`, allowing us to print it:

```python
def my_func(name, age):
   return 'my name is {} and I am {} years old'.format(name, age)

info_str = my_func('Arjun', 33)
print(info_str)
```

## parameters

You can set default parameters for functions, which is the value they will take on if no argument is passed for that parameter.

> NOTE: Parameters with default values **must** always come after arguments that do not have default values.

```python
def say_it(exclamation, name='You'):
   print('{} {}!'.format(exclamation ,name.upper())

say_it('Wow')
say_it('Oh my god', 'Becky')
```

Functions can take a variable number of arguments and make a local list with those arguments. You use the `*<list name>` parameter to do this, and this must come after all of the positional arguments:

```python
def print_before_each_in_list(before_text, *args):
   for item in args:
       print '{} {}'.format(before_text, item)
print_before_each_in_list('Here\'s an item', 'cat', 'hairbrush', 'VCR', 'telephoto lens')
```

Functions can also take `<key>=<value` arguments and make a local dictionary with those arguments. You use the `**<dict name>` parameter to do this, and this must come after all of the individual named arguments, and list argument:

```python
def print_kwargs(**kwargs):
   for key, val in kwargs.iteritems():
       print('{}: {}'.format(key, val))

print_kwargs(name="Arjun", age=33, occupation="?")
```

> ## TRY IT

Write a function called `print_if_key_in_list` that takes a `prefix` argument with a default value of `'\t'`, a list
argument as `*args` and a dict arguments as `**kwargs`. For every key in `kwargs`, if the key is also in `args`, print
the `prefix` and the key value:

```python

```

<details>
<summary>Solution</summary>

Remember that list params have to be defined after positional params, and dict params after that!

```python
def print_if_key_in_list(prefix='\t', *args, **kwargs):
   for key, val in kwargs.iteritems():
       if key in args:
           print('{} {}'.format(prefix, val))

print_if_key_in_list('~~~~', 'tele', 'email', tele='7742700099', address='32 Franklin ave', email='georger@got.org')
```

</details>

## scope

The indented block of code inside a function `def` statement is scoped to the function, which means that it only available locally within the function block. If you declare new variables inside of the function block, they will not be accessible outside the function block. However,
you can access values of pre-existing variable from the outer scope from within the function.

You can access the variables made outside of the function within it:

```python
my_var = 20

def get_my_var():
    print(my_var)

get_my_var()
```

However, you cannot change the variable in the outer scope:

```python
my_var = 20


def change_my_var():
    my_var = 30
    # this is a different 'my_var' variable than what is in the outer scope
    print(my_var)

change_my_var()
print(my_var)
```

The outer scope cannot access variables declared within the function:

```python
def in_the_block():
    block_var = 'hi'

in_the_block()
print(block_var)
```