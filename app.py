import streamlit as st
from parsers.doc import DocumentExtractor

file = st.file_uploader("Upload file", type=["pdf", "pptx"])
if file:
    extractor = DocumentExtractor()
    extractor.extract(file)
    documents = extractor.get_documents()            
    st.write(documents)        