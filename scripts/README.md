# Use guide

This directory stores all the scripts and files you will use in this assignment.

## deseq2.R

In the official version of DESeq2 Galaxy tool, filtering the low-quality KOs by 'baseMean' is not supported, which however is
required in metaModule. Therefore, we provide a bespoke version to enable this function.

## visualization.py (The renamed version of graphviz.py)

**We have renamed the script to `visualization.py`, due to the naming conflicts, which probably stops you from running the script.**

You may use this Python script to visualise the output of Heinz (the final output of the workflow). This script can only run
in Python 3.5+ and you need to solve the Python package dependencies. Alternatively, you can look for your own solution to
visualise the Heinz output.

### Common problems

#### Install graphviz

Two installations are needed here. One is [graphviz package](http://www.graphviz.org/), the other is graphviz python library, which is usually installed via pip.

#### Alternative solution

You can try eXamine plugin from [[1]](https://github.com/ibivu/B4TM-Galaxy-2017/blob/master/papers/metaModules.pdf), if you like, or any other solution.

## workflow.ga

The workflow file you need in the first part of the assignment.

## deseq2 (a directory)

This directory contains all the files of Deseq2 Galaxy tool.

Copy the whole folder `deseq2` here into `/galaxy-central/tools` into the container of Galaxy Instance 2, by preferably using the command `docker cp deseq2 b4tm2017:/galaxy-central/tools`, then modify `/export/galaxy-central/config/tool_conf.xml` by adding `<tool file="deseq2/deseq2.xml" />` to any section you like, then restart Galaxy.
