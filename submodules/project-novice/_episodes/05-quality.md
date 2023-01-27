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
- "Use docstrings at the start of functions and files to explain their behaviour and input/output parameters."
---

Now we've covered the process around developing and releasing our software. However, one key part of software development we haven't touched on yet is **the code itself**. No matter how well we manage our development, if we don't write **sustainable** code, then our project will suffer. 

One major problem in software development is **technical debt** - a term for when decisions made early-on in the project (often made on the fly without much thought) end up causing long-term problems, and require a major expenditure of effort to fix (or to *pay off* the technical debt). If you accrue too much technical debt without fixing it, the whole project can become unsustainable, and the effort required to fix them becomes so large you have to throw the project away and start from scratch.

So when developing academic software, we need to make sure it's **sustainable**. One of the key factors for this is keeping your code **readable** and **maintainable**. We want to minimise the amount of effort required for you (or others) to read your code, understand what's going on, and make changes to it.

In this episode, we're going to use **python** as an example language. The kind of principles we discuss will be applicable to any language!

## Naming Things

Good names are one of the key requirements to make a code easy to maintain. Take a look at the `temp_conversion.py` file in our `climate-analysis` repository:

~~~
def Fc(x):
    Y = (x - 32) * (5 / 9)
    return Y

def FK(x):
    y = Fc(x)
    z = y + 273.15
    return z
~~~
{: .language-python}

What do these functions actually do? From the context of the filename (`temp_conversion.py`) we can make a good guess that they're probably functions for converting temperatures in Fahrenheit into Celsius and Kelvin, but it's not especially clear. When you see these functions referred to in *other* files, though, their behaviour's a lot less clear. The more complex your code gets, the harder it becomes to figure out what it does from context clues and scattered comments and the harder it gets to maintain it.

It's much easier to upkeep a code where what happens on each line is clear **on that line** (it's especially easier for people who didn't write it in the first place and have had it passed on to them!). We want to make our functions a little clearer, and there's some common naming recommendations:

- Variables are usually lower case (e.g. `speed`, `participant_age`)
- Classes are typically capitalised *nouns* (e.g. `Molecule`, `BlackHole`, `DNASequence`)
- Functions are typically *verbs* (e.g. `calculateOrbit`, `splice_gene_sequence`)

We'll rewrite the `Fc` function to follow those guidelines:

~~~
def convert_fahr_to_celsius(fahr):
    celsius = (fahr - 32) * (5 / 9)
    return celsius
~~~
{: .language-python}


Whilst these names are a lot longer than `x` and `Fc`, text editors like **Visual Studio Code** offers code completion. You can start typing <kbd>c</kbd> and be prompted with your function `convert_fahr_to_celsius`. Not only does this mean it's no more difficult or time-consuming to write easily-maintainable code, it also helps avoid you making typos! If your variables are `f`, `g` and `v`, a single mispressed key can cause you a world of trouble.


> ## Exercise: Fixing Functions
> Now we've re-written `Fc` to `convert_fahr_to_celsius` we need to rewrite `FK` to match. Either in a text editor, or on GitHub, fix `FK` to match `convert_fahr_to_celsius`.
>
> > ## Solution
> > We want to keep the style and naming internally consistent as best we can, so the new `FK` should look something like:
> > 
> > ~~~
> > def convert_fahr_to_kelvin(fahr):
> >     celsius = convert_fahr_to_celsius(fahr)
> >     kelvin = celsius + 273.15
> >     return kelvin
> > ~~~
> > {: .language-python}
> > Now every single line of the function is explicit about what it does - you don't need to make any guesses!
>{: .solution}
{: .challenge}

{: .callout}
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

## Defensive Programming

Generally, when we write code we have a pretty solid idea of how we're expecting to use it - and, importantly, its limitations. We know the input file formats we're expecting, the range of physical parameters we can simulate, that kind of thing. But it's very easy to accidentally push code beyond its limits. Then, it can end up simply giving answers that don't make sense, or worse, are *plausible but wrong*. We call problems like this **silent errors**, and you tend to only find out about then when it's too late - they've already quietly ruined weeks of work.

Imagine if we were using our code to calculate the average temperature in a series of climate data files, but it turns out *one* of them has missing temperature readings for some dates. Since `0` is a valid temperature, whoever made the file indicated missing readings with an impossible temperature value of `-999`. Our functions will happily convert that to **-572.7 degrees Celsius**, and drag down our average without telling us!

Instead, we'll make sure that if our code tries to do something we never intended it to do, it stops, and lets the user know:

~~~
def convert_fahr_to_celsius(fahr):
    celsius = (fahr - 32) * (5 / 9)
    if celsius < -273.15:
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius
~~~
{: .language-python}

It's easy to go overboard on defensive programming, 
but making incorrect assumptions about the values your functions will be given has cost multiple space missions like [the ESA's first Ariane 5 rocket](https://en.wikipedia.org/wiki/Ariane_flight_V88), [NASA's Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) and the [Japanese Hitomi X-ray telescope](https://en.wikipedia.org/wiki/Hitomi_(satellite)).

## Documenting Your Code

If your code has descriptive variables and function names, then it should go a long way towards making it clear what it does. But unfortunately, codes of any real size rapidly become too complicated to understand just by reading the code! Even if your code doesn't *start* that large, **it will almost certainly end up that way**. So it's a good idea to write clear documentation from the start, to make sure you don't have to go back and do it later.

### Comments

If you've used clear variable names, then the actual logic and processes of the code should be readable from the text. So with comments, we can describe things in more detail - explaining what's going on at a high level, or things that aren't immediately obvious.

In Python, you can comment your code by starting a line with a `#` (other languages use a different comment character, like `%`, `!` or `//`):
~~~
def convert_fahr_to_celsius(fahr):
    celsius = (fahr + 32) * (5 / 9)
    if celsius < -273.15:
        # If temperature is below absolute zero, throw an error
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius
~~~
{: .language-python}

You can also add these at the end of lines, e.g.:

~~~
def convert_fahr_to_celsius(fahr):
    celsius = (fahr + 32) * (5 / 9) 
    if celsius < -273.15:  # If temperature is below absolute zero, throw an error
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius
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

We're going to look at an example of how to do this in Python. If the first thing in a function is a string that isn't assigned to a variable, that string is attached to the function as its documentation. We'll do this for our `convert_fahr_to_celsius` function (in this example, using the [Sphinx docstring format, which we'll get to later](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)): 

~~~
def convert_fahr_to_celsius(fahr):
    """
    Given a temperature in Fahrenheit, converts it to Celsius

    :param fahr: The temperature in Fahrenheit
    :raises ValueError: If the temperature is below absolute zero
    :return: The temperature in Celsius
    """
    celsius = (fahr + 32) * (5 / 9)
    if celsius < -273.15:
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius
~~~
{: .language-python}

This documentation lists the input variables (as `:param VARIABLE_NAME: Description`), what the function returns (`:return: Description`), and any errors it might raise too (`:raises ErrorType: Description`). Along with a helpful description of what the function does, this information can act as a *contract* for readers to understand what to expect in terms of behaviour when using the function, as well as how to use it.

This kind of clear, firm description of a function provides a solid basis for future development. If you write a function that can only take positive numbers, but don't document that, then someone else might try and feed it negative numbers without realising that's not possible. Then, they'll be faced with a crash at best, or another **silent failure**.

These types of comments are called *docstrings* in Python. We don't need to use triple quotes when we write one, but if we do, we can break the string across multiple lines. 



> ## Exercise: Writing Docstrings
> Now we've written a docstring for `convert_fahr_to_celsius` we need to write one for `convert_fahr_to_kelvin` to match, again either on GitHub or in a text editor.
> 
> > ## Solution
> > As before, we'll use the same format to make the code easier to read:
> > 
> > ~~~
> > def convert_fahr_to_kelvin(fahr):
> >     """
> >     Given a temperature in Fahrenheit, converts it to Kelvin
> >
> >     :param fahr: The temperature in Fahrenheit
> >     :return: The temperature in Kelvin
> >     """
> >     celsius = convert_fahr_to_celsius(fahr)
> >     kelvin = celsius + 273.15
> >     return kelvin
> > ~~~
> > {: .language-python}
> > In this example the comments for this function are longer than the code, but once you have a function that's a hundred or more lines long the value of a clear summary quickly increases!
>{: .solution}
{: .challenge}

You can also write docstrings for entire Python modules. It's useful to have a brief description of a module's purpose, and a list of the classes and functions within it. It's a bit redundant for our small example, but for a large project it can be a real timesaver:

~~~
"""
A module for converting temperature from Imperial to Metric units.
Will throw ValueErrors for temperatures < absolute zero.

Functions:
    convert_fahr_to_celsius: Converts Fahrenheit to Celsius
    convert_fahr_to_kelvin: Converts Fahrenheit to Kelvin
"""
~~~
{: .language-python}

Every language has a few common standards for documentation - for Python, they're the [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html), [Google](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) and [Numpy](https://numpydoc.readthedocs.io/en/latest/format.html) formats.

It's a good idea to stick to a standard not just because it makes it easier for others to read your comments, but because these standards are also **machine-readable**. Well-formatted comments can be converted by tools like [Sphinx & ReadTheDocs](https://readthedocs.io)) into a searchable website, and you can even include images, LaTeX equations or Jupyter Notebooks. [PoliAstro](https://docs.poliastro.space/en/stable/api.html) is an example scientific project using ReadTheDocs to include not just function documentation generated from its code, but full installation instructions and a list of references.

> ## Help
>
> For languages like Python, docstrings are particularly useful as they're what's displayed when you use `help` to get more information about a function.
> 
> If you have installed Python and downloaded your `climate-analysis` repository, you can test this by opening a terminal, navigating to the repository, and launching a Python interpreter with the command `python` then trying:
> ~~~
> from temp_conversion import convert_fahr_to_celsius
> help(convert_fahr_to_celsius)
> ~~~
> {: .language-python}
{: .callout}
