
<a href="https://galaxyproject.org/"><img src="https://galaxyproject.org/images/galaxy-logos/galaxy_project_logo.jpg" align="left" width="200" ></a>
# Assignment Instruction

In this group assignment, you will play and tweak with Galaxy workflows as both users and developers.

In the first part of the assignment, you will run a Galaxy workflow as end users by importing, editing a workflow and tweaking its parameters; in the second part, as developers and administrators of Galaxy, you will develop a new Galaxy tool, install and modify another tool and create a workflow. After finishing this assignment, you will be familiar with Galaxy from different perspectives.

## Before starting your assignment

### Make a team

You need to form your team by enrolling a group on [Blackboard](https:://bb.vu.nl). Each group consists of 2 people.

### Get the access to a Galaxy instance on the cloud

There are two Galaxy instances running on the cloud. Please click here to sign up one of the instances for your team (each team has one account).

### Prepare Docker and stuff

Please refer to [this](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/docker), which will guide you through the preparation.

### Read all the documents in this Github repo

We have covered as many answers to the questions you might be confronted with as possible in these documents. Therefore, before posing questions, please look them up in these documents to check whether they have been answered or not. 

## Part 1: run a workflow in Galaxy

### Setup

Please create a user account in your Galaxy instance on the cloud. Each team should have one account. Due to the expensive computation of the workflow and the limited cloud computation resources, for each team, we strongly suggest running one workflow collectively rather than individually.

### To-do list
In this part, you are required to:
1. import the workflow from the given Galaxy [workflow file](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/workflow.ga).
2. finish the workflow using the existing tools in Galaxy by referring to [[1]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/Heinz.pdf)
3. test the workflow without running Heinz (the tool at the end of the workflow), because Heinz is really time-consuming.
4. run this workflow on the dataset given, using the parameters $\alpha=0.7$, $\lambda=0.3$, and FDR from [[1]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/Heinz.pdf)
5. visualise the output of workflow (either by the given [script](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/graphviz.py) or in your own way).

It probably takes more than 12 hours to run this workflow using the full dataset given, because running Heinz is time-consuming.

For this part, you need to hand in:
* 1.1 a screenshot of the workflow.
* 1.2 a visualisation of the workflow output.

## Part 2: develop tools and a workflow for Galaxy

Actually in the first part, we just used some random values for parameters $\alpha$ and $\lambda$, making the result less interpretable. $\alpha$ and $\lambda$ should come from BUM model [[2]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/Heinz.pdf), therefore we need to run this statistical model to approximate the parameters instead. However, in the current Galaxy workflow, there is no such a tool, we need to develop it and make it available in the Galaxy instance you are working on.

### Setup

To set up a local Galaxy instance, [this document](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/docker) will guide you through the setup procedure.

You need to register an account in this Galaxy instance and then make it the administrator ([how?](https://galaxyproject.org/admin/)).

Hereafter, the default home directory in this document `/export` in the docker container or the local directory mapped to `/export`.

### To-do list

In this part, you are required to:
1. log in to the Galaxy instance and install DESeq2 ([iuc](https://github.com/galaxyproject/tools-iuc)).
2. replace DESeq R script (deseq2.R) in the folder `shed_tools` with the [bespoke one](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/deseq2.R) provided ([why?](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/scripts)).
3. finish the Galaxy tool of BUM model (xml file) in the folder `galaxy-central/tools/bionet`.
4. recreate a workflow that can be run automatically from the beginning to the end.
5. run the workflow and visualise the output.

For this part, you need to hand in:
* 2.1 an XML file
* 2.2 the output file of BUM model.
* 2.3 a screenshot of the new workflow.
* 2.4 a visualisation of the workflow output.

## Submit your assignment

Please prepare everything into a PDF document, where you name, email, student No. should be clearly mentioned. The document should be well-structured (using the ordinal numbers 1.1, 1.2, 2.1, etc)

The whole XML file should appear in the document **in a code style with your code highlighted**.

The file name of the document has to be ‘groupXX.pdf’ (e.g. group03.pdf).

The document should be submitted via Blackboard by the end of **8 May 2017**
