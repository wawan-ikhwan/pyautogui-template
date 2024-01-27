'''
This script contains functions to interact with Firefox using the pyautogui library.

Functions:
----------
open_new_tab_in_firefox():
  Opens a new tab in Firefox by simulating the 'ctrl' + 't' hotkey.

open_firefox_in_new_window():
  Opens a new Firefox window by simulating keyboard inputs to open the Run dialog,
  type the command to open a new Firefox window, and press Enter.
'''

import logging
from logging import Logger
from time import sleep
import pyautogui as pag

logger: Logger = logging.getLogger(__name__)

def open_new_tab():
  '''
  Opens a new tab in Firefox using a hotkey.
  '''
  try:
    logger.info('Opening a new tab in Firefox...')
    pag.hotkey('ctrl', 't')
    sleep(1)
    logger.info('New tab opened.')
  except Exception as e:
    logger.error('Failed to open a new tab in Firefox: %s', str(e))

def open_new_window():
  '''
  Opens a new Firefox window.

  This function simulates keyboard inputs to open the Run dialog, 
  type the command to open a new Firefox window, and press Enter.

  Parameters:
  -----------
  None

  Returns:
  --------
  None
  '''
  logger.info('Opening a new Firefox window...')
  # Press the hotkey to open the Run dialog
  pag.hotkey('win', 'r')
  sleep(1)  # Wait for the Run dialog to appear
  # Type "firefox -new-window" and press Enter
  pag.typewrite('firefox -new-window')
  pag.press('enter')
  sleep(1)  # Wait for Firefox to open
  logger.info('New Firefox window opened.')
