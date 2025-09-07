# scripts/ai_test.py
from dotenv import load_dotenv
import os, sys

load_dotenv()  # loads .env in project root if present

print("Python:", sys.version.splitlines()[0])
print("OPENAI_API_KEY present:", bool(os.getenv("OPENAI_API_KEY")))

try:
    import openai
    print("openai version:", getattr(openai, "__version__", "unknown"))
except Exception as e:
    print("openai import error:", e)

try:
    from langchain.llms import OpenAI
    print("langchain import OK")
    # instantiate LangChain wrapper — will use OPENAI_API_KEY from env
    llm = OpenAI(temperature=0)
    resp = llm("Say 'hello' once and return only one word.")
    print("LLM response:", resp)
except Exception as e:
    print("langchain test error:", e)
