from random import randrange
import time
import pyautogui

print("mouse x,mouse y,  tl  ,  tr  ,  bl  ,  br  ")

LPX=1664
RPX=1699
TPX=1002
BPX=1027

MIN_MS=750
MAX_MS=1250

while True:
    X, Y = pyautogui.position()
    TLPX = pyautogui.pixel(LPX, TPX)
    TRPX = pyautogui.pixel(RPX, TPX)
    BLPX = pyautogui.pixel(LPX, BPX)
    BRPX = pyautogui.pixel(RPX, BPX)
    TLGS = (TLPX[0] + TLPX[1] + TLPX[2]) / 3
    TRGS = (TRPX[0] + TRPX[1] + TRPX[2]) / 3
    BLGS = (BLPX[0] + BLPX[1] + BLPX[2]) / 3
    BRGS = (BRPX[0] + BRPX[1] + BRPX[2]) / 3
    print(f"{X:07.2f},{Y:07.2f},{TLGS:06.2f},{TRGS:06.2f},{BLGS:06.2f},{BRGS:06.2f}", end="\r")
    gs = (TLGS + TRGS + BLGS + BRGS) / 4
    if gs > 100:
        time.sleep(randrange(MIN_MS,MAX_MS)/1000.0)
        pyautogui.moveTo(
            randrange(LPX,RPX),
            randrange(TPX,BPX),
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
