---
lesson_title: 'Building Programs with Python'
lesson_schedule_slug: python-novice-schedule
title: Python Basics
slug: python-novice-python-basics
minutes: 25
teaching: 15
exercises: 10
questions:
- How do I start the Python interpreter?
- What is a variable?
objectives:
- Introduction to running the Python interpreter
- Introduction to Python variables
- Creating and Assigning values to variables
keypoints:
- Start the python interpreter by typing `python` in the shell.
- Variables are named memory locations, they are used to access data.
---


## Running the Python interpreter

Normally, you write Python programs in a Python script, which is basically a file of Python commands you can run.
But to start with, we'll take a look at the Python interpreter.
It's similar to the shell in how it works, in that you type in commands and it
gives you results back, but instead you use the Python language.

It's a really quick and convenient way to get started with Python, particularly when learning about things like how to use variables, and it's good for playing around with what you can do and quickly testing small things.
But as you progress to more interesting and complex things you need to move over to writing proper Python scripts, which we'll see later.

You start the Python interpreter from the shell by:



~~~
$ python
~~~
{: .bash}

And then you are presented with something like:



~~~
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~
{: .output}



~~~
In some cases GitBash will hang on this command and not launch the Python interpreter. 
In this case close and reopen git bash and issue the following commands:
~~~
{: .callout}


~~~
cd ~
echo 'alias python="winpty python.exe"' >> .bashrc
source .bashrc
python
~~~
{: .bash}

And lo and behold! You are presented with yet another prompt.
So, we're actually running a Python interpreter from the shell - it's only yet another program we can run from the shell after all.
But shell commands won't work again until we exit the interpreter.

You can exit the interpreter and get back to the shell by typing:



~~~
>>> exit()
~~~
{: .python}

...or alternatively pressing the Control and D keys at the same time.
Then you'll see:



~~~
$
~~~
{: .output}

Phew - back to the shell!

But let's get back to the Python interpreter and learn about variables in Python:



~~~
$ python
~~~
{: .bash}

And we're back to the Python interpreter:


~~~
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~
{: .output}


## Variables

A variable is just a name for a value,
such as `x`, `current_temperature`, or `subject_id`.
Python's variables must begin with a letter.
A variable in Python is defined through assignment i.e. we can create a new variable simply by assigning a value to it using `=`.
As an illustration,
consider the simplest `collection` of data,
a single value.
The line below assigns a value to a variable:



~~~
weight_kg = 55
~~~
{: .python}

Once a variable has a value, we can print it:


~~~
print(weight_kg)
~~~
{: .python}

~~~
55
~~~
{: .output}

and do arithmetic with it:


~~~
print('weight in pounds:', 2.2 * weight_kg)
~~~
{: .python}

~~~
weight in pounds: 121.0
~~~
{: .output}

In the above example, a floating point number `55` object has a tag labelled `weight_kg`.

If we reassign to `weight_kg`, we just move the tag to another object as shown below.

We can change a variable's value by assigning it a new one:


~~~
weight_kg = 57.5
print('weight in kilograms is now:', weight_kg)
~~~
{: .python}

~~~
weight in kilograms is now: 57.5
~~~
{: .output}

Now the name `weight_kg` is attached to another floating point number `57.5` object.

Hence, in Python, a `name` or `identifier` or `variable` is like a name tag attached to an object.
Python has `names` and everything is an `object`.

As the example above shows,
we can print several things at once by separating them with commas.

If we imagine the variable as a sticky note with a name written on it,
assignment is like putting the sticky note on a particular value:

![Variables as Sticky Notes](fig/python-sticky-note-variables-01.svg)

This means that assigning a value to one variable does *not* change the values of other variables.
For example,
let's store the subject's weight in pounds in a variable:


~~~
weight_lb = 2.2 * weight_kg
print('weight in kilograms:', weight_kg, 'and in pounds:', weight_lb)
~~~
{: .python}

~~~
weight in kilograms: 57.5 and in pounds: 126.5
~~~
{: .output}

![Creating Another Variable](fig/python-sticky-note-variables-02.svg)

and then change `weight_kg`:



~~~
weight_kg = 100.0
print('weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb)
~~~
{: .python}


~~~
weight in kilograms is now: 100.0 and weight in pounds is still: 126.5
~~~
{: .output}

![Updating a Variable](fig/python-sticky-note-variables-03.svg)

Since `weight_lb` doesn't remember where its value came from,
it isn't automatically updated when `weight_kg` changes.
This is different from the way spreadsheets work.

Although we commonly refer to `variables` even in Python (because it is the common terminology), we really mean `names` or `identifiers`. In Python, `variables` are name tags for values, not labelled boxes.


> ## What's inside the box?
>
> Draw diagrams showing what variables refer to what values after each statement
> in the following program:
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


> ## Sorting out references
>
> What does the following program print out?
>
>
> > ~~~
> > first, second = 'Grace', 'Hopper'
> > ~~~
> > {: .python}
>
> > ~~~
> > first = Grace
> > second = Hopper
> > ~~~
> > {: .output}
>
> > ~~~
> > third, fourth = second, first
> > print(third, fourth)
> > ~~~
> > {: .python}
> 
> {: .challenge}


