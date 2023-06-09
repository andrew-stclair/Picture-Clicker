"""Module providing function to select a random number from a range."""
from random import randrange
import time
import datetime
import pyautogui

MIN_MS=750
MAX_MS=1250

print("Date/Time (ISO Format),Button X Position,Button Y Position")

while True:
    X, Y = pyautogui.position()
    location = pyautogui.locateCenterOnScreen('src/Button.png', region=(1581, 990, 250, 50))
    BTN_X, BTN_Y = (0, 0)
    if isinstance(location, tuple):
        BTN_X, BTN_Y = location
        print(f"{datetime.datetime.utcnow().isoformat()}Z,{BTN_X:4.0f},{BTN_Y:4.0f}")
        time.sleep(randrange(MIN_MS,MAX_MS)/1000.0)
        pyautogui.moveTo(
            randrange((BTN_X-(36/2)),(BTN_X+(36/2))),
            randrange((BTN_Y-(26/2)),(BTN_Y+(26/2))),
            duration=(randrange(MIN_MS,MAX_MS)/1000),
            tween=pyautogui.easeInOutQuad
        )
        pyautogui.click()
        pyautogui.moveTo(
            X,
            Y,
            duration=(randrange(MIN_MS,MAX_MS)/1000),
            tween=pyautogui.easeInOutQuad
        )
