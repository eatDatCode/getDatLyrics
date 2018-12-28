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
                'ilikelyrics':3,
                'metrolyrics':5,
                'lyricsmode':4,
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
                'lyrics':20,       # Originally it's lyrics.wikia , since there's no lyrics.com Let's keep it simple
                'lyricsmania':21,
                'allthelyrics':22,
                'lyricsoff':23,
                'glamsham':24,
                'lyricsmint':25,
                'brainly':26,
                'lyricsfreak':27,
                'lyricsbogie':28,
                'paroles-musique':29,
                'lyricsgram':30,
                'oldhindilyrics':31,
                'geetmanjusha':32,
                'lyricstranslate':33
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

        url = ''
        for i in range(l):

            #Try this it will give lyrics from different website by using random choice of links
            #link = self.ancors[random.randint(0,l-1)].get('href')
            link = self.ancors[i].get('href')

            # Google stores ancors href in a special way
            url = re.compile(r'.+http').sub('http',link)
            url = re.compile(r'&.+').sub('',url)
            url = re.compile(r'%2F').sub('/',url)  # %2F means a /
            url = re.compile(r'%3A').sub(':',url)  # %3A means a :
            url  = re.compile(r'%2').sub('+',url)  # %2 means a +

            address = re.compile(r'http(s)?://(www.)?([a-z,0-9,-]+)(.[a-z,0-9]+)').search(url)
            domain = address.group(3)

            if domain in plugin_sites.keys():
                return [url,plugin_sites[domain]]
                break
        if url == '':
            return None
