#!/usr/bin/python4.7
"""
file: getDatLyrics.py
author: @github.com/eatDatCode
"""
import sys
import re

from support.search import Google
from support.plugins import Plugin

def getDatLyrics(query):
    """Make the query using search module and print lyrics using plugins modlue."""

    # Look search module and get the link on the top of the results
    search_google = Google(query)
    link = search_google.get_links()

    # If the lyrics not found ,print error or fetch the lyrics
    if link == None:
        print("""
                Sorry, that lyrics wasn't found!
                Please leave comment as the song name
                We will try to get more plugins to fetch that song too.
              """)
    else:
        # Request the lyrics usgin plugins module
        lyrics_request = Plugin(link[0])
        url = (re.compile(r'(http(s)?://)?(www.)?([a-z,0-9]+)(.[a-z]+)').search(link[0]))
        provider = url.group(4)+url.group(5)
        lyrics = lyrics_request.get_lyrics(link[1])
        print(lyrics)
        print("Provided by:%s" % provider)

if __name__=='__main__':
    """Main method take arguments from command line and form a query."""

    if len(sys.argv) < 2:
        print("Please type the songs name after the program.")
        exit()

    query = 'https://www.google.com/search?q=lyrics+of+' + '+'.join(sys.argv[1:])
    getDatLyrics(query)
