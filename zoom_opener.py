"""
Created by Jan Schiffeler on 06.11.20
jan.schiffeler[at]gmail.com

Changed by



Python 3.
Library version:


"""

import argparse
import webbrowser
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from time import sleep

parser = argparse.ArgumentParser(description='Open Zoom link')
parser.add_argument('-l', '--link', required=True, default=10, help='link to meeting')
parser.add_argument('-p', '--password', required=True, default=10, help='password')
args = vars(parser.parse_args())

link = args['link']
password = args['password']

keyboard = KeyboardController()
mouse = MouseController()

webbrowser.open(link)

sleep(1)

keyboard.press(Key.enter)
sleep(0.2)
keyboard.release(Key.enter)

sleep(0.5)

keyboard.press(Key.cmd)
sleep(0.2)
keyboard.press(Key.tab)
sleep(0.5)
keyboard.release(Key.cmd)
keyboard.release(Key.tab)

sleep(0.3)

mouse.position = (900, 500)
sleep(0.1)
mouse.press(Button.left)
mouse.release(Button.left)

keyboard.type(password)
sleep(0.1)
keyboard.press(Key.enter)
sleep(0.1)
keyboard.release(Key.enter)
