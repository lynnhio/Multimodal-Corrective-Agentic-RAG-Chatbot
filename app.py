import streamlit as st
from parsers.pdf_parser import PdfParser
from parsers.pptx_parser import PPTXParser

file = st.file_uploader("Upload file", type=["pdf", "pptx"])
if file:
    if(file.name.endswith("pptx")):
        st.header("PPTX")
        # Example usage:
        parser = PPTXParser(output_folder="extracted_files")
        text_list, documents = parser.extract_from_pptx(file)
        for i, x in enumerate(text_list):
            st.write(f"\nNEW PAGE {i+1}:\n")
            st.markdown(x)
            
    elif file.name.endswith("pdf"):
        # Example usage:
        pdf_parser = PdfParser(output_folder="extracted_files")
        text_list, documents = pdf_parser.extract_from_pdf(file)
        for x in text_list:
            st.markdown(x)
            st.write("\nNEW PAGE:\n")
                    
            
            