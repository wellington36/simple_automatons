import pyautogui as pt
import pyperclip
import random
from time import sleep
from pynput.keyboard import Controller

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

    pt.moveTo(x, y, duration=0.05)
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
    pt.typewrite(msg, interval=.01)

    pt.typewrite("\n", interval=.01)


#post_response(get_msg())
n = 1

while True:
    post_response('Test bot number ' + str(n))
    n+=1

