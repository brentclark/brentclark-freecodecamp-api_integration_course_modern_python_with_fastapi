import os

from dotenv import load_dotenv
from openai import OpenAI

from app.crud import update_translation_task

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


# def perform_translation(task_id: int, text: str, languages: list, db:get_session):
def perform_translation(task_id: int, text: str, languages: list):
    translations = {}

    # Lets pretend we got text back from CHATGPT
    mock_text = {
        "fr": "Bonjour, comment ça va?",  # French
        "es": "Hola, ¿cómo estás?",  # Spanish
        "de": "Hallo, wie geht es dir?",  # German
        "it": "Ciao, come stai?",  # Italian
        "pt": "Olá, como você está?",  # Portuguese
        "nl": "Hallo, hoe gaat het met je?",  # Dutch
        "sv": "Hej, hur mår du?",  # Swedish
        "no": "Hei, hvordan har du det?",  # Norwegian
        "da": "Hej, hvordan har du det?",  # Danish
        "fi": "Hei, kuinka voit?",  # Finnish
        "pl": "Cześć, jak się masz?",  # Polish
        "cs": "Ahoj, jak se máš?",  # Czech
        "ru": "Привет, как дела?",  # Russian
        "zh": "你好，你好吗？",  # Chinese
        "ja": "こんにちは、お元気ですか？",  # Japanese
        "ko": "안녕하세요, 어떻게 지내세요?",  # Korean
        "ar": "مرحبًا، كيف حالك؟",  # Arabic
        "hi": "नमस्ते, आप कैसे हैं?",  # Hindi
        "en": "Hiya",  # English
    }

    # client = OpenAI(api_key=OPENAI_API_KEY)
    for lang in languages:
        #     completion = client.chat.completions.create(
        #         model="gpt-4o-mini",
        #         store=True,
        #         messages=[
        #             {"role": "system", "content": f"You are a helpful assistant that translate text in {lang}"},
        #             {"role": "user", "content": text},
        #         ],
        #     )
        # translated_text = completion.choices[0].message.strip()

        translated_text = mock_text[lang]
        translations[lang] = translated_text
        # update_translation_task(task_id=task_id, translations=translated_text)

    update_translation_task(task_id=task_id, translations=translations)
