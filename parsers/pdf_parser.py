from langchain.schema import Document
from utils.helper import get_description
import fitz  # PyMuPDF
import hashlib
import os


class PdfParser:
    def __init__(self, output_folder):
        self.output_folder = output_folder
        # Create output folder if it doesn't exist
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        self.seen_images = set()
        self.text_list = []
        self.documents = []

    def extract_from_file(self, pdf_file):
        # Extract text and images using PyMuPDF
        # pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        pdf_document = fitz.open(pdf_file, filetype="pdf")
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]

            # Extract text
            text = page.get_text()
            self.text_list.append(text)

            # Extract images
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]  # the xref of the image
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_hash = hashlib.md5(image_bytes).hexdigest()

                # Check if the image has already been seen
                if image_hash not in self.seen_images:
                    self.seen_images.add(image_hash)
                    description, useful = get_description(image_bytes, self.text_list[page_number])
                    print(f"{useful} at page: {page_number + 1}")

                    if useful == "yes":
                        self.text_list[page_number] += f"\n Image Description:\n{description}"
                        image_filename = os.path.join(self.output_folder,
                                                      f'page_{page_number + 1}_img_{img_index + 1}.png')
                        doc = Document(
                            page_content=description,
                            metadata={
                                'type': 'image',
                                'img_path': image_filename,
                            }
                        )
                        self.documents.append(doc)

                        # Save the image
                        with open(image_filename, 'wb') as image_file:
                            image_file.write(image_bytes)

        pdf_document.close()
        return self.text_list, self.documents

# Example usage:
# pdf_parser = PdfParser(output_folder="extracted_files")
# text_list, documents = pdf_parser.extract_from_file(uploaded_file)