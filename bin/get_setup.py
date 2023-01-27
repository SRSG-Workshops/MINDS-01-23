import logging
import os
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from distutils.dir_util import copy_tree
import warnings

log = logging.getLogger(__name__)

# change this to get setup docs

log.info(f"Getting setup info")
os.system(f"git submodule add --force -b main https://github.com/Southampton-RSG-Training/setup-documents.git submodules/setup-documents")
os.system("git submodule update --remote --merge")

with open('_config.yml') as config:
    website_config = load(config, Loader=Loader)

# get list of setup.md chunks from _config.yml and apply order to them
# Open the website config, which contains a list of the lessons we want in the
# workshop, then create the directory "submodules" which will contain the files
# for each lesson.

# First get any docs that are at workshop level. The setup_docs structure is
# a dictionary where the keys are the workshop/lesson title and the values are
# a list of filepaths to the setup docs
try:
    setup_docs = {website_config['title']: [x for x in website_config['setup_docs']]}
except (KeyError, TypeError):  # KeyError for when there is no setup_docs, TypeError for when it's empty
    setup_docs = {website_config['title']: []}

# create a list of setup files already included, so we dont add duplicates
setups_included = list(setup_docs.values())

# Then get the docs from lesson episode
for n, lesson_info in enumerate(website_config['lessons']):
    with open(f'submodules/{lesson_info.get("gh-name")}/_config.yml') as config:
        episode_config = load(config, Loader=Loader)
        #select element of the dictionary called setup_docs
        try:
            docs = [x for x in episode_config['setup_docs'] if x not in setups_included]
            setup_docs[episode_config['title']] = docs
            setups_included += docs
        except (KeyError, TypeError):  # KeyError for when there is no setup_docs, TypeError for when it's empty
            warnings.warn(f'{episode_config["title"]} does not have any setup docs')

# Get the images for the setup documents
copy_tree(f"submodules/setup-documents/fig", "fig/")

#for each element in the list
#paste into a string 'submodules/setup-documents/markdown'+setup docs element
with open("setup.md", "w") as file_out:
    for n, (lesson_title, lesson_setups) in enumerate(setup_docs.items()):
        if n == 0:
            file_out.write(f'---\ntitle: Setup for {lesson_title}\n---\n')
        else:
            file_out.write('\n\n' + f'# {lesson_title}')

        for setup in lesson_setups:
            doc_filepath = 'submodules/setup-documents/markdown/' + setup
            with open(doc_filepath, "r", encoding="utf-8") as file_in:
                file_out.write('\n\n' + file_in.read())
