import keyboard as kb
import time
import datetime as dt
import random as r
import datetime as dt

time.sleep(3)
h=dt.datetime.now().hour



words=['#ElvishIsTheWinner winner', '#ElvishIsTheBoss jeetega', '#ElvishIsTheBoss jeetegabhai', '#ElvishIsTheBoss win']
while True:
    n = dt.datetime.now().minute
    print(n)
    if n==4:

        w = r.choice(words)
        kb.write(w)
        time.sleep(0.5)
        kb.press_and_release('enter')