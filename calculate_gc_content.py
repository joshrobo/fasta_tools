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

print("\nBase counts for file %s:" % sys.argv[1])
print("\nFull length: %dbp" % base_total)
print("Adenine (A) count: %d" % a_count), "which is",\
    round((float(a_count)/float(base_total)*100),1), "%"
print("Thymine (T) count: %d" % t_count), "which is",\
    round((float(t_count)/float(base_total)*100),1), "%"
print("Guanine (G) count: %d" % g_count), "which is",\
    round((float(g_count)/float(base_total)*100),1), "%"
print("Cytosine (C) count: %d" % c_count), "which is",\
    round((float(c_count)/float(base_total)*100),1), "%"
print "GC content is:",round((float(g_count+c_count)/float(base_total)*100),1),\
    "%\n"