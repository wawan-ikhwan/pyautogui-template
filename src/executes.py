'''
This script contains a function to execute all commands in the commands folder.

Functions:
----------
execute_commands():
  Executes all commands in the commands folder.
'''

from commands import msedge
from commands import input_keyboard
from commands import input_mouse
from commands import terminal

def execute_commands_for_windows():
  '''
  Executes a series of commands for Windows platform.
  
  The commands include opening a new window and tab in Microsoft Edge,
  navigating to GitHub,
  moving the mouse cursor to the follow button on GitHub,
  activating the find function,
  and writing a message.
  '''
  msedge.open_new_window()
  msedge.open_new_tab()
  input_keyboard.go_to_my_github()
  input_mouse.move_mouse_cursor_to_follow_button_in_my_github()
  input_keyboard.click_ctrl_f()
  input_keyboard.write_message_to_follow_my_github()

def execute_commands_for_linux():
  '''
  Executes a series of commands for Linux platform.
  
  The commands include opening a terminal and writing a message.
  '''
  terminal.open_terminal()
  input_keyboard.write_message_to_follow_my_github()
