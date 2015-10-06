#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys

a_count = 0
c_count = 0
g_count = 0
t_count = 0
base_total = 0

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        a_count += line.count("A")
        c_count += line.count("C")
        g_count += line.count("G")
        t_count += line.count("T")
    base_total += (a_count + c_count + g_count + t_count)

print("Base counts for file %s:" % sys.argv[1])
print("A: %d" % a_count)
print("C: %d" % c_count)
print("G: %d" % g_count)
print("T: %d" % t_count)
print("Base A percentage: ", round((float(a_count)/float(base_total)*100),2),"%")

print("Total %d" % base_total)
