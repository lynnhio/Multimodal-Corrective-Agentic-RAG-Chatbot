import streamlit as st
from parsers.doc import DocumentExtractor
from utils.helper import set_env_keys
from database.chromadb import VectorDB
from constants.constansts import PERSIST_DIRECTORY
import shutil
import os

set_env_keys()

file = st.file_uploader("Upload file", type=["pdf", "pptx"])
if file:
    extractor = DocumentExtractor()
    extractor.extract(file)
    documents = extractor.get_documents()
    vector_db = VectorDB(documents)
    retriever = vector_db.get_retriever()            
    st.write(documents)
    
else:
    if os.path.exists(PERSIST_DIRECTORY):
      shutil.rmtree(PERSIST_DIRECTORY)
 
