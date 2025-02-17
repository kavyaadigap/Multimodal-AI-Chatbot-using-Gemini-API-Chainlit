import google.generativeai as genai  # Correct import
import base64
import chainlit as cl
import os

# Set API Key (if using an older version of the library)
genai.configure(api_key="AIzaSyCmim8ay_rNkYlfpheQri3lvomW1lNGCMU")  

# Initialize the model correctly
model = genai.GenerativeModel("gemini-1.5-flash")

def append_messages(image_url=None, query=None, audio_transcript=None):
    message_list = []

    if image_url:
        message_list.append({"type": "image_url", "image_url": {"url": image_url}})

    if query:
        message_list.append({"type": "text", "text": query})

    if audio_transcript:
        message_list.append({"type": "text", "text": audio_transcript})

    try:
        response = model.generate_content(contents=message_list)  # ✅ Corrected API call
        return response.text
    except Exception as e:
        print(f"Error in API call: {e}")
        return "Error generating response"

def image2base64(image_path):
    try:
        with open(image_path, "rb") as img:
            return base64.b64encode(img.read()).decode("utf-8")
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

@cl.on_message
async def chat(msg: cl.Message):
    images = [file for file in msg.elements if "image" in file.mime]
    
    image_url = None
    if len(images) > 0:
        base64_image = image2base64(images[0].path)
        if base64_image:
            image_url = "data:image/png;base64," + base64_image

    response = append_messages(image_url=image_url, query=msg.content)

    response_msg = cl.Message(content=response)
    await response_msg.send()
