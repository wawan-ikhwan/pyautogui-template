'''
This script contains a function to execute all commands in the commands folder.

Functions:
----------
execute_commands():
  Executes all commands in the commands folder.
'''

import logging
from logging import Logger
from commands import msedge
from commands import input_keyboard
from commands import input_mouse
from commands import terminal

logger: Logger = logging.getLogger(__name__)

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
  logger.info('open_new_window has been executed.')
  msedge.open_new_tab()
  logger.info('open_new_tab has been executed.')
  input_keyboard.go_to_my_github()
  logger.info('go_to_my_github has been executed.')
  input_mouse.move_mouse_cursor_to_follow_button_in_my_github()
  logger.info('move_mouse_cursor_to_follow_button_in_my_github has been executed.')
  input_keyboard.click_ctrl_f()
  logger.info('click_ctrl_f has been executed.')
  input_keyboard.write_message_to_follow_my_github()
  logger.info('write_message_to_follow_my_github has been executed.')

def execute_commands_for_linux():
  '''
  Executes a series of commands for Linux platform.
  
  The commands include opening a terminal and writing a message.
  '''
  terminal.open_terminal()
  input_keyboard.write_message_to_follow_my_github()
