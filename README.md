# pyautogui-template

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/)

A Python template project for GUI Automation using PyAutoGUI. Basically this is for design pattern purpose.

## Design Pattern
  * `main.py`: Run this file to start actual automation.
  * `executes.py`: Executing all commands orderly based on defined commands in `commands/` folder.
  * `commands/`: All defined command must be inside this folder.

## Prerequisites
All dependencies are written in'requirements.txt', but there are optional dependencies for optical recognition character purposes (OCR). It's [Tesseract] (https://github.com/tesseract-ocr/tesseract), and you might need to install that. So far, I can't guarantee that this template will work fine if it's not installed.

## Getting Started
To working on this template , follow these steps:
1. **Create a Virtual Environment:**

   ```bash
   python -m venv .venv
   ```

2. **Activate the Virtual Environment:**
    * On Windows:
    ```powershell
    .venv\Scripts\activate
    ```
    * On Linux:
    ```bash
    source .venv/bin/activate
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Copy Environment Variables:**
    * On Windows:
    ```powershell
    copy .env.example .env
    ```
    * On Linux:
    ```bash
    cp .env.example .env
    ```
    Modify the values in the `.env` file according to your environment.
5. **Run `main.py`:**
    ```bash
    python src/main.py
    ```
    This will run automation to follow my github :).

## Support
If you encounter any issues or have questions, please feel free start issues.

## Contributing
We welcome contributions! Whether it's bug reports, feature requests, or code contributions.

## License
It's licensed under the MIT License - see the LICENSE file for details.