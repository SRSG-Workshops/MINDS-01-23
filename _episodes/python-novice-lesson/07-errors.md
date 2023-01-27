---
lesson_title: 'Building Programs with Python'
lesson_schedule_slug: python-novice-schedule
title: Handling Errors
slug: python-novice-handling-errors
minutes: 40
teaching: 15
exercises: 25
questions:
- How can I use an error to understand where my code stopped working?
- What types of errors are there in Python?
objectives:
- Be able to read and understand how Python reports errors through tracebacks
- Understand how and why errors occur in Python, and common types of errors
keypoints:
- Python has built in error names that give a hint to the type of problem you are looking for.
- We can use the traceback to find which bit of the code threw an error.
---


Every programmer encounters errors,
both those who are just beginning,
and those who have been programming for years.
Encountering errors and exceptions can be very frustrating at times,
and can make coding feel like a hopeless endeavour.
However,
understanding what the different types of errors are
and when you are likely to encounter them can help a lot.
Once you know *why* you get certain types of errors,
they become much easier to fix.

Errors in Python have a very specific form,
called a [traceback](reference.html#traceback).
Let's examine one:



~~~
print(a)
~~~
{: .python}


~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
~~~
{: .error}

Take a look at the traceback. It shows 1 level of error, here, Name Error. The traceback shows shows the line number where the error occured and the type of error.

Variable name errors come with some of the most informative error messages, which are usually of the form “name ‘the_variable_name’ is not defined”.


## Variable Name Errors

In the above example, let's look at why does this error message occur?
That's harder question to answer,
because it depends on what your code is supposed to do.
However,
there are a few very common reasons why you might have an undefined variable.
The first is that you meant to use a [string](reference.html/#string), but forgot to put quotes around it:


~~~
print(hello)
~~~
{: .python}

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
~~~
{: .error}

The second is that you just forgot to create the variable before using it.
In the following example,
`count` should have been defined (e.g., with `count = 0`) before the for loop:



~~~
for number in range(10):
    count = count + number
print("The count is:", count)
~~~
{: .python}


~~~
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'count' is not defined
~~~
{: .error}

Finally, the third possibility is that you made a typo when you were writing your code.
Let's say we fixed the error above by adding the line `Count = 0` before the for loop.
Frustratingly, this actually does not fix the error.
Remember that variables are [case-sensitive](reference.html/#case-sensitive),
so the variable `count` is different from `Count`. We still get the same error, because we still have not defined `count`:


~~~
Count = 0
for number in range(10):
    count = count + number
print("The count is:", count)
~~~
{: .python}

~~~
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'count' is not defined
~~~
{: .error}


> ## Identifying Variable Name Errors
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
>
> > ## Solution
> > 3 `NameError`s for `number` being misspelled, for `message` not defined, and for `a` not being in quotes.
> >
> > Fixed version:
> >
> > > ~~~
> > > message = ""
> > > for number in range(10):
> > >     # use a if the number is a multiple of 3, otherwise use b
> > >     if (number % 3) == 0:
> > >         message = message + "a"
> > >     else:
> > >         message = message + "b"
> > > print(message)
> > > ~~~
> > > {: .python}
> > 
> > {: .solution}
> 
> {: .challenge}

## Syntax Errors

When you forget a colon at the end of a line,
accidentally add one space too many when indenting under an `if` statement,
or forget a parenthesis,
you will encounter a [syntax error](reference.html/#syntax-error).
This means that Python couldn't figure out how to read your program.
This is similar to forgetting punctuation in English:
for example,
this text is difficult to read there is no punctuation there is also no capitalization
why is this hard because you have to figure out where each sentence ends
you also have to figure out where each sentence begins
to some extent it might be ambiguous if there should be a sentence break or not

People can typically figure out what is meant by text with no punctuation,
but people are much smarter than computers.
If Python doesn't know how to read the program,
it will just give up and inform you with an error.
For example:

~~~
def some_function()
    msg = "hello, world!"
    print(msg)
     return msg
~~~
{: .python}

~~~
  File "<stdin>", line 1
    def some_function()

SyntaxError: invalid syntax
~~~
{: .error}

Here, Python tells us that there is a `SyntaxError` on line 1,
and even puts a little arrow in the place where there is an issue.
In this case the problem is that the function definition is missing a colon at the end.

Actually, the function above has *two* issues with syntax.
If we fix the problem with the colon,
we see that there is *also* an `IndentationError`,
which means that the lines in the function definition do not all have the same indentation:



~~~
def some_function():
    msg = "hello, world!"
    print(msg)
     return msg
~~~
{: .python}


~~~
  File "<stdin>", line 4
    return msg
    ^
IndentationError: unexpected indent
~~~
{: .error}

Both `SyntaxError` and `IndentationError` indicate a problem with the syntax of your program,
but an `IndentationError` is more specific:
it *always* means that there is a problem with how your code is indented.


> ## Tabs and Spaces
>
> A quick note on indentation errors:
> they can sometimes be insidious,
> especially if you are mixing spaces and tabs.
> Because they are both [whitespace](reference.html/#whitespace),
> it is difficult to visually tell the difference.
> In the following example, where we have a file called `hello_world.py`,
> the first two lines are using a tab for indentation,
> while the third line uses four spaces:
>
>
>
> > ~~~
> > def some_function():
> >     msg = "hello, world!"
> >     print(msg)
> >     return msg
> > ~~~
> > {: .python}
>
> > ~~~
> >  File "hello_world.py", line 4
> >    return msg
> >             ^
> > TabError: inconsistent use of tabs and spaces in indentation
> > ~~~
> > {: .error}
> 
> By default, one tab is equivalent to eight spaces,
> so the only way to mix tabs and spaces is to make it look like this.
> In general, it is better to just never use tabs and always use spaces,
> because it can make things very confusing.
> 
> {: .callout}


> ## Identifying Syntax Errors
>
> 1. Read the code below (or open the file `error_syntax_ch.py` in code folder), and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
> > ~~~
> > def another_function
> >   print("Syntax errors are annoying.")
> >    print("But at least python tells us about them!")
> >   print("So they are usually not too hard to fix.")
> > ~~~
> > {: .python}
>
>
> > ## Solution
> > `SyntaxError` for missing `():` at end of first line, `IndentationError` for mismatch 
> > between second and third lines. A fixed version is:
> >
> > > ~~~
> > > def another_function():
> > >     print("Syntax errors are annoying.")
> > >     print("But at least python tells us about them!")
> > >     print("So they are usually not too hard to fix.")
> > > ~~~
> > > {: .python}
> >
> > {: .solution}
> 
> {: .challenge}

## Index Errors

Next up are errors having to do with containers (like lists and strings) and the items within them.
If you try to access an item in a list or a string that does not exist,
then you will get an error.
This makes sense:
if you asked someone what day they would like to get coffee,
and they answered "caturday",
you might be a bit annoyed.
Python gets similarly annoyed if you try to ask it for an item that doesn't exist:

~~~
letters = ['a', 'b', 'c']
print("Letter #1 is", letters[0])
print("Letter #2 is", letters[1])
print("Letter #3 is", letters[2])
print("Letter #4 is", letters[3])
~~~
{: .python}

~~~
Letter #1 is a
Letter #2 is b
Letter #3 is c
~~~
{: .output}

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
~~~
{: .error}

Here,
Python is telling us that there is an `IndexError` in our code,
meaning we tried to access a list index that did not exist.


> ## Identifying Index Errors
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
>
>
> > ## Solution
> > `IndexError`; the last entry is `seasons[3]`, so `seasons[4]` doesn't make sense.
> > A fixed version is:
> >
> >
> >
> > > ~~~
> > > seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> > > print('My favorite season is ', seasons[-1])
> > > ~~~
> > > {: .python}
> >
> > {: .solution}
> 
> {: .challenge}

Here's another example of Index Error.

~~~
# This code has an intentional error. You can type it directly or
# use it for reference to understand the error message below.
def favorite_ice_cream():
    ice_creams = [
        "chocolate",
        "vanilla",
        "strawberry"
    ]
    print(ice_creams[3])

favorite_ice_cream()
~~~
{: .python}

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 9, in favorite_ice_cream
IndexError: list index out of range
~~~
{: .error}

This particular traceback has two levels.
You can determine the number of levels by looking for the number of arrows on the left hand side.
In this case:

1.  The first shows code from the cell above,
    with an arrow pointing to Line 8 (which is `favorite_ice_cream()`).

2.  The second shows some code in the function `favorite_ice_cream`,
    with an arrow pointing to Line 6 (which is `print(ice_creams[3])`).

The last level is the actual place where the error occurred.
The other level(s) show what function the program executed to get to the next level down.
So, in this case, the program first performed a [function call](reference.html/#function-call) to the function `favorite_ice_cream`.
Inside this function,
the program encountered an error on Line 6, when it tried to run the code `print(ice_creams[3])`.

> ## Long Tracebacks
>
> Sometimes, you might see a traceback that is very long -- sometimes they might even be 20 levels deep!
> This can make it seem like something horrible happened,
> but really it just means that your program called many functions before it ran into the error.
> Most of the time,
> you can just pay attention to the bottom-most level,
> which is the actual place where the error occurred.
>
> {: .callout}

So what error did the program actually encounter?
In the last line of the traceback,
Python helpfully tells us the category or type of error (in this case, it is an `IndexError`)
and a more detailed error message (in this case, it says "list index out of range").

If you encounter an error and don't know what it means,
it is still important to read the traceback closely.
That way,
if you fix the error,
but encounter a new one,
you can tell that the error changed.
Additionally,
sometimes just knowing *where* the error occurred is enough to fix it,
even if you don't entirely understand the message.

If you do encounter an error you don't recognize,
try looking at the [official documentation on errors](http://docs.python.org/3/library/exceptions.html).
However,
note that you may not always be able to find the error there,
as it is possible to create custom errors.
In that case,
hopefully the custom error message is informative enough to help you figure out what went wrong.


> ## Reading Error Messages
>
> Read the python code (or open the file `error_index_ch.py` in code folder) and the resulting traceback below, and answer the following questions:
>
> 1.  How many levels does the traceback have?
> 2.  What is the function name where the error occurred?
> 3.  On which line number in this function did the error occurr?
> 4.  What is the type of error?
> 5.  What is the error message?
>
>
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
>
> > ~~~
> > Traceback (most recent call last):
> >   File "test.py", line 18, in <module>
> >     print_friday_message()
> >   File "test.py", line 16, in print_friday_message
> >     print_message("Friday")
> >   File "test.py", line 13, in print_message
> >     print(messages[day])
> > KeyError: 'Friday'
> > ~~~
> > {: .error}
>
> 
> > ## Solution
> > 1. 3 levels
> > 2. `print_message`
> > 3. 11
> > 4. `KeyError`
> > 5. There isn't really a message; you're supposed to infer that `Friday` is not a key in `messages`.
> >
> > {: .solution}
> 
> {: .challenge}

## Silent Errors

Not all problems with our code will be revealed through explicit errors.
Some defects can cause output to be incorrect, and display no error message.

Consider the following code (which you can find in `normalize.py` in the code directory):

~~~
def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
    x0, y0, x1, y1 = rect

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    return (0, 0, upper_x, upper_y)
~~~
{: .python}

So if we normalize a rectangle that is taller than it is wide...:

~~~
from normalize import normalize_rectangle
print(normalize_rectangle( (0.0, 0.0, 1.0, 5.0) ))
~~~
{: .python}

...everything seems ok:

~~~
(0, 0, 0.2, 1.0)
~~~
{: .output}

And if we normalize one that's wider than it is tall:

~~~
print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) ))
~~~
{: .python}

Everything still seems... wait a minute!

~~~
(0, 0, 1.0, 5.0)
~~~
{: .output}

Since the longest axis should be 1.0, we can see this is incorrect.
Looking at our code, line 8 should divide dy by dx.

> ## Debug with a Neighbour
>
> Take a function that you have written today, and introduce a tricky bug.
> Your function should still run, but will give the wrong output.
> Switch seats with your neighbor and attempt to identify - or debug - the problem
> that they introduced into their function.
> 
> {: .challenge}


> ## Not Supposed to be the Same
>
> You are assisting a researcher with Python code that computes the
> Body Mass Index (BMI) of patients (open the file `error_silent_ch.py` in code folder).  The researcher is concerned because
> all patients seemingly have identical BMIs, despite having different
> physiques.  BMI is calculated as **weight in kilograms**
> divided by the the square of **height in metres**.
>
>
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
> >  {: .output}
>
> > ## Solution
> > * The loop is not being utilised correctly. `height` and `weight` are always
> >   set as the first patient's data during each iteration of the loop.
> >
> > * The height/weight variables are reversed in the function call to
> >   `calculate_bmi(...)`
> >
> > {: .solution}
> 
> {: .challenge}

In our `normalize_rectangle` example, we identified and fixed the error.
But we could have missed it,
particularly if our function was doing something more complex.

So what should we do?
We should test our code as thoroughly as we can before we intend to use it,
by coming up with `test cases`. These `tests` are a set of inputs we can use to test
that our code gives the correct result, and are designed deliberately to
find faults in our code.
This means as continually add features to our code and test it, we can check
the behaviour of our code continues to be correct.
We also automate this process, and there are ways to do this, which are
beyond the scope of this course.

If you're interested, look up [unit testing](https://en.wikipedia.org/wiki/Unit_testing)
in general, and for Python,
you can look at [Nose](http://nose.readthedocs.io/en/latest/) and
[PyTest](http://doc.pytest.org/en/latest/)
which are examples of tools used to write tests in an easy to use way.


## File Errors

The last type of error we'll cover today
are those associated with reading and writing files: `FileNotFoundError`.
If you try to read a file that does not exist,
you will receive a `FileNotFoundError` telling you so.
If you attempt to write to a file that was opened read-only, Python 3
returns an `UnsupportedOperationError`.
More generally, problems with input and output manifest as
`IOError`s or `OSError`s, depending on the version of Python you use.

~~~
file_handle = open('myfile.txt', 'r')
~~~
{: .python}


~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
~~~
{: .error}

One reason for receiving this error is that you specified an incorrect path to the file.
For example,
if I am currently in a folder called `myproject`,
and I have a file in `myproject/writing/myfile.txt`,
but I try to just open `myfile.txt`,
this will fail.
The correct path would be `writing/myfile.txt`.
It is also possible (like with `NameError`) that you just made a typo.

A related issue can occur if you use the "read" flag instead of the "write" flag.
Python will not give you an error if you try to open a file for writing when the file does not exist.
However,
if you meant to open a file for reading,
but accidentally opened it for writing,
and then try to read from it,
you will get an `UnsupportedOperation` error
telling you that the file was not opened for reading:

~~~
file_handle = open('myfile.txt', 'w')
file_handle.read()
~~~
{: .python}

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
~~~
{: .error}

These are the most common errors with files,
though many others exist.
If you get an error that you've never seen before,
searching the Internet for that error type
often reveals common reasons why you might get that error.
