# importing necessary libraries
import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

pi = DigitalInOut(board.D6)
pi.direction = Direction.INPUT
pi.pull = Pull.UP

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

r = 255
g = 0
b = 0

toggle = True
time_toggle = True

current_time = 0

interrupts = 0

while True:
    dot.fill((r, g, b))

    if pi.value and toggle:
        interrupts += 1
        g = 255
        r = 0
        toggle = False

    if not pi.value:
        r = 255
        g = 0
        toggle = True

    if time_toggle:
        current_time = time.time()
        time_toggle=False
        lcd.print("Number of")
        lcd.set_cursor_pos(1,0)
        lcd.print("Interrupts: " + str(interrupts))

    if current_time == time.time()-4:
        time_toggle = True
        lcd.clear()
