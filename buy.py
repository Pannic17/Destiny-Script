import pydirectinput
import time


def halt():
    exit()


if __name__ == '__main__':

    time.sleep(3)

    for i in range(100):
        print('NO.' + str(i) + ' iteration')
        pydirectinput.click(900, 120)
        time.sleep(1)

    time.sleep(1)

    for i in range(24):
        print('NO.' + str(i) + ' iteration')
        pydirectinput.click(750, 120)
        time.sleep(1)