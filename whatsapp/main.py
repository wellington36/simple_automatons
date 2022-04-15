import pyautogui as pt
import pyperclip
import random
from time import sleep
from pynput.keyboard import Controller
from requests import post

sleep(2)

position1 = pt.locateOnScreen("whatsapp/paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

# Gets message
def get_msg():
    global x, y
    keyboard = Controller()

    position = pt.locateOnScreen("whatsapp/paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x, y, duration=0.1)
    pt.moveTo(x + 40, y - 40, duration=.5) # Verify the window possition
    pt.tripleClick()
    pt.rightClick()
    keyboard.press('c')
    whatsapp_msg = str(pyperclip.paste())
    print("Message received: " + whatsapp_msg)


    return whatsapp_msg


# Posts
def post_response(msg):
    global x, y

    position = pt.locateOnScreen("whatsapp/paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(msg, interval=.05)

    pt.typewrite("\n", interval=.01)


# Processes response
def processes_response(msg: str) -> str:
    rnumber = random.randint(0, 3)

    if "?" in str(msg).lower():
        return "Eh uma pergunta."
    else:
        if rnumber == 0:
            return "Ok"
        elif rnumber == 1:
            return "Claro"
        else:
            return "Sem problemas"


# Check for new messagens
def check_for_new_msg():
    pt.moveTo(x+50,y-35, duration=.5)


check_for_new_msg()
