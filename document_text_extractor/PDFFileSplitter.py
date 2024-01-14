import logging

import fitz


class PDFSplitter:
    def __init__(self):
        pass

    def split_pdf_to_images(self, pstr_pdf_file_path: str, pstr_temp_folder_path: str):
        try:
            llist_pages = list()

            pdf_document = fitz.open(pstr_pdf_file_path)

            # Iterate through each page and convert it to an image
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                image = page.get_pixmap()
                lint_page_number = page_number + 1
                image_path = f"{pstr_temp_folder_path}/page_{lint_page_number}.png"
                image.save(image_path, "png")
                llist_pages.append({"page_number": lint_page_number, "page_path": image_path})

            # Close the PDF file
            pdf_document.close()
            return llist_pages
        except Exception as e:
            logging.error(str(e), exc_info=True)
