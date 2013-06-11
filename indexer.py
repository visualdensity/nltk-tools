#!/usr/bin/env python
# encoding: utf-8
"""
indexer.py

Script crawls through content/* items and generates
an index of labels for contents in a cats.txt file. This
is created for use with NLTK's corpus library.
"""
import os

index_file    = 'cats.txt'
training_path = 'training/'

if not os.path.exists(training_path):
    print "Input path " + training_path + " not found."
    sys.exit()

if not os.access( index_file, os.W_OK):
    print "Target file " + training_path + " could not be created. Permission issue?"
    sys.exit()

f = open(index_file, 'w')

for top, dirs, files in os.walk(training_path):
    for nm in files:
        filepath = os.path.join(top, nm)
        filepath_chunk = filepath.split("/")
        cat_line = filepath + " " + filepath_chunk[-2] + "\n"

        f.write(cat_line)
f.closed 
