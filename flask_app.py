from flask import Flask, Response
import requests
import re

app = Flask(__name__)

@app.route('/')
def home():
    #request json data from reddit
    subreddit = "Eyebleach"
    url = 'https://www.reddit.com/r/%s/top.json?sort=top&limit=20' % subreddit
    r =requests.get(url, headers={'User-agent': 'iredditcrawler 0.1'})

    html = "";
    try:
        children = r.json()['data']['children']

        html += "<center>"
        for child in children:
            childUrl = child['data']['url']
            title = child['data']['title']
            if len( re.findall(r'gifv',childUrl) ) > 0:
                html += ("""
                        (gif)<br>
                        <video class="preview" preload="auto" autoplay="autoplay" muted="muted" loop="loop"">
                            <source src="%s" type="video/mp4">
                        </video>
                        <br>
                        %s
                        """ % (re.sub(r'gifv',r'mp4',childUrl),title) )
            else:
               html +=  ("""
                        (image)<br>
                        <img src="%s" style="max-height:500px"> 
                        <br>
                        %s
                        """ % (childUrl,title) )
            html += ("<br><hr>")
        html += ("</center>")
    except Exception as e:
        html += (e)
    r.close()
    return Response(html, mimetype="text/html")

