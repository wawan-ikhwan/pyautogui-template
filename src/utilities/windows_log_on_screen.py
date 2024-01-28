'''
This module provides a class for creating a debug screen on Windows platform using
tkinter, win32api, win32con, and pywintypes.
'''

import platform
from collections import deque
import tkinter as Tkinter
import win32api
import win32con
import pywintypes
import logging

class WindowsScreenLogger:
  '''
  A class used to create a debug screen on Windows platform.

  ...

  Attributes
  ----------
  text : tkinter.Text
      a tkinter text that is used to display the debug screen

  Methods
  -------
  hide_text():
      Hides the tkinter text.
  '''
  def __init__(self):
    '''
    Constructs all the necessary attributes for the WindowsDebugScreen object.

    ...

    Attributes
    ----------
    text : tkinter.Text
        a tkinter text that is used to display the debug screen
    '''
    text = Tkinter.Text(font=('Consolas', 12), bg='#222222', borderwidth=0, width=512)
    text.tag_configure(logging.DEBUG, foreground='cyan')
    text.tag_configure(logging.INFO, foreground='lime')
    text.tag_configure(logging.WARNING, foreground='gold')
    text.tag_configure(logging.ERROR, foreground='tomato')
    text.tag_configure(logging.CRITICAL, foreground='red')

    text.master.overrideredirect(True)
    text.master.geometry("+20+20")
    text.master.lift()
    text.master.wm_attributes("-topmost", True)
    text.master.wm_attributes("-disabled", True)
    text.master.wm_attributes("-transparentcolor", "#222222")

    h_window = pywintypes.HANDLE(int(text.master.frame(), 16))
    ex_style: int = (
      # win32con.WS_EX_COMPOSITED |
      win32con.WS_EX_LAYERED |
      win32con.WS_EX_NOACTIVATE |
      win32con.WS_EX_TOPMOST |
      win32con.WS_EX_TRANSPARENT
    )
    win32api.SetWindowLong(h_window, win32con.GWL_EXSTYLE, ex_style)

    text.pack()
    self.text = text
    self.text_lines = deque(maxlen=10)

  def hide_text(self):
    '''
    Hides the tkinter text.
    '''
    self.text.master.withdraw()
    self.text.master.update()

  def show_text(self):
    '''
    Makes the tkinter text visible if it was previously hidden.
    '''
    self.text.master.deiconify()
    self.text.master.update()

  def append_text(self, new_text, log_level=logging.DEBUG):
    '''
    Appends the new text to the text displayed on the tkinter text.

    Parameters
    ----------
    new_text : str
      The new text to be appended to the text.
    '''
    self.text_lines.append((f'{new_text}\n', log_level))
    self.update_text()

  def update_text(self):
    '''
    Update the text in the log window.

    This method clears the existing text in the log window and inserts new text
    based on the `text_lines` attribute. It then updates the log window to
    reflect the changes.

    Parameters:
      None

    Returns:
      None
    '''
    self.text.delete('1.0', 'end')
    for text, log_level in self.text_lines:
      self.text.insert('end', text, log_level)
    self.text.master.update()

if platform.system() == 'Windows':
  WINDOWS_LOGGER = WindowsScreenLogger()
else:
  WINDOWS_LOGGER = None
  