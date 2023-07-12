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


NUM_GPIO = 18
pi = pigpio.pi()
pi.set_mode(NUM_GPIO, pigpio.OUTPUT)
pi.set_PWM_frequency(NUM_GPIO, 50)

MIN_WIDTH = 500
MAX_WIDTH = 610
min_sec = float(sys.argv[1])
ran_1 = float(sys.argv[2])
ran_2 = float(sys.argv[3])

while True:

   try:

        pi.set_servo_pulsewidth(NUM_GPIO, MIN_WIDTH)
        time.sleep(0.1)
        pi.set_servo_pulsewidth(NUM_GPIO, MAX_WIDTH)
        time.sleep(min_sec)
        time.sleep(random.uniform(ran_1,ran_2))

   except KeyboardInterrupt:
      break

print("\nTidying up")
pi.set_servo_pulsewidth(NUM_GPIO, 0)
pi.set_PWM_dutycycle(NUM_GPIO, 0)
pi.set_PWM_frequency(NUM_GPIO, 0)

pi.stop()
