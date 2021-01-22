import speech_recognition as noi1 # thư viện speech_recognition ở đây mình đặt tên biến là noi
from datetime import date,time # thư viện ngày tháng thời gian
from gtts import gTTS # thư viện nói giọng google -->pip install gTTS link:https://pythonprogramminglanguage.com/text-to-speech/
#pip install gTTS-token --upgrade google vừa update pb mới
#https://www.calculateme.com/temperature/kelvin-to-celsius/272
#https://hongtin.net/ai/huong-dan-get-api-thoi-tiet-voi-python-lam-man-du-bao-thoi-tiet-tren-win-va-ubuntu/
# python -m pip install --upgrade gtts-token
# python -m pip install --upgrade gtts
import os  # xử lý file tệp hệ thống
import time # thư viện thời gian 
import webbrowser # thư viện webbrowser
import requests
from youtube_search import YoutubeSearch # thư viện youtube_search -->pip install youtube-search
from  tkinter import * # thư viện đồ họa
from PIL import ImageTk,Image
import webbrowser
import pyautogui # thư viện auto click keyboard
from pydub import AudioSegment # thư viện âm thanh
from pydub.playback import play # thư viện âm thanh
from playsound import playsound
import random
#code có tham khảo trên 1 vài trang ytb!!!
random123 = ['bạn đẹp như ma', 'bạn xinh như thúy kiều', 'so beautiful', 'bạn rất đẹp còn đẹp như gì thì tôi không biết',
 'đẹp nghiêng nước nghiêng thành']


def thoitiet1(a):
    bien="trời trong lành không khí thoáng đãng, phù hợp cho việc đi chơi"
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
    elif "clear sky" in a:
        bien="trời hôm nay thoáng đãng không khí trong lành"
    return bien

def noi(you):
    tts= gTTS(text =you,lang='vi')
    tts.save("audio.mp3")
    tts=playsound('audio.mp3')
    tts=os.remove("audio.mp3")

def bien():
    robot = noi1.Recognizer()
    with noi1.Microphone() as mic:
        print(" chào Hoàng Bạn cần gì")
        
        audio = robot.listen(mic,phrase_time_limit=5) #biến tự đặt
        
        print("loading...")
        try: 
            you = robot.recognize_google(audio,language='vi-VN')
            return you.lower()
        except:
            you="mời bạn thử lại"
            return 0
            
def time_day(text):
    if "giờ" in text:
        time1 = time.localtime()
        you = time.strftime("%I:%M:%S %p", time1) 
        noi(you)
    elif "ngày" in text:
        today = str(date.today())
        you=today
        noi("ngày"+you)
    else:
        noi("tôi không nghe rõ mời bạn thử lại")

def tongthongnuocmy(text):
    if "tổng thống của nước mỹ là ai" in text:
        noi("Job Biden")
    elif "chủ tịch nước của việt nam là ai" in text:
        noi("Nguyễn Phú Trọng")

def thoitiet():
    noi("Bạn muốn xem thời tiết ở khu vực nào")
    r = "http://api.openweathermap.org/data/2.5/weather?"
    city = bien()
    print(city)
    if not city:
        pass
    api_key = "b4750c6250a078a943b3bf920bb138a0"
    call_url = r + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        nhiet_do = city_res["temp"]
        do_am = city_res["humidity"]
        wthr = data["weather"]
        thoi_tiet = wthr[0]["description"]
        content = f"""
        {thoitiet1(thoi_tiet)}
        Nhiệt độ trung bình {nhiet_do}  độ C
        Độ ẩm {do_am}%"""
        noi(content)
    else:
        noi("xin lỗi tôi không tìm thấy địa chỉ của bạn")

def mo_app(text):
    if "google" in text:
        noi("Mở Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    elif "garena" in text:
        noi("Mở Garena")
        os.startfile("C:\Program Files (x86)\Garena\Garena\Garena.exe")
    elif "c" in text:
        noi("Mở C Plus Plus")
        os.startfile("C:\Program Files (x86)\Dev-Cpp\devcpp.exe") 
    elif "zalo" in text:
        noi("Mở Zalo")
        os.startfile("C:Users\luuki\AppData\Local\Programs\Zalo\Zalo.exe")
        
def google_search():
    noi("bạn cần tìm kiếm gì")
    a=bien()
    url = f"https://www.google.com/search?q={a}"
    webbrowser.open(url)

def calculate():
    noi("mời bạn nhập phép tính")
    a=bien()
    url = f"https://www.google.com/search?q={a}"
    webbrowser.open(url)

def camera():
    noi('mở camera')
    pyautogui.hotkey('win')
    pyautogui.write('camera')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.hotkey('enter')

def maps():
    noi('vị trí của bạn')
    pyautogui.hotkey('win')
    pyautogui.write('m')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl','y')
    time.sleep(2)
    pyautogui.hotkey('ctrl','home')
    time.sleep(5)
def chucodau():
    pyautogui.hotkey('ctrl','shift')

def write():
    noi("mời bạn nhập ghi chú")
    a=bien()
    pyautogui.write(a)
    time.sleep(2)
    
def luu():
    pyautogui.hotkey('ctrl','s')
    pyautogui.write(bien())
    pyautogui.hotkey('enter')

def note():
    noi('mở ghi chú')
    pyautogui.hotkey('win')
    pyautogui.write('n')
    time.sleep(1)
    pyautogui.hotkey('enter')


def tramxang():
    noi('các trạm xăng gần vị trí của bạn')
    webbrowser.open('https://www.google.com/search?q=tr%E1%BA%A1m%20x%C4%83ng')

def vietkey():
    noi('mở unikey')
    pyautogui.hotkey('win')
    pyautogui.write('U')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')

def alt_f4():
    pyautogui.hotkey('alt','f4')

def delate_page():
    pyautogui.hotkey('ctrl','w')

def demo():
    while True:       
        time.sleep(2.0)
        song = AudioSegment.from_wav("siri.wav")
        play(song)
        biennoi=bien()
        if "thời tiết" in biennoi:
            thoitiet()
        elif "tính toán" in biennoi:
            calculate()
        elif "tìm kiếm" in biennoi:
            google_search()
        elif "chụp hình" in biennoi:
            camera()
        elif "ghi chú" in biennoi:
            note()
        elif "tắt ứng dụng" in biennoi:
            alt_f4()
        elif "người yêu" in biennoi:
            noi('ca này hơi khó người ta có câu vạn sự tùy duyên còn duyên ở đâu thì tôi không biết')
        elif "vị trí" in biennoi:
            maps()
        elif "đẹp" in biennoi:
            noi(random.choice(random123))
        elif "buồn" in biennoi:
            noi("không sao đã có tôi đây rồi")
        elif "bạn là ai" in biennoi:
            noi("tôi là một trợ lý có thể giúp bạn giải đáp các thắc mắc và thư giãn đầu óc")
        elif "bạn có người yêu chưa" in biennoi:
            noi("tôi chưa có người yêu tôi còn sợ ế đây này")
        elif "tắt một trang" in biennoi:
            delate_page()
        elif "trạm xăng" in biennoi:
            tramxang()
        elif "unikey" in biennoi:
            vietkey()
        elif "chữ có dấu" in biennoi:
            chucodau()
        elif "lưu" in biennoi:
            luu()
        elif "viết" in biennoi:
            write()  
        elif "giờ" in biennoi or "ngày" in biennoi:
            time_day(biennoi)
        elif "tổng thống" in biennoi or "chủ tịch" in biennoi:
            tongthongnuocmy(biennoi)
        elif "google" in biennoi or "garena" in biennoi or "zalo" in biennoi:
            mo_app(biennoi)
        elif "tạm biệt" in biennoi or "dừng lại" in biennoi or "kết thúc" in biennoi:
            noi("hẹn gặp lại")
            break;

window = Tk() #biến tự đặt tên là window
window.title("TRỢ LÝ ẢO")
window.iconbitmap('c:/fbchatbox/fileico/dhspdn_1.ico')

def delete():
    mytext.delete(1.0,END)  

anh4=ImageTk.PhotoImage(Image.open("dhspdn.jpg"))
anh5=ImageTk.PhotoImage(Image.open("anh.jpg"))
# list_array_anh=[anh,anh1,anh2,anh3,anh4,anh5]
labelanh=Label(image=anh4).place(width=200,height=200,x=300,y=0)
labelanh=Label(image=anh5).place(width=500,height=250,x=0,y=200)
window.geometry("550x660+400+50")
window.configure(bg="#585858")
window.resizable(width=False,height=False) #kích thức sẽ không thay đổi
label1=Label(window,text="TRỢ LÝ ẢO",fg="lightblue",font="Times 20 bold",bg="#585858").grid(row=0,column=0,stick=E,ipady=12)
label2=Label(window,text="Đồ án cuối kỳ LƯU KIM HOÀNG 18CNTT4",fg="black",font="Times 12 bold",bg="#585858").grid(row=1,column=0,stick=W,ipady=15)
label3=Label(window,text="Giáo viên hướng dẫn : VŨ THỊ TRÀ",fg="black",font="Times 14 bold",bg="#585858").grid(row=2,column=0,stick=W,ipady=10)
mytext=Text(window,height=100, width=100)
mytext.place(width=400,height=50,x=50,y=460)
mytext.insert(INSERT,"Bot: "+'Chào Hoàng bạn cần gì'+"\n")
button2=Button(window,text="Exit",font="Times 14 bold",command=window.destroy,background="gray").place(width=100,height=50,x=100,y=520)
button1=Button(window,text="Xóa",font="Times 14 bold",command=delete,fg="black",background="gray",).place(width=100,height=50,x=200,y=520)
button1=Button(window,text="Mic",font="Times 14 bold",command=demo,fg="black",background="gray",).place(width=100,height=50,x=300,y=520)
window.update();
window.mainloop()