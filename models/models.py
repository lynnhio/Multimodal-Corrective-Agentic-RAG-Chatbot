from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini_flash():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        max_tokens=1024
        )
    return llm

def get_gemini_pro():
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", 
        temperature=0
        )
    return llm

def get_mistral_model():
    llm = ChatMistralAI(temperature=0)
    return llm

def get_mistral_embedding():
    embeddings = MistralAIEmbeddings(
        model="mistral-embed"
        )
    return embeddings
