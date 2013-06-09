NLTK Tools
==========

A collection of tools that I'm building to help me with a little NLP project
using Python's [NLTK](http://nltk.org/) package. 

Currently, this repo allows you to build your own corpus in the format that
is inline with how the rest of the NLTK's corpora is structured. Things here 
will quite likely change as I add more tools.

Quick use
---------

Before you begin, please head over to http://developer.nytimes.com and
get yourself a set of API keys. For the Articles to work, you'll need the
Articles API. 

CD into the project directory:

    % git clone git@github.com:visualdensity/nltk-tools.git
    % cd nltk-tools

Then import the library and start grabbing content:

    % python
    Python 2.6.6 (r266:84292, Dec 26 2010, 22:31:48)
    [GCC 4.4.5] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from nytimes import *
    >>> a = Articles("7a8503faa92f5e01e3d6454ef3ab1626:10:67753100")
    >>> a.max_pages(5)
    >>> a.get_by_subject("fashion", "content/fashion")

Once you've imported the content, you can then generate an index, labelling each
content file with its context for training:

    % ./indexer.py


Resources
---------

  * http://nltk.org/
  * http://nltk.org/book/
  * http://www.ibm.com/developerworks/library/l-cpnltk/index.html
