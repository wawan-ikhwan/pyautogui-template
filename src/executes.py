'''
This script contains a function to execute all commands in the commands folder.

Functions:
----------
execute_commands():
  Executes all commands in the commands folder.
'''

import platform
import logging
from logging import Logger
from commands import msedge
from commands import input_keyboard
from commands import input_mouse
from commands import terminal

logger: Logger = logging.getLogger(__name__)

def execute_commands():
  '''
  Execute all commands in the commands folder.
  '''
  current_platform: str = platform.system()
  logger.info('Current platform detected: %s', current_platform)
  if current_platform == 'Windows':
    msedge.open_new_window()
    msedge.open_new_tab()
    input_keyboard.go_to_my_github()
    input_mouse.move_mouse_cursor_to_follow_button_in_my_github()
    input_keyboard.click_ctrl_f()
    input_keyboard.write_message_to_follow_my_github()
  elif current_platform == 'Linux':
    terminal.open_terminal()
    input_keyboard.write_message_to_follow_my_github()
  else:
    logger.error('%s is not supported yet for executing commands.', current_platform)

