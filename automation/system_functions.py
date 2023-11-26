import os
import time

def key_event(x):
    os.system(f'adb shell input keyevent {x}')
    time.sleep(1.5)

def swipe_up():
    os.system('adb shell input swipe 500 700 500 500 100')
    time.sleep(1.5)

def swipe_down():
    os.system('adb shell input swipe 500 500 500 700 100')
    time.sleep(1.5)

def tap(x, y):
    os.system(f'adb shell input tap {x} {y}')
    time.sleep(1.5)