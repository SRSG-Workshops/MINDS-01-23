---
title: "Writing Sustainable Code"
slug: project-novice-writing-sustainable-code
teaching: 20
exercises: 5
questions:
- "How do I write code to make future development easier?"
objectives:
- "Understand the benefits of making your code more readable."
- "Rename variables and functions to be more descriptive."
- "Understand how to use comments to describe the code."
- "Use docstrings to describe the inputs and outputs of functions."
keypoints:
- "Always assume that someone else will read your code at a later date, including yourself."
- "Rename variables and functions to add context to make your code more readable."
- "Add comments to explain why something was done in a certain way if not obvious."
- "Don't add comments that just restate what code clearly already does."
- "Use docstrings contained within `\"\"\"` at the start of functions and files to explain their behaviour and input/output parameters."
---

Now we've covered the process around developing and releasing our software. However, one key part of software development we haven't touched on yet is **the code itself**. No matter how well we manage our development, if we don't write **sustainable** code, then our project will suffer. 

One major problem in software development is **technical debt**- a term for when decisions made early-on in the project (often made on the fly without much thought) end up causing long-term problems, and require a major expenditure of effort to fix (or to *pay off* the technical debt). If you accrue too much technical debt without fixing it, the whole project can become unsustainable, and the effort required to fix them becomes so large you have to throw the project away and start from scratch.

So when developing academic software, we need to make sure it's **sustainable**. One of the key factors for this is keeping your code **readable** and **maintainable**. We want to minimise the amount of effort required for you (or others) to read your code, understand what's going on, and make changes to it.

In this episode, we're going to use **python** as an example language. The kind of principles we discuss will be applicable to any language!

## Naming Things

Good names are one of the key requirements to make a code easy to maintain. Take a look at the two lines of code below:

~~~
out(p(f(v), 2) + 1)

print(process(fibonacci(argument), 2) + 1)
~~~
{: .language-python}

Which one of the two is easiest to read and understand? It's much easier to upkeep a code where what happens on each line is clear **on that line**, without having to read comments describing what each variable actually is. When you have to go back to a function you wrote in a hurry six months ago to figure out where the bug is, you'd definitely prefer it was written like the latter.

There's some common naming recommendations:

- Variables are usually lower case (e.g. speed, participant_age)
- Classes are typically capitalised *nouns* (e.g. Molecule, BlackHole, DNASequence)
- Functions are typically *verbs* (e.g. splice_gene_sequence, calculateOrbit)

Whilst these names are a lot longer than `a` or `val_x`, text editors like **Visual Studio Code** offers code completion. You can start typing <kbd>p</kbd> and be prompted with your variable `patient_id`. Not only does this mean it's no more difficult to write easily-maintainable code, it also helps avoid you making typos! If your variables are `f`, `g` and `v`, a single mispressed key can cause you a world of trouble.

> ## Naming Styles
> 
> There's two main styles of naming multi-word variables, **camelCase** and **snake_case**. Some languages have common *standards* which recommend which to use, but in general it's good to be consistent whichever you pick!
>
> Python recommends **capitalised CamelCase** for classes, **lower-case snake_case()** for functions and variables, and **upper-case SNAKE_CASE** for constants.
{: .callout}

> ## Single-Character Names
>
> You might think that some single-character names are perfectly clear- for example, `C` obviously refers to the speed of light!  Unfortunately, not everyone will agree. 
> Any mathematical libraries you use are likely to have their own interpretation of what each letter should stand for that are likely to be at odds with your field's definitions.
> If so, this can lead to some very inconvenient errors to debug.
>
> In general, it's best to give everything a name at least three characters long. You might use a prefix, e.g. `CONST_C` for 'constant', 
> or a more verbose description, e.g. `V_LIGHT`.
{: .callout}

## Documenting your Code

If your code has descriptive variables and function names, then it should go a long way towards making it clear what it does. But unfortunately, codes of any real size rapidly become too complicated to understand just by reading the code! Even if your code doesn't *start* that large, **it will almost certainly end up that way**. So it's a good idea to write clear documentation from the start, to make sure you don't have to go back and do it later.

### Comments

If you've used clear variable names, then the actual logic and processes of the code should be readable from the text. So with comments, we can describe things in more detail- explaining what's going on at a high level, so you don't have to read an entire function to understand what it does.

In Python, you can comment your code by starting a line with a `#`:
~~~
def fahr_to_cels(fahr):
    # Convert temperature in Fahrenheit to Celsius
    cels = (fahr + 32) * (5 / 9)
    return cels
~~~
{: .language-python}

You can also add these at the end of lines, e.g.:

~~~
def fahr_to_cels(fahr):
    cels = (fahr + 32) * (5 / 9)  # Convert temperature in Fahrenheit to Celsius
    return cels
~~~
{: .language-python}

A good rule of thumb is to assume that someone will **always** read your code at a later date, and this includes a future version of yourself. It can be easy to forget why you did something a particular way in six months time.

They should be able to understand a single function or method from its code and its comments, and shouldn't have to look elsewhere in the code for clarification. It can be easy to get lost in code, and others will not have the same knowledge of our project or code as we do.

The kind of things that need to be commented are:

- Why certain design or implementation decisions were adopted, especially in cases where the decision may seem counter-intuitive
- The names of any particular equations you've implemented or algorithms you've used
- The format of input or output files the code uses

There are some restrictions. Comments that simply restate what the code does are redundant, and comments have to be accurate, as an incorrect comment is more confusing than no comment at all.

### Docstrings

For your functions, it can be incredibly helpful to have this documentation on what they do in a structured way. The key properties of a function are what it does, what arguments it takes, and what values it returns. If you have this information everywhere, then when you're scanning through the code and come across a function, you can just hop over and check out the summary and you'll know exactly what's going on.

We're going to look at an example of how to do this in Python. If the first thing in a function is a string that isn't assigned to a variable, that string is attached to the function as its documentation. Take a look at the example in this function for calculating Fibonacci numbers:

~~~
def fibonacci(n):
    """
    Calculate the Fibonacci number of the given integer.

    A recursive implementation of Fibonacci.

    :param n: integer
    :raises ValueError: raised if n is less than zero
    :returns: fibonacci number, integer
    """
    if n < 0:
        raise ValueError('Fibonacci is not defined for N < 0')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
~~~
{: .language-python}

This documentation lists the input variables, what the function returns, and any errors it might raise too. Along with a helpful description of what the function does, this information can act as a *contract* for readers to understand what to expect in terms of behaviour when using the function, as well as how to use it.

This kind of clear, firm description of a function provides a solid basis for future development. If you write a function that can only take positive numbers, but don't document that, then someone else might try and feed it negative numbers without realising that's not possible. Then, they'll be faced with a crash at best, or at worst the code will quietly give them the wrong answer.

These types of comments are called *docstrings* in Python. We don't need to use triple quotes when we write one, but if we do, we can break the string across multiple lines. 

You can also write docstrings for entire Python modules- the community standard **PEP 257** suggests each Python module should have a brief description, and then list the classes and functions within it. So at the beginning of a file we can just add a docstring explaining what is it, and what it contains. For example, if `fibonacci()` was included in a module with other functions, our module could have at the start of it:

~~~
"""
A module for generating numerical sequences of numbers that occur in nature.

Functions:
  fibonacci - returns the Fibonacci number for a given integer
  golden_ratio - returns the golden ratio number to a given Fibonacci iteration
  ...
"""
...
~~~
{: .language-python}

There's a number of different docstring formats:

- reST - based on reStructuredText, is the most common at the moment
- Epytext - historically based on a format of docstrings used for Java, in their javadoc documentation
- Google - they have their own format
- numpydoc - recommended by Numpy, based on the Google format, quite verbose

The format we're using here for our examples is reST. The various formats differ in terms of how they format things like parameters and output values.

Not only does having well-structured docstrings (or their equivalents in another language) make development easier for you, if you stick to an existing format for them then they can be **machine-readable** too. That allows sites (like [ReadTheDocs (linked here)](https://readthedocs.io)) to compile your code comments into a searchable website. You can even hyperlink between functions, or use add-ons to include LaTeX equations into the site (look at the [Dask Documentation (linked here)](https://docs.dask.org/en/latest/dataframe-api.html#dask.dataframe.read_csv) for an example of a large, sophisticated site built by ReadTheDocs).

> ## Improved Commenting for our Temperature Functions
>
> Let's think about some example functions:
>
> ~~~
> def fahr_to_cels(fahr):
>     # Convert temperature in Fahrenheit to Celsius
>     cels = (fahr + 32) * (5 / 9)
>     return cels
>
> def fahr_to_kelv(fahr):
>     # Convert temperature in Fahrenheit to Kelvin
>     cels = fahr_to_cels(fahr)
>     kelv = cels + 273.15
>     return kelv
> ~~~
> {: .language-python}
>
> Open up **Visual Studio Code** and create a new file called `temperature_conversion.py`, then paste the example functions in and save it. Then turn each of the comments into Python docstrings that explain briefly what the function does, its arguments, and what the function returns. Finally, add a docstring to the top of the file that describes it.
>
> > ## Solution
> > ~~~
> > """
> > A module for converting temperatures between imperial and metric.
> >
> > Functions:
> >   fahr_to_celcius - Converts a float temperature in Fahrenheit to Celcius
> >   fahr_to_kelvin - Converts a float temperature in Fahrenheit to Kelvin
> > """
> > def fahr_to_celsius(fahr):
> >     """
> >     Convert Fahrenheit to Celsius.
> >
> >     Uses standard Fahrenheit to Celsius formula.
> >
> >     :param fahr: float temperature in Fahrenheit
> >     :returns: float temperature in Celsius
> >     """
> >     celsius = ((fahr - 32) * (5/9))
> >     return celsius
> >
> > def fahr_to_kelvin(fahr):
> >     """
> >     Convert Fahrenheit to Kelvin.
> >
> >     Uses standard Fahrenheit to Kelvin formula, making use of fahr_to_celsius function.
> >
> >     :param fahr: float temperature in Fahrenheit
> >     :returns: float temperature in Kelvin
> >     """
> >     kelvin = fahr_to_celsius(fahr) + 273.15
> >     return kelvin
> > ~~~
> > {: .language-python}
> > This level of commenting is a bit overkill for our example code - but once you have a file that's a few hundred lines long this kind of quick and clear overview is very useful! 
>{: .solution}
{: .challenge}

> ## Help
>
> For languages like Python, docstrings are useful as they're what's displayed when you use `help` to get more information about a function.
> 
> If you have Python installed, you can test this by opening up a terminal wherever you saved the `temperature_conversion.py` file, and trying:
> ~~~
> from temperature_conversion import fahr_to_celcius
> help(fahr_to_celcius)
> ~~~
> {: .language-python}
{: .callout}

{% include links.md %}
