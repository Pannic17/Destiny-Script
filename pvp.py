import time
from random import random, randint

import pydirectinput

if __name__ == '__main__':
    time.sleep(3)

    for i in range(100):
        pydirectinput.press("w")
        # pydirectinput.mouseDown()
        pydirectinput.moveTo(120, 70)
        time.sleep(1)
        pydirectinput.press("w")
        time.sleep(1)
        pydirectinput.moveTo(960, 690)
        # pydirectinput.mouseUp()
        time.sleep(1)
        pydirectinput.press("c")
        pydirectinput.press("w")
        time.sleep(1)
        pydirectinput.press("w")
        time.sleep(1)
        pydirectinput.press("w")
        # pydirectinput.mouseDown()
        pydirectinput.press("w")
        time.sleep(1)
        pydirectinput.moveTo(randint(200, 1000), randint(60, 690))
        time.sleep(1)
        pydirectinput.press("w")
        pydirectinput.press("v")
        time.sleep(1)
        pydirectinput.press("w")
        # pydirectinput.mouseUp()
        time.sleep(1)
