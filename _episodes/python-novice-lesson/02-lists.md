---
lesson_title: 'Building Programs with Python'
lesson_schedule_slug: python-novice-schedule
title: Arrays, Lists etc
slug: python-novice-arrays-lists-etc
minutes: 30
teaching: 15
exercises: 15
questions:
- What is a list?
- How do I access values in a list?
- How to select a range of values from a list?
objectives:
- Lists and Arrays in Python
- Indexing and slicing
keypoints:
- A list is an ordered collection of items of any type.
- Values in the list can be accessed using their index in square brackets e.g. my_list\[ix\]
- Lists can be manipulated in place using attribute functions e.g. my_list.reverse()
- Ranges of values in a list can be obtained via slicing e.g. mylist\[start:stop\]
---


### Arrays in Python

So we can use variables to hold values which we can then manipulate - useful! But what about
when we need to hold many different values, such as a set of phone numbers?

One of the most fundamental data structures in any language is the array, used to hold many
values at once. Python doesn't have a native array data structure, but it has the list which
is much more general and can be used as a multidimensional array quite easily.

### List basics

A list in python is just an ordered collection of items which can be of any type. By comparison
an array is an ordered collection of items of a single type - so a list is more flexible than an
array.

We can also add and delete elements from a Python list at any time - Python lists are what is known
as a *dynamic and mutable* type.

Lists are built into the language (so we don't have to load a library to use them).

To define a list we simply write a comma separated list of items in square brackets:



~~~
odds = [1, 3, 5, 7, 9, 11, 15]
print('Odds are:', odds)

~~~
{: .python}


~~~
Odds are: [1, 3, 5, 7, 9, 11, 15]
~~~
{: .output}

This looks like an array because we can use indexing to pick out an individual element -
indexes start from 0.

Programming languages like Fortran and MATLAB start counting at 1,
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because that's simpler for computers to do.

It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.

We select individual elements from lists by indexing them:



~~~
print('first and last:', odds[0], odds[-1])
~~~
{: .python}

Which will print first and last elements, i.e. value 1 and 15 in this case.



~~~
first and last: 1 15
~~~
{: .output}

*See slide [Indexing a List Example I](https://southampton-rsg.github.io/swc-python-novice-websci/motivation/index.html#indexing-a-list-example-i)*.

Similarly to change the seventh element we can
assign directly to it:



~~~
odds[6] = 13
~~~
{: .python}

*See slide [Indexing a List Example II](https://southampton-rsg.github.io/swc-python-novice-websci/motivation/index.html#indexing-a-list-example-ii)*.

### Slicing

The *Slicing* notation looks like array indexing but it is a lot more flexible. For example:



~~~
odds[2:5]
~~~
{: .python}


~~~
[5, 7, 9]
~~~
{: .output}

*See slide [Slicing a List Example I](https://southampton-rsg.github.io/swc-python-novice-websci/motivation/index.html#slicing-a-list-example-i)*.

is a sublist from the third element to the fifth i.e. from `odds[2]` to `odds[4]`. Notice that the
final element specified i.e. `[5]` is not included in the slice.

Also notice that you can leave out either of the start and end indexes and they will be assumed to have their maximum possible value.
For example:



~~~
odds[5:]
~~~
{: .python}


~~~
[11, 13]
~~~
{: .output}

is the list from `odds[5]` to the end of the list and


~~~
odds[:5]
~~~
{: .python}


~~~
[1, 3, 5, 7, 9]
~~~
{: .output}

is the list up to and not including odds[5] and


~~~
odds[:]
~~~
{: .python}


~~~
[1, 3, 5, 7, 9, 11, 13]
~~~
{: .output}

is the entire list.

### Slicing strings

A section of an array is called a [slice](reference.html#slice).
We can take slices of character strings as well:



~~~
element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])
~~~
{: .python}

*See slide [Slicing a List Example II](https://southampton-rsg.github.io/swc-python-novice-websci/motivation/index.html#slicing-a-list-example-ii)*.


~~~
first three characters: oxy
last three characters: gen
~~~
{: .output}


> ## Slicing strings
>
> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> What is `element[-1]`?
> What is `element[-2]`?
> Given those answers,
> explain what `element[1:-1]` does.
{: .challenge}

List slicing is more or less the same as string slicing except that we can modify a slice. For example:


~~~
odds[0:2]=[17,19]
~~~
{: .python}

has the same effect as



~~~
odds[0]=17
odds[1]=19
~~~
{: .python}

**NOTE:**

Finally, it is worth knowing that the list we assign to a slice doesn't have to be the same size as the slice -
it simply replaces it even if it is a different size.

### Thin slices

The expression `element[3:3]` produces an [empty string](reference.html#empty-string),
 i.e., a string that contains no characters.

### Lists and Strings

There is one important difference between lists and strings:
we can change the values in a list,
but we cannot change the characters in a string.
For example:


~~~
names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin' # correct the name
print('final value of names:', names)
~~~
{: .python}


~~~
names is originally: ['Newton', 'Darwing', 'Turing']
final value of names: ['Newton', 'Darwin', 'Turing']
~~~
{: .output}

works, but:

~~~
name = 'Bell'
name[0] = 'b'
~~~
{: .python}

~~~
>>> name[0]='b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
~~~
{: .error}

does not.


> ## Ch-Ch-Ch-Changes
>
> Data which can be modified in place is called [mutable](reference.html#mutable),
> while data which cannot be modified is called [immutable](reference.html#immutable).
> Strings and numbers are immutable. This does not mean that variables with string or number values are constants,
> but when we want to change the value of a string or number variable, we can only replace the old value
> with a completely new value.
>
> Lists and arrays, on the other hand, are mutable: we can modify them after they have been created. We can
> change individual elements, append new elements, or reorder the whole list.  For some operations, like
> sorting, we can choose whether to use a function that modifies the data in place or a function that returns a
> modified copy and leaves the original unchanged.
>
> Be careful when modifying data in place.  If two variables refer to the same list, and you modify the list
> value, it will change for both variables! If you want variables with mutable values to be independent, you
> must make a copy of the value when you assign it.
>
> Because of pitfalls like this, code which modifies data in place can be more difficult to understand. However,
> it is often far more efficient to modify a large data structure in place than to create a modified copy for
> every small change. You should consider both of these aspects when writing your code.
{: .callout}


There are many ways to change the contents of lists besides assigning new values to
individual elements:

~~~
odds.append(21)
print('odds after adding a value:', odds)
~~~
{: .python}

~~~
odds after adding a value: [17, 19, 5, 7, 9, 11, 13, 15, 21]
~~~
{: .output}


~~~
del odds[0]
print('odds after removing the first element:', odds)
~~~
{: .python}


~~~
odds after removing the first element: [19, 5, 7, 9, 11, 13, 15, 21]
~~~
{: .output}


~~~
odds.reverse()
print('odds after reversing:', odds)
~~~
{: .python}


~~~
odds after reversing: [21, 15, 13, 11, 9, 7, 5, 19]
~~~
{: .output}

While modifying in place, it is useful to remember that python treats lists in a slightly counterintuitive way.

If we make a list and (attempt to) copy it then modify in place, we can cause all sorts of trouble:



~~~
odds = [1, 3, 5, 7]
primes = odds
primes += [2]
print('primes:', primes)
print('odds:', odds)
~~~
{: .python}


~~~
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7, 2]
~~~
{: .output}

This is because python stores a list in memory, and then can use multiple names to refer to the same list.
If all we want to do is copy a (simple) list, we can use the list() command, so we do not modify a list we did not mean to:


~~~
odds = [1, 3, 5, 7]
primes = list(odds)
primes += [2]
print('primes:', primes)
print('odds:', odds)
~~~
{: .python}

~~~
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7]
~~~
{: .output}

This is different from how variables worked in lesson 1, and more similar to how a spreadsheet works.

### Basic array operations

So far so good, and it looks as if using a list is as easy as using an array.

Where things start to go wrong just a little is when we attempt to push the similarities
between lists and arrays one step too far. For example, suppose we want to create an array
initialised to a particular value. Following the general array idiom in most languages we
might initialise the elements to a value, say, 1. e.g.:



~~~
myList=[]
myList[1]=1
myList[2]=1
...
~~~
{: .python}

only to discover that this doesn't work because we can't assign to a list element that doesn't already exist.

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
~~~
{: .error}

One solution is to use the append method to add elements one by one:

~~~
myList=[]
myList.append(1)
myList.append(1)
...
~~~
{: .python}

This works but it only works if we need to build up the list in this particular order - which most of the time you want to do anyway.


> ## Slicing From the End
>
> Use slicing to access only the last four characters of a string or entries of a list.
>
>
> 
> ~~~
> string_for_slicing = "Observation date: 02-Feb-2013"
> list_for_slicing = [["fluorine", "F"], ["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
> ~~~
> {: .python}
>
>
> ~~~
> "2013"
> [["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
> ~~~
> {: .output}
> 
> Would your solution work regardless of whether you knew beforehand
> the length of the string or list
> (e.g. if you wanted to apply the solution to a set of lists of different
> lengths)?
> If not, try to change your approach to make it more robust.
>
>
> 
> > ## Solution
> > Use negative indices to count elements from the end of a container
> > (such as list or string):
> >
> > 
> > ~~~
> > string_for_slicing[-4:]
> > list_for_slicing[-4:]
> > ~~~
> > {: .python}
> >
> {: .solution}
> 
{: .challenge}


> ## Overloading
>
> `+` usually means addition, but when used on strings or lists, it means
> "concatenate".
> Given that, what do you think the multiplication operator `*` does on lists?
> In particular, what will be the output of the following code?
>
>
>
> ~~~
> counts = [2, 4, 6, 8, 10]
> repeats = counts * 2
> print(repeats)
> ~~~
> {: .python}
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
>
> > ## Solution
> > The multiplication operator `*` used on a list replicates elements of the
> > list and concatenates them together:
> >
> > ~~~
> > [2, 4, 6, 8, 10, 2, 4, 6, 8, 10]
> > ~~~
> > {: .output}
> >
> > It's equivalent to:
> >
> > ~~~
> > counts + counts
> > ~~~
> > {: .python}
> > 
> > So using `*` on lists works in a similar way as it does on strings.
> > Where Python employs overloading, it tries to be consistent!
> {: .solution}
> 
{: .challenge}
