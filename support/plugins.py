"""
file: plugins.py
author: @github.com/eatDatCode
"""

import re

from support.webpage import Request

class Plugin():
    """Request a plugin method and return the lyrics in printed form."""

    def __init__(self,link):
        """Constructor of the class Pluggin."""
        self.link = link

    def get_lyrics(self,index):
        """Fetch lyrics according to the index of the website."""

        self.index = index

        if self.index == 1:                                                 #gneius.com
            request_lyrics = Request(self.link,'.lyrics')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 2:                                               #azlyrics.com
            request_lyrics = Request(self.link,'.col-xs-12 div')
            lyrics = request_lyrics.get_tags()
            return (lyrics[6].get_text())

        elif self.index == 3:                                              #ilikelyrics.com
            request_lyrics = Request(self.link,'.lyric')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 4:                                               #lyricsmode.com
            request_lyrics = Request(self.link,'#lyrics-text')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 5:                                               #metrolyrics.com
            request_lyrics = Request(self.link,'.verse')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += lyrics[i].get_text()
            return (lyrical)

        elif self.index == 6:                                               #elyrics.com
            request_lyrics = Request(self.link,'#inlyr')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 7:                                               #stlyrics.com
            request_lyrics = Request(self.link,'#page')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 8:                                               #lyricsmasti.com
            request_lyrics = Request(self.link,'.col-md-7')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 9:                                               #rekhta.org
            request_lyrics = Request(self.link,'.c')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += lyrics[i].get_text()
                lyrical += '\n'
            return (lyrical)

        elif self.index == 10:                                              #songlyrics.com
            request_lyrics = Request(self.link,'#songLyricsDiv')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 11:                                              #bollywoodlyrics.com
            request_lyrics = Request(self.link,'.lyric-text pre')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 12:                                              #sweetlyrics.com
            request_lyrics = Request(self.link,'.lyrics_full_text')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 13:                                              #lyricsmotion.com
            request_lyrics = Request(self.link,'.col-sm-6 p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)-2):
                lyrical += re.compile(r'<br/>').sub('\n',str(lyrics[i]))
            lyrical = re.compile(r'<(/)?p>').sub('\n',lyrical)
            return (lyrical)

        elif self.index == 14:                                              #lyricsbd.com
            self.link = re.compile(r'%.+').sub('',self.link)
            request_lyrics = Request(self.link,'.print-lyrics')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 15:                                              #gdn8.com
            request_lyrics = Request(self.link,'.MsoPlainText span')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += lyrics[i].get_text()
            return (lyrical)

        elif self.index == 16:                                              #bengalilyrics24.blogspot.com
            request_lyrics = Request(self.link,'#lv')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 17:                                              #songlyrics24.com
            request_lyrics = Request(self.link,'.entry-content p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)-2):
                lyrical += lyrics[i+2].get_text()
            lyrical = re.compile(r']').sub(']\n',lyrical)
            return (lyrical)

        elif self.index == 18:                                              #bongsonglyrics.com
            request_lyrics = Request(self.link,'.MsoNormal span')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            print(len(lyrics))
            for i in range(len(lyrics)):
                lyrical += lyrics[i].get_text()
            return (lyrical)

        elif self.index == 19:                                              #lyrics71.net
            request_lyrics = Request(self.link,'.print-lyrics p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += str(lyrics[i])
            lyrical = re.compile(r'</p>').sub('\n',lyrical)
            lyrical = re.compile(r'<(/)?(p)?(br/)?(strong)?>').sub('',lyrical)
            return (lyrical)

        elif self.index == 20:                                              #lyrics.wikia.com
            request_lyrics = Request(self.link,'.lyricbox')
            lyrics = request_lyrics.get_tags()
            lyrical = re.compile(r'<br/>').sub('\n',str(lyrics[0]))
            lyrical = re.compile(r'<(/)?div(.+)?>').sub('',lyrical)
            return lyrical

        elif self.index == 21:                                              #lyricsmania.com
            request_lyrics = Request(self.link,'.lyrics-body')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 22:                                              #allthelyrics.com
            request_lyrics = Request(self.link,'.content-text-inner p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += str(lyrics[i])
            lyrical = re.compile(r'(<p>)|(<br/>)').sub('',lyrical)
            lyrical = re.compile(r'</p>').sub('\n',lyrical)
            return (lyrical)

        elif self.index == 23:                                              #lyricsoff.com
            request_lyrics = Request(self.link,'.final-lyrics p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += lyrics[i].get_text()
            lyrical = re.compile(r'google.+').sub('',lyrical)
            return (lyrical)

        elif self.index == 24:                                              #glamsham.com
            request_lyrics = Request(self.link,'.col-sm-6 font')
            lyrics = request_lyrics.get_tags()
            lyrical = re.compile(r'<br/>').sub('\n',str(lyrics[0]))
            lyrical = re.compile(r'<(/)?font(.+)?>').sub('',lyrical)
            return (lyrical)

        elif self.index == 25:                                              #lyricsmint.com
            request_lyrics = Request(self.link,'#lyric p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += str(lyrics[i])
            lyrical = re.compile(r'<br/>|</p>').sub('\n',lyrical)
            lyrical = re.compile(r'<p>|(<a.+>.+</a>)').sub('',lyrical)
            return (lyrical)

        elif self.index == 26:                                              #brainly.in
            request_lyrics = Request(self.link,'.brn-answer__text div')
            lyrics = request_lyrics.get_tags()
            lyrical = re.compile(r'<br/>').sub('\n',str(lyrics[0]))
            lyrical = re.compile(r'<(/)?div(.+)?>').sub('',lyrical)
            return (lyrical)

        elif self.index == 27:                                               #lyricsfreak.com
            request_lyrics = Request(self.link,'#content')
            lyrics = request_lyrics.get_tags()
            lyrical = str(lyrics[0])
            lyrical = re.compile(r'<br/><br/>').sub('\n',lyrical)
            lyrical = re.compile(r'<br/>|<(/)?div(.+)?>').sub('',lyrical)
            return (lyrical)

        elif self.index == 28:                                              #lyricsbogie.com
            request_lyrics = Request(self.link,'#lyricsDiv p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += str(lyrics[i])
            lyrical = re.compile(r'<br/>|<p>').sub('',lyrical)
            lyrical = re.compile(r'</p>').sub('\n',lyrical)
            return (lyrical)

        elif self.index == 29:                                             #paroles-musique.com
            request_lyrics = Request(self.link,'#lyrics')
            lyrics = request_lyrics.get_tags()
            return (lyrics[0].get_text())

        elif self.index == 30:                                              #lyricgram.com
            request_lyrics = Request(self.link,'.lyric-text blockquote')
            lyrics = request_lyrics.get_tags()
            lyrical = str(lyrics[0])
            lyrical = re.compile(r'<(/)?blockquote>|<(/)?p>').sub('',lyrical)
            lyrical = re.compile(r'<br/>').sub('\n',lyrical)
            return (lyrical)

        elif self.index == 31:                                                #oldhindilyrics.com
            request_lyrics = Request(self.link,'.entry-content p')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += str(lyrics[i])
            lyrical = re.compile(r'<p>|<br/>|<u>').sub('',lyrical)
            lyrical = re.compile(r'</p>|</u>').sub('\n',lyrical)
            return (lyrical)

        elif self.index == 32:                                              #geetmanjusha.com
            request_lyrics = Request(self.link,'.entity-description pre')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range():
                lyrical += lyrics[i].get_text()
            return (lyrical)

        elif self.index == 33:                                                #lyricstranslate.com
            request_lyrics = Request(self.link,'.song-node-text div.par')
            lyrics = request_lyrics.get_tags()
            lyrical = ''
            for i in range(len(lyrics)):
                lyrical += lyrics[i].get_text()
            return (lyrical)


        """Add your plugins from here on."""
        #elif self.index == :                                                #plugin_site_name
        #    request_lyrics = Request(self.link,'')
        #    lyrics = request_lyrics.get_tags()
        #    lyrical = ''
        #    return (lyrical)

