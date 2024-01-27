'''
This module contains a function to capture screenshots using the pyautogui library. 
It also includes a utility to hide and show a windows label during the screenshot process.

Imports:
- sleep from time: Used to pause the execution of the program
- pyautogui as pag: Used to take screenshots
- Image from PIL: Used to represent the screenshot
- WINDOWS_LABEL from utilities.windows_debug_on_screen: Used to hide and show a windows label
'''

from time import sleep
import pyautogui as pag
from PIL import Image
from utilities.windows_debug_on_screen import WINDOWS_LABEL

def get_screenshot():
  '''
  Captures a screenshot of the current screen. If a windows label is present, 
  it hides the label, takes the screenshot, and then shows the label again.

  Returns:
    Image: The captured screenshot.
  '''
  if WINDOWS_LABEL is not None:
    WINDOWS_LABEL.hide_label()
    sleep(1)
    screenshot: Image = pag.screenshot()
    WINDOWS_LABEL.show_label()
    return screenshot
  else:
    return pag.screenshot()