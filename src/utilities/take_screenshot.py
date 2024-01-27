'''
This module contains a function to capture screenshots using the pyautogui library. 
It also includes a utility to hide and show a windows label during the screenshot process.

Imports:
- sleep from time: Used to pause the execution of the program
- pyautogui as pag: Used to take screenshots
- Image from PIL: Used to represent the screenshot
- WINDOWS_LOGGER from utilities.WINDOWS_LOGGER_on_screen: Used to hide and show a windows label
'''

from time import sleep
import pyautogui as pag
from PIL import Image
from utilities.windows_log_on_screen import WINDOWS_LOGGER

def get_screenshot(delay_sec=0.25):
  '''
  Captures a screenshot of the current screen. If a windows label is present, 
  it hides the label, takes the screenshot, and then shows the label again.

  Returns:
    Image: The captured screenshot.
  '''
  if WINDOWS_LOGGER is not None:
    WINDOWS_LOGGER.hide_text()
    sleep(delay_sec)
    screenshot: Image = pag.screenshot()
    sleep(delay_sec)
    WINDOWS_LOGGER.show_text()
  else:
    screenshot: Image = pag.screenshot
  return screenshot
