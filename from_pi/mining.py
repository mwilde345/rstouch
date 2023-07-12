#!/usr/bin/env python

# servo_demo.py
# 2016-10-07
# Public Domain

# servo_demo.py          # Send servo pulses to GPIO 4.
# servo_demo.py 23 24 25 # Send servo pulses to GPIO 23, 24, 25.

import sys
import time
import random
import pigpio

pi = pigpio.pi()

NUM_GPIO = 32

MIN_WIDTH = 1650
MAX_WIDTH = 2000

while True:

   try:

        pi.set_servo_pulsewidth(18, MIN_WIDTH)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(18, MAX_WIDTH)
        time.sleep(random.randrange(1,4))

   except KeyboardInterrupt:
      break

print("\nTidying up")
pi.set_servo_pulsewidth(18, 0)

pi.stop()

