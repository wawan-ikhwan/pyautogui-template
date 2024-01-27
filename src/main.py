'''
This script is the entry point of the application.
It imports and executes the execute_commands function from the executes module.

Invoked when the script is run directly. Executes all commands in the commands folder.
'''
import platform
import os
import logging
from time import sleep
from logging import Logger
import datetime
from executes import execute_commands_for_windows, execute_commands_for_linux
from utilities.windows_debug_on_screen import WINDOWS_LABEL
from utilities.log_handler import LabelUpdateHandler

if __name__ == "__main__":
  current_datetime: datetime = datetime.datetime.now()
  current_directory_of_this_python_file: str = os.path.dirname(os.path.realpath(__file__))
  logging.basicConfig(
    filename=f"{current_directory_of_this_python_file}/../log/bot_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
  )
  logger: Logger = logging.getLogger(__name__)
  current_platform: str = platform.system()
  logger.info('Application started with current platform: %s', current_platform)
  if current_platform == 'Windows':
    logging.getLogger().addHandler(LabelUpdateHandler(WINDOWS_LABEL)) # Create the custom handler and add it to the root logger
    execute_commands_for_windows()
  elif current_platform == 'Linux':
    execute_commands_for_linux()
  else:
    logger.critical('Current platform (%s) not supported.', current_platform)
    raise Exception(f'Platform {current_platform} not supported.')
  logger.info('Application finished with total elapsed time: %s', str(datetime.datetime.now() - current_datetime))
  sleep(10) # Just to display last log
