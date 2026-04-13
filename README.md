 🤖 AI Web Search Agent

An intelligent agent that combines **real-time web search** with a **Large Language Model (LLM)** to generate accurate, contextual answers.

---

 🚀 Overview

This project simulates a real-world AI assistant that:

* Searches the web for relevant information
* Processes and filters useful results
* Uses an LLM to generate a final answer

---

 🏗️ Architecture Overview

```
User Query
    ↓
Web Search (SerpAPI)
    ↓
Top Links + Snippets
    ↓
LLM (Qwen - Hugging Face)
    ↓
Final Answer + Sources
```

---
⚙️ Setup Instructions

 1️⃣ Clone the repository

```
git clone https://github.com/thejagithub-dot/ai-agent-project.git
cd ai-agent-project
```

2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

 4️⃣ Configure environment variables

Create a `.env` file in root:

```
HUGGINGFACE_API_KEY=your_api_key
SERPAPI_API_KEY=your_api_key
```
---

 ▶️ How to Run

```
cd agent
python main.py
```

Example:

```
Ask something: What are the latest MacBook specs?
```

---

 📦 Dependencies Used

* Python
* requests
* python-dotenv
* huggingface_hub
* serpapi

---

 🧠 Design Decisions & Trade-offs

 ✅ Decisions

* Used **SerpAPI** for reliable web search results
* Used **Hugging Face (Qwen model)** for cost-effective LLM
* Modular structure (`search.py`, `llm.py`) for scalability

⚖️ Trade-offs

* Only uses snippets (not full page scraping) → faster but less detailed
* CLI-based interface instead of UI → simple but less interactive
* Depends on external APIs → may face rate limits

---

📂 Project Structure

```
ai-agent-project/
│
├── agent/
│   ├── main.py
│   ├── llm.py
│   ├── search.py
│
├── .env.example
├── requirements.txt
├── README.md
```
HUGGINGFACE_API_KEY=your_key_here
SERPAPI_API_KEY=your_key_here
---

 📸 Demo
![WhatsApp Image 2026-04-13 at 1 56 22 PM](https://github.com/user-attachments/assets/62cae11d-fcf1-4937-9699-77b558b8941d)
<img width="936" height="553" alt="image" src="https://github.com/user-attachments/assets/a3917fbe-65ba-4816-b95e-96a16178eb6d" />
<img width="1080" height="563" alt="image" src="https://github.com/user-attachments/assets/7574c899-7db6-4236-aaed-8b3a5ddd25c0" />
<img width="1179" height="532" alt="image" src="https://github.com/user-attachments/assets/423678a8-17e9-47c4-a6c2-68568a783c1f" />
<img width="1179" height="532" alt="image" src="https://github.com/user-attachments/assets/27cb37a3-f27d-4b59-8b26-7245a81d3cf6" />

---

 💡 Future Improvements

* Add full webpage scraping (RAG)
* Build Streamlit UI
* Add caching for performance
* Improve answer formatting

---

 🎯 Key Learnings

* Built an end-to-end AI agent
* Integrated APIs with LLM workflows
* Handled real-world debugging issues
* Applied prompt engineering

---

 📌 Conclusion

This project demonstrates how AI agents can combine **external data sources** with **LLMs** to provide meaningful, real-time insights - similar to real-world AI systems.

---
