# RSG Training Workshop Template

**To use this repository please use the template functionality. When you use this template, please include all branches 
and use a descriptive name as this will become the url that is provided to learners.**

## Setting up a workshop

To configure a workshop please follow the steps below.

1) Create a copy of this workshop using the GitHub (GH) templating function. Note the name of your new workshop will be the website URL, so be descriptive, concise as possible and accurate. Note the git org for workshops should not be Southampton-RSG-Training. For members of the RSG please use SRSG-Workshops.
2) Using either the GH online code editor or pulling a local version, edit the _config.yml file. This is the only file that needs to be modified.
3) The fields to change are as follows:
   - kind: workshop depending on if you want a site with schedules and dates (workshop) or a site which hosts the content for people to access in their own time (course).
   - title, form_title: the title of the workshop and the title of the workshop with spaces replaced with '+' and special characters removed, this is used for Google forms.
   - venue, address, country, lat/long: updates the details for the workshop location. You can use, e.g., Google Maps or https://www.latlong.net/convert-address-to-lat-long.html to find the latitude and longitude of the venue.
   - humandate, humantime, startdate, enddate: human- and machine-readable dates and times, respectively, for the start and end of the workshop. Machine readable dates should be in YYYY-MM-DD format. The human-readable dates are free form.
   - instructor, instructor-email: YAML lists of instructor names and associated email addresses.
   - helper: YAML list of the names of the helpers.
   - **lessons: a YAML list of the lessons to include in the workshop. Each lesson must have:**
      - title: the name of the lesson.
      - org-name (optional): the name of the organisation, or user account, which hosts the content, defaults to Southampton-RSG-Training
      - gh-name: the name of a lesson repository in the provided (or default <https://github.com/Southampton-RSG-Training>) GH organisation e.g. 'git-novice'.
      - branch: the git branch to generate lessons from. To customise a lesson, one can specify another branch - more details below. The default choice is 'main'.
      - type: choose from either 'episode' for standard markdown lessons or 'episode_r' for R markdown.
      - order (if delivery == static): the position in the lesson running order used when 'kind' is set to 'course'
      - date (if kind == workshop): the date the lesson is to be taught. Many date formats accepted, more information can be found [here](https://dateutil.readthedocs.io/en/stable/parser.html) about accepted formats. If a date format is not accepted, then the build process will abort. For multi-day lessons, multiple dates have to be specified in a YAML list. The number of dates must equal the number of schedule tables in `_includes/rsg/lesson/schedule.html`.
      - time (if kind == workshop): the time to start the lesson, both 12-hour and 24-hour timestamps are accepted. For multi-day lessons, multiple start times must also be specified in a YAML list.
4) Build the website 
   1) For an online hosted site: **Commit (and push) changes to the 'main' branch**. The site is built, and published to the 'gh-pages' branch. The site build is handled by GH Actions, more details in development below.
   2) For a local site, useful for testing: run `bash bin/build_me.sh`

The currently available lessons are:

- shell-novice <https://github.com/Southampton-RSG-Training/shell-novice>
- git-novice <https://github.com/Southampton-RSG-Training/git-novice>
- python-novice <https://github.com/Southampton-RSG-Training/python-novice>
- spreadsheets <https://github.com/Southampton-RSG-Training/spreadsheets>
- openrefine-data-cleaning <https://github.com/Southampton-RSG-Training/openrefine-data-cleaning>
- r-novice <https://github.com/Southampton-RSG-Training/r-novice>
- project-novice <https://github.com/Southampton-RSG-Training/project-novice>


## The workshop should now be built, information below are for development of the lessons and templates.
### The steps below here require a strong working knowledge of git.

## To reattach to this template and pull updates and changes the following steps are required.

1) Warning: To do this you need to understand both Git Remotes, Git merges (specifically solving conflicts).
2) ```git remote add template https://github.com/Southampton-RSG-Training/workshop-template```
3) ```git fetch --all```
4) Copy changes from the template to your workshop:
   1) Use an IDE to compare the diff between remote template and local.
      1) I prefer IntelliJ IDEA with git-toolbox and this sublist details a recommended workflow.
      2) In the git tab at the bottom of the window open the Remote->template dropdown.
      3) Right-click the main branch in the template dropdown and select 'Show Diff with Working Tree'.
      4) Use the file explorer to investigate changes between the template and your branch. 
         1) Config will be very different usually one only merges new fields.
         2) ./bin may have updates usually accept all of these.
         3) .github/workflows/website.yml if changed should be merged.
   2) I strongly discourage this it creates a lot of conflicts that then need to be manually fixed. ```git merge template/main --allow-unrelated-histories```
   3) Please document other IDEs or methods... 
5) Finally, add and commit the changes to the main branch the push to 'origin/main'.

## Customising Lessons

No lesson material resides in the workshop main branch, on gh-pages it is pulled from submodules and is thus 'read-only'.
To customise a lesson's content it must be updated in the lesson repository and the lesson's config entry updated to 
point to the custom version. For more detail on writing lessons see the lesson repo. In brief one branches the lesson 
makes the custom version then uses the branch tag to point to the new custom branch. Once the custom branch is written
and the branch added to the workshop _config.yml committing and pushing the config will cause the workflows to rerun
and the workshop to update with the custom lesson.

## Getting updated lessons

If a lesson is updated we need to re-trigger the build process to pull the changes. We can do this via the actions tab 
on GitHub, alternatively, the following script can be used:

```bash
$ git commit --allow-empty -m "rebuild lesson to (re)add lesson submodules"
$ git push origin main 
```

## Development and Build Logic

To develop this template requires an understanding of:

1) **Jekyll** and **Liquid templating** are used in the deployment of static GitHub pages sites.
2) **GitHub Actions** and **python** are used to parse the `_config.yml`, clone submodules, and move/generate files to customise the workshop.
3) **Markdown** and/or **Rmarkdown** used to write the lesson material.
4)  **GitHub/git (especially branches)** to manage lesson version, and to separate configuration from deployment.

The main branch of each lesson are to be kept in a build ready state. Development for these lessons is detailed in each
lesson repository. The config file is used by the jekyll build and also parsed to control the GitHub Actions.

Firstly, the _config.yml is parsed by `bin/get_submodules.py` and `bin/get_schedules.py`. `get_submodules.py` gets each 
of the lesson repositories and clones them as a submodules. The episode markdown files are
moved into `collections/_episodes(_rmd)/gh-name-lesson/`, and the various includes and slide files are moved into their 
appropriate locations. Next, `get_schedules.py` parses _config.yml, and generates the top-level and detailed lesson 
schedules. Following on, `bin/clean_setup_md.py` is used to stitch together the various setup files into a single 
markdown file.

There are then two ways to build the workshop:
1) Use ./bin/build_me.sh to build locally. (There may be some install requirements to make this work)
the website will be served locally then when ctrl-c is passed the built website will be torn down and deleted. Remember
to run git status after to make sure your main branch is clean.
2) Use the GH Pages process, (Jekyll/Liquid) is instructed to build the site, the webpage is stored in the `gh-pages` 
branch.
