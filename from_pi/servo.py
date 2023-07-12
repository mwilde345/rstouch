from gpiozero import Servo
from time import sleep

servo = Servo(17)

servo.min()
sleep(1.5)
servo.mid()
sleep(1.5)
servo.max()
sleep(1.5)
