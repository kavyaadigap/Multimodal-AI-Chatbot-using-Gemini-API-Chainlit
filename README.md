
# **Multimodal AI Chatbot using Gemini API & Chainlit**  

This project is a **multimodal AI chatbot** that integrates **Google's Gemini AI** with **Chainlit** to handle text, images, and audio inputs. The chatbot processes user queries, images, and audio, then responds with AI-generated content.  

## **🚀 Features**  
- ✅ **Supports text-based conversations**  
- 🖼️ **Processes images** (converts to Base64 before sending)  
- 🔊 **Handles audio inputs** (transcribes audio using Whisper)  
- ⚡ **Built using Google's Gemini AI (Gemini 1.5 Flash)**  
- 🎨 **Interactive UI powered by Chainlit**  

## **🛠️ Tech Stack**  
- **Python**  
- **Google Generative AI (Gemini API)**  
- **Chainlit** (for chat interface)  
- **Base64** (for image encoding)  

## **📌 Setup Instructions**  
1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/yourusername/multimodal-chatbot.git
cd multimodal-chatbot
```

2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

3️⃣ **Set Up Your API Key**  
- Get an API key from **Google Gemini AI**  
- Add it to the script:  
  ```python
  genai.configure(api_key="your_api_key_here")
  ```

4️⃣ **Run the Chatbot**  
```sh
chainlit run main.py
```

5️⃣ **Access the Chatbot**  
- Open your browser and go to: **http://localhost:8000**  

## **📌 How It Works**  
1. The chatbot takes user input (text, image, or audio).  
2. If an image is uploaded, it's converted to Base64 and sent to the Gemini API.  
3. If audio is provided, it gets transcribed before being sent.  
4. The chatbot generates a response and displays it in the chat UI.  

## **📝 Future Enhancements**  
- Improve **UI design** for a better user experience.  
- Add **more advanced NLP processing** for improved accuracy.  
- Support **multiple AI models** (e.g., OpenAI, Gemini, LLaMA).  

## **📄 License**  
This project is open-source and available under the **MIT License**.  

