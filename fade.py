# importing necessary libraries
import board
import neopixel
import pulseio
import time

#defining variables for the r, g, b values for the built-in led
#on the board
r = 255
g = 0
b = 255

#defining variable "i" for later usage
i = 0

#defining "dot" as a neopixel object and "led" as a pulseio object
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)

while True:
    #adding 1 to i everytime the loop runs, used for the fading sequence
    i += 1
    #resets i to 0 if it passes 100 so as not to tell the pulseio to go
    #to a value past its maximum
    if i > 100:
        i = 0

    if i < 50: #Fading up code
        led.duty_cycle = int(i * 2 * 65535 / 100)  # Up * 65535 / 100
    else: #Fading down code
        led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down * 65535 / 100
    time.sleep(0.025)

    #making dot the color determined by r, g, and b
    #dot.fill((r, g, b))