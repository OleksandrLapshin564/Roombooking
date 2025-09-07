from django.http import JsonResponse
import os
import openai
from dotenv import load_dotenv

# Завантажуємо змінні середовища з .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def ask_ai(request):
    """
    Простий endpoint для тесту OpenAI.
    Повертає коротку відповідь на запитання через GET-параметр 'q'.
    """
    question = request.GET.get("q", "Hello AI")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=50
        )
        answer = response.choices[0].message.content.strip()
        return JsonResponse({"answer": answer})
    except Exception as e:
        return JsonResponse({"error": str(e)})


# Create your views here.
