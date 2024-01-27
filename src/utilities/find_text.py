'''
This module contains functions to find the coordinates of a given text on the screen.
It uses the pytesseract library
to perform optical character recognition (OCR) on a screenshot of the screen,
and then finds the coordinates of the
given text in the resulting data.

Dependencies:
- os
- pyautogui
- pytesseract
- cv2
- numpy
- PIL
'''
import os
import logging
from logging import Logger
import platform
import pyautogui as pag
import pytesseract
import cv2
import numpy as np
from PIL import Image
from dotenv import load_dotenv

logger: Logger = logging.getLogger(__name__)
current_platform: str = platform.system()

if load_dotenv():
  logger.info('Loaded environment variables from .env file')
else:
  logger.warning('Could not load environment variables from .env file')

def is_tesseract_installed():
  """
  This function checks if Tesseract-OCR is installed at the specified path.

  Args:
    path (str): The path to the Tesseract-OCR executable.

  Returns:
    bool: True if Tesseract-OCR is installed at the specified path, False otherwise.
  """
  return os.path.exists(os.environ['TESSERACT_BASEPATH'])

if current_platform == 'Windows':
  # In case you're on Windows and pytesseract doesn't find your installation (Happened to me)
  os.environ['TESSDATA_PREFIX'] = os.path.join(os.environ['TESSERACT_BASEPATH'], 'tessdata')
  pytesseract.pytesseract.tesseract_cmd = os.path.join(
    os.environ['TESSERACT_BASEPATH'], 'tesseract.exe'
  )
else:
  logger.error('%s is not supported yet for OCR.', current_platform)
  raise Exception(f'{current_platform} is not supported yet for OCR.')

def find_coordinates_text(text, lang='eng') -> (float, float):
  '''
  This function takes a screenshot of the main screen, converts it to grayscale,
  and then uses pytesseract to perform
  OCR on the image. It then finds the coordinates of the given text in the resulting data.

  Args:
    text (str): The text to find on the screen.
    lang (str, optional): The language to use for OCR. Defaults to 'eng'.

  Returns:
    tuple: The x and y coordinates of the top-left corner
    of the first occurrence of the text on the screen.
    If the text is not found, returns None.
  '''
  if not is_tesseract_installed():
    logger.error(
      'Tesseract is not installed at the specified path %s',
      os.environ['TESSERACT_BASEPATH']
    )
    raise Exception(
      f'Tesseract is not installed at the specified path: {os.environ["TESSERACT_BASEPATH"]}'
    )
  else:
    logger.info('Tesseract is installed at the specified path %s', os.environ['TESSERACT_BASEPATH'])
  logger.info('Finding coordinates of "%s" on the screen...', text)
  # Take a screenshot of the main screen
  screenshot: Image = pag.screenshot()

  # Convert the screenshot to grayscale
  img: np.ndarray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

  # Find the provided text (text) on the grayscale screenshot
  # using the provided language (lang)
  data = pytesseract.image_to_data(img, lang=lang, output_type='data.frame')

  # Find the coordinates of the provided text (text)
  try:
    x, y = data[data['text'] == text]['left'].iloc[0], data[data['text'] == text]['top'].iloc[0]
  except IndexError:
    # The text was not found on the screen
    logger.warning('Text "%s" not found on the screen', text)
    return None

  # Text was found, return the coordinates
  logger.info('Coordinates of "%s" found: (%d, %d)', text, x, y)
  return (x, y)

def find_coordinates_text_center(text, lang='eng') -> (float, float):
  '''
    This function is similar to find_coordinates_text,
    but it returns the coordinates of the center of the text instead of the top-left corner.

  Args:
    text (str): The text to find on the screen.
    lang (str, optional): The language to use for OCR. Defaults to 'eng'.

  Returns:
    tuple: The x and y coordinates of the center of the first occurrence of the text on the screen.
    If the text is not found, returns None.
  '''
  if not is_tesseract_installed():
    logger.error(
      'Tesseract is not installed at the specified path %s',
      os.environ['TESSERACT_BASEPATH']
    )
    raise Exception(
      f'Tesseract is not installed at the specified path: {os.environ["TESSERACT_BASEPATH"]}'
    )
  else:
    logger.info('Tesseract is installed at the specified path %s', os.environ['TESSERACT_BASEPATH'])
  logger.info('Finding center coordinates of "%s" on the screen...', text)
  # Take a screenshot of the main screen
  screenshot: Image = pag.screenshot()

  # Convert the screenshot to grayscale
  img: np.ndarray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

  # Find the provided text (text) on the grayscale screenshot
  # using the provided language (lang)
  data = pytesseract.image_to_data(img, lang=lang, output_type='data.frame')

  # Find the coordinates of the provided text (text)
  try:
    x, y = (
      data[data['text'] == text]['left'].iloc[0] + data[data['text'] == text]['width'].iloc[0] // 2,
      data[data['text'] == text]['top'].iloc[0] + data[data['text'] == text]['height'].iloc[0] // 2
    )
  except IndexError:
    # The text was not found on the screen
    return None

  # Text was found, return the coordinates
  logger.info('Center coordinates of "%s" found: (%d, %d)', text, x, y)
  return (x, y)
