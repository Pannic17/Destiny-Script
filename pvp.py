import sys
import time
from random import random, randint

import pydirectinput


def terminate(signum, frame):
    sys.exit()


if __name__ == '__main__':
    time.sleep(3)

    key_list = ["w", "q", "c", "v", "a", "s", "d", "space"]

    for i in range(1000):
        choice = randint(0, 9)
        if choice < 3:
            pydirectinput.press(key_list[randint(0, 7)])
        elif choice < 6:
            pydirectinput.moveTo(randint(200, 1400), randint(100, 700))
        elif choice < 9:
            pydirectinput.click()
        time.sleep(random() * 1)
