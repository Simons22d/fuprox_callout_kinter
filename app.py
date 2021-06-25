from flask import Flask
import eventlet.wsgi
from subprocess import call
import os

app = Flask(__name__)


@app.route("/start/callout",methods=["POST"])
def callout():
    call(["python",f"{os.path.join(os.getcwd(),'callout.py')}"])
    return {"phrase": "phrase"}


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 9999)), app)
