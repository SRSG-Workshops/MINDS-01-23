---
layout: page
title: Challenges
slug: python-novice-challenges
---

## Python basics: Variables, Objects, Arrays, Lists etc


> #### What's inside the box?
>
> Draw diagrams showing what variables refer to what values after each statement in the following program:
>
> > ~~~
> > weight = 70.5
> > age = 35
> > # Take a trip to the planet Neptune
> > weight = weight * 1.14
> > age = age + 20
> > ~~~
> > {: .python}
> 
> {: .challenge}

> #### Sorting out references
>
> What does the following program print out?
>
> > ~~~
> > first, second = 'Grace', 'Hopper'
> > third, fourth = second, first
> > print(third, fourth)
> > ~~~
> > {: .python}
> 
> {: .challenge}


## Arrays, Lists, etc.


> #### Slicing strings
>
> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> What is `element[-1]`?
> What is `element[-2]`?
> Given those answers,
> explain what `element[1:-1]` does.
> 
> {: .challenge}



> #### Slicing From the End
>
> Use slicing to access only the last four characters of a string or entries of a list.
>
> > ~~~
> > string_for_slicing = "Observation date: 02-Feb-2013"
> > list_for_slicing = [["fluorine", "F"], ["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
> > ~~~
> > {: .python}
>
> ~~~
> "2013"
> [["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
> ~~~
> > {: .output}
>
> Would your solution work regardless of whether you knew beforehand
> the length of the string or list
> (e.g. if you wanted to apply the solution to a set of lists of different
> lengths)?
> If not, try to change your approach to make it more robust.
> 
> {: .challenge}


> #### Overloading
>
> `+` usually means addition, but when used on strings or lists, it means
> "concatenate".
> Given that, what do you think the multiplication operator `*` does on lists?
> In particular, what will be the output of the following code?
>
> > ~~~
> > counts = [2, 4, 6, 8, 10]
> > repeats = counts * 2
> > print(repeats)
> > ~~~
> > {: .python}
> 
> 1.  `[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]`
> 2.  `[4, 8, 12, 16, 20]`
> 3.  `[[2, 4, 6, 8, 10],[2, 4, 6, 8, 10]]`
> 4.  `[2, 4, 6, 8, 10, 4, 8, 12, 16, 20]`
>
> The technical term for this is *operator overloading*:
> a single operator, like `+` or `*`,
> can do different things depending on what it's applied to.
> 
> {: .challenge}


## Repeating actions using loops


> #### From 1 to N
>
> Python has a built-in function called `range` that creates a list of numbers:
> `range(3)` produces `[0, 1, 2]`, `range(2, 5)` produces `[2, 3, 4]`.
> Using `range`,
> write a loop to print the first 3 natural numbers:
>
> > ~~~
> > 1
> > 2
> > 3
> > ~~~
> > {: .python}
> 
> {: .challenge}


> #### Turn a String Into a List
>
> Use a for-loop to convert the string "hello" into a list of letters:
>
> > ~~~
> > ["h", "e", "l", "l", "o"]
> > ~~~
> > {: .python}
> 
> Hint: You can create an empty list like this:
>
> ~~~
> my_list = []
> ~~~
> > {: .python}
> 
> {: .challenge}


> #### Computing powers with loops
>
> Exponentiation is built into Python:
>
> > ~~~
> > print(5 ** 3)
> > 125
> > ~~~
> > {: .python}
> 
> Write a loop that calculates the same result as `5 ** 3` using multiplication (and without exponentiation).
>
> {: .challenge}

> #### Reverse a string
>
> Write a loop that takes a string, and produces a new string with the characters in reverse order, so `Newton`
> becomes `notweN`.
> {: .challenge}

## Making choices

> #### How many paths?
>
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> * A
> * B
> * C
> * B and C
>
> > ~~~
> > if 4 > 5:
> >     print('A')
> > elif 4 <= 5:
> >     print('B')
> > elif 4 < 5:
> >     print('C')
> > ~~~
> > {: .python}
> 
> {: .challenge}

> ## What Is Truth?
>
> `True` and `False` are special words in Python called `booleans`
> which represent true and false statements.
> However, they aren't the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
>
> > ~~~
> > if '':
> >     print('empty string is true')
> > if 'word':
> >     print('word is true')
> > if []:
> >     print('empty list is true')
> > if [1, 2, 3]:
> >     print('non-empty list is true')
> > if 0:
> >     print('zero is true')
> > if 1:
> >     print('one is true')
> > ~~~
> > {: .python}
> 
> {: .challenge}

## Modularising your code using functions

> #### Combining Strings
>
> "Adding" two strings produces their concatenation:
> `'a' + 'b'` is `'ab'`.
> Write a short function called `fence` that takes two parameters called
> `original` and `wrapper` and returns a new string that has the wrapper
> character at the beginning and end of the original.
> A call to your function should look like this:
>
> > ~~~
> > print(fence('name', '*'))
> > ~~~
> > {: .python}
>
> > ~~~
> > *name*
> > ~~~
> > {: .output}
> 
> {: .challenge}


> ## How do function parameters work?
>
> We actually used the same variable name `fahr` in our main code and
> and the function. But it's important to note that even though they
> share the same name, they don't refer to the same thing. This is
> because of variable **scoping**.
>
> Within a function, any variables that are created (such as parameters
> or other variables), only exist within the **scope** of the function.
>
> For example, what would be the output from the following:
>
> > ~~~
> > f = 0
> > k = 0
> >
> > def multiply_by_10(f):
> >   k = f * 10
> >   return k
> >
> > multiply_by_10(2)
> > multiply_by_10(8)
> >
> > print(k)
> > ~~~
> > {: .python}
>
> 1. 20
> 2. 80
> 3. 0
> 
> {: .challenge}

> ## Does the sum of a list equal a given value?
>
> Write a function to take a list of numbers and another value, and return
> whether or not the sum of the list of numbers is equal to that value.
>
> Following the function definition, a call to your function should look like this:
>
> > ~~~
> > is_sum_equal([1,2,3], 6))
> > True
> > is_sum_equal([2,4,6], 100)
> > False
> > ~~~
> > {: .python}
> 
> This is really useful, since it means we don't have to worry about
> conflicts with variable names that are defined outside of our function
> that may cause it to behave incorrectly.
> 
> {: .challenge}

> ## Readable Code
>
> Revise a function you wrote for one of the previous exercises to try to make
> the code more readable. Then, collaborate with one of your neighbors
> to critique each other's functions and discuss how your function
> implementations
> could be further improved to make them more readable.
> 
> {: .challenge}


## How to deal with problems in your code


> #### Identifying Variable Name Errors
>
> 1. Read the code below (or open the file `error_name_ch.py` in code folder), and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message.
>    What type of `NameError` do you think this is?
>    In other words, is it a string with no quotes,
>    a misspelled variable,
>    or a variable that should have been defined but was not?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
>
> > ~~~
> > for number in range(10):
> >     # use a if the number is a multiple of 3, otherwise use b
> >     if (Number % 3) == 0:
> >         message = message + a
> >     else:
> >         message = message + "b"
> > print(message)
> > ~~~
> > {: .python}
> 
> {: .challenge}

> #### Identifying Syntax Errors
>
> 1. Read the code below (or open the file `error_syntax_ch.py` in code folder), and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
>
> > ~~~
> > def another_function
> >   print("Syntax errors are annoying.")
> >    print("But at least python tells us about them!")
> >   print("So they are usually not too hard to fix.")
> > ~~~
> > {: .python}
> 
> {: .challenge}



> #### Identifying Index Errors
>
> 1. Read the code below, and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message. What type of error is it?
> 3. Fix the error.
>
> > ~~~
> > seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> > print('My favorite season is ', seasons[4])
> > ~~~
> > {: .python}
> 
> {: .challenge}


> #### Reading Error Messages
>
> Read the python code (or open the file `error_index_ch.py` in code folder) and the resulting traceback below, and answer the following questions:
>
> 1.  How many levels does the traceback have?
> 2.  What is the function name where the error occurred?
> 3.  On which line number in this function did the error occurr?
> 4.  What is the type of error?
> 5.  What is the error message?
>
> > ~~~
> > # This code has an intentional error. Do not type it directly;
> > # use it for reference to understand the error message below.
> > def print_message(day):
> >     messages = {
> >         "monday": "Hello, world!",
> >         "tuesday": "Today is tuesday!",
> >         "wednesday": "It is the middle of the week.",
> >         "thursday": "Today is Donnerstag in German!",
> >         "friday": "Last day of the week!",
> >         "saturday": "Hooray for the weekend!",
> >         "sunday": "Aw, the weekend is almost over."
> >     }
> >     print(messages[day])
> >
> > def print_friday_message():
> >     print_message("Friday")
> >
> > print_friday_message()
> > ~~~
> > {: .python}
> 
> > ~~~
> > Traceback (most recent call last):
> >   File "<stdin>", line 1, in <module>
> >   File "<stdin>", line 2, in print_friday_message
> >   File "<stdin>", line 11, in print_message
> > KeyError: 'Friday'
> > ~~~
> > {: .error}
> 
> {: .challenge}

> #### Debug with a Neighbour
>
> Take a function that you have written today, and introduce a tricky bug.
> Your function should still run, but will give the wrong output.
> Switch seats with your neighbor and attempt to identify - or debug - the problem
> that they introduced into their function.
> {: .challenge}

> #### Not Supposed to be the Same
>
> You are assisting a researcher with Python code that computes the
> Body Mass Index (BMI) of patients (open the file `error_silent_ch.py` in code folder).  The researcher is concerned because
> all patients seemingly have identical BMIs, despite having different
> physiques.  BMI is calculated as **weight in kilograms**
> divided by the the square of **height in metres**.
>
> > ~~~
> > patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
> >
> > def calculate_bmi(weight, height):
> >     return weight / (height ** 2)
> > 
> > for patient in patients:
> >     height, weight = patients[0]
> >     bmi = calculate_bmi(height, weight)
> >     print("Patient's BMI is: %f" % bmi)
> > ~~~
> > {: .python}
>
> > ~~~
> > Patient's BMI is: 21.604938
> > Patient's BMI is: 21.604938
> > Patient's BMI is: 21.604938
> > ~~~
> > {: .output}
> 
> {: .challenge}

## Reading and analysing Patient data using libraries

> #### Thin slices
>
> From our previous topic challenges, the expression `element[3:3]` produces an [empty string](reference.html#empty-string),
> i.e., a string that contains no characters.
> If `data` holds our array of patient data,
> what does `data[3:3, 4:4]` produce?
> What about `data[3:3, :]`?
> 
> {: .challenge}

## Data Visualisation

> #### Make your own plot
>
> Create a plot showing the standard deviation of the inflammation data for each day across all patients.
> Hint: `data.std(axis=0)` gives you standard deviation.
> 
> {: .challenge}

> #### Moving plots around
>
> Modify the program to display the three plots on top of one another instead of side by side.
> {: .challenge}

## Making choices

> #### How many paths?
>
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> * A
> * B
> * C
> * B and C
>
> > ~~~
> > if 4 > 5:
> >     print('A')
> > elif 4 <= 5:
> >     print('B')
> > elif 4 < 5:
> >     print('C')
> > ~~~
> > {: .python}
> 
> {: .challenge}

