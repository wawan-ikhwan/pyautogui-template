'''
This script contains a function to simulate typing into any input form using the pyautogui library.

Functions:
----------
input_example_com():
  Simulates typing "example.com" into an input form, such as the address bar of a web browser.
  This function can be adapted to type into any input form.
'''

import logging
from logging import Logger
from time import sleep
import pyautogui as pag

logger: Logger = logging.getLogger(__name__)

def go_to_example_site():
  '''
  Opens a new tab in Firefox and types "example.com" into the address bar.
  '''
  try:
    logger.info('Typing "example.com" into the address bar...')
    pag.typewrite('example.com')  # Type "example.com"
    sleep(1)
    pag.press('enter')  # Press the enter key
    sleep(1)
    logger.info('Typed "example.com" into the address bar.')
  except Exception as e:
    logger.error('Failed to type into the address bar: %s', str(e))

def go_to_my_github():
  '''
  Opens a new tab in Firefox and types "github.com/wawan-ikhwan" into the address bar.
  '''
  try:
    logger.info('Typing "github.com/wawan-ikhwan" into the address bar...')
    pag.typewrite('github.com/wawan-ikhwan')  # Type "github.com/wawan-ikhwan"
    sleep(1)
    pag.press('enter')  # Press the enter key
    sleep(3) # wait site loaded
    logger.info('Typed "github.com/wawan-ikhwan" into the address bar.')
  except Exception as e:
    logger.error('Failed to type into the address bar: %s', str(e))

def click_ctrl_f():
  '''
  Presses the Ctrl+F key combination.
  '''
  pag.hotkey('ctrl', 'f')  # Press the ctrl+f key

def write_message_to_follow_my_github():
  '''
  Write message to follow my github with ctrl+f in a tab of browser and type message at there.
  '''
  try:
    logger.info('Typing pleasure message...')
    sleep(1)
    pag.typewrite('Follow me on github please :)')  # Type "Follow me on github"
    sleep(1)
    logger.info('Typed "Follow me on github" into the ctrl+f.')
  except Exception as e:
    logger.error('Failed to type into ctrl+f: %s', str(e))
