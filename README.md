# Multimodal Agentic Corrective RAG Chatbot

**Multimodal Agentic CRAG Chatbot** is a comprehensive document question answering tool that leverages the power of large language models (LLMs), vector databases, and advanced RAG techniques to provide insightful answers to your questions. Whether you're a researcher, a student, or simply looking for a smart way to extract information from documents, tis app has got you covered.  
> **Corrective-RAG (CRAG)** is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents.
---

# Project Structure (main components):

- **agent_graph:** Contains the core logic for the CRAG agent graph.  

- **agents:** Defines the functions of each agent.  

- **database:** Handles the interaction with ChromaDB for vector storage and retrieval.  

- **models:** Defines the underlying models used whithin each node in the graph (retriever model, grader model, ...).  

- **parsers:** Handles document parsing for different extentions (PDF/PPTX for now).  

- **utils:** Handles functions that are commonly used in differnt places in the project.  

- **app:** The main class that integrates all together and lanch the gradio interface.  

---

# Technologies Used

- **Langchain**: A framework for developing applications powered by language models.
  
- **ChromaDB**: A vector database that allows for efficient data retrieval and similarity search.
  
- **LangGraph**: A framework for building stateful, multi-actor agents with LLMs that can handle complex scenarios and collaborate with humans.
  
- **Gradio**: A library for creating user-friendly web interfaces for machine learning models.

---
# Installation

To set up and test the project, follow these steps:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/corrective-agentic-rag.git
   cd corrective-agentic-rag
   ```
   
2. **Install Dependencies:** Ensure you have `Python 3.10+` and install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:2.** Start the application using:  
   ```bash
   python app.py
   ```

4. **Access the Interface:** Open your web browser and navigate to http://localhost:7860 to interact with the application.

---
# Usage
TODO:
<</Show images here >>

---
# Contributing
### Contributions are welcome! If you’d like to contribute to the project, please follow these steps: 

- Fork the repository.
  
- Create a new branch `git checkout -b feature/YourFeature`.
  
- Make your changes and commit them `git commit -m 'Add some feature'`.
  
- Push to the branch `git push origin feature/YourFeature`.

- Open a pull request.

---
# Contact
For questions or feedback, feel free to reach out:

TODO:
</ Add contacts>

