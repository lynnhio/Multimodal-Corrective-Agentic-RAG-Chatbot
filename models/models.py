from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel, Field

from prompts.prompts import (
    grader_prompt_template,
    rewriter_system_prompt,
    rag_prompt_template
)


def get_retrieval_grader():
    class GradeDocuments(BaseModel):
        """Binary score for relevance check on retrieved documents."""

        binary_score: str = Field(description="Documents are relevant to the question, 'yes' or 'no'")

    grade_prompt = PromptTemplate.from_template(grader_prompt_template)
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
    structured_llm_grader = llm.with_structured_output(GradeDocuments)

    retrieval_grader = grade_prompt | structured_llm_grader

    return retrieval_grader


def get_rag_chain():
    rag_prompt = ChatPromptTemplate.from_template(rag_prompt_template)
    llm = ChatMistralAI(temperature=0)

    # Chain
    rag_chain = rag_prompt | llm | StrOutputParser()

    return rag_chain


def get_question_rewriter():
    re_write_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", rewriter_system_prompt),
            ("human", "Here is the initial question: \n\n {question} \n Formulate an improved question."),
        ]
    )
    llm = ChatMistralAI(temperature=0)

    question_rewriter = re_write_prompt | llm | StrOutputParser()

    return question_rewriter


def get_web_search_tool(k=3):
    web_search_tool = TavilySearchResults(k=k)
    return web_search_tool
