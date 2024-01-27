'''
This script contains functions to interact with Microsoft Edge using the pyautogui library.

Functions:
----------
open_new_tab():
  Opens a new tab in Edge by simulating the 'ctrl' + 't' hotkey.

open_new_window():
  Opens a new Edge window by simulating keyboard inputs to open the Run dialog,
  type the command to open a new Edge window, and press Enter.
'''
import logging
from logging import Logger
from time import sleep
import pyautogui as pag

logger: Logger = logging.getLogger(__name__)

def open_new_tab():
  '''
  Opens a new tab in Edge.

  This function simulates the 'ctrl' + 't' hotkey to open a new tab in Edge.

  Parameters:
  -----------
  None

  Returns:
  --------
  None
  '''
  try:
    logger.debug('Opening a new tab in Edge...')
    pag.hotkey('ctrl', 't')
    sleep(1)
    logger.debug('New tab opened.')
  except Exception as e:
    logger.error('Failed to open a new tab in Edge: %s', str(e))

def open_new_window():
  '''
  Opens a new Edge window.

  This function simulates keyboard inputs to open the Run dialog,
  type the command to open a new Edge window, and press Enter.

  Parameters:
  -----------
  None

  Returns:
  --------
  None
  '''
  try:
    logger.debug('Opening a new Edge window...')
    # Press the hotkey to open the Run dialog
    pag.hotkey('win', 'r')
    sleep(1)  # Wait for the Run dialog to appear
    # Type "msedge -inprivate" and press Enter
    pag.typewrite('msedge')
    pag.press('enter')
    sleep(1)
    logger.debug('New Edge window opened.')
  except Exception as e:
    logger.error('Failed to open a new Edge window: %s', str(e))
