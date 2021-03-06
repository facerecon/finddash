import cv2
import time
import json
import cognitive_face as CF
import pyglet
from gtts import gTTS
import os

subscription_key = '8777598e1ed6400b819e1ca46ce59f19'
CF.Key.set(subscription_key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

target_img = CF.face.detect("target.jpg")[0]

name = input("Please enter the person's name you want to find: ")

while True:
    cam = cv2.VideoCapture(0)
    retval, frame = cam.read()
    cv2.imwrite('base.jpg', frame)
    #cv2.imshow("preview", frame)
    faces = CF.face.detect("base.jpg")
    print(faces)
    for face in faces:
        result = CF.face.verify(target_img['faceId'], face['faceId'])
        if result['confidence'] >= 0.5:
            music = pyglet.resource.media("trumpet.wav")
            music.play()

            text_to_display = "Please follow me " + name

            tts = gTTS(text=text_to_display, lang='en')
            os.system('rm good.mp3')
            tts.save("waitup.mp3")
            os.system("open waitup.mp3")
            # pyglet.app.run()

        print(result)
    cam.release()
    time.sleep(3)

