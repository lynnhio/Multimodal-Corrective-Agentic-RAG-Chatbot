import streamlit as st
from parsers.doc import DocumentExtractor
from utils.helper import set_env_keys

set_env_keys()

file = st.file_uploader("Upload file", type=["pdf", "pptx"])
if file:
    extractor = DocumentExtractor()
    extractor.extract(file)
    documents = extractor.get_documents()            
    st.write(documents)        