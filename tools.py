import os
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("generate_image") 
def generate_image(prompt: str) -> str:
    """
    Generates an image URL based on the provided text prompt.
    """
    clean_prompt = str(prompt).replace(" ", "%20").strip()
    image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=500&height=500&model=flux"
    return image_url