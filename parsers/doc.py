from parsers.pdf_parser import PdfParser
from parsers.pptx_parser import PPTXParser
from langchain.schema import Document


class DocumentExtractor:
    def __init__(self, output_folder="extracted_images"):
        self.output_folder = output_folder
        self.documents = []

    def extract(self, file):
        if(file.name.endswith("pptx")):
            pptx_parser = PPTXParser(output_folder=self.output_folder)
            text_list, documents = pptx_parser.extract_from_file(file)
                
        elif file.name.endswith("pdf"):
            pdf_parser = PdfParser(output_folder=self.output_folder)
            text_list, documents = pdf_parser.extract_from_file(file)
    
        extended_docs = self.text_to_docs(text_list)
        documents.extend(extended_docs)
        self.documents = documents

    def text_to_docs(self, text_list):
        documents = []
        for text in text_list:
            if text not in ["", "\n"]:
                doc = Document(
                    page_content = text,
                    metadata = {
                        'type': 'text'
                    }
                )
                documents.append(doc)
        
        return documents
    
    def get_documents(self):
        return self.documents
        