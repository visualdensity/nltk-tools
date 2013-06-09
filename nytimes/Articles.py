#!/usr/bin/env python
# encoding: utf-8
"""
Articles.py

NYTimes.com provides developers with means for pulling in data. Usage:

    nyt = Articles("f5907cf5d2a365222ae936e082230e81:5:67753100")
    nyt.get_by_newsdesk("technology", "content/nytimes/technology/")

Full with keywords:
http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=subject:("%s")&api-key=%s&fl=keywords,snippet,headline,news_desk&page=%s
"""

import urllib
import pprint
import errno
import json
import os

class Articles:

    endpoint   = "http://api.nytimes.com/svc/search/v2/articlesearch.json"

    search_fl  = "fl=keywords,snippet,headline,news_desk"
    search_api = "api-key=%s"
    search_pg  = "page=%s"
    search_fq  = { 'by_subject':"fq=subject:(\"%s\")", 'by_newsdesk': "fq=news_desk:(\"%s\")" }

    page_limit = 10

    def __init__(self, api_key):
        self.search_api = self.search_api % api_key

    def get_by_newsdesk(self, string, path):
        search_url = self.endpoint + "?" + self.search_fl + "&" + self.search_api + "&" + self.search_fq['by_newsdesk'] % string + "&" + self.search_pg
        self.capture(search_url, path)

    def get_by_subject(self, string, path):
        search_url = self.endpoint + "?" + self.search_fl + "&" + self.search_api + "&" + self.search_fq['by_subject'] % string + "&" + self.search_pg
        self.capture(search_url, path)

    def capture(self, search_url, path):
        if not os.path.exists( path ):
            self.mkdir_p(path)

        count = 0
        for i in range(0, self.page_limit):
            content = self.get_data(search_url % i)

            for item in content['response']['docs']:
                stanza   = self.build_stanza(item)
                filepath = path + '/' + str(count).zfill(4)

                self.save_content(filepath, stanza)
                count += 1

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

    def get_data(self, url):
        response = urllib.urlopen(url)
        content  = json.load(response)

        return content

    def save_content(self, path, content):
        f = open( path, 'w' )
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
