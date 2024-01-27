'''
This script contains a function to simulate mouse of the scree using the pyautogui library.
'''

import logging
from logging import Logger
from time import sleep
import pyautogui as pag
from utilities.find_text import find_coordinates_text

logger: Logger = logging.getLogger(__name__)

def find_follow_button_in_my_github():
  '''
  This will finding the "Follow" button in my github.
  '''
  return find_coordinates_text('Follow', center=True)

def move_mouse_cursor_to_follow_button_in_my_github():
  '''
  Moving mouse cursor to the "Follow" button for appreciation of this project.
  '''
  try:
    logger.debug('Moving mouse cursor to the "Follow" button...')
    follow_button_coordinates = find_follow_button_in_my_github()
    pag.moveTo(follow_button_coordinates[0], follow_button_coordinates[1], duration=1)
    sleep(1)
    logger.debug('Mouse cursor moved to the "Follow" button.')
  except Exception as e:
    logger.error('Failed to move mouse cursor to the "Follow" button: %s', str(e))
