import os
from pynput.keyboard import Key, Controller
import time
import random
from pykeyboard import PyKeyboard

move_keylist = ['w','a','s','d']
action_keylist = ['1','2','3','4','5','6','7','8','9']
min_time = 8*60
max_time = 14*60

key = PyKeyboard()

while(True):
    #Press movement keys
    i = 0
    for i in range(random.randint(2,7)):
        key_choice = random.choice(move_keylist)
        key.press_key(key_choice)
        time.sleep(random.randint(1,4))
        key.release_key(key_choice)
    time.sleep(5)
    #press action key
    i = 0
    for i in range(random.randint(2,6)):
        key_choice = random.choice(action_keylist)
        key.press_key(key_choice)
        time.sleep(random.randint(1,2))
        key.release_key(key_choice)
    #wait some minutes
    time.sleep(random.randint(min_time,max_time))
