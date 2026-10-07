import pydirectinput
import time


def halt():
    exit()


if __name__ == '__main__':
    start = time.time()

    while True:

        pydirectinput.moveTo(900+960, 540)
        pydirectinput.click()
        