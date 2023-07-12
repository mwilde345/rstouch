
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
from multiprocessing import Process

pi = pigpio.pi()

MAIN_NUM_GPIO = 18
MAIN_MIN_WIDTH = 500
MAIN_MAX_WIDTH = 610
MAIN_MIN_SEC = float(sys.argv[1])
MAIN_RAN_1 = float(sys.argv[2])
MAIN_RAN_2 = float(sys.argv[3])
pi.set_mode(MAIN_NUM_GPIO, pigpio.OUTPUT)
pi.set_PWM_frequency(MAIN_NUM_GPIO, 50)


EXTRA_NUM_GPIO = 12
EXTRA_MIN_WIDTH = 630
EXTRA_MAX_WIDTH = 500
EXTRA_MIN_SEC = float(sys.argv[4])
EXTRA_RAN_1 = float(sys.argv[5])
EXTRA_RAN_2 = float(sys.argv[6])
pi.set_mode(EXTRA_NUM_GPIO, pigpio.OUTPUT)
pi.set_PWM_frequency(EXTRA_NUM_GPIO, 50)


def loop_main():
  while True:
    try:
      pi.set_servo_pulsewidth(MAIN_NUM_GPIO, MAIN_MIN_WIDTH)
      time.sleep(0.1)
      pi.set_servo_pulsewidth(MAIN_NUM_GPIO, MAIN_MAX_WIDTH)
      time.sleep(MAIN_MIN_SEC)
      time.sleep(random.uniform(MAIN_RAN_1,MAIN_RAN_2))
    except KeyboardInterrupt:
      print('got interrupt main')
      break

def loop_extra():
  while True:
    try:
      pi.set_servo_pulsewidth(EXTRA_NUM_GPIO, EXTRA_MIN_WIDTH)
      time.sleep(0.1)
      pi.set_servo_pulsewidth(EXTRA_NUM_GPIO, EXTRA_MAX_WIDTH)
      time.sleep(EXTRA_MIN_SEC)
      time.sleep(random.uniform(EXTRA_RAN_1,EXTRA_RAN_2))
    except KeyboardInterrupt:
      print('got interrupt extra')
      break


p_main = Process(target=loop_main)
p_extra = Process(target=loop_extra)
try:
  p_main.start()
  p_extra.start()
  p_main.join()
  p_extra.join()
except KeyboardInterrupt:
  p_main.terminate()
  p_extra.terminate()
  print("\nTidying up")
  pi.set_servo_pulsewidth(EXTRA_NUM_GPIO, 0)
  pi.set_PWM_dutycycle(EXTRA_NUM_GPIO, 0)
  pi.set_PWM_frequency(EXTRA_NUM_GPIO, 0)
  pi.stop()
