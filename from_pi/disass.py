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

MIN_WIDTH = 500
MAX_WIDTH = 610
min_sec = 65
ran_1 = 1.0
ran_2 = 3.0
# min_sec = float(sys.argv[1])
# ran_1 = float(sys.argv[2])
# ran_2 = float(sys.argv[3])

while True:

   try:

        pi.set_servo_pulsewidth(18, MIN_WIDTH)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(18, MAX_WIDTH)
        time.sleep(random.uniform(3,5))
        pi.set_servo_pulsewidth(18, MIN_WIDTH)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(18, MAX_WIDTH)
        time.sleep(min_sec)
        time.sleep(random.uniform(ran_1,ran_2))

   except KeyboardInterrupt:
      break

print("\nTidying up")
pi.set_servo_pulsewidth(18, 0)

pi.stop()
