import platform
import pyautogui as pag
from PIL import Image
from time import sleep
from utilities.windows_debug_on_screen import windows_label

def get_screenshot():
  if windows_label is not None:
    windows_label.hide_label()
    sleep(1)
    screenshot: Image = pag.screenshot()
    windows_label.show_label()
    return screenshot
  else:
    return pag.screenshot()
  