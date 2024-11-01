import gradio as gr
from parsers.doc import DocumentExtractor
from utils.helper import set_env_keys, get_img_data_from_path
from database.chromadb import VectorDB
from agent_graph.graph import compile_workflow
from constants.constansts import OUTPUT_FOLDER
import shutil
import os


def process_file(file):
    if not file:
        return "Please, upload file"

    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER)

    global retriever
    global app

    set_env_keys()
    extractor = DocumentExtractor()
    extractor.extract(file)
    documents = extractor.get_documents()
    vector_db = VectorDB(documents)
    retriever = vector_db.get_retriever()
    app = compile_workflow()

    return "File Processed Successfully"


def get_answer(message, history):
    user_input = message["text"]
    try:
        inputs = {
            "question": user_input,
            "retriever": retriever
        }
        for output in app.stream(inputs):
            for key, value in output.items():
                pass

        answer = value['generation']
        if value["relevant_images"]:
            image_data = get_img_data_from_path(value["relevant_images"][0])
            # image_data = value["relevant_images"][0]
            image_to_show = f"<p align='center'><img src='data:image/png;base64, {image_data}' alt='My Image'> </p>"
            answer = answer + image_to_show

        return answer
    except:
        return "Somthing went wrong, Please, upload a file if you did not."


with gr.Blocks(theme='Nymbo/Nymbo_Theme') as iface:
    file_input = gr.File(label="Upload PDF/PPTX Document")
    file_text = gr.Textbox(label="File Response Text", interactive=False)
    file_button = gr.Button("Submit File")
    file_button.click(process_file, inputs=[file_input], outputs=[file_text])

    gr.ChatInterface(fn=get_answer,
                     type="messages",
                     examples=[{"text": "What is this document about?", "files": []}],
                     title="Let's Chat", multimodal=True)

iface.launch(debug=True)
