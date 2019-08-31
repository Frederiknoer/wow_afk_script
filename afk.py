import os
from pynput.keyboard import Key, Controller
import time
import random

key = Controller()

move_keylist = ['w','a','s','d']
action_keylist = ['1','2','3','4','5','6','7','8','9']
min_time = 8*60
max_time = 14*60


while(True):
    i = 0
    for i in range(100):
        key.press(random.choice(move_keylist))
        time.sleep(0.2)
    time.sleep(5)
    key.press(random.choice(action_keylist))
    time.sleep(5)
    key.press(random.choice(action_keylist))
    time.sleep(random.randint(min_time,max_time))
