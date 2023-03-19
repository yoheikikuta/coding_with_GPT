import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

def translate_text(text, api_key, target_language="ja"):
    service = build("translate", "v2", developerKey=api_key)
    result = service.translations().list(source="en", target=target_language, q=text).execute()
    return result["translations"][0]["translatedText"]

def load_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key
