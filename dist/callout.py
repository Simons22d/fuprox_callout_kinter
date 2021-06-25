import time
from flask import Flask,request
import os
import secrets
import platform
from pygame import mixer
import eventlet.wsgi
import pyttsx3


app = Flask(__name__)


@app.route("/callout",methods=["POST"])
def callout():
    phrase = request.json["phrase"]
    try:
        mixer.init()
        mixer.music.load('sounds/notification.mp3')
        mixer.music.play()
        time.sleep(0.5)
        engine = pyttsx3.init()
        import platform
        platform = platform.system()
        if platform == "Windows":
            engine.setProperty('rate', 130)
        else:
            engine.setProperty('rate', 180)
        engine.setProperty('volume', 1.0)
        engine.say(phrase)
        engine.runAndWait()
    except RuntimeError:
        pass
    return {"phrase": phrase}


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 9900)), app)
