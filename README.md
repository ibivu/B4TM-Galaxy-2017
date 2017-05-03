
<a href="https://galaxyproject.org/"><img src="https://galaxyproject.org/images/galaxy-logos/galaxy_project_logo.jpg" align="left" width="200" ></a>
# Assignment Instruction

In this group assignment, you will play and tweak with Galaxy workflows as both users and developers.

In the first part of the assignment, you will run a Galaxy workflow as end users by importing, editing a workflow and tweaking its parameters; in the second part, as developers and administrators of Galaxy, you will develop a new Galaxy tool, install and modify another tool and create a workflow. After finishing this assignment, you will be familiar with Galaxy from different perspectives.

**In the year of 2017, the assignment starts from 25 Apr and lasts until 8 May.**

## Known issues (Updated on 3rd May)

### VU WiFi problem
Up to know, VU WiFi seems to occasionally affect the usage of your local Galaxy instance. The know cases are:
1. occasionally getting stuck in uploading data
2. occasionally white screen in installing tool
3. Incomplete installation of dependencies of Galaxy tools.

### Overwriting problem
After restarting Galaxy instance when editing bum.xml is finished, the bum.xml file just restores to the original version. It only happens in the `/export/galaxy-central/tools` folder.

The solution is editing bum.xml in or transferring the modified one to the folder `/galaxy-central/tools/bionet` instead.

### DESeq2 problem
After the installation of Version 5 of DESeq2 Galaxy tool, ‘deseq2.R’ does not appear. It is probably a bug in Galaxy toolshed in installing the older version of DESeq2. The expected behavior is that we can install any available version of DESeq2 from Galaxy toolshed. To fix it, we provide a few solutions:
1. Install DESeq2 locally instead of from toolshed. [how?](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/README.md#deseq2-a-directory)
2. Alternatively, you may recreate a new Galaxy instance for Part 2 using a newer version of Docker image: docker.bioinformatician.science:5678/b4tm/local:0.2, which has preinstalled DESeq2.
3. Alternatively again, you may still use docker.bioinformatician.science:5678/b4tm/local:0.1 to recreate a new Galaxy instance for Part 2, just install Version 9 of Deseq2 and then replace ‘deseq2.R’ with the one in https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/scripts/, for this operation, you don’t need to restart Galaxy. The result of Version 9 has been tested on 2nd May, it is the same with Version 5’s.

## Before starting your assignment

### Make a team

You need to form your team by enrolling a group on [Blackboard](https:://bb.vu.nl). Each group consists of 2 people.

### Prepare Docker and stuff

Please refer to [this](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/docker), which will guide you through the preparation.

### Read all the documents in this Github repo

We have covered as many answers to the questions you might be confronted with as possible in these documents. Therefore, before posing questions, please look them up in these documents to check whether they have been answered or not.

### Tips

When you start running a job, an item will be immediately created in 'History'. You can monitor the progress of the job in 'History'. You might notice that the job has been in the state ***'This job is waiting to run'*** for a long time. In this case, please just wait for a while, because Galaxy is installing the dependencies of the Galaxy tool on your first use. **Never cancel the job** ('cancel' means deleting this item in 'History'), or else you will screw up the installation of dependencies rendering the tool useless (Fixing it is not an easy thing).

## Part 1: run a workflow in Galaxy

### Setup

This part will be done on **Galaxy Instance 1**. Please refer to [this document](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/docker) for setting
it up. Alternatively, you can use a Galaxy server running at SurfSara for this part of the assignment; please refer to the [galaxy server instructions](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/galaxy).

You need to register an account in this Galaxy instance before continuing the assignment.

### To-do list
In this part, you are required to:
1. import the workflow from the given Galaxy [workflow file](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/workflow.ga). Note that you need to download the file from Github (do not use the URL directly for import).
2. finish the workflow using the existing tools in Galaxy. Note that further details un this workflow can be found in Ref. [[1]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/metaModules.pdf) Hint: **p-value** not adjust p-value should be used.
3. test the workflow.
4. run this workflow on the dataset given, using the parameters $\alpha=0.612345$, $\lambda=0.435674$, and FDR from [[1]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/metaModules.pdf)(in its result section)
5. visualise the output of workflow (either by the given [script](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/visualization.py) or in your own way).

It probably takes about 15 minutes to run this workflow using the full dataset given. Note that with different setting, Heinz can take a long time (>12 hours) to run.

#### Test the workflow
There is no point using the full dataset to test the workflow, because it is time-consuming. Instead, you can try one of the following methods.
1. Run the workflow without Heinz.
2. Use a smaller dataset to run the whole workflow, you can pare down the output data of 'Calculate Heinz scores' by selecting
the first 100 lines using the existing Galaxy tools, for example.

For this part, you need to hand in:
* 1.1 a screenshot of the workflow.
* 1.2 a visualisation of the workflow output.

## Part 2: develop tools and a workflow for Galaxy

Actually in the first part, we just used some random values for parameters $\alpha$ and $\lambda$, making the result less interpretable. $\alpha$ and $\lambda$ should come from BUM model [[2]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/Heinz.pdf), therefore we need to run this statistical model to approximate the parameters instead. However, in the current Galaxy workflow, there is no such a tool, we need to develop it and make it available in the Galaxy instance you are working on.

### Setup

This part will be done on **Galaxy Instance 2**. Please refer to [this document](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/docker) for setting it up.  If you do not have access to a docker environment on at least one device in your group, please contact us: we can provide you with a small VM to perform the development part of the assignment.


You need to register an account in this Galaxy instance and then make it the administrator ([how?](https://galaxyproject.org/admin/)).

Hereafter, the default home directory in this document `/export` in the docker container or the local directory mapped to `/export`.

### To-do list

In this part, you are required to:
1. log in to the Galaxy instance and install DESeq2 ([iuc](https://github.com/galaxyproject/tools-iuc)).
2. replace DESeq R script (deseq2.R) in the folder `shed_tools` with the [bespoke one](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/scripts/deseq2.R) provided ([why?](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/scripts)).
3. finish the Galaxy tool of BUM model (xml file) in the folder `galaxy-central/tools/bionet`.
4. recreate a workflow that can be run automatically from the beginning to the end.
5. run the workflow and visualise the output.

Note that the last Heinz step can take a very long time. If you do not want to run this last step on your own latop for the full data set you can use a Galaxy server at SurfSara. Please refer to the [galaxy server instructions](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/galaxy).



For this part, you need to hand in:
* 2.1 an XML file
* 2.2 the output file of BUM model Galaxy tool.
* 2.3 a screenshot of the new workflow.
* 2.4 a visualisation of the workflow output.


## Submit your assignment

Please prepare everything (except output file of BUM model Galaxy tool) into a PDF document, where you name, email, student No. should be clearly mentioned. The document should be well-structured (using the ordinal numbers 1.1, 1.2, 2.1, etc)

The whole XML file should appear in the document **in a code style with your code highlighted**.

The file name of the document has to be ‘groupXX.pdf’ (e.g. group03.pdf).

Please don't rename the output file of BUM model Galaxy tool (just leave it as it is).

The document and the output file need to be submitted via Blackboard by the end of **8 May 2017**
