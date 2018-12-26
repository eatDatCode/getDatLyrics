"""
file: webpage.py
author: @github.com/eatDatCode
This acts as a module and request page and
,returns soup of source code
"""

import requests
from bs4 import BeautifulSoup

class Request():
    """Try and request a html page and returns a soup of source code"""

    def __init__(self,query,tag):
        """constructor of the class Request"""
        self.query = query
        self.tag = tag

    def get_tags(self):
        """
        Use the module requests to request a html page
        And use the bs4 module to beautify the webpage.
        """
        html = requests.get(self.query).text
        soup = BeautifulSoup(html,"lxml")
        tags = soup.select(self.tag)
        return tags
