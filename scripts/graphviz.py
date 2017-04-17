#!/usr/bin/env python3.6
"""Visualise the output of Heinz.

This script is used to visualise the output of Heinz, which is in the form of
DOT language:
    1. Clear the output of Heinz, extract the DOT source code.
    2. Visualise the DOT source code and save it into file.

The function of this script is rather simple, for more advanced visualisation,
please adopt other solutions by reading metaModule paper
doi: 10.1093/bioinformatics/btv526

This tool is developed for the master course 'Bionformatics for Tranlational
Medicine' at VU Amsterdam.

This tool is only designed for Heinz output.

For more information on this course, please visit https://goo.gl/ggXp12
"""

# Author: Cico Zhang
# Date: 17 Mar 2017

from graphviz import Source
import argparse
import sys

parser = argparse.ArgumentParser(
    description='Visualise the output of Heinz')
parser.add_argument('-i', '--input', required=True, dest='heinz',
                    metavar='Heinz_output.txt', type=str,
                    help='Output file of Heinz as the input')
parser.add_argument('-o', '--output', required=True, dest='output',
                    metavar='graph.pdf', type=str,
                    help='The output file that saves the visualisation')
args = parser.parse_args()

if args.heinz is None:
    sys.exit('Input file must be designated.')

with open(args.heinz) as r:
    graph_dot = r.readlines()

src = Source(''.join(graph_dot))
src.render(args.output, cleanup=True)

print('The visualization is saved as PDF!')
sys.exit(0)
