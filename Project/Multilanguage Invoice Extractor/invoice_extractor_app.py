from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
from google import genai


# Function to get response from Gemini
def get_gemini_response(prompt, image, question):

    api_key = os.getenv("GOOGLE_API_KEY")

    client = genai.Client(api_key=api_key)

    full_prompt = prompt + "\n\n" + question

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            full_prompt,
            image
        ]
    )

    return response.text

# Function to prepare image
def image_setup(upload_file):

    if upload_file is not None:
        image = Image.open(upload_file)
        return image
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit configuration
st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")

# User question
user_question = st.text_input("Input Prompt:", key="input")

# File uploader
upload_file = st.file_uploader(
    "Choose an image of the invoice...",
    type=["jpg", "jpeg", "png"]
)

# Show uploaded image
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Submit button
submit = st.button("Tell me about the invoice")

# System prompt
input_prompt = """
You are an expert in understanding invoices.

We will upload an invoice image and you must answer questions
based on the invoice content.

If the answer is not present in the image, respond with:
'Information not available'.
"""

# When user clicks submit
if submit:
    img_data = image_setup(upload_file)
    response = get_gemini_response(
        input_prompt,
        img_data,
        user_question
    )
    st.subheader("Response:")
    st.write(response)