#!/usr/bin/env python
# encoding: utf-8
"""
Articles.py

NYTimes.com provides developers with means for pulling in data. This 
is just a simple a wrapper around it. 

Usage:

    from nytimes import *
    nyt = Articles("{api_key}")
    nyt.max_pages(10) # pull up to 10 pages of data - there are 10 records per page
    nyt.get_by_newsdesk("technology", "content/nytimes/technology/")

For more info:
http://developer.nytimes.com/docs/read/article_search_api_v2

Todo:
  * Extract fl query configuration
  * Constructable query
"""

import urllib
import errno
import json
import os

class Articles:

    endpoint   = "http://api.nytimes.com/svc/search/v2/articlesearch.json"

    search_fl  = "fl=keywords,snippet,headline,news_desk"
    search_api = "api-key=%s"
    search_pg  = "page=%s"
    page_limit = 10

    search_q   = { 
                    'by_subject'  : "fq=subject:(\"%s\")", 
                    'by_newsdesk' : "fq=news_desk:(\"%s\")", 
                    'by_query'    : "q=%s"
                 }

    base_url   = ''
    search_url = ''


    def __init__(self, api_key):
        self.search_api = self.search_api % api_key
        self.base_url = self.endpoint + "?" + self.search_fl + "&" + self.search_api

    def search_by_newsdesk(self, string):
        self.search_url = self.base_url + "&" + self.search_q['by_newsdesk'] % string

    def search_by_subject(self, string):
        self.search_url = self.base_url + "&" + self.search_q['by_subject'] % string

    def search_by_query(self, string):
        self.search_url = self.base_url + "&" + self.search_q['by_query'] % string

    def get_query_url(self):
        return self.search_url

    def capture(self, path):
        count = 0
        for i in range(0, self.page_limit):
            content = self.get_data(self.search_url + "&" + self.search_pg % i)

            for item in content['response']['docs']:
                stanza   = self.build_stanza(item)
                filename = str(count).zfill(4)

                self.save_content(path, filename, stanza)
                count += 1

    def get_data(self, url):
        response = urllib.urlopen(url)
        content  = json.load(response)

        return content

    def build_stanza(self, item):
        stanza = ''
        if item['headline']['main']:
            stanza += item['headline']['main'].encode('utf-8').strip() + '\n'

        stanza += '\n' + item['snippet'].encode('utf-8').strip() + '\n'

        for keyword in item['keywords']:
            if keyword['name'] == 'subject':
                stanza += '\n' + keyword['name'].encode('utf-8').strip() + ':' + keyword['value'].encode('utf-8').strip() 

        return stanza

    def max_pages(self, page_limit):
        self.page_limit = int(page_limit)

    def save_content(self, path, filename, content):
        if not os.path.exists( path ):
            self.mkdir_p(path)

        filepath = path + '/' + filename

        f = open( filepath, 'w' )
        f.write(content)
        f.close()

    def mkdir_p(self, path):
        """
        Picked from here:
        http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
        """
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

