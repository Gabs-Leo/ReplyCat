import pyautogui as pt
from time import sleep
import pyperclip
import tkinter as tk

screenSize = pt.size()
screenWidth = screenSize[0]
screenHeight = screenSize[1]

def main():
    #sleep(3)
    checkNewMessages()

#Criando Interface para iniciar o bot
#Working on interface to start the bot
def windowStart():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("ReplyCat 1.0")
    root.iconbitmap("16x16.ico")
    root.mainloop()

#ZzzZzzZ
def sleepTime():
    pinZap = pt.locateOnScreen("whatsapp/pin_contact.png", confidence=.7)
    pt.moveTo(pinZap)
    pt.moveRel(-100, 0)
    pt.click()

    pinTG = pt.locateOnScreen("telegram/pin_contact.png", confidence=.7)
    pt.moveTo(pinTG)
    pt.moveRel(-100, 0)
    pt.click()

#Whatsapp
def getZapMessage():
    paperclip = pt.locateOnScreen("whatsapp/smiley_paperclip.png")
    pt.moveTo(paperclip, duration=.5)
    pt.moveRel(0, -70, duration=.5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    zapMessage = pyperclip.paste()
    return zapMessage
def answerZapMessage(message):
    paperclip = pt.locateOnScreen("whatsapp/smiley_paperclip.png")
    pt.moveTo(paperclip, duration=.5)
    pt.moveRel(200, 0, duration=.5)
    pt.click()
    if message == "hello":
        pt.typewrite("Hello :)")
    elif message == "default":
        pt.typewrite("Cool, bro!")
    sleepTime()

#Telegram
def getTGMessage():
    paperclip = pt.locateOnScreen("telegram/smiley.png")
    pt.moveTo(paperclip[0] - 10, paperclip[1]+ 10, duration=.5)
    pt.moveRel(60, -60, duration=.5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    tgMessage = pyperclip.paste()
    return tgMessage
def answerTGMessage(message):
    paperclip = pt.locateOnScreen("telegram/smiley.png")
    pt.moveTo(paperclip, duration=.5)
    pt.moveRel(200, 0, duration=.5)
    pt.click()
    if message == "hello":
        pt.typewrite("Hello :)")
    elif message == "default":
        pt.typewrite("Cool, bro!")
    sleepTime()

#Validação de Mensagens
#Message Validation
def validateMessage(message):
    if "hello" in str(message).lower():
        return "hello"
    else:
        return "default"

#Checagem contínua de novas mensagens
#Continuously checking for new messages
def checkNewMessages():
    while True:
        if pt.locateOnScreen("telegram/green_ball.png", confidence=.7) is not None:
            print("new message!")
            pt.moveTo(pt.locateOnScreen("telegram/green_ball.png", confidence=.7))
            pt.moveRel(-100, 0, duration=.5)
            pt.click()
            mousePosition = pt.position()
            if mousePosition[0] > screenWidth/2:
                print("new TG message!")
                answerTGMessage(validateMessage(getTGMessage()))
            else:
                print("new Zap message!")
                answerZapMessage(validateMessage(getZapMessage()))
        else:
            print("no new messages!")
            sleep(3)

main()