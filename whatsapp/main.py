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
    pt.moveTo(x+50,y-35, duration=1)

    while True:
        #Continuously checks for green dot and new msg
        try:
            position = pt.locateOnScreen("whatsapp/unread.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(1)
        except(Exception):
            print("No new other msg")

        print(pt.pixel(pt.position()[0], pt.position()[1]))
        print((x, y), pt.pixel(x, y))
        if pt.pixelMatchesColor(int(x), int(y), (47, 59, 67), tolerance=10):
            print("is_white")
            processed_message = processes_response(get_msg())
            post_response(processed_message)
        else:
            print("No new messages yet...")
        sleep(5)


check_for_new_msg()
