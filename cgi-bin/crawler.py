#!/home/nischal/magic_sauce/python/iredditcrawler/env/bin/python3
import requests
import re

#request json data from reddit
subreddit = "Eyebleach"
url = 'https://www.reddit.com/r/%s/top.json?sort=top&limit=20' % subreddit
r =requests.get(url, headers={'User-agent': 'iredditcrawler 0.1'})

#headers
print("Content-Type: text/html\n")
print()

try:
    children = r.json()['data']['children']
    print("<center>")
    for child in children:
        childUrl = child['data']['url']
        title = child['data']['title']
        if len( re.findall(r'gifv',childUrl) ) > 0:
            print("""
                    (gif)<br>
                    <video class="preview" preload="auto" autoplay="autoplay" muted="muted" loop="loop"">
                        <source src="%s" type="video/mp4">
                    </video>
                    <br>
                    %s
                    """ % (re.sub(r'gifv',r'mp4',childUrl),title) )
        else:
            print("""
                    (image)<br>
                    <img src="%s" style="max-height:500px"> 
                    <br>
                    %s
                    """ % (childUrl,title) )
        print("<br><hr>")
    print("</center>")
except Exception as e:
    print(e)
r.close()

