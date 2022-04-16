import pyautogui as pt
from time import sleep
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller
from utils import *

for m in get_monitors():
    if m.is_primary :
        x_max = m.width
        y_max = m.height

sleep(3)

keyboard = Controller()

#check_pos()

# Pos nave x=684, y=602
# Pos blocks x=500, y=513 | x=680, y=451 | x=860, y=513

# 0 is <-
# 1 is |
# 2 is ->

def mov(n1:int, n2:int, n3:int) -> int:
    if n2 == 1:
        return 1
    else:
        if n1 == 0:
            return 0
        else:
            return 2

# Funcao chata
#def check():
#    if not pt.pixelMatchesColor(680, 480, (255, 255, 255)):
#        if pt.pixelMatchesColor(500, 500, (255, 255, 255)):
#            print('move to left')
#            keyboard.press(Key.left)
#            sleep(1)
#            keyboard.release(Key.left)
#
#        elif pt.pixelMatchesColor(860, 500, (255, 255, 255)):
#            print('move to right')
#            keyboard.press(Key.right)
#            sleep(1)
#            keyboard.release(Key.right)
        

while True: # 2411 | 12773
    pass