"""
file: search.py
author: @github.com/eatDatCode
This file make the query and returns the links of lyrics sites
"""

import sys
import re
import random

from support.webpage import Request

plugin_sites = {'genius':1,
                'azlyrics':2,
                'metrolyrics':3,
                'lyricsmode':4,
                'lyricsfreak':5,
                'elyrics':6,
                'stlyrics':7,
                'lyricsmasti':8,
                'rekhta':9,
                'songlyrics':10,
                'bollywoodlyrics':11,
                'sweetlyrics':12,
                'lyricsmotion':13,
                'lyricsbd':14,
                'gdn8':15,
                'bengalilyrics24':16,
                'songlyrics24':17,
                'bongsonglyrics':18,
                'lyrics71':19,
                'lyrics.wikia':20,       # one problem here is it will not come in use(lyrics.com will be searched instead)
                'lyricsmania':21,
                'allthelyrics':22,
                'lyricsoff':23,
                'glamsham':24,
                'lyricsmint':25,
                'brainly':26
               }

class Google(Request):
    """Try to find top sites that has the required lyrics in google.com"""

    def __init__(self,query):
        """Requests the query through requests module"""
        super().__init__(query,'.r a')
        self.ancors = self.get_tags()

    def get_links(self):
        """Check if the list self.sites has an available lyrical site
        to pull the lyrics from."""
        l = len(self.ancors)

        for i in range(l):

            #Try this it will give lyrics from different website by using random choice of links
            #link = self.ancors[random.randint(0,l-1)].get('href')

            link = self.ancors[i].get('href')
            regx = re.compile(r'=([a-z]+://)?(www.)?([a-z,0-9]+)(.+).sa=')
            match = regx.search(link)
            url = match.group()[1:-4]
            domain = match.group(3)

            if '%' in url:
                url = re.compile(r'%.+').sub('',url)
            if domain in plugin_sites.keys():
                return [url,plugin_sites[domain]]
                break
        if url == None:
            return None
