import google.generativeai as genai

from config.settings import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model=genai.GenerativeModel("gemini")

def chat_with_gemini(prompt:str):
    response=model.generate_content(prompt)
    return response.text
