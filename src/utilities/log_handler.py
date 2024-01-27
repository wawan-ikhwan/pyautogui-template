'''
log_handler.py
--------------
This module contains the LabelUpdateHandler class which is a custom logging handler.
It is used to update a label with the latest log messages.

Classes:
  LabelUpdateHandler: A custom logging handler that updates a label with the latest log messages.
'''

import logging
from collections import deque

class LabelUpdateHandler(logging.Handler):
  '''
  A custom logging handler that updates a label with the latest log messages.

  Attributes:
    label (str): The label to be updated.
    last_logs (collections.deque): A deque that stores the last 10 log messages.

  Methods:
    emit(record): Formats the log record and updates the label with the latest log messages.
  '''
  def __init__(self, label):
    '''
    Constructs all the necessary attributes for the LabelUpdateHandler object.

    Parameters:
      label (str): The label to be updated.
    '''
    super().__init__()
    self.label = label
    self.last_logs = deque(maxlen=10)

  def emit(self, record):
    '''
    Formats the log record and updates the label with the latest log messages.

    Parameters:
      record (logging.LogRecord): The log record to be formatted and added to the deque.
    '''
    log_message: str = self.format(record)
    self.last_logs.append(log_message)

    # Update the label with the log messages, separated by new lines
    self.label.update_label('\n'.join(self.last_logs))
