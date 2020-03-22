# youtube-downloader
Python program to download videos from youtube using pytube module

ALGORITHM:

#import pytube
#store user input of youtube url into URL variable
#parse the url and store the expression into video variable
#define youtube variable - call the video variable and have it stream
#invoke youtube.download function and specify where you want to store the downloaded video

Note:

Upon execution, if you come across error "ImportError: cannot import name 'quote' from 'pytube.compat'", follow this :

Go to the pytube python packge file in the machine (C:\Users\USER\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pytube)
Open compat.py
  Under elif PY3 module, add the below code:

elif PY3:
    from urllib import request
    from urllib.parse import quote, urlencode, parse_qsl, unquote
    from urllib.request import urlopen
