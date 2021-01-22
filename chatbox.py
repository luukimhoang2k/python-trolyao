import pyttsx3 #thư viện nói tiếng anh
import speech_recognition as noi # thư viện speech_recognition đổi thành noi cho dễ ghi :))
from datetime import date # thư viện ngày tháng thời gian
import time # thư viện thời gian
from gtts import gTTS # thư viện nói giọng google -->pip install gTTS link:https://pythonprogramminglanguage.com/text-to-speech/
import os

robot = noi.Recognizer() # biến tự đặt
with noi.Microphone() as mic: 
    print(" chào Hoàng Bạn cần gì")
    audio = robot.listen(mic) #biến tự đặts
    print("loading...")

    try: 
        you = robot.recognize_google(audio)
    except:
        you="try again !!!"
        print("Hoang: " + you)

    
    if you=="giờ":
        time1 = time.localtime()
        you = time.strftime("%I:%M:%S %p", time1)
        print("bot: ",you)
    elif you=="ngày":
        today = str(date.today())
        you=today
        print("bot: ",you)
    elif you=="tạm biệt":
        print("bot: good bye")
        tts = gTTS(text ="good bye see you again",lang='vi')
        tts.save("robot.mp3")
        os.system("robot.mp3")
    
    tts = gTTS(text =you,lang='vi')
    tts.save("robot.mp3")
    os.system("robot.mp3")
