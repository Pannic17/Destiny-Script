import sys
import time
from random import random, randint

import pydirectinput


def terminate(signum, frame):
    sys.exit()


if __name__ == '__main__':
    time.sleep(3)

    for i in range(1000):
        pydirectinput.click()
        time.sleep(random() * 1)
        pydirectinput.click()
        time.sleep(random() * 1)
        pydirectinput.press("a")