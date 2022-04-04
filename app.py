from flask import Flask
from datetime import datetime

app = Flask(__name__)

request_tracker = {}


@app.route("/")
def base():
    request_time = int(datetime.now().timestamp())
    if request_time not in request_tracker.keys():
        request_tracker[request_time] = 1
    else:
        request_tracker[request_time] += 1

    return f'num times this second: {str(request_tracker[request_time])}'


@app.route("/tracker")
def tracker():
    return request_tracker
