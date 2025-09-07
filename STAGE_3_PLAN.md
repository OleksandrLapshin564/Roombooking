# 📄 Stage_3_PLAN.md — OpenAI + LangChain integration (Roombooking)

## 0️⃣ Вступ
- Stage 3: інтеграція OpenAI + LangChain в Roombooking.
- Мета: створити AI-помічника, який може відповідати на запитання про кімнати та бронювання.
- Робимо все **обережно**, в окремій гілці (`feature/ai-integration`) і ізольованих файлах.

---

## 1️⃣ План інтеграції (стор. 1–3)
1. **Підготовка середовища**
   - Додати залежності у `requirements_rest.txt`:
     - openai
     - langchain
     - (опційно) langchain-community, tiktoken
   - Створити `.env` змінну `OPENAI_API_KEY`.
2. **Архітектура**
   - Новий Django app `chatbot`.
   - API endpoint `/api/chatbot/`.
3. **Базова функціональність**
   - Прості питання → OpenAI GPT → JSON відповідь.
4. **Інтеграція з даними проєкту**
   - LangChain → DjangoORM / SQLDatabaseChain.
5. **UI (Frontend)**
   - Чат через Bootstrap або React.
6. **Оптимізація та безпека**
   - Обмеження (rate limit), логування запитів.

---

## 2️⃣ Детальний чек-лист Stage 3 (стор. 1–6)
- Dependencies: `openai`, `langchain`, `tiktoken`, `python-dotenv`.
- Створити `.env` з `OPENAI_API_KEY`.
- Новий app `chatbot`.
- API endpoint `ask_ai`.
- LangChain chain: `ConversationChain`.
- Frontend: кнопка, форма, fetch/axios.
- Docs & History: оновити `README.md` і `PROJECT_HISTORY.md`.

---

## 3️⃣ Database-aware AI (опційно, стор. 6)
- Використати `langchain_community.utilities.SQLDatabase` для PostgreSQL.
- Створити chain, який формує SQL-запити та відповідає з бази.

---

## 4️⃣ Frontend POC (стор. 6–7)
- `base.html` → кнопка "AI Assistant".
- `chat.html` → форма для введення запитання, блок для відповіді.
- JS → fetch POST `/api/chatbot/ask/`, виводимо відповідь.

---

## 5️⃣ Docker / ізольоване середовище (стор. 7–9)
- `Dockerfile.rest.txt`, `docker-compose.rest.yml`.
- `.env` з секретами (не комітити!).
- Можливість локального тесту у virtualenv перед Docker.
- Ризики: конфлікти версій, розмір образу, витрати на OpenAI, безпека ключів.

---

## 6️⃣ Малий proof-of-concept (стор. 10–12)
- Локальний venv: встановити deps, перевірити імпорти.
- Docker test ізольовано: `docker-compose -f docker-compose.rest.yml up --build`.
- Після успішного тесту — зафіксувати версії: `pip freeze > requirements_rest.txt`.

---

## 7️⃣ POC API endpoint + Frontend

### 7.1 Django app
```bash
python manage.py startapp chatbot
