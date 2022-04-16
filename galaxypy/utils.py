import pyautogui as pt
from time import sleep
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller

def check_pos():
    while True:
        posXY = pt.position()
        print(posXY, pt.pixel(posXY[0], posXY[1]))

        sleep(1)

        if posXY[0] == 0:
            break

        for m in get_monitors():
            print(str(m))

#check_pos()