---
lesson_title: 'Building Programs with Python'
lesson_schedule_slug: python-novice-schedule
title: Modularising your code using functions
slug: python-novice-modularising-your-code-using-functions
minutes: 35
teaching: 15
exercises: 20
questions:
- What is a function?
- Why would I want to use a function?
- Where should I put my functions?
objectives:
- Define a function that takes parameters.
- Return a value from a function.
- Understand the scope of function variables and parameters.
- Documenting a function.
- Understand why we should divide programs into small, single-purpose functions.
- Define and use a module that contains functions.
keypoints:
- A function is created using the `def` keyword.
- Functions take variables that are specified in the function definition and use the `return` keyword to specify their output.
- We can use a module to keep our functions separate to the main body of our code to improve code readability.
---


At this point, we've written some scripts to do various things, including one to
loop through a data file and output its contents.
But it's not hard to imagine our code getting more complicated as we add
more features.

We'll see how we can amend our code to be better structured to further increase its readability, as well as its maintainability and reuse in other applications.

### Converting from Fahrenheit to Celsius

Let's look at adding a feature to our code to perform a conversion
from Fahrenheit to Celsius on the temperature data we are looking at:

~~~
celsius = ((data[3] - 32) * (5/9))
~~~
{: .python}

Now this wouldn't work as it is - we can't just apply this formula directly to
`data[3]` since it's a string. We need to convert it to a number first. To be
specific, a floating point number.

Fortunately, Python has some built-in functions to do these `type` conversions
(*see `climate_analysis-5.py`*):



~~~
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        # apply standard Fahrenheit to Celsius formula
        celsius = ((fahr - 32) * (5/9))

        print('Max temperature in Celsius', celsius)
~~~
{: .python}

So we first convert our `data[3]` value to a floating point number using
`float()`, then we are free to use it in our conversion formula. Depending on
the structure of your own data, you may find you end up doing this a lot!

So now we get:

~~~
Max temperature in Celsius 14.73888888888889
Max temperature in Celsius 14.777777777777779
Max temperature in Celsius 14.61111111111111
Max temperature in Celsius 13.838888888888887
Max temperature in Celsius 15.477777777777778
Max temperature in Celsius 14.972222222222225
Max temperature in Celsius 14.85
Max temperature in Celsius 16.33888888888889
Max temperature in Celsius 16.261111111111113
Max temperature in Celsius 16.33888888888889
~~~
{: .output}

### Modularising conversion code into a function

Whilst this is a simple calculation, there are many things we may want to do
that are more complex. What is essentially a single task may require a number of
lines of code to accomplish it, and with many of these our code could become
quite messy. And if we'd like to reuse that code elsewhere, we'd have to copy
it.

Duplicating portions of code can lead to a host of problems with
modifying our code in the future, aside from making the code more
lengthy and unreadable. We'd have to update all our copies if we
wanted to update how we accomplished that task, which can introduce errors.
And if errors already exist in our original code, we would have to correct all
copies, which would become a code maintenance nightmare.

We'd ideally like a way to package our code succinctly, so we only need to
change it in one place, and so that it is easier to reuse.
Python provides for this by letting us define things called 'functions' -
a shorthand way of re-executing pieces of code.

So going back to our climate code, we can modularise our temperature
conversion code into a function (*see `climate_analysis-6.py`*):


~~~
climate_data = open('../data/sc_climate_data_10.csv', 'r')

def fahr_to_celsius(fahr):
    # apply standard Fahrenheit to Celsius formula
    celsius = ((fahr - 32) * (5/9))
    return celsius

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = fahr_to_celsius(fahr)

        print('Max temperature in Celsius', celsius)
~~~
{: .python}

The definition opens with the word `def`,
which is followed by the name of the function
and a parenthesized list of parameter names.
The [body](reference.html#function-body) of the function --- the
statements that are executed when it runs --- is indented below the definition line,
typically by four spaces.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a [return statement](reference.html#return-statement) to send a result back to whoever asked for it.


> ## Combining Strings
>
> "Adding" two strings produces their concatenation:
> `'a' + 'b'` is `'ab'`.
> Write a short function called `fence` that takes two parameters called
> `original` and `wrapper` and returns a new string that has the wrapper
> character at the beginning and end of the original.
> A call to your function should look like this:
>
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
>
> > ## Solution
> > > ~~~
> > > def fence(original, wrapper):
> > >     return wrapper + original + wrapper
> > > ~~~
> > > {: .python}
> >
> >  {: .solution}
> 
> {: .challenge}


> ## How large should functions be?
>
> We use functions to define a big task in terms of smaller ones. This helps
> to make our code more readable, as well as allowing us to more easily
> reuse and maintain that code.
>
> The trick when writing functions is to ensure they don't themselves become
> unmanageable, and it's very easy to write large functions. So when your
> function starts getting large, consider decomposing it further into separate
> functions. There's no hard and fast rule for when a function is too 'large'
> --- some say 15-20 lines, some say no more than a page long. But in general,
> think about how complex it is to understand, generally how readable
> it is, and whether it would benefit from splitting up into more functions.
> {: .callout}

Note that the function is at the top of the script. This is because Python
reads the script from top to bottom, and if we called the function before we
defined it, Python wouldn't know about it and throw an error like this:



~~~
Traceback (most recent call last):
  File "climate_analysis-6.py", line 13, in <module>
    celsius = fahr_to_celsius(fahr)
NameError: name 'fahr_to_celsius' is not defined
~~~
{: .error}

And when we run it again --- which we most definitely should, to make sure it's still working as expected --- we see the same output, which is correct.


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
>
> > ## Solution
> > 3 - the f and k variables defined and used within the function
> > do not interfere with those defined outside of the function.
> >
> > This is really useful, since it means we don't have to worry about
> > conflicts with variable names that are defined outside of our function
> > that may cause it to behave incorrectly. This is known as variable scoping.
> > {: .solution}
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
>
> > ## Solution
> > > ~~~
> > > def is_sum_equal(number_list, sum_value):
> > >     count = 0
> > >     for number in number_list:
> > >         count = count + number
> > >
> > >     return count == sum_value
> > > ~~~
> >
> > {: .solution}
> 
> {: .challenge}

## Performing more temperature conversions

Of course, we can also add more functions. Let's add another, which performs
a conversion from Fahrenheight to Kelvin. The formula looks like this:



~~~
kelvin = ((fahr - 32) * (5/9)) + 273.15
~~~
{: .python}

Now, we could just add a new function that does this exact conversion. But
Kelvin uses the same units as Celsius, the part of the formula that
converts to Celsius units is the same. We could just used our `fahr_to_celsius`
function for the unit conversion, and add 273.15 to that to get Kelvin. So
our new function becomes:


~~~
def fahr_to_kelvin(fahr):
    # apply standard Fahrenheit to Kelvin formula
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin
~~~
{: .python}

Which we insert after the `fahr_to_celsius` function (since our new function
needs to call that one). We can then amend our code to also call that new
function and output the result. Our code then becomes (*see `climate_analysis-7.py`*):



~~~
climate_data = open('../data/sc_climate_data_10.csv', 'r')

def fahr_to_celsius(fahr):
    # apply standard Fahrenheit to Celsius formula
    celsius = ((fahr - 32) * (5/9))
    return celsius

def fahr_to_kelvin(fahr):
    # apply standard Fahrenheit to Kelvin formula
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = fahr_to_celsius(fahr)
        kelvin = fahr_to_kelvin(fahr)

        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
~~~
{: .python}

Hmm... our code is starting to get a little large with these functions.
What could we do to make it clearer and less cluttered?

### Modularising conversion code into a library

Words are useful,
but what's more useful are the sentences and stories we build with them.
Similarly,
while a lot of powerful tools are built into languages like Python,
even more live in the [libraries](reference.html#software-library) they are used to build.

A library is a collection of code (precompiled routines, functions) that a program can use. They are particularly
useful for storing frequently used routines because you don't need to explicitly link them to every program
that uses them. Libraries will be automatically looked for routines that are not found elsewhere.

So we can go one step further to improve the structure of our
code. We can separate out the two functions and have them in a separate
Python module (or library) which we can use.

Create a new file called
`temp_conversion.py` and copy and paste those two functions into it, then
save it, and remove those functions from the original `climate_analysis.py`
script and save that. We'll see how to use those library functions
shortly. But first, let's take this opportunity to improve our
documentation of those functions!

The usual way to put documentation in software is to add comments, as
we've already seen. But when describing functions, there's a better way.
If the first thing in a function is a string that isn't assigned to a variable,
that string is attached to the function as its documentation (*see `temp_conversion.py`*):



~~~
"""A library to perform temperature conversions"""

def fahr_to_celsius(fahr):
    """Convert Fahrenheit to Celsius.

    Uses standard Fahrenheit to Celsius formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    celsius = ((fahr - 32) * (5/9))
    return celsius

def fahr_to_kelvin(fahr):
    """Convert Fahrenheight to Kelvin.

    Uses standard Fahrenheit to Kelvin formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin
~~~
{: .python}

A string like this is called a [docstring](reference.html#docstring).
We don't need to use triple quotes when we write one,
but if we do, we can break the string across multiple lines. This also
applies to modules

So how would we use this module and its functions in code?
We do this by `import`ing the module into Python.



~~~
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import temp_conversion
~~~
{: .python}

When modules and functions are described in docstrings, we can ask for these
explanations directly from the interpreter which can be useful. Following on
from the above:

~~~
>>> help(temp_conversion)
~~~
{: .python}

So here's the help we get for the module:


~~~
Help on module temp_conversion:

NAME
    temp_conversion - A library to perform temperature conversions

FUNCTIONS
    fahr_to_celsius(fahr)
        Convert Fahrenheit to Celsius.

        Uses standard Fahrenheit to Celsius formula

        Arguments:
        fahr -- the temperature in Fahrenheit

    fahr_to_kelvin(fahr)
        Convert Fahrenheight to Kelvin.

        Uses standard Fahrenheit to Kelvin formula

        Arguments:
        fahr -- the temperature in Fahrenheit

FILE
    /Users/user/.../python-novice/code/temp_conversion.py (note your path will vary)
~~~
{: .output}

Here, note we've used the term `library` in the code documentation. This
is a more conventional, general term for a set of routines in any language.

Similarly, for Docstrings in functions, e.g.:



~~~
>>> help(temp_conversion.fahr_to_celsius)
~~~
{: .python}

Note that we need to put in `temp_conversion.` prior the function name. We need
to do this to specify that the function we want help on is within the
`temp_conversion` module.

So we get:

~~~
Help on function fahr_to_celsius in module temp_conversion:

fahr_to_celsius(fahr)
    Convert Fahrenheit to Celsius.

    Uses standard fahrenheit to Celsius formula

    Arguments:
    fahr -- the temperature in Fahrenheit
~~~
{: .output}

And then we need to `import` that function from our module into our script, so
we can use it (*see `climate_analysis-8.py`*).



~~~
import temp_conversion

climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = temp_conversion.fahr_to_celsius(fahr)
        kelvin = temp_conversion.fahr_to_kelvin(fahr)

        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
~~~
{: .python}

Like when we used the interpreter to ask for help on the `fahr_to_celsius()`
function, we need to prefix the function with its `temp_conversion` module name.

Again, the results should be the same as before.


> ## Readable Code
>
> Revise a function you wrote for one of the previous exercises to try to make
> the code more readable. Then, collaborate with one of your neighbors
> to critique each other's functions and discuss how your function
> implementations
> could be further improved to make them more readable.
> 
> {: .challenge}
