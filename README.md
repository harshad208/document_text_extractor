# document_text_extractor

## Overview

Brief description of your Python project module. Mention its purpose, main features, and any other relevant information.

## Installation

```bash
pip install document_text_extractor==1.0.0


├── document_text_extractor
│ ├── document_text_extractor
│ │ ├── data
│ │ ├── __init__.py
│ │ ├── CommonOperations.py
│ │ ├── Configuration.py
│ │ ├── GetTextFromImage.py
│ │ ├── DocumentTextExtractor.py
│ │ ├── PDFFileDplitter.py    
│ ├── MANIFEST.in
│ ├── README.md
│ ├── setup.py

```

``` bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-eng
```

**Current Version: v1.0.0**

Brief description of your project.

## How to Run

Follow these steps to set up and run the Document Text Extractor on your local machine.

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```bash
    git clone git@github.com:harshad208/document_text_extractor.git
2. Navigate to the project directory
3. cd document_text_extractor/document_text_extractor
4. create a virtual environment -> python -m venv venv
5. source venv/bin/activate
6. pip install -r requirements.txt
7. For Linux (Ubuntu/Debian)
   ```
   sudo apt-get update
   sudo apt-get install tesseract-ocr
   sudo apt-get install tesseract-ocr-eng # Optional: English language pack
8. For Windows
   Download and install Tesseract OCR from https://github.com/tesseract-ocr/tesseract.
   Add Tesseract to your system's PATH.
   Verify the installation by running tesseract --version in the command prompt.
9. For macOS
   ```
   brew install tesseract
10. Feel free to customize this template further based on the specifics of your project and the setup instructions.
    Providing clear and concise instructions will make it easier for others to use and contribute to your project.

## Dependencies

The following Python packages are required to run this project. You can install them using the
provided `requirements.txt` file:

``` requirements.txt
 uvicorn==0.25.0
 fastapi==0.109.0
 python-multipart==0.0.6
 pytesseract==0.3.10
 Pillow==10.2.0
 PyMuPDF==1.23.12
```

``` 
# v1.0.0
1. initial phase
```