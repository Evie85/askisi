import time
import redis
from flask import Flask
from string import Template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<head>
   <title>Mysite</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Welcome to this window of the outside world! </h1>
    <p>Looking forward to the after Covid-19 era!</p>
    <p><a href="https://en.wikipedia.org/wiki/Manhattan">Manhattan</a> loading...</p>
    <a href="https://www.flickr.com/photos/zokuga/14615349406/">
        <img src="http://stash.compjour.org/assets/images/sunset.jpg" alt="it's a nice sunset">
    </a>
</body>
"""


