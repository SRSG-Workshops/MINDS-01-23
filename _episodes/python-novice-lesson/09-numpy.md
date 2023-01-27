---
lesson_title: 'Building Programs with Python'
lesson_schedule_slug: python-novice-schedule
title: Reading and analysing Patient data using libraries
slug: python-novice-reading-and-analysing-patient-data-using-libraries
minutes: 25
teaching: 20
exercises: 5
questions:
- I work mostly with numerical data are there better methods than strings and lists?
- I've heard python can be slow when working with big data is there anything I can do about that?
objectives:
- Explain what a library is, and what libraries are used for.
- Load a Python library and use the things it contains.
- Read tabular data from a file.
- Select individual values and subsections from data.
- Perform operations on arrays of data.
keypoints:
- Python has many libraries that add to the core language to improve functionality in specific use cases.
- Numpy is a **num**erical **py**thon library that makes working with vectors, matricies, or large data tables easier.
- Numpy can be used to load datasets directly from CSV files bypassing Pythons built in file systems.
---


This lesson presents an end-to-end scientific Python example, from analysing data (using a library), to visualisation (using a library).

We are studying inflammation in patients who have been given a new treatment for arthritis,
and need to analyse the first dozen data sets of their daily inflammation.
The data sets are stored in [comma-separated values](reference.html#comma-separated-values) (CSV) format:
each row holds information for a single patient,
and the columns represent successive days.
The first few rows of our first file look like this:


~~~
0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
0,0,2,0,4,2,2,1,6,7,10,7,9,13,8,8,15,10,10,7,17,4,4,7,6,15,6,4,9,11,3,5,6,3,3,4,2,3,2,1
0,1,1,3,3,1,3,5,2,4,4,7,6,5,3,10,8,10,6,17,9,14,9,7,13,9,12,6,7,7,9,6,3,2,2,4,2,0,1,1
~~~
{: .output}

We want to:

*   load that data into memory,
*   calculate the average inflammation per day across all patients, and
*   plot the result.

In order to load our inflammation data,
we need to [import](reference.html#import) a library called NumPy.
In general you should use this library if you want to do fancy things with numbers,
especially if you have matrices.

Let's start by ensuring we are in the `python-novice/' directory, e.g.:

~~~
$ pwd
~~~
{: .bash}

And we should see:

~~~
/Users/nelle/python-novice
~~~
{: .output}

First, let's go into the `code` subdirectory, and run the Python interpreter.

~~~
$ cd code
$ python
~~~
{: .bash}

We can load NumPy using:

~~~
import numpy
~~~
{: .python}

Importing a library is like getting a piece of lab equipment out of a storage locker
and setting it up on the bench.
Once it's done,
we can ask the library to read our data file for us.

Just as we can assign a single value to a variable, we can also assign an array of values
to a variable using the same syntax:

~~~
data = numpy.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')
~~~
{: .python}

This statement doesn't produce any output because assignment doesn't display anything.

The expression `numpy.loadtxt(...)` is a [function call](reference.html#function-call)
that asks Python to run the function `loadtxt` that belongs to the `numpy` library.
This [dotted notation](reference.html#dotted-notation) is used everywhere in Python
to refer to the parts of things as `thing.component`.

`numpy.loadtxt` has two [parameters](reference.html#parameter):
the name of the file we want to read,
and the [delimiter](reference.html#delimiter) that separates values on a line.
These both need to be character strings (or [strings](reference.html#string) for short),
so we put them in quotes.

By default,
only a few rows and columns are shown
(with `...` to omit elements when displaying big arrays).
To save space,
Python displays numbers as `1.` instead of `1.0`
when there's nothing interesting after the decimal point.

Now that our data is in memory, we can start doing things with it.

If we want to check that our data has been loaded, we can print the variable's value:

~~~
print(data)
~~~
{: .python}

~~~
array([[ 0.,  0.,  1., ...,  3.,  0.,  0.],
       [ 0.,  1.,  2., ...,  1.,  0.,  1.],
       [ 0.,  1.,  1., ...,  2.,  1.,  1.],
       ...,
       [ 0.,  1.,  1., ...,  1.,  1.,  1.],
       [ 0.,  0.,  0., ...,  0.,  2.,  0.],
       [ 0.,  0.,  1., ...,  1.,  1.,  0.]])
~~~
{: .output}

Let's ask what [type](reference.html#type) of thing `data` refers to:

~~~
print(type(data))
~~~
{: .python}

~~~
<type 'numpy.ndarray'>
~~~
{: .output}

The output tells us that `data` currently refers to an N-dimensional array created by the NumPy library.
We can see what its [shape](reference.html#shape) is like this:

~~~
print(data.shape)
~~~
{: .python}

~~~
(60, 40)
~~~
{: .output}

This tells us that `data` has 60 rows and 40 columns, representing 60 patients over 40 days.
`data.shape` is a [member](reference.html#member) of `data`,
i.e.,
a value that is stored as part of a larger value.
We use the same dotted notation for the members of values
that we use for the functions in libraries
because they have the same part-and-whole relationship.

If we want to get a single value from the matrix,
we must provide an [index](reference.html#index) in square brackets,
just as we do in math:

~~~
print('first value in data:', data[0, 0])
~~~
{: .python}

~~~
first value in data: 0.0
~~~
{: .output}

~~~
print('middle value in data:', data[30, 20])
~~~
{: .python}

~~~
middle value in data: 13.0
~~~
{: .output}

The expression `data[30, 20]` may not surprise you,
but as with lists, `data[0, 0]` might.
<!--
Programming languages like Fortran and MATLAB start counting at 1,
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because that's simpler for computers to do.
As a result,
-->
So if we have an M&times;N array in Python,
its indices go from 0 to M-1 on the first axis
and 0 to N-1 on the second.
It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.


> ## In the Corner
>
> What may also surprise you is that when Python displays an array,
> it shows the element with index `[0, 0]` in the upper left corner
> rather than the lower left.
> This is consistent with the way mathematicians draw matrices,
> but different from the Cartesian coordinates.
> The indices are (row, column) instead of (column, row) for the same reason,
> which can be confusing when plotting data.
> {: .callout}

An index like `[30, 20]` selects a single element of an array,
but we can select whole sections as well.
For example,
we can select the first ten days (columns) of values
for the first four (rows) patients like this:

~~~
print(data[0:4, 0:10])
~~~
{: .python}

~~~
[[ 0.  0.  1.  3.  1.  2.  4.  7.  8.  3.]
 [ 0.  1.  2.  1.  2.  1.  3.  2.  2.  6.]
 [ 0.  1.  1.  3.  3.  2.  6.  2.  5.  9.]
 [ 0.  0.  2.  0.  4.  2.  2.  1.  6.  7.]]
~~~
{: .output}

The [slice](reference.html#slice) `0:4` means, numpy selects items between boundries [0,4] and [0,10].

*See slide [Slicing a List Example I](https://southampton-rsg.github.io/swc-python-novice-websci/motivation/index.html#slicing-a-list-example-i)*.

Again, this takes a bit of getting used to,
but the rule is that the difference between the upper and lower bounds is the number of values in the slice.

We don't have to start slices at 0:

~~~
print(data[5:10, 0:10])
~~~
{: .python}

~~~
[[ 0.  0.  1.  2.  2.  4.  2.  1.  6.  4.]
 [ 0.  0.  2.  2.  4.  2.  2.  5.  5.  8.]
 [ 0.  0.  1.  2.  3.  1.  2.  3.  5.  3.]
 [ 0.  0.  0.  3.  1.  5.  6.  5.  5.  8.]
 [ 0.  1.  1.  2.  1.  3.  5.  3.  5.  8.]]
~~~
{: .output}

We also don't have to include the upper and lower bound on the slice.
If we don't include the lower bound,
Python uses 0 by default;
if we don't include the upper,
the slice runs to the end of the axis,
and if we don't include either
(i.e., if we just use ':' on its own),
the slice includes everything:

~~~
small = data[:3, 36:]
print('small is:')
print(small)
~~~
{: .python}


~~~
small is:
[[ 2.  3.  0.  0.]
 [ 1.  1.  0.  1.]
 [ 2.  2.  1.  1.]]
~~~
{: .output}

Arrays also know how to perform common mathematical operations on their values.
The simplest operations with data are arithmetic:
add, subtract, multiply, and divide.
 When you do such operations on arrays,
the operation is done on each individual element of the array.
Thus:

~~~
doubledata = data * 2.0
~~~
{: .python}

will create a new array `doubledata`
whose elements have the value of two times the value of the corresponding elements in `data`:

~~~
print('original:')
print(data[:3, 36:])
print('doubledata:')
print(doubledata[:3, 36:])
~~~
{: .python}

~~~
original:
[[ 2.  3.  0.  0.]
 [ 1.  1.  0.  1.]
 [ 2.  2.  1.  1.]]
doubledata:
[[ 4.  6.  0.  0.]
 [ 2.  2.  0.  2.]
 [ 4.  4.  2.  2.]]
~~~
{: .output}

If,
instead of taking an array and doing arithmetic with a single value (as above)
you did the arithmetic operation with another array of the same size and shape,
the operation will be done on corresponding elements of the two arrays.
Thus:

~~~
tripledata = doubledata + data
~~~
{: .python}

will give you an array where `tripledata[0,0]` will equal `doubledata[0,0]` plus `data[0,0]`,
and so on for all other elements of the arrays.

~~~
print('tripledata:')
print(tripledata[:3, 36:])
~~~
{: .python}

~~~
tripledata:
[[ 6.  9.  0.  0.]
 [ 3.  3.  0.  3.]
 [ 6.  6.  3.  3.]]
~~~
{: .output}

Often, we want to do more than add, subtract, multiply, and divide values of data.
Arrays also know how to do more complex operations on their values.
If we want to find the average inflammation for all patients on all days,
for example,
we can just ask the array for its mean value

~~~
print(data.mean())
~~~
{: .python}

~~~
6.14875
~~~
{: .output}

`mean` is a [method](reference.html#method) of the array,
i.e.,
a function that belongs to it
in the same way that the member `shape` does.
If variables are nouns, methods are verbs:
they are what the thing in question knows how to do.
This is why `data.shape` doesn't need to be called
(it's just a thing)
but `data.mean()` does
(it's an action).
It is also why we need empty parentheses for `data.mean()`:
even when we're not passing in any parameters,
parentheses are how we tell Python to go and do something for us.

NumPy arrays have lots of useful methods:

~~~
print('maximum inflammation:', data.max())
print('minimum inflammation:', data.min())
print('standard deviation:', data.std())
~~~
{: .python}

~~~
maximum inflammation: 20.0
minimum inflammation: 0.0
standard deviation: 4.613833197118566
~~~
{: .output}

When analyzing data,
though,
we often want to look at partial statistics,
such as the maximum value per patient
or the average value per day.
One way to do this is to select the data we want to create a new temporary array,
then ask it to do the calculation:

~~~
patient_0 = data[0, :] # 0 on the first axis, everything on the second
print('maximum inflammation for patient 0:', patient_0.max())
~~~
{: .python}

~~~
maximum inflammation for patient 0: 18.0
~~~
{: .output}

We don't actually need to store the row in a variable of its own.
Instead, we can combine the selection and the method call:

~~~
print('maximum inflammation for patient 3:', data[2, :].max())
~~~
{: .python}

~~~
maximum inflammation for patient 3: 19.0
~~~
{: .output}

What if we need the maximum inflammation for *all* patients,
or the average for each day?
As the diagram below shows,
we want to perform the operation across an axis:

![Operations Across Axes](fig/python-operations-across-axes.svg)

To support this,
most array methods allow us to specify the axis we want to work on.
If we ask for the average across axis 0 (representing the patients axis),
we get:

~~~
print(data.mean(axis=0))
~~~
{: .python}

~~~
[  0.           0.45         1.11666667   1.75         2.43333333   3.15
   3.8          3.88333333   5.23333333   5.51666667   5.95         5.9
   8.35         7.73333333   8.36666667   9.5          9.58333333
  10.63333333  11.56666667  12.35        13.25        11.96666667
  11.03333333  10.16666667  10.           8.66666667   9.15         7.25
   7.33333333   6.58333333   6.06666667   5.95         5.11666667   3.6
   3.3          3.56666667   2.48333333   1.5          1.13333333
   0.56666667]
~~~
{: .output}

As a quick check,
we can ask this array what its shape is:

~~~
print(data.mean(axis=0).shape)
~~~
{: .python}

~~~
(40,)
~~~
{: .output}

The expression `(40,)` tells us we have an N&times;1 vector,
so this is the average inflammation per day for all patients.
If we average across axis 1, we get:

~~~
print(data.mean(axis=1))
~~~
{: .python}

~~~
[ 5.45   5.425  6.1    5.9    5.55   6.225  5.975  6.65   6.625  6.525
  6.775  5.8    6.225  5.75   5.225  6.3    6.55   5.7    5.85   6.55
  5.775  5.825  6.175  6.1    5.8    6.425  6.05   6.025  6.175  6.55
  6.175  6.35   6.725  6.125  7.075  5.725  5.925  6.15   6.075  5.75
  5.975  5.725  6.3    5.9    6.75   5.925  7.225  6.15   5.95   6.275  5.7
  6.1    6.825  5.975  6.725  5.7    6.25   6.4    7.05   5.9  ]
~~~
{: .output}

which is the average inflammation for each patient across all days.


> ## Thin slices
>
> From our previous topic, the expression `element[3:3]` produces an [empty string](reference.html#empty-string),
> i.e., a string that contains no characters.
> If `data` holds our array of patient data,
> what does `data[3:3, 4:4]` produce?
> What about `data[3:3, :]`?
> {: .challenge}
