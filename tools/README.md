Tools Package
=============
Just a collection of tools. Will continue to expand on this whenever
I have the time. Currently, you can do the following:

  1. Build index ala [NLTK corpora](http://nltk.org/nltk_data/)
  2. Use `tools.nytimes` wrapper to quickly build training data


Build Index
-----------
If you would like to build an index of path-to-file against a specific 
classification label, you can use the `indexer.py` right away:

    % python tools/indexer.py

Or if you're using it in your own script:

    from tools import *
    build_index('index_file.txt', 'training/data/folder')


NYTimes
-------
Please refer the [`nytimes/`](https://github.com/visualdensity/nltk-tools/tree/master/tools/nytimes) 
for more info.
