import logging

import pytesseract
from PIL import Image

from Configuration import *
from PDFFileSplitter import PDFSplitter


class GetTextFromImage:
    def __init__(self):
        try:
            self.obj_pdf_splitter = PDFSplitter()
        except Exception as e:
            logging.error(str(e), exc_info=True)

    def get_text_from_image_path(self, pstr_file_path: str):
        try:
            llst_file_path = list()
            if self.get_file_format(pstr_file_path) == "pdf":
                llst_file_path = self.get_images_from_pdf_file(pstr_file_path)
            else:
                llst_file_path = [{
                    "page_number": 1, "page_path": pstr_file_path
                }]
            llst_file_path = self.extract_text_from_image(llst_file_path)
            return llst_file_path
        except Exception as e:
            logging.error(str(e), exc_info=True)

    def extract_text_from_image(self, list_images: list):
        try:
            for ldict_image in list_images:
                # Open the image using Pillow
                image = Image.open(ldict_image['page_path'])

                # Perform OCR using pytesseract
                text = pytesseract.image_to_string(image)
                ldict_image['text'] = text
            return list_images
        except Exception as e:
            logging.error(str(e), exc_info=True)

    def get_images_from_pdf_file(self, pstr_file_path: str):
        try:
            llist_file_path = self.obj_pdf_splitter.split_pdf_to_images(pstr_file_path, temp_path)
            return llist_file_path
        except Exception as e:
            logging.error(str(e), exc_info=True)

    def get_file_format(self, pstr_file_path):
        try:
            root, extension = os.path.splitext(pstr_file_path)
            formatted_extension = extension[1:]
            return formatted_extension
        except Exception as e:
            logging.error(str(e), exc_info=True)
