import base64
from dotenv import load_dotenv
import os


def set_env_keys():
    load_dotenv()
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'

def get_img_data(image_data):
    image_data_b64 = base64.b64encode(image_data).decode("utf-8")
    return image_data_b64

def get_img_data_path(img_path):
    with open(img_path, "rb") as image_file:
        image_data = image_file.read()
    image_data_b64 = base64.b64encode(image_data).decode("utf-8")
    return image_data_b64