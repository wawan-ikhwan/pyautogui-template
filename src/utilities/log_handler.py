import logging
from collections import deque

class LabelUpdateHandler(logging.Handler):
  def __init__(self, label):
    super().__init__()
    self.label = label
    self.last_logs = deque(maxlen=10)

  def emit(self, record):
    log_message: str = self.format(record)
    self.last_logs.append(log_message)

    # Update the label with the log messages, separated by new lines
    self.label.update_label('\n'.join(self.last_logs))