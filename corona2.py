import requests
from bs4 import BeautifulSoup
from tkinter import *
from time import ctime
from plyer import notification
import threading
import time
from gtts import gTTS
import playsound



def test():
    sound1=gTTS(text="welcome In covid-19 updater",lang='en')
    f="helololo.mp3"
    sound1.save(f)
    playsound.playsound(f)
test()
def corono():
    url = "https://www.mygov.in/covid-19/"

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    page = requests.get(url, headers=headers)
    sou = BeautifulSoup(page.content, 'html.parser')
    active = sou.find("div", class_="info_label").get_text()
    print(active)

    active_count = sou.find("span", class_="icount").get_text()
    print(active_count)
    ac=Label(root,text=f"{active}:-{active_count}",font=f)
    ac.pack(fill=Y)



    discharge = sou.find("div", class_="iblock discharge").find("div", class_="iblock_text").find("div",
                                                                                                  class_="info_label").get_text()
    print(discharge)
    discharge_count = sou.find("div", class_="iblock discharge").find("span", class_="icount").get_text()
    print(discharge_count)
    dis=Label(root,text=f"{discharge}:-{discharge_count}",font=f)
    dis.pack(fill=Y)

    death = sou.find("div", class_="iblock death_case").find("div", class_="info_label").get_text()
    print(death)
    death_count = sou.find("div", class_="iblock death_case").find("span", class_="icount").get_text()
    print(death_count)
    de=Label(root,text=f"{death}:-{death_count}",font=f)
    de.pack()
    sound1 = gTTS(text=f"{active}   is{active_count}{discharge}   case   is  {discharge_count}{death}  case    is  {death_count} this are the cases   Thank You", lang='en')
    f1 = "hkelololo.mp3"
    sound1.save(f1)
    playsound.playsound(f1)


#text=f"{active}:-{active_count}\n{discharge}:-{discharge_count}\n{death}:-{death_count}"


def refresh():
    tk=Label(root,text=t,font=f).pack()
    tk1=Label(root,text="The New Update Is",font=f).pack()
    new=corono()
    root.update()
def noti():
    while True:
        notification.notify(
            title="BE UPDATE IN COVID-19",
            message="Check The cases",
            timeout=100,
            app_icon='c.ico'
        )
        time.sleep(30000)
root=Tk()
root.title("BE UPDATE IN COVID-19")
root.iconbitmap("c.ico")
root.configure(bg='white')
f=('arial',10,'bold')
ti=Label(text="BE UPDATE IN COVID-19",font=f).pack(fill=Y)
im=PhotoImage(file="covid-19ui.png")
li=Label(root,image=im).pack()

root.geometry("633x677")

b=Button(text="Check",font=f,command=corono,bg='red').pack()
b1=Button(text="Refresh",font=f,command=refresh,bg='green').pack()
t=ctime()
tl=Label(root,text=t,font=f).pack()
threading.Thread(target=noti).start()
root.mainloop()


