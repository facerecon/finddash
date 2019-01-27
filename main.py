from flask import Flask
import requests

app = Flask(__name__)

subscription_key = '8777598e1ed6400b819e1ca46ce59f19'
assert subscription_key

img_data = open("base1.jpg", "rb").read()

emotion_recognition_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0"

header = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream"}

data = {'url': None}


@app.route("/")
def hello():
    # r = requests.get('https://api.github.com/')
    r = requests.post(emotion_recognition_url, headers=header, data=img_data)
    print(r)

    return r.json()
