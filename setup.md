---
title: Setup for MINDS CDT Software Carpentry
---


# Version Control with Git

## Text Editor ##

A text editor is the piece of software you use to view and write code. If you
have a preferred text editor, please use it. Suggestions for text editors are,
Notepad++ (Windows), TextEdit (macOS), Gedit (GNU/Linux), GNU Nano, Vim.
Alternatively, there are IDE's (integrated developer environments) that have
more features specifically for coding such as VS Code; there are also IDEs
specific to languages will be listed in the appropriate section(s) below.

## Git Setup ##

### Windows
We'll be using Git Bash for both git and a shell to run it in. If you've already installed Git Bash then go to the next section. Otherwise, go to [git for windows](https://gitforwindows.org/) and click **Download**, then install it. 
Most of the options can be left on default, but be sure you check these:

- **Choosing the default editor used by Git:** Make sure **Nano** is selected from the drop-down. If you're comfortable with other editors, feel free to change it, but we recommend Nano - we use it as it's present on Windows, Mac *and* Linux. If you change it, you might not quite match what we're doing on-screen.
- **Adjusting your PATH environment:** Make sure **Git from the command line and also from 3rd-party software** is selected.
- **Choosing HTTPS transport backend:** Make sure **Use the native Windows Secure Channel Library** is selected.
- **Configuring the terminal emulator to use with Git Bash:** Make sure **Use Windows' default console window** is selected.

#### Mac OS
To use Git you must install the Apple Command Line Tools, this may take a few minutes.  

You can obtain these [from Apple](https://developer.apple.com/download/more/?name=command%20line%20tools%20for%20xcode%2012) (requires your Apple ID)

- Select **Command Line Tools for Xcode 12 (or higher)** and click the link to download the dmg archive.
- If prompted, choose to allow downloads from developer.apple.com
- Open the downloaded dmg archive from the Downloads folder
- Double-click the Command Line Tools.pkg icon to install

Alternatively, you can install the tools from the command line:

~~~
$ xcode-select --install
~~~
{: .language-bash}

#### Linux
Git comes pre-installed on most Linux distributions. You can test if it's installed by running `git --version`. 
If it's not installed, you can install it by running `sudo apt-get install git` or `sudo yum install git`, depending on 
your distribution.


# Managing Academic Software Development

## GitHub ##
Later on in the session, we'll be demonstrating how to share work with collaborators using [GitHub](https://github.com/). You'll need to [create an account there](https://github.com/signup). As your GitHub username will appear in the URLs of your projects there, it's best to use a short, clear version of your name if you can.


## Project Demo Repository

We'll be showing you how to manage an example academic software project. 
If you've completed our **Version Control with git** workshop, you'll have a finished version of our `climate-analysis` repository ([you'll have used the template from here](https://github.com/Southampton-RSG-Training/git-novice-template/))
If not, please [create a copy of it from this template (linked here)](https://github.com/Southampton-RSG-Training/project-novice-template/generate), and name it `climate-analysis`.


## Install Visual Studio Code

This workshop involves editing code files. 
Whilst you can use any text editor to do this, some code editors or Integrated Development Environments (IDEs) have features designed to make coding easier.
If you're already using a code editor or IDE (e.g. [Atom](https://atom.io/), [Sublime Text](https://www.sublimetext.com/) or [Spyder](https://www.spyder-ide.org/)), 
stick with what you're comfortable with. If not, we'd recommend installing [Visual Studio Code (link here)](https://code.visualstudio.com/).

### Windows / MacOS
Go to [the Visual Studio Code website](https://code.visualstudio.com/), and download and run the installer.

### Linux
If you're on **Ubuntu**, Visual Studio Code should be available through the software centre! 
If not, [follow the detailed instructions here](https://code.visualstudio.com/docs/setup/linux) to install it.
