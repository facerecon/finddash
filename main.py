from flask import Flask
import cognitive_face as CF

app = Flask(__name__)

subscription_key = '8777598e1ed6400b819e1ca46ce59f19'
CF.Key.set(subscription_key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)



@app.route("/")
def hello():
    faces = CF.face.detect("base1.jpg")

    return str(faces)


if __name__ == "__main__":
    hello()
