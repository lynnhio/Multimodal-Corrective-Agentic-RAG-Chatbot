from langchain.schema import Document
from models.models import (
    get_retrieval_grader,
    get_rag_chain,
    get_question_rewriter,
    get_web_search_tool
)


def retrieve(state):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """

    question = state["question"]
    retriever = state['retriever']

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}


def generate(state):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation
    """

    question = state["question"]
    documents = state["documents"]
    relevant_images = []
    for d in documents:
        if d.metadata['type'] == 'image':
            relevant_images.append(d.metadata['img_path'])
    rag_chain = get_rag_chain()
    generation = rag_chain.invoke({"context": documents, "question": question})

    return {
        "documents": documents,
        "question": question,
        "generation": generation,
        "relevant_images": relevant_images}


def grade_documents(state):
    """
    Determines whether the retrieved documents are relevant to the question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with only filtered relevant documents
    """

    question = state["question"]
    documents = state["documents"]

    # Score each doc
    filtered_docs = []
    web_search = "No"
    for d in documents:
        retrieval_grader = get_retrieval_grader()
        score = retrieval_grader.invoke({"question": question, "document": d.page_content})
        grade = "no"
        if score is not None and hasattr(score, 'binary_score'):
            grade = score.binary_score
        if grade == "yes":
            filtered_docs.append(d)
        else:
            web_search = "Yes"
            continue
    return {"documents": filtered_docs, "question": question, "web_search": web_search}


def transform_query(state):
    """
    Transform the query to produce a better question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates question key with a re-phrased question
    """

    question = state["question"]
    documents = state["documents"]

    # Re-write question
    question_rewriter = get_question_rewriter()
    better_question = question_rewriter.invoke({"question": question})
    return {"documents": documents, "question": better_question}


def web_search(state):
    """
    Web search based on the re-phrased question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with appended web results
    """

    question = state["question"]
    documents = state["documents"]

    # Web search
    web_search_tool = get_web_search_tool(k=3)
    docs = web_search_tool.invoke({"query": question})
    web_results = "\n".join([f"Content from Url:{d['url']}:\n{d['content']}" for d in docs])
    web_results = Document(
        page_content=web_results,
        metadata={
            'type': 'text'
        })
    documents.append(web_results)

    return {"documents": documents, "question": question}


def decide_to_generate(state):
    """
    Determines whether to generate an answer, or re-generate a question.

    Args:
        state (dict): The current graph state

    Returns:
        str: Binary decision for next node to call
    """

    if state["web_search"] == "Yes":
        return "transform_query"
    else:
        return "generate"
