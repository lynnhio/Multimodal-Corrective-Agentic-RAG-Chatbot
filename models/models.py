from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults

def get_gemini_model(model_name = "gemini-pro", max_tokens= None, temperature = None):
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        max_tokens=max_tokens,
        temperature = temperature
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

def get_search_tool(k=3):
    web_search_tool = TavilySearchResults(k=k)
    return web_search_tool