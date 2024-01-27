'''
This script is the entry point of the application.
It imports and executes the execute_commands function from the executes module.

Invoked when the script is run directly. Executes all commands in the commands folder.
'''
import platform
import logging
from logging import Logger
import datetime
from executes import execute_commands_for_windows, execute_commands_for_linux
import os

if __name__ == "__main__":
  current_datetime: datetime = datetime.datetime.now()
  current_directory_of_this_python_file: str = os.path.dirname(os.path.realpath(__file__))
  logging.basicConfig(
    filename=f"{current_directory_of_this_python_file}/../log/bot_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
  )
  logger: Logger = logging.getLogger(__name__)
  current_platform: str = platform.system()
  logger.info('Application started with current platform: %s', current_platform)
  if current_platform == 'Windows':
    execute_commands_for_windows()
  elif current_platform == 'Linux':
    execute_commands_for_linux()
  else:
    logger.critical('Current platform (%s) not supported.', current_platform)
    raise Exception(f'Platform {current_platform} not supported.')
  logger.info('Application finished with total elapsed time: %s', str(datetime.datetime.now() - current_datetime))
