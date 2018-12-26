# getDatLyrics
Use this python script to pull lyrics off from more than 25 websites, this script scraps lyrics from top lyrics provider site, some of them are right protected so use this for personal use only.

For those who uses Windows , please setup your python environment before using this script.

# Requirements
First make sure you have requirements met before using it, type the next line to ensure 
1) Python version == 3.7

$ pip install -r requirements.txt

# How to setup

$ git clone https://github.com/eatDatCode/getDatLyrics.git

$ cd getDatLyrics

$ sudo chmod a+x getDatLyrics.py

$ sudo mv ./getDatLyrics.py lyrics

$ sudo mv lyrics /usr/bin/

$ sudo mv support/ /usr/lib/python3.7/site-packages/

# Congrats !

If no error occured in those steps then opent a terminal from anywhere and type

$ lyrics (your song)

e.g $ lyrics yesterday

# Guidelines for better result :

i) Try not to make too many spelling mistakes in typing the song

ii) Try adding the singer of the song if the lyrics did't match as required

iii) For regional languages try adding the language after the song

e.g. $ lyrics ben cok sev turkish


# Need more plugins?

If you think your taste of songs is little unique and these plugins lyrics are not enough to get you that lyrics,
then please leave a comment.

Or if you want you can add a plugin for your favourite lyrical website.

Just do the following:

1) Go to support directory of the git repo and open search.py

2) Add the domain name of the site and give the index as value in the plugins_site dictionary

3) Go to plugins.py and add at the bottom of teh get_lyrics() method another elif condition and give the new index as condition
and add the details of the attributes and class where the lyrics is found in the website( Tips: Use mozilla developer tool to inspect the webpage)
