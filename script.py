import keyboard as keyboard
from pymouse import PyMouse
import pyautogui
import keyword
import pydirectinput
import time


def buy():
    pydirectinput.press("f1")

    time.sleep(1)

    for i in range(100):
        print('NO.' + str(i) + ' exchange')
        pydirectinput.click(900, 120)
        time.sleep(1)

    time.sleep(1)

    for i in range(24):
        print('NO.' + str(i) + ' purchase')
        pydirectinput.click(750, 120)
        time.sleep(1)


def iterate():
    for i in range(46):
        print('NO.' + str(i) + ' iteration')
        pydirectinput.click(600, 300)
        time.sleep(1)
        pydirectinput.click(240, 550)
        time.sleep(1)
        pydirectinput.click(1200, 550)
        time.sleep(1)

        for i in range(9):
            pydirectinput.moveTo(480, 580)
            pydirectinput.mouseDown(480, 580)
            time.sleep(3)
            pydirectinput.mouseUp(480, 580)

        pydirectinput.press("f1")
        time.sleep(0.5)
        pydirectinput.press("f1")

        time.sleep(1)

        pydirectinput.moveTo(900, 180)
        time.sleep(1)
        pydirectinput.moveTo(1000, 180)

        for i in range(9):
            pydirectinput.press("f")
            time.sleep(0.5)
            pydirectinput.keyDown("f")
            time.sleep(1)
            pydirectinput.keyDown("f")
            time.sleep(0.5)

        pydirectinput.press("a")
        time.sleep(0.5)
        pydirectinput.press("a")
        time.sleep(1)


def random():
    return random


if __name__ == '__main__':
    time.sleep(3)

    for i in range(1):

        time_start = time.time()

        iterate()
        buy()
        time.sleep(1)
        pydirectinput.press("f1")
        time.sleep(1)
        pydirectinput.press("a")
        time.sleep(1)
        pydirectinput.press("a")
        time.sleep(1)

        time_cost = time.time() - time_start

        print("#####################################")
        print("NO." + str(i) + "FINISHED  TIME::" + str(time_cost))
        print("#####################################")

    # mouse = PyMouse()
    # currPos = mouse.position()
    # time.sleep(2)
    # print(currPos)
    # mouse.click(900, 1300)
    # time.sleep(0.1)
    # mouse.click(500, 1700)
    # time.sleep(0.1)
    # mouse.click(1800, 1600)
    # time.sleep(0.1)
    #
    # for i in range(8):
    #     mouse.click(700, 1750)
    #     mouse.press(700, 1750)
    #     time.sleep(3)
    #     mouse.release(700, 1750)
