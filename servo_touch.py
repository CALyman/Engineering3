# importing necessary libraries
import board
import neopixel
import time
import pulseio
import random
import touchio
from adafruit_motor import servo

#defining variables for the r, g, b values for the built-in led
#on the board
i = 0
r = 0
g = 0
b = 0
x = 5
#defining "dot" as a neopixel object
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
pwm = pulseio.PWMOut(board.A3, duty_cycle= 2**15, frequency=50)

my_servo = servo.Servo(pwm)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)


while True:
    if touch_A1.value and not touch_A2.value:
        if i < 180:
            i+=5
        else:
            i = 180
        my_servo.angle = i
        dot.fill((255, 0, 0))
        time.sleep(0.01)
        print("A1 touched")

    if touch_A2.value and not touch_A1.value:
        if i > 0:
            i-=5
        else:
            i = 0
        my_servo.angle = i
        dot.fill((0, 255, 0))
        time.sleep(0.01)
        print("A2 touched")

    if touch_A1.value and touch_A2.value:
        dot.fill((0,0,255))
        i += x
        if i > 180 or i < 0:
            x *= -1
            i += x
        my_servo.angle = i
        time.sleep(0.01)

    print(i)