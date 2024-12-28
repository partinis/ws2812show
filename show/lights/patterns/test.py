from .pattern import Pattern
import time
import math
from .putil import *

NUM_PIXELS = 300

class Test(Pattern):

    @classmethod
    def get_id(self):
        return 0

    @classmethod
    def update(self, strip, state):
        color = get_random_color()
        color1 = get_random_color()
        color2 = get_random_color()
        iterations=100
        size = 5
        delay=0.1
        gravity=0.8
        center = random.randint(0, NUM_PIXELS - 1)
        center = random.randint(0, NUM_PIXELS - 1)
        for radius in range(1, 10):
            for i in range(NUM_PIXELS):
                distance = abs(center - i)
                if distance == radius:
                    strip.setPixelColor(i, (0, 0, 255))  # Blue ripple
                else:
                    strip.setPixelColor(i, (0, 0, 0))  # Off
            strip.show()
            time.sleep(delay)