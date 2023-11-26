import os
import time

from system_functions import *

def message_send():
    tap(1014, 1322)

def message_box():
    tap(275, 2210)

def type_text(s):
    os.system(f'adb shell input text {s}')
    time.sleep(1.5)

def first_user_search():
    tap(529, 408)
    time.sleep(1.5)

def start_chat():
    tap(384, 611)
    time.sleep(1.5)

def top_search_bar():
    tap(900, 150)
    time.sleep(1.5)

def exit_chat():
    for i in range(4):
        key_event(4)

def open_reddit():
    tap(429, 755)
    time.sleep(1.5)

def exit_reddit():
    for i in range(6):
        key_event(4)
    key_event(3)