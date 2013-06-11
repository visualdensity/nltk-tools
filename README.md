NLTK Tools
==========

A collection of tools that I'm building to help me with a little NLP project
using Python's [NLTK](http://nltk.org/) package. 

Currently, this repo allows you to build your own corpus in the format that
is inline with how the rest of the NLTK's corpora is structured. Things here 
will likely change as I add more tools.

Indexing
--------
Once you've imported the content, you can then generate an index, labelling each
content file with its context for training:

    % ./indexer.py

The above will generate `cats.txt` that contains a list of paths and its label
in the following format:

    content/health/0000 health
    content/health/0001 health
    content/business/0000 business
    content/business/0001 business
    content/business/0002 business
    ...

Note
----
  * Training data under `training/` is meant to be a sample only. 
  * Go to `tools/` folder for more info.

Resources
---------

  * http://nltk.org/
  * http://nltk.org/book/
  * http://www.ibm.com/developerworks/library/l-cpnltk/index.html
