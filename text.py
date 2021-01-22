#import os
#print(os.listdir())
#print(os.listdir("D:\\"))
#f = open("test1.txt", "r")
#print(f.read())
# tài liệu tham khảo
# https://pypi.org/project/pyttsx3/
# https://www.youtube.com/watch?v=wVboOz_O8rE&t=1361s
# https://pypi.org/project/SpeechRecognition/
# https://pypi.org/project/gTTS/
# https://codelearn.io/sharing/lam-tro-ly-ao-tieng-viet-bot-siri-p2
# https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.engine
# https://openweathermap.org/api#current
# https://stackoverrun.com/vi/q/281749
# https://pypi.org/project/googletrans/

import speech_recognition as noi # thư viện speech_recognition đổi thành noi cho dễ ghi :))
from datetime import date,time # thư viện ngày tháng thời gian
from gtts import gTTS # thư viện nói giọng google -->pip install gTTS link:https://pythonprogramminglanguage.com/text-to-speech/
import os  # xử lý file tệp hệ thống
import time # thư viện thời gian 
import requests
import pyttsx3,os
robot = noi.Recognizer() # biến tự đặt
with noi.Microphone() as mic: 
    print(" chào Hoàng Bạn cần gì")
    audio = robot.listen(mic) #biến tự đặt

    print("loading...")
    try: 
        you = robot.recognize_google(audio,language='vi-VN')
    except:
        you="mời bạn thử lại"
        print("Hoang: " + you)
    
    elif "thời tiết" in you:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=DaNang&APPID=85cedb588bf04ea4df4d757ddeaadff2').json()
        thoitiet = r['weather'][0]['description']
        print('description: ',thoitiet)
        tts = gTTS(text =thoitiet,lang='vi')
        tts.save("test5.mp3")
        os.system("test5.mp3")    
        continue    
    tts = gTTS(text =you,lang='vi')
    tts.save("test5.mp3")
    os.system("test5.mp3")
"""
import array as mang
gio=["giờ","bây giờ là mấy giờ","mấy giờ rồi"]
you="mấy giờ rồi"
if you in gio:
    print("cc")
"""

