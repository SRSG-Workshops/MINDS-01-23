---
title: "Project Management"
slug: project-novice-project-management
teaching: 25
exercises: 5
questions:
- "How can I manage the development of my code?"
objectives:
- "Explain how project boards work."
- "Explain how to set up a Kanban board on GitHub."
- "Discuss strategies for using a Kanban board."
- "Explain what a fork is, and how to fork a repository."
keypoints:
- "Projects are broken-down into self-contained tasks."
- "Tasks are represented as cards on a board."
- "Cards are arranged to show their status."
- "Issues can be added to project boards and labelled."
- "Project boards can show the priority of their tasks."
- "Forks are copies of entire repositories that can be synced up with the original."
---

Developing academic software is a project, and most projects (software and *non*-software alike!) consist of multiple tasks. Keeping track of the list of tasks you have to do, and how far you are through each, quickly becomes a non-trivial task itself. Without a good framework, it can be hard to keep track of what's done, or what needs doing, and particularly hard to convey that to others or share the responsibilities out. 

## Project boards

A **project board** (or **kanban board**, from the japanese for a card) is a tool for keeping track of all the different components of a project, and what their current status is. They do this using **columns** and **cards** - you break your project down into tasks which you write on **cards**, then move them between **columns** that describe the status of each task. Cards are usually small, descriptive and self-contained tasks that build on each other - think "Add reader for .csv files" instead of "Get input working". Breaking a project down into clearly-defined tasks makes it a lot easier.

In industry, they often use formal project management styles for their boards with specific columns and usages, but we're going to use a simple, flexible format - not least because the more complicated your project board gets, the harder it is for you to get your collaborators to use it...

### To GitHub

There's a lot of sites that host project boards. For non-software projects like thesis-writing or organising conferences, you might use [Trello](https://trello.com), but repository hosting sites like GitHub and GitLab have built-in project boards that interact with the other features of the site, so we're going to use them (though other tools like [Jira](https://www.atlassian.com/software/jira) also offer this functionality). This episode will use GitHub as an example, but GitLab has almost identical functionality. 

Let's go to our `climate-analysis` repository, go to the **Projects** tab, then select click on the green **Link a project** dropdown and select **New Project**. Then, click the **New Project** button.

![Link a project to a repository](fig/03-boards/project-new.png)

Then just name it *"Climate Analysis"*, and select **Board** from the list on the left. Then we've got our new **Project Board**! A repository can have any number of project boards linked to it - for example, each PhD student in a collaboration can have their own project board, or you can create a new project board for each paper you're writing.

![Creating project details](fig/03-boards/project-new-details.png)

### Columns

Almost all styles of board have three 'basic' columns, with pretty self-explanatory names:
* To Do
* In Progress
* Done

GitHub's default project boards that automatically have those columns - and more it **automates them**. If you add a pull request to the board, it can automatically move it to **Done** for you when you merge it.

One common extra column is **On hold** or **Waiting**. If you have tasks that get held up by waiting on other people (e.g. to provide you with data or respond to your questions) then moving them to a separate column makes their current state clearer. We're going to click on the **+** button (you might have to scroll over a bit to see it!):

![Adding a column, part 1](fig/03-boards/project-columns-new.png)

 Then click the **New Column** button, add a **Waiting** column, and drag it in-between **In Progress** and **Done**:

![Adding a column, part 2](fig/03-boards/project-columns-new-button.png)

Now we've got our board fully set up:

![Board fully set up](fig/03-boards/project-columns-new-done.png)

### Cards

One of the advantages of using GitHub or GitLab to host your project board is the integration with **issues**. You can easily add issues to your project board, to keep track of how they're progressing.

You can create cards on the project board, or you can **import existing issues**. Scroll down to the bottom of the **To Do** column and select the **+** box:

![Where to add issues](fig/03-boards/project-issues-add.png)

If we start typing <kbd>#</kbd>, it'll show us a list of the repositories we could link, and then once we select `climate-analysis` it'll list the issues on that repository. We can click on them one-by-one, or select **Add items from yourname/climate-analysis** and import them in a batch:

![Adding existing issues](fig/03-boards/project-issues-add-dropdown.png)

We can also create a card without an issue. The repo currently doesn't tell people how to use the code - it needs an example. So let's create a card about it, that we can promote to a full issue later!

Click **+** box at the bottom of the **To Do** column, delete the `climate-analysis` link, and start typing a title like *"Add example of use"* then hit <kbd>Return</kbd>:

![Adding new cards](fig/03-boards/project-card-add.png)

Then double-click on the card, and you can add more detail:

![Turning a card into an issue](fig/03-boards/project-card-add-details.png)

Cards can have detailed content like checklists, but that only goes so far. Later on you might want to convert the card to an issue so you can add labels or write detailed comments. Fortunately, you can click **Convert to issue** at the bottom of the expanded card, and selecting the repository for it.

It's often a good idea as you can use the comments section on the issue to write everything you tried - and, importantly, everything that *failed* for future reference. Sometimes, an issue you thought was simple and self-contained might turn out to be a bigger task than you thought. In that case, it's sensible to create new cards or issues that reference the one they broke off from.

Our project board is looking a little thin, but for an example full one check out the plotting library [Plotly](https://github.com/orgs/plotly/projects/3).

{: .challenge}
> ## Exercise: Issue Labels
> You can see that your issue card has a 'bug' label, but the one you made has no labels. Convert your new card to an issue, and add the **Documentation** label to it.
>
>{: .solution}
> > ## Solution
> > We convert the card to an issue, and add a quick description, then click **Convert to issue** and select `climate-analysis` from the dropdown:
> > ![Convert card to issue](fig/03-boards/project-card-challenge-issue.png)
> > Once we've made the issue, we can follow the link to see it and add the **Documentation** label:
> > ![Select the documentation label](fig/03-boards/project-card-challenge-issue-label.png)


### Board Details

By default, the board only shows the status of each issue, and who's working on it. If we want to see a little bit more info (like the **Documentation** label we just applied!) we need to change that.

Go to the **View 1** tab at the top, click the **Down arrow**, and select **Fields**:

![Filtering project board info](fig/03-boards/project-filter.png)

Then we can tick the **Labels** field and use the **Save changes** button on the right-hand side:

![Saving updated filters](fig/03-boards/project-filter-save.png)


### Prioritisation

Once your project board has a large number of cards on it, you might want to begin priorisiting them. Not all tasks are going to be equally important, and some will require others to be completed before they can even be begun. Common methods of prioritisation include:

* **Vertical position:** The vertical arrangement of cards in a column represents their importance. High-priority bugs go to the top of **To Do**, whilst tasks that depend on others go beneath them. This is the easiest one to implement, though you have to remember to correctly place cards when you add them.
* **Priority columns:** Instead of a single **To Do** column, you have two or more- a **To Do: Low Priority** and a **To Do: High Priority**. When adding a card, you pick which is the appropriate column for it. You can even add a **Triage** column for newly-added issues that you've not yet had time to classify. This format works well for project boards devoted to bugs.
* **Labels:** If you convert each card into an issue, then you can label them with their priority- GitHub lets you create new labels and set their colour. **Green low**, **orange medium** and **red high** priority labels make for a very visually clear indication, but require the most admin as each card has to be an issue to receive a label.

Making a new label is a little more involved: You have to go back to your repository, go to the **Issues** tab, and select **Labels**:

![Issues button](fig/03-boards/project-priority-labels.png)

Then you can pick **New label** on the right, and in the dialog give your new label a name, description, and then pick its colour:

![New label button](fig/03-boards/project-priority-labels-new.png)


{: .challenge}
> ## Exercise: Prioritisation
> 
> Currently, we don't really have enough cards to prioritise. Create a new card named **"High priority"**, and using one of the prioritisation schemes arrange your board so it's the most important.
>
>{: .solution}
> > ## Solution
> > We type *High priority* into the box at the bottom of the **Todo** column:
> > ![Creating a new card](fig/03-boards/project-priority-challenge.png)
> > Then we can click and drag to move it to the top of the column:
> > ![Prioritisation by order in column](fig/03-boards/project-priority-challenge-top.png)
> >
> > Or, we can convert the card to an issue as we did before, then select the **High priority** label we made earlier:
> > ![Labelling a new issue](fig/03-boards/project-priority-challenge-label.png)
> > Then we have prioritisation by label:
> > ![Labeled a new issue](fig/03-boards/project-priority-challenge-labeled.png)


> ## Advanced Schemes
> 
> Whilst you can prioritise your tasks using simple schemes, more advanced ones exist in industry. **MoSCoW** (**Must, Should, Could, Won't**) is one such scheme, which splits your tasks up into no more than 60% **must-have** features, and no less than 20% **could-have** features.
> 
> If your must-have features take longer than expected to implement, you have a pre-made list of what you can cut to complete the project on-time. If you have a relatively well-defined project that needs to be completed to a strict deadline, consider looking into MoSCoW.
{: .callout}

## Feature-branch workflows

The **Feature-branch workflow** is a common way of structuring how you develop your code using version control, that sites like GitHub make easy to apply.

In the feature-branch workflow, you make use of the ease of creating new 'branches' with Git, parallel versions of your code that you can modify independently and easily merge back together.

![Feature-branch workflow](fig/03-boards/git-feature-branch.svg)

You have a `main` branch, that contains the stable version of the code you want to share with other people, and **create new branches to add features to your code**. When you're happy with a new feature, it's fully-tested, and you want to share it with others, you can make a **Pull Request** to merge your **feature branch** in.

Let's go back to our repository and select the `rainfall_conversion.py` file:

![Opening a file in GitHub](fig/03-boards/project-branch.png)

Now, click the **Edit** button (that looks like a pencil, on the right side of the text):

![Documenting rainfall module](fig/03-boards/project-branch-edit.png)

Then, add some comments to document the code in the file. Don't worry if you don't know Python - just write anything!:

![Documenting rainfall module](fig/03-boards/project-branch-edited.png)

We have to commit these changes to our repository. We'll write a commit message - in this case, we can use the issue linking features we described earlier to connect it to issue #3. In case we want to keep working on this file and not just commit straight away, we're going to select **Create a new branch**. Let's name it after the issue that it solves, then click **Propose changes**:

![Documenting rainfall module](fig/03-boards/project-branch-edited-commit.png)

Now we have a **Pull Request**! We can keep our stable version of the code on our `main` branch, and work on our `issue-document-rainfall` branch until we're happy, and then action the pull request to merge it in. Until then, our changes don't affect the version on our `main` branch that our collaborators are using. We can also see a summary of the changes we've made in our pull request, and even request that others review them!

This makes it easy to work on multiple things at once - even if we're half-way through adding a new feature on one branch, we can deal with a bug that a collaborator has run into by creating a new branch, fixing the bug in that branch, and then doing a pull request to merge the fixes in. If we weren't using the feature-branch method and were working directly on `main`, we'd have to finish and test our work on adding a new feature before we could fix the bug!

Plus, we can easily add new developers to our code, and test new features in isolation to avoid confounding effects.

### Best Practise 

If we're plan to use our code in publications, we can take this one step further and add a `dev` branch. We update the `main` branch whenever we publish a new paper - it contains all the code and methods we've used in it, readily accessible for anyone to reproduce our results.

The `dev` branch is the version we keep *within* our collaboration, and it's where we build up our work *between* papers. Instead of making new **feature branches** off of `main`, we work off of `dev`, and make pull requests from our finished features back into `dev` too. Then when we're sure that all our features work well together, and we're using the code to make published results, we make a pull request from `dev` back to `main`.

There's some best practise associated with this workflow:

* When adding a new feature, use a feature branch, and **test the feature in your feature branch**.
* It's OK to commit broken, work-in-progress code to a feature branch as it's not expected to be 'finished' until you submit a pull request.
* Once your feature is tested and it's ready to merge, submit a pull request to `dev`.
* Don't commit broken, work-in-progress code to `dev`! If someone wants to make a new branch, or fix a bug, they'll be using `dev` as a base, so it needs to work fine.
* Only pull from `dev` to `main` when you think `dev` is stable. This is the version people will be downloading to verify the results from your papers.

In industry, there's normally strict testing criteria for when you merge in feature branches or merge `dev` into `main`. 
That's a lot harder to apply in academia - in an experimental code, there is often no known ideal behaviour to test against,
and you expect your code's output to change as you alter the equations and assumptions.


## Forks

'Forking' a repository is similar to creating a new branch, but on a much larger scale - you create your own copy of the **whole repository**, that is **linked back to the original**.

For some large projects, or open-source projects, it's not practical to have all the collaborators working on the same repository. Multiple different developers might both create branches with the same name, leading to conflicts, and developers can end up with access to dozens of work-in-progress branches they don't know anything about. Others limit the ability of unauthorised users to push to the repository to prevent abuse, or accidental uploads of sensitive or restricted material. In these contexts, it makes more sense for **every collaborator to have their own fork**. Then, once they finish work on a feature branch, they can **submit a pull request back to the original**.

We're going to create a fork of an existing repository - `project-novice-demo`. [Go to the repository on GitHub](https://github.com/Southampton-RSG-Training/project-novice-demo), and click **Fork**. You can fork a repository to your own account, or any **Team** you have access to. For now, we'll make a personal copy:

![Create a fork](fig/04-features/fork-button.png)

As you can see, the fork looks and works just like a normal repository, but handily tells you how far you are behind the original.

![Created fork](fig/04-features/fork-made.png)

You may also be able to use forks to create modified versions of existing codes that better suit your needs, depending on their software license. It is good practise to submit your modifications and improvements back to the original, though.
