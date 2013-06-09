NYTimes API Wrapper
===================

Before you begin, please head over to http://developer.nytimes.com 
and get yourself a set of API keys. 


Articles API (v2)
-----------------

For the Articles package to work, you'll need the Articles API, then 
do the following:

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


Resources
---------

  * http://developer.nytimes.com/docs/read/article_search_api_v2
