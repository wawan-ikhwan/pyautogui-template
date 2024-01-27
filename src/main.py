'''
This script is the entry point of the application.
It imports and executes the execute_commands function from the executes module.

Invoked when the script is run directly. Executes all commands in the commands folder.
'''
import logging
import datetime
from executes import execute_commands

if __name__ == "__main__":
  current_datetime: datetime = datetime.datetime.now()
  logging.basicConfig(
    filename=f"./log/bot_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
  )
  logging.info('Starting application...')
  execute_commands()
  logging.info('Application finished with total elapsed time: %s', str(datetime.datetime.now() - current_datetime))
