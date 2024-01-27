'''
This module contains a function to open the terminal using keyboard shortcuts.

Imported Libraries:
- pyautogui : Used to automate keyboard and mouse events.

Functions:
- open_terminal() : Opens the terminal using a keyboard shortcut.
'''

import pyautogui as pag

def open_terminal():
  '''
  Function to open the terminal using a keyboard shortcut, LINUX ONLY.
  
  The function uses the pyautogui library to simulate the pressing of the 'ctrl', 'alt', and 't' keys simultaneously,
  which is a common shortcut to open the terminal in many Linux distributions.
  
  Parameters: None
  
  Returns: None
  '''
  pag.hotkey('ctrl', 'alt', 't')