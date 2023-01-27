---
title: "Introduction"
slug: project-novice-introduction
teaching: 10
exercises: 0
questions:
- "Why should I manage my software development?"
objectives:
- "Explain why academic software development requires management."
keypoints:
- "Well-made software is easier to expand and reuse"
- "You need to produce reproducible research."
- "You are a user of your own code."
---

Developing academic software can be an unusual exercise, especially compared to traditional software development. 

Unlike in traditional development, the software itself often isn't the end goal - it's the *papers* it enables that are. This can lead to the focus being on how to get the results needed for the latest paper, without considering how this works in the long run. As a result, a large proportion of academic software is **paperware** - ad-hoc, poorly-written code made without any real plans, where all the information on how it works and how to run it is undocumented.

This usually means the code is harder for you to develop later, and hard for you to get collaborators on board to develop and/or use it. In the worst case, mismanaged software development can result in you having to rewrite from scratch. Given how much effort it takes to produce scientific software, this can be a huge waste of your time and effort! 


## Better Software, Better Research

One key reason to make sure you properly manage the development of your academic software, even when the software is just a by-product of doing the science, is because **better software** makes **better research**. Organisations like the [Software Sustainability Institute](https://software.ac.uk/) exist to make this point.

If you plan your project out clearly in advance, openly list your future goals and the limitations of your software, and write code that's consistent and designed to be easy-to-interpret, you'll find it to be much more **sustainable**. Sustainable software is easier to keep maintained, to expand to cover new problems, and to bring in new collaborators on. The benefits to your research from this will rapidly outweigh the time you spend on software project management.


## Single User-Developer Projects

Many academic software projects have pretty limited scale, often run by a single user-developer, or just a small team. In these circumstances, it can be tempting not to spend the time on 'user-facing' project features like documentation. After all, everybody involved in the project has a deep grasp of the code and knows how it works and all the existing problems!

That's not necessarily the case:

* You might want to bring a new PhD student or postdoc onto the project later, and they'll have a much harder time getting started if all the information on the project lives within your head. Not only do they have huge areas of unknown unknowns, *you* will have large areas of unknown **knowns** - things that you've forgotten are essential to build the code, or edge cases it can't cope with.
* The results of your research should be **reproducible**. That means that referees on your papers, or those who read them, should be able to take your code and re-create your results. If you write your project in a way that only you can use it, then you're doing bad science.
* Knowledge can decay. Whilst you might know all the ins and outs of the code now, trying to come back to the project in two years' time (when you're writing it up in your thesis, or starting a new collaboration re-using it).

So as a result a lot of project management features that are designed to work as part of a team, or communicate information to users, are still useful for you as a sole user-developer.

> ## The Bus Factor
> 
> One other reason it's important to document how your code is developed, managed and used is to get your **Bus Factor** up. The bus factor describes the number of developers who have to be hit by a bus for a project to be impossible to continue. For *a very large percentage* of academic software projects, the bus factor is 1...
>
> Even if you aren't hit by a bus, accident, illness, family emergencies or other unplanned events (like global pandemics) can prevent you working on a project for a while. Fortunately, if you've documented your code, goals and the current status of your project collaborators can pick it up and get the results required for a referee response or conference presentation!
{: .callout}

## Project Management Tools

Fortunately, a lot of tools exist to help manage the development of your academic software. You should already be familiar with Git and [GitHub](https://github.com), already a great way to keep track of how your code evolves and share it with others. GitHub and other repository hosting sites (for example, [GitLab](https://gitlab.com)) have a whole range of project management tools that we can use - and we're going to start with them.
