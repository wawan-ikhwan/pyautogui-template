'''
This module provides a class for creating a debug screen on Windows platform using
tkinter, win32api, win32con, and pywintypes.
'''

import platform
import tkinter as Tkinter
import win32api
import win32con
import pywintypes

class WindowsDebugScreen:
  '''
  A class used to create a debug screen on Windows platform.

  ...

  Attributes
  ----------
  label : tkinter.Label
      a tkinter label that is used to display the debug screen

  Methods
  -------
  hide_label():
      Hides the tkinter label.
  '''
  def __init__(self):
    '''
    Constructs all the necessary attributes for the WindowsDebugScreen object.

    ...

    Attributes
    ----------
    label : tkinter.Label
        a tkinter label that is used to display the debug screen
    '''
    label = Tkinter.Label(
      text='Debug',
      font=('Consolas', 12),
      fg='lime',
      bg='green',
      justify=Tkinter.LEFT
    )
    label.master.overrideredirect(True)
    label.master.geometry("+20+20")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "green")

    h_window = pywintypes.HANDLE(int(label.master.frame(), 16))
    ex_style: int = (
      win32con.WS_EX_COMPOSITED |
      win32con.WS_EX_LAYERED |
      win32con.WS_EX_NOACTIVATE |
      win32con.WS_EX_TOPMOST |
      win32con.WS_EX_TRANSPARENT
    )
    win32api.SetWindowLong(h_window, win32con.GWL_ex_style, ex_style)

    label.pack()
    self.label = label

  def hide_label(self):
    '''
    Hides the tkinter label.
    '''
    self.label.master.withdraw()
    self.label.master.update()

  def show_label(self):
    '''
    Makes the tkinter label visible if it was previously hidden.
    '''
    self.label.master.deiconify()
    self.label.master.update()

  def update_label(self, new_text):
    '''
    Updates the text displayed on the tkinter label.

    Parameters
    ----------
    new_text : str
      The new text to be displayed on the label.
    '''
    self.label.config(text=new_text)
    self.label.master.update()

if platform.system() == 'Windows':
  WINDOWS_LABEL = WindowsDebugScreen()
else:
  WINDOWS_LABEL = None
  