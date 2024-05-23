# Text Translator

A simple text translation application built using Python and Tkinter, leveraging the Google Translate API.

## Features

- Translate text between various languages.
- User-friendly graphical interface.
- Supports a wide range of languages available in Google Translate.

## Requirements

- Python 3.x
- `googletrans` library (version 4.0.0-rc1)
- `tkinter` (usually included with Python)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/text-translator.git
cd text-translator
Create a virtual environment (optional but recommended):
bash
Копиране на код
python -m venv env
source env/bin/activate  # On Windows: `env\Scripts\activate`
Install the required libraries:
bash
Копиране на код
pip install googletrans==4.0.0-rc1
Usage
Run the script:

bash
Копиране на код
python translator.py
How to Use
Select the source language from the "Source Language" dropdown.
Select the target language from the "Target Language" dropdown.
Enter the text you want to translate in the "Input Text" field.
Click the "Translate" button.
The translated text will appear in the "Translated Text" field.
Troubleshooting
If you encounter any issues with the googletrans library, ensure you are using the correct version:

bash
Копиране на код
pip install googletrans==4.0.0-rc1
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Google Translate for providing the translation API.
Tkinter for the GUI framework.
