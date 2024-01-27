'''
log_handler.py
--------------
This module contains the ScreenLoggerUpdateHandler class which is a custom logging handler.
It is used to update log on screen.

Classes:
  ScreenLoggerUpdateHandler: A custom logging handler that updates log on screen.
'''

import logging

class ScreenLoggerUpdateHandler(logging.Handler):
  '''
  A custom logging handler that sends the latest log messages to a screen logger.

  Attributes:
    screen_logger (ScreenLogger): The screen logger to be updated.

  Methods:
    emit(record): Formats the log record and sends it to the screen logger.
  '''
  def __init__(self, screen_logger):
    '''
    Constructs all the necessary attributes for the ScreenLoggerUpdateHandler object.

    Parameters:
      screen_logger (ScreenLogger): The screen logger to be updated.
    '''
    super().__init__()
    self.screen_logger = screen_logger

  def emit(self, record):
    '''
    Formats the log record and sends it to the screen logger.

    Parameters:
      record (logging.LogRecord): The log record to be formatted and sent to the screen logger.
    '''
    log_message: str = self.format(record)
    self.screen_logger.append_text(log_message, record.levelno)
