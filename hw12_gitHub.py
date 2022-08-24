#coding:utf-8
import smtplib  #匯入smtplib
from email.mime.multipart import MIMEMultipart #匯入MIMEMultipart
from email.mime.text import MIMEText #匯入MIMEText，製作文字內文並附加到容器中
from email.mime.base import MIMEBase #匯入MIMEBase，用於承載附檔並附加到容器中
from email import encoders #匯入encoders，用於附檔編碼
import datetime #匯入datetime
import tkinter
import random   #匯入random


"""
*****************************副程式****************************************
Send():開始寄信
【ctmBtn按下時】
    customReceiver():輸入收件人名稱及信箱
    【enterBtn按下時】
        getName():回傳收件人信箱並寄信
【cphBtn按下時】
    cphReceiver():將收件人名稱設為"老師",及email位址設為""並開始寄信(Send())
【pllBtn按下時】
    pllReceiver():將收件人名稱設為"助教",及email位址設為""並開始寄信(Send())
"""
def Send():

    #組合郵件內容
    mail = MIMEMultipart()      # mail作為郵件內容的容器
    mail['From'] = "my name"     #寄信者的暱稱
    mail['To'] = reName         #rename為收件人的名稱
    mail['Subject'] = "Christmas Greeting Card" #郵件的主旨


    #郵件內文
    content = 'Hi,%s:\n'%mail['To'] #content為'Hi,{收件者名稱}'
    deltaDate = datetime.date(2019,12,25)-datetime.date.today() #距離聖誕節的時間
    if deltaDate.days > 0:  #若距離聖誕節的日期數 > 0
        content +='離聖誕節還有%d天,祝您聖誕快樂!'%deltaDate.days    #content增加'離聖誕節還有{距離的天數}天,祝您聖誕快樂!'
    elif deltaDate.days == 0:   #若距離聖誕節的日期數 == 0
        content +='今天是聖誕節耶!!!祝您聖誕快樂!'%deltaDate.days    #content增加'今天是聖誕節耶!!!祝您聖誕快樂!'
    else:
        content += '過了聖誕節!代表這一年即將結束，準備迎接全新的一年!Fighting!'    #content增加'過了聖誕節!代表這一年即將結束，準備迎接全新的一年!Fighting!'
    mail.attach(MIMEText(content,"plain","utf-8"))  #將郵件內文(content)加到mail中

    #從三件附件中隨機選兩個加入
    attachList = ["XmasSnow.gif","Xmas.txt","XmasLight.gif"]   #附件列表(attachList)
    random.shuffle(attachList)  #洗牌attachList
    #將附件列表(attachList)的前兩項附加到mail中
    i = 0
    while(i < 2):
        with open(attachList[i], "rb") as file:
            Base = MIMEBase('application', "octet-stream")
            fileContent=file.read()
            Base.set_payload(fileContent)
        encoders.encode_base64(Base)
        Base.add_header('Content-Disposition','attachment',filename=attachList[i])
        mail.attach(Base)
        i+=1


    smtPort = smtplib.SMTP("smtp.gmail.com",587)    #建立SMTP安全連線
    smtPort.starttls()  #啟動TLS加密模式
    smtPort.ehlo()  # 向郵件主機註冊身份
    smtPort.login('senderEmail@mail.nknu.edu.tw', 'emailPwd') #登入信箱
    smtPort.sendmail('senderEmail@mail.nknu.edu.tw',to, mail.as_string()) #寄信
    smtPort.quit()  #關閉郵件主機連線


def customReceiver():   #自訂收件人
    global toEntry,enterBtn,nameEntry,textName,textAdd  #設定全域變數(GUI): toEntry,enterBtn,nameEntry,textName,textAdd
    textName = tkinter.Label(text="收件人的名稱:",fg = "brown",font=("微軟正黑體",15),background='#c5e5ea',anchor='nw')#建立內容為"收件人的名稱"的標籤
    textName.pack() #放置textName
    nameEntry = tkinter.Entry() #輸入欄nameEntry:"收件人的名稱"
    nameEntry.pack()    #放置=nameEntry
    textAdd = tkinter.Label(text="收件人的信箱:",fg = "brown",font=("微軟正黑體",15),background='#c5e5ea',anchor='nw') #建立內容為"收件人的信箱"的標籤
    textAdd.pack() #放置textAdd
    toEntry = tkinter.Entry()   #輸入欄toEntry:"收件人的信箱"
    toEntry.pack()  #放置toEntry
    enterBtn = tkinter.Button(text="Enter",command=getName) #按鈕enterBtn被按下時，執行getName()
    enterBtn.pack() #放置enterBtn

def getName():
    global toEntry,enterBtn,nameEntry,textName,textAdd  #設定全域變數(GUI): toEntry,enterBtn,nameEntry,textName,textAdd
    global to,reName    #設定全域變數to,reName
    to = toEntry.get()  #設定to為toEntry裡的字串
    reName = nameEntry.get()    #設定reName為nameEntry裡的字串
    toEntry.pack_forget()   #將toEntry隱藏
    nameEntry.pack_forget() #將nameEntry隱藏
    enterBtn.pack_forget()  #將enterBtn隱藏
    textName.pack_forget()  #將textName隱藏
    textAdd.pack_forget()   #將textAdd隱藏
    Send()  #執行Send()

def cphReceiver():
    global to,reName    #設定全域變數to,reName
    to ='xxx@gmail.com'    #設定to為老師的email位址'apacph@gmail.com' 
    reName = '老師'   #設定reName為"老師"
    Send()  #執行Send()

def pllReceiver():
    global to,reName  #設定全域變數to,reName
    reName = '助教'   #設定reName為"助教"
    to ='xxx@mail.nknu.edu.tw'    #設定to為助教的email位址
    Send()  #執行Send()


#######################主程式:建立GUI###################################

capitalWin = tkinter.Tk()   #建立主視窗

capitalWin.title("Christmas Greeting Card")   #主視窗的標題


capitalWin.geometry("400x300")  #主視窗的大小
capitalWin.config(background='#c5e5ea') #主視窗的背景顏色


#標籤
Text = tkinter.Label(text="選擇收件人:",fg = "brown",font=("微軟正黑體",15),background='#c5e5ea',anchor='nw') #建立內容為"選擇收件人:"的標籤
Text.pack() #放置Text

#按鈕
cphBtn =tkinter.Button(text="CPH",command=cphReceiver)   #建立文字內容為"CPH"的按鈕，命令執行cphReceiver()
cphBtn.pack()  #放置

pllBtn =tkinter.Button(text="助教",command=pllReceiver)   #建立文字內容為"助教"的按鈕，命令執行pllReceiver()
pllBtn.pack()  #放置
custom = 0
ctmBtn =tkinter.Button(text="其他(自訂)",command=customReceiver)   #建立文字內容為"其他(自訂)"的按鈕，命令執行customReceiver()
ctmBtn.pack()  #放置

capitalWin.mainloop()  #常駐主視窗


