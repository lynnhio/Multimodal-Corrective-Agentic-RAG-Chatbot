description_prompt = """
Analyze the following photo from an academic document and provide a concise description,
including relevant details that would aid in retrieving the photo when questioned about its contents.
Exclude any extraneous text. Use the following context around the image:  
{context}
If the image seems to be useless (e.g., logos or personal photos), respond with (no description) and indicate it is not useful.
{format_instructions}
"""

grader_prompt_template = """
You are a grader assessing relevance of a retrieved document to a user question.   
If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant.   
Provide a binary score: 'yes' if the document is relevant, and 'no' if it is not.  
Retrieved document: \n\n {document} \n\n User question: {question}
"""

rewriter_system_prompt = """
You a question re-writer that converts an input question to a better version that is optimized for web search.
Look at the input and try to reason about the underlying sematic intent / meaning.
Give the question only without any acknowledgement or extra words.
"""

rag_prompt_template = """human

You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
Structure your response in a readable one.

Please include the Resources that found in the context, which can be URLs or page_numbers.
For example if you have Document(page_number=4, type='text', ...) so the resource is page 5.
Also if you found Urls in your context show them in the resources section.  
IGNORE image paths and page content, just show (page_number or Url) if found.
DON'T show Document object, page content or image paths. Just show page number (number). 

Show the resources at the end of the response in a bulleted list points. 
Question: {question} 

Context: {context} 

Answer: 

"""
