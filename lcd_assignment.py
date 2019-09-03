# importing necessary libraries
import board
#import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode


# defining variables for the r, g, b values for the built-in led
# on the board

button_alt = DigitalInOut(board.D6)
button_alt.direction = Direction.INPUT
button_alt.pull = Pull.UP

button_ud = DigitalInOut(board.D5)
button_ud.direction = Direction.INPUT
button_ud.pull = Pull.UP

button_res = DigitalInOut(board.D4)
button_res.direction = Direction.INPUT
button_res.pull = Pull.UP

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

mods = [1, 2, 5, 10, -1, -2, -5, -10]

num = 0
m = 0
mod = mods[m]

toggle1 = 0
toggle2 = 0

while True:

    lcd.set_cursor_pos(0,0)
    lcd.print("Number: " + str(num))
    lcd.set_cursor_pos(1,0)
    lcd.print("Modif.: " + str(mod))

    if not button_alt.value and toggle1 == 0:
        toggle1 = 1
        x = len(str(num))
        num += mod
        y = len(str(num))
        if x > y or y > x:
            lcd.clear()
        if num >= 1000:
            num = 999
            lcd.set_cursor_pos(0,11)
            lcd.print(" MAX ")
        elif num <= -1000:
            num = -999
            lcd.set_cursor_pos(0,12)
            lcd.print(" MIN")

    if button_alt.value:
        toggle1 = 0

    if not button_ud.value and toggle2 = 0:
        toggle2 = 1
        m += 1
        if m <= 7:
            mod = mods[m]
        else:
            m = 0
            mod = mods[m]
        lcd.clear()

    if button_ud.value:
        toggle2 = 0

    if not button_res.value:
        lcd.clear()
        lcd.print("  Resetting...")
        num = 0
        m = 0
        mod = mods[m]
        time.sleep(.5)
        lcd.clear()