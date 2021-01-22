import speech_recognition as noi # thư viện speech_recognition ở đây mình đặt tên biến là noi
from datetime import date,time # thư viện ngày tháng thời gian
# thư viện nói giọng google -->pip install gTTS link:https://pythonprogramminglanguage.com/text-to-speech/
#pip install gTTS-token --upgrade google vừa update pb mới
import os  # xử lý file tệp hệ thống
import time # thư viện thời gian 
import webbrowser # thư viện webbrowser
import requests
from youtube_search import YoutubeSearch # thư viện youtube_search -->pip install youtube-search
from  tkinter import * # thư viện đồ họa
from gtts import gTTS

def thoitiet(a):
    bien="trời trong lành không khí thoáng đãng !!!"
    if "moderate rain" in a:
        bien="trời hôm nay mưa vừa "
    elif "heavy intensity rain" in a:
        bien="trời hôm nay mưa lớn"
    elif "broken clouds" in a:
        bien="trời hôm nay mây rải rác"
    elif "light rain" in a:
        bien="trời hôm nay mưa nhỏ"
    elif "overcast clouds" in a:
        bien="trời hôm nay u ám"
    return bien

while True:
    robot = noi.Recognizer() # biến tự đặt
    with noi.Microphone() as mic: 
        print(" chào Hoàng Bạn cần gì")
        audio = robot.listen(mic) #biến tự đặt
        print("loading...")
        try: 
            you = robot.recognize_google(audio,language='vi-VN')
        except:
            you="tôi không nghe rõ mời bạn thử lại"
        print("Hoang: " + you)
    
        if "giờ" in you:
            time1 = time.localtime()
            you = time.strftime("%I:%M:%S %p", time1)
            print("bot: ",you)
        elif "ngày" in you:
            today = str(date.today())
            you=today
            print("bot: ",you)
        elif "thời tiết" in you:
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=DaNang&APPID=85cedb588bf04ea4df4d757ddeaadff2').json()
            thoitiet1 = r['weather'][0]['description']
            print('description: ',thoitiet(thoitiet1))
            you=thoitiet(thoitiet1)
            # continue
        elif "Google" in you:
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        elif "Garena" in you:
            os.startfile("C:\Program Files (x86)\Garena\Garena\Garena.exe")
        elif "plus" in you:
            os.startfile("C:\Program Files (x86)\Dev-Cpp\devcpp.exe")
        elif "tạm biệt"in you:
            print("bot: hẹn gặp lại")
            tts = gTTS(text ="hẹn gặp lại",lang='vi')
            tts.save("robot.mp3")
            os.system("robot.mp3")
            break
        tts = gTTS(text =you,lang='vi')
        tts.save("robot.mp3")
        os.system("robot.mp3")
