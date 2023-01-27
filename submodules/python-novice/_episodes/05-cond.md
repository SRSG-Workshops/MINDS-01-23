---
title: Making choices
slug: python-novice-making-choices
minutes: 25
teaching: 15
exercises: 10
questions:
- How do I perform logical operations in Python?
objectives:
- Write conditional statements including `if`, `elif`, and `else` branches.
- Evaluate expressions containing `and` and `or`.
- Use conditionals to conditionally process input data.
keypoints:
- We can use logical operations to change the behavior of our code when it meets certain conditions.
- Using if, elif, and else we can check conditions and add a branch that runs if none of the conditions are met.
- We can combine conditions using `and `and `or` to make more complicated logical statements.
---


So what if we want to do something that's dependent on whether a given condition is true? In this lesson, we'll learn how to write code that runs only when certain conditions are true.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an if statement
(you'll need to type this in - don't copy and paste this code directly, it won't work):


~~~
num = 37
if num > 100:
    print("greater")
else:
    print("not greater")
print("done")
~~~
{: .python}

~~~
not greater
done
~~~
{: .output}

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows it is true,
the body of the `if`
(i.e., the lines indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](fig/python-flowchart-conditional.svg)

Conditional statements don't have to necessarily include an `else`.
If there isn't one,
Python simply does nothing if the test is false
(you'll need to type this in - don't copy and paste this code directly, it won't work):



~~~
num = 53
print("before conditional...")
if num > 100:
    print("53 is greater than 100")
print("...after conditional")
~~~
{: .python}


~~~
before conditional...
...after conditional
~~~
{: .output}

We can also chain several tests together using `elif`,
which is short for "else if" as shown in the example code chunk below:

~~~
num = -3
if num > 0:
    print("Sign of a number:",num,"is:",1)
elif num == 0:
    print("Sign of a number",num,"is:",0)
else:
    print("Sign of a number",num, "is:",-1)
~~~
{: .python}


~~~
sign of a number -3 is:  -1
~~~
{: .output}

The keyword `elif` is short for `else if`, and is useful to avoid excessive indentation. An
`if ... elif ... elif ...` sequence is a substitute for the `switch` or `case` statements
found in other languages.

One important thing to notice in the code above is that we use a double equals sign `==` to test for equality
rather than a single equals sign
because the latter is used to mean assignment.
This convention was inherited from C,
and while many other programming languages work the same way,
it does take a bit of getting used to...

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:



~~~
if (1 > 0) and (-1 > 0):
    print("both parts are true")
else:
    print("one part is not true")
~~~
{: .python}

~~~
one part is not true
~~~
{: .output}

while `or` is true if either part is true:

~~~
if (1 < 0) or ('left' < 'right'):
    print("at least one test is true")
~~~
{: .python}

~~~
at least one test is true
~~~
{: .output}

In this case,
"either" means "either or both", not "either one or the other but not both".


> ## How many paths?
>
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> * A
> * B
> * C
> * B and C
>
>
>
> ~~~
> if 4 > 5:
>     print('A')
> elif 4 <= 5:
>     print('B')
> elif 4 < 5:
>     print('C')
> ~~~
> {: .python}
>
> > ## Solution
> > B gets printed. The first condition, `4 > 5` is not true so it moves 
> > to the next elif, but `4 <= 5` is true so that statement executes 
> > printing B. The third condition is therefore not checked and C is 
> > not printed.
> {: .solution}
> 
{: .challenge}


> ## What Is Truth?
>
> `True` and `False` are special words in Python called `booleans`
> which represent true and false statements.
> However, they aren't the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
>
> 
> ~~~
> if '':
>     print('empty string is true')
> if 'word':
>     print('word is true')
> if []:
>     print('empty list is true')
> if [1, 2, 3]:
>     print('non-empty list is true')
> if 0:
>     print('zero is true')
> if 1:
>     print('one is true')
> ~~~
> {: .python}
{: .challenge}

## Another type of loop

We've seen how to write loops where perhaps we know how many times we want the loop to
execute beforehand, e.g. printing out each character in a string. So we can use
for loops to execute a fixed operation over a known number of steps.

But what if we want our loop to continue to execute until some other condition is true?
Perhaps our code runs a simulation that generates a set of results each time through
the loop, but we're not sure when the results will be what we want, i.e. we don't
know how many times the loop needs to execute. For these types of cases, we can use a
`while` loop, which is similar to a `for` loop but exits the loop when some condition is
true.

Consider the following example:

~~~
from random import randint
number = 0
while number != 5:
    number = randint(1, 10)
    print(number)
~~~
{: .python}

We use Python's ability to generate a random number here for clarity, but this could
instead be calling a function that runs another step in our simulation and returns a
result.

So in this case, our loop will continue to generate and print out random numbers between
and 10 while the generated number is not equal to 5. When the random number generated is
5, the loop will exit.

`while` loops are a more general case of loops which are often useful (you can even
simulate a `for` loop using a `while` loop). But you should preferably use `for` loops
as opposed to `while` loops where you can, since they are more specific and it's more
readable - it's easier to figure out how many times the loop will execute.


## Climate Analysis: adding a condition to avoid printing comments

We're still getting our column header at the top of our output, and perhaps
we don't want that. We need to able to check whether the line begins with
a '#' (which denotes a comment line), and if so, avoid printing it out.

So let's use an `if` statement to do that (*see `climate_analysis-4.py`*):


~~~
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # print 4th column (max temperature)
        print('Max temperature', data[3])
~~~
{: .python}


~~~
Max temperature 58.53
Max temperature 58.60
Max temperature 58.30
Max temperature 56.91
Max temperature 59.86
Max temperature 58.95
Max temperature 58.73
Max temperature 61.41
Max temperature 61.27
Max temperature 61.41
~~~
{: .output}
