---
lesson_title: 'Best Practices in Data Organisation Using Spreadsheets'
lesson_schedule_slug: spreadsheets-schedule
title: "Common spreadsheet errors"
slug: spreadsheets-common-spreadsheet-errors
teaching: 15
exercises: 30
questions:
- "What are some common challenges with formatting data in spreadsheets and how can we avoid them?"
objectives:
- "Recognise and resolve common spreadsheet formatting problems."
keypoints:
- "Avoid using multiple tables within one spreadsheet."
- "Avoid spreading data across multiple tabs."
- "Record zeros as zeros."
- "Use an appropriate null value to record missing data."
- "Do not use formatting to convey information or to make your spreadsheet look pretty."
- "Place comments in a separate column."
- "Record units in column headers."
- "Include only one piece of information in a cell."
- "Avoid spaces, numbers and special characters in column headers."
- "Avoid special characters in your data."
---

There are a few potential errors to be on the lookout for in spreadsheet data. If you are aware of the errors, and the
complications they can cause on downstream data analysis and result interpretation, it helps motivate you and your
project members to try and avoid them. It's far more efficient to prevent problems by making small changes in the way
you collect data, than spending weeks or months cleaning messy data. Ultimately, good organisation of your data in
improves your research efficiency and reliability. Here are some common spreadsheet errors, which we will cover in
detail below:

- [Entering more than one piece of information in a cell](#-entering-more-than-one-piece-of-information-in-a-cell)
- [Using multiple tables](#using-multiple-tables)
- [Using multiple tabs](#-using-multiple-tabs)
- [Using problematic field names](#-using-problematic-field-names)
- [Not filling in zeros](#-not-filling-in-zeros)
- [Using problematic null values](#-using-problematic-null-values)
- [Placing comments or units in cells](#-placing-comments-or-units-in-cells)
- [Using formatting to make the spreadsheet look pretty](#-using-formatting-to-make-the-spreadsheet-look-pretty)
- [Using formatting to convey information](#-using-formatting-to-convey-information)

## <a name="info"></a> Entering more than one piece of information in a cell

As described on the previous page, the rule is "one cell, one observation". For example, if you are counting species and
you find one male and one female of the same species, you could enter this as '1M, 1F.' If you record two pieces of data
in the same cell, you will confuse data analysis software and this risks mistakes in analysis.

The solution is to include one column for the number of individuals and a separate column for the sex.

## Using multiple tables

A common mistake is creating multiple data tables within a single spreadsheet, as shown below. This will confuse a data analysis
program (and many humans too).

![multiple tabs](fig/2_datasheet_example.jpg)

There are a number of problems with multiple tables on one page. The main problem is that - although clearly separate to
a human observer - a computer will rigidly interpret anything in the same row as belonging to the same observation.

In the example above, the computer will read row 4 and assume that all
columns A-AF refer to the same sample. This row actually represents four distinct samples (sample 1 for each of four
different collection dates - May 29th, June 12th, June 19th, and June 26th), as well as some calculated summary
statistics (an average (avr) and standard error of measurement (SEM)) for two of those samples.

There is no reason why observations from different sites or different years should not go into a single table. You just
need to keep track of them by using new columns (in this examples, one for site and one for year). Keeping data
from the same experiment in a single table will help you stick to a consistent data structure, and avoid errors when
looking up data from different tables.

Using multiple tables on one page also makes it difficult for humans to keep track of the data - especially if one of
the tables is *hidden* off the edge of the spreadsheet. Multiple tables also increases the risk of using the same column
name in multiple places, which will make it significantly harder to clean your data.

## <a name="tabs"></a> Using multiple tabs

But what about workbook tabs? Are they the easy solution to organising data? In a word, no!

* When you create extra tabs, you prevent the computer from seeing connections that exist in the data. Before you can
analyse the data, you need to explicitly tell the computer how to combine the data across tabs. If the tabs are
inconsistently formatted, you might even have to do this manually, which is inefficient. We used multiple tabs in our
example messy data file, and you have now seen how difficult it is to consolidate the data across tabs.

* Separating your data over multiple tabs means that you are more likely to accidentally add inconsistencies to your data,
because it is all too easy to forget to change to the appropriate tab before recording new data. Similarly, when it
comes to analysis, it's easy to draw data from the wrong tab.

Rather than entering data into multiple tabs, try adding another column to your spreadsheet.

> ## Note on bigger data and column headers
>
> Your datasheet might get very long over the course of the experiment. This makes it harder to enter data if you cannot
> see your headers at the top of the spreadsheet. But do not be tempted to repeat your header row in the middle of your
> data - these headers will get mixed into the data leading to problems down the road. Instead, you can freeze the
> column headers so that they remain visible even when you have a spreadsheet with many rows. If you are not sure how to
> do this, see the [documentation on how to freeze column headers in Excel](https://support.office.com/en-ca/article/Freeze-column-headings-for-easy-scrolling-57ccce0c-cf85-4725-9579-c5d13106ca6a).
> {: .callout}

> ## Exercise - 15 minutes
> At the moment the data in [messy survey data](data/messy_survey_data.xlsx) is in multiple, inconsistent, tables
> across two tabs. Following from what we've just learnt, reformat the data into a format which
> makes it easier for both a person and a computer to understand by, for example, bringing the data from both tabs into
> one and creating new columns. Note that some cells contain data for multiple variables. Think carefully about how you
> should deal with those.
>
> At this stage, you don't need to worry about formatting your spreadsheet or fixing any suspicious looking dates and
> messy cells. We'll deal with these in later exercises.
>
> > ## Keep your raw data raw
> > Don't forget to create a new file or a new tab for the cleaned data; never modify your original (raw) data.
> > {: .callout}
>
> > ## Solution
> > Combine the data from both tables into one table by adding both a date and plot column. Be careful when copying the
> > data across, as the format and order of the columns are not the same in all of the tables. An example of what you
> > may end up with is shown below:
> >
> > ![solution ex 1](fig/episode3_ex1_sol.png)
> >
> > This format is much easier for data analysis programs to read. Humans will have an easier time as well, since there
> > is no need to scroll to the right or switch between tabs to find all of the data.
> >
> > If you didn't manage to finish in time, or if you just want to look at the solution instead, you can download
> > the updated [messy survey data](data/messy_survey_data_ex1.xlsx).
> > {: .solution}
> 
> {: .challenge}


## <a name="field_name"></a> Using problematic field names

We need to choose descriptive column names to allow for easy data identification.
There is a delicate balance in choosing the correct length of column name. Longer names allow you to adequately describe
the data, but they can become unwieldy. It is better to err on the side of a longer, descriptive column name,
than a shorter, ambiguous one. You can use abbreviations to reduce the length of column names, but these can quickly
become obscure (especially if you don't return to the data for 6 months or longer). If you use unconventional
abbreviations, make sure to keep a record of their full description in the text file you keep with the spreadsheet data.

You must be careful with the characters you use. Do not use spaces, numbers, or special characters of any kind. All of
these can cause problems when conducting later analysis. Spaces can be misinterpreted as delimiters (i.e. they can be
used by some programs to show where a column begins and ends), some programs do not like field names that are text
strings that start with numbers, and some characters (e.g. "/") can be misinterpreted by data analysis programs.

Instead of spaces, the best advice is to use underscores (`_`) to separate words. Some people use PascalCase (where
uppercase letters are used to delimit words, e.g. ExampleFileName) but if you ever
want to return the whitespaces later in your analysis, it is easier to do this with underscore-separated words.

Do not use your spreadsheet as a word processor! If you copy text directly from a Microsoft Word (or similar
applications), you are likely to include lots of formatting information (e.g. tabs, line breaks, etc.)
and fancy non-standard characters (left- and right-aligned quotation marks, em-dashes, etc.) that will confuse data
analysis software. Avoid adding anything other than text and spaces into a cell.

Where all the observations share the same unit, it can be useful to include the unit in the field name to avoid later
confusion. Alternatively, as described above, include the unit in a separate column.

The table below gives some examples of best practice in naming:

<table>
<tr>
	<td> <b>Good Name</b></td> <br />
	<td> <b>Good Alternative</b> </td><br />
	<td> <b>Avoid</b></td><br />
    <td> <b>Reason to avoid</b></td><br />
</tr>
<tr>
	<td>Max_temp_C</td>
	<td>MaxTempC</td>
	<td>Maximum Temp (°C)</td>
    <td>Uses a special character (°)</td>
</tr>
<tr>
	<td>Precipitation_mm</td>
	<td>Precipitation</td>
	<td>precmm </td>
    <td>Not very readable</td>
</tr>
<tr>
	<td>Mean_year_growth</td>
	<td>MeanYearGrowth </td>
	<td>Mean growth/year</td>
    <td>Uses a special character (/)</td>
</tr>
<tr>
	<td>sex</td>
	<td>sex</td>
	<td>M/F</td>
    <td>Uses special character (/) and not very readable</td>
</tr>
<tr>
	<td>weight</td>
	<td>weight</td>
	<td>w.</td>
    <td>Uses a special character (.) and not very readable</td>
</tr>
<tr>
	<td>cell_type </td>
	<td>CellType </td>
	<td>Cell Type </td>
    <td>Uses a blank character</td>
</tr>
<tr>
	<td>Observation_01 </td>
	<td>first_observation</td>
	<td>1st Obs</td>
    <td>Uses a blank character and starts with a number</td>
</tr>
</table>

## <a name="zeros"></a> Not filling in zeros

Sometimes the thing you are measuring throws out the odd zero - sometimes the observations are almost all zeros. Is it
really necessary to keep typing in zeros? Wouldn't it be more efficient to leave the column blank unless there's a
non-zero? To a computer, there is a big difference between a zero and a blank cell. A zero is data. A blank cell means
that there was no measurement, and the computer will likely interpret it as an unknown value (otherwise known as a
*null* value).

Spreadsheets are likely to misinterpret blank cells that you intend to be zeros, and statistical analysis programs
are very likely to interpret them as blank cells. By not entering the value of your observation, you are telling your
computer to represent that data as unknown or missing (null). This can cause problems with later analysis. To take a
simple example: the average of a set of numbers which includes a single null value is always null (because the computer
cannot guess the value of the missing observations).

It is very important to record zeros as zeros and truly missing data as nulls.

## <a name="null"></a> Using problematic null values

Null values are also problematic! Different people take different approaches to recording the lack of data (see below),
but not all approaches are useful.

![White et al.](fig/3_white_table_1.jpg)

Sometimes different null values are used to describe the different reasons why the observation could not be made.
"NULL", "missing data" and "malfunction", all convey important information but you are in effect using a single column
to capture three different types of information. This is messy, as described on the previous page, and the solution is
to include new columns - one for each type of information you need to capture.

Sometimes unacceptable null values are automatically recorded by the device you use to measure the observation (older
devices are especially guilty of not following best practice). If the erroneous null values stem from the measuring
device, you're left with little choice but to clean the data and replace them with a better null value. A tool like
[OpenRefine](https://openrefine.org/), which is introduced in another lesson, is perfect for this kind of cleaning.

Whatever the reason, it is a problem if unknown or missing data is recorded as -999, 999, or 0.
Statistical programs do not know that these are intended to represent missing (null) values and, because they are
valid numbers, they will be included in calculations which will lead to incorrect results. How these values are
interpreted will depend on the software you use to analyse your data.

It is essential to use a clearly defined and consistent null indicator. Although open to ambiguity, blanks are still
 used by a number of applications, but options like and 'NA' (for R) and 'NaN' (for Python) are good choices. For more
 information, see White et al.
 [Nine simple ways to make it easier to (re)use your data](http://doi.org/10.4033/iee.2013.6b.6.f).

## <a name="units"></a> Placing comments or units in cells

Sometimes you need to make a note or a comment on an observation. For example, you may want to identify observations
that were collected by a summer student who you later found out was misidentifying some of your species. These data you
will want to identify as suspect. The problem is the same as that with formatting data to convey information: most
analysis software cannot see Excel or LibreOffice comments, so they would be ignored. The solution is to create another
column if you need to add notes to cells.

Do not include units in cells! They cause a headache in later analysis when you have to separate out the unit from its
associated value. Ideally, all the measurements you place in one column should be in the same unit, but if for some
reason they are not, create a new column to specify the units.

> ## Exercise - 10 minutes
> Our [messy survey data](data/messy_survey_data.xlsx) is still full of formatting choices which makes the data difficult
> for a computer to interpret. With your new knowledge on best practices for field names, cell values and null values,
> clean up the data by updating column variable names and by editing the contents of cells.
>
> Don't worry about formatting the dates or cleaning up any formatting just yet, we will cover those soon.
>
> If you want, you can use the [solution from the previous example]((data/messy_survey_data_ep3_ex1.xlsx)) as your
> starting point.
>
> > ## Solution
> > Rename the columns to replace spaces with underscores (`_`), e.g. 'Date_collected', and include the units in the
> > column names rather than in the cell. Additionally, add a notes column to indicate where there have been problems
> > during the data capture. Finally, choose a null value to use -- there are a new observations which have the value
> > -999. In the example below, blank cells are used, but either NULL, NA or None would have be a reasonable choice
> > as well.
> >
> > ![solution](fig/episode3_ex3.png)
> >
> > If you didn't manage to finish in time, or if you just want to look at the solution instead, you can download
> > the updated [messy survey data](data/messy_survey_data_ex2.xlsx).
> > {: .solution}
>
> {: .challenge}

## <a name="formatting_pretty"></a> Using formatting to make the spreadsheet look pretty

It's very difficult not to tweak your tables to make them look prettier, e.g. merging cells (especially in
headers) or using borders to separate different data. If you are not careful, formatting a worksheet to be more
aesthetically pleasing can compromise a computer’s ability to see associations in the data. For example, merged cells
will confuse statistics software, which will read the merged cell as a single data value and cause misalignment with
data in the following rows.

Your primary goal with structuring data is to accurately capture the data and make the connections in the data transparent
to yourself and any program you use for analysis. You will want pretty tables for publications and suchlike, but those
should be completely separate from the tables you use to record the data.

## <a name="formatting"></a> Using formatting to convey information

A common example of using formatting to convey information is to highlight cells in a specific colour that you want
dealt with differently to others. For example, highlighting cells that should be excluded from the analysis (see
below). Another example is to leave a blank row to indicate a separation in the data. Both of these highlighting
 approaches will cause problems with later analysis because they are undetectable to computers.

![formatting](fig/formatting.png)

The solution - as is so often the case with spreadsheets - is to create a new column to encode the data that should be
excluded.

![good formatting](fig/good_formatting.png)

<!-- TODO: include text about formatting cell data types
	 TODO: add reference to formatting data types into the exercise
 -->
<!-- ## <a name="formatting_cell_types"></a> Setting the data format for cells

It is often occurrence to input data into Excel, and to then watch it come out in a format you are not expecting. -->

> ## Exercise - 5 minutes
> Some data has been highlighted to indicate that something was wrong. As mentioned earlier,
> the computer is unable to see this formatting when you come to analyse your data. Remove this formatting, whilst
> keeping the information conveyed by the formatting.
>
> If you want, you can use the [solution from the previous example]((data/messy_survey_data_ep3_ex2.xlsx)) as your starting
> point.
>
> > ## Solution
> > Replace the highlighted cells in the 2013 data with your choice of null character. For the 2014 data, highlighted
> > cells refer to weight measurements which were taken when the measuring device was not calibrated correctly. You
> > should create a new column to track which measurements were with a calibrated measuring device, or probably not as
> > good, you could instead create a note in the note column mentioning the calibration was not correct.
> >
> > ![weight calibrated](fig/episode3_ex3.png)
> >
> > If you didn't manage to finish in time, or if you just want to look at the solution instead, you can download
> > the updated [messy survey data](data/messy_survey_data_ex3.xlsx).
> >
> > {: .solution}
>
> {: .challenge}



> ## Full & clean dataset
> If you want to have a look at other full, clean datasets - have a look at some of the other files you downloaded.
> [surveys.csv](https://ndownloader.figshare.com/files/2292172) combines data from all the surveys
> and [combined.csv](https://ndownloader.figshare.com/files/10717186) includes the cleaned data from [surveys.csv](https://ndownloader.figshare.com/files/2292172), [plots.csv](https://ndownloader.figshare.com/files/3299474) and [species.csv](https://ndownloader.figshare.com/files/3299483) combined into one clean file.
> {: .testimonial}
