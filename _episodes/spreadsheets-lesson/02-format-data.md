---
lesson_title: 'Best Practices in Data Organisation Using Spreadsheets'
lesson_schedule_slug: spreadsheets-schedule
title: "Organising data in spreadsheets"
slug: spreadsheets-organising-data-in-spreadsheets
teaching: 10
exercises: 10
questions:
- "How do we organise and format data in spreadsheets for effective data use?"
objectives:
- "Describe best practices for data entry and formatting in spreadsheets."
- "Apply best practices to arrange variables and observations in a spreadsheet."
keypoints:
- "Never modify your raw data. Always make a copy before making any changes."
- "Keep track of all of the steps you take to clean your data in a plain text file."
- "Organise your data according to tidy data principles."
- "Record metadata in a separate plain text file (such as README.txt) in your project root folder or folder with data."
---

A common mistake is to use a spreadsheet like a lab notebook. In other words,
to convey information not just with the data, but with notes in the margin and the spatial layout of the data.
We can (usually) interpret these things, but computers cannot. They are incredibly literal, so unless we explain
every single nuance of meaning that we intended, the computer will misinterpret our data - and that causes problems. This is why it is extremely important to start with well-formatted
tables from the outset - before you even start entering data from your first preliminary experiment.

Data organisation is the foundation of your research project. It can make it easier or more difficult
to work with your data throughout your analysis. You should start
thinking about data organisation before you start collecting data. There's a lot of flexibility, but some of the
choices you make now will limit your ability to work with the data in the future.

> ## Best data formats may differ
> The best layout for data entry might change dependent on the specific use case. Do not stick to a format just because
> you have used it previously. Choose the best format on a case-by-case basis. (And if you need to convert between formats,
> ideally you would automate the conversion with a script in, say, Python or R.
> {: .callout}

## Structuring data in spreadsheets

The cardinal rule of using spreadsheet programs for data is to keep it "tidy":

1. Put all your variables (i.e. the thing you are measuring,
   like 'weight' or 'temperature') in its own column
2. Put each observation in its own row
3. Do not combine multiple variables in one cell
4. Leave the raw data raw - do not change it!
5. Export the cleaned data to a text-based format like CSV (comma-separated values). This
   ensures that anyone can use the data, and is required by most data repositories.

To see some of these rules in action, let's look at the following data from a survey of small mammals in a desert
ecosystem. Different people have gone to the field and entered data into a spreadsheet. They kept track of variables
like species, plot, weight, sex and date collected.

Here's a poor example of data collection:

![multiple-info example](fig/multiple-info.png)

There are problems like the species and sex variables being in the same field. This data format would make it difficult
to easily look at all of one species, or look at different weight distributions by sex. If, instead, we put sex and
species in different columns, it would be much easier to perform such analyses.

The data could be better organised as:

![single-info example](fig/single-info.png)

> ## Columns for variables and rows for observations
> The rule of thumb, when setting up data in a table is: columns = variables, rows = observations, cells = data values.
> {: .callout}

## <a name="metadata"></a> Including metadata in the spreadsheet

"Metadata" is the data you record about your data (such as the date the experiment was conducted, who conducted it, etc). It
is essential to understanding the circumstances under whic your data was collected. You may be on intimate terms with
your dataset while you are collecting and analysing it, but this will change over time. After six months, you are
 unlikely to remember the exact algorithm you used to transform a variable, or that "sglmemgp" means "single member of
 group". You don't need a photographic memory if you collect good metadata.

Your data is important, which means there will be many people who will want to examine it. They will need good metadata if they
are to understand your findings, review your submitted publication, replicate your results, design a similar study, or
even just want to archive your data. While digital data by definition are machine-readable, understanding their meaning
is a job for human beings - and they need the help that metadata provides. The importance of documenting your data
during the collection and analysis phase of your research cannot be overstated - it is fundamental.

Metadata should not be contained in the data file itself, because it can disrupt how programs interpret your data file.
Rather, metadata should be stored as a separate file in the same directory as your data file, preferably in plain text
format (i.e. `.txt`) with a name that clearly associates it with your data file. Because metadata files are free text format,
they allow you to encode comments, units, information about how null values are encoded and related information.

Additionally, file or database level metadata describes how files that make up the dataset relate to each other; what format they are
in; and whether they supersede or are superseded by previous files. A folder-level `README.txt` file is the classic way of accounting for
all the files and folders in a project.

> ## Credit: MANTRA
> The above text on metadata was adapted from the online course Research Data [MANTRA](http://datalib.edina.ac.uk/mantra) by EDINA and Data Library, University of Edinburgh. MANTRA is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
> {: .testimonial}

## Keeping track of your analyses

When you are working with data in spreadsheets, the spreadsheet you end up with will often look very different to the one
you started with. With each change, you are losing information about the history of the data. How many times have you
needed to roll back an analysis, only to become completely lost when retracing your steps? There are ways of mitigating
this problem:

- Before starting your analysis, create a new copy of the original data file to keep alongside your analysed data. This
way, you will always be able to check changes against your original dataset and, if the worst comes to the worst, it
will be easy to start the analysis again!
- Record the steps you take as you conduct your analysis. You should record
these steps as you would any step in an experiment. We recommend that you
do this in a plain text file stored in the same folder as the data file.

In the following example, the spreadsheet has 'raw' tabs in which to store the original, untouched data and 'clean'
tabs in which the processed data is stored. It is accompanied with a text file that describes the steps that have been
taken.

![spreadsheet setup](fig/spreadsheet-setup-updated.png)

> ## Version controlling your data
> Although out of scope for this lesson, you can learn about version control in a separate course,
> which can be used to record the transformation of your data over time, and provides tools to roll back to any
> previous version of the data.
> {: .callout}

## A messy dataset

To put theory into practise, throughout this lesson we will be working with some [messy survey
data](data/messy_survey_data.xlsx) and applying what we learn to that data. The data is a simple
survey of small mammals in a desert ecosystem. Different people have gone to the field and entered data into a
spreadsheet. They kept track of variables like species, plot, weight, sex and date collected. The spreadsheet contains
four tabs,

- The first two tabs, named '2013' and '2014', contain data taken by two field assistants in 2013 and 2014 respectively.
  This is the main data we will be working with.
- The ‘semi-cleaned-combined’ tab contains the combined data from tabs ‘2013’ and ‘2014’, in a 'semi-cleaned' state. We
  will revisit this tab in the episode on quality assurance and control and you will see why it is ‘semi-clean’.
- Ignore the 'dates' tab for now, as we will come back to this in a later episode.

> ## Exercise
> If you haven't done so already, first download the [messy survey data](data/messy_survey_data.xlsx).
> Once you have it downloaded, open it up and have a look around the spreadsheet to see what's there. You will only need
> to worry about the '2013' and '2014' tabs; the other two tabs will be used later.
>
> When you feel ready, create a metadata file (e.g. `README.txt`) to document the key parts of the data. Try to think
> about what you would like to know about the data, if you had to analyse it. For example, you may want to know more
> about the study, when data collection began, and you will probably want to know what the data actually represents.
>
> Since this is not our study or data, we naturally won't know all of this information to fully fill out the metadata.
> Try to fill it in as much as you can, but feel free to leave some parts empty or make up something reasonable to fill
> in any blanks.
>
> > ## Solution
> > You should create a metadata file in the same directory as the spread sheet named something like `README.txt` or
> `METADATA.txt`. It should contain information such as:
> >
> > - The name of the study
> > - The author(s) of the study and data
> > - Contact information for the author(s)
> > - The date data collection began
> > - A brief description of the study and data
> > - A description on the data collection methodology
> > - A list of publications using the data
> > - The date the data was last modified
> > - A list of changes which been made to the data, and analysis done on the data
> >
> > {: .solution}
> 
> {: .challenge}
