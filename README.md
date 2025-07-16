
# AI Agent Assistant with LangGraph, LangChain, Groq, and Streamlit

This project is an AI-powered automation system using `LangGraph` to orchestrate a workflow of modular AI agents for tasks like query classification, data retrieval, and response generation.

The project demonstrates an interactive **customer support chatbot UI** built with Streamlit, powered by Groq’s fast LLM API (e.g., Llama 3 70B).

---

## Features
- Modular AI agents:
  - Query classification (billing, technical, general)
  - Data retrieval by category
  - Response generation using `langchain_groq.ChatGroq`
- Workflow orchestration via `LangGraph` and `StateGraph`
- Async processing for fast responses
- Web-based chat UI using Streamlit’s native chat API (`st.chat_message`, `st.chat_input`)
- Easily extensible and production-ready

---

## Project structure
```plaintext
ai_agent_automation/
├── agents/
├── workflows/
├── utils/
├── tests/
├── app.py
├── .env
├── pyproject.toml          # Project dependencies for uv sync
└── README.md
```

---

## Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv):
  ```bash
  pip install uv
  ```

- Groq API key: [Get API Key](https://console.groq.com/)

---

## Setup

**Clone the repo:**
```bash
git clone https://github.com/masumbillah21/ai_agent_automation.git
cd ai_agent_automation
```

**Sync dependencies (auto-create env if needed):**
```bash
uv sync
```

**Configure environment variables:**  
Create a `.env` file in project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Usage

### Run chatbot UI:
```bash
uv run streamlit run app.py
```

It will generate a web url example: `http://localhost:8501/`

### Example queries:
- I want a refund for my last order.
- I’m getting an error when I try to log in.
- What are your business hours?

---

## Run tests:
```bash
uv run pytest
```

---

## Dependencies (declared in `pyproject.toml`):
- langchain>=0.3.26
- langchain-groq>=0.3.6
- langgraph>=0.5.3
- pydantic>=2.11.7
- pytest>=8.4.1
- pytest-asyncio>=1.1.0
- python-dotenv>=1.1.1
- streamlit>=1.46.1

---

## License
MIT License — free to use, modify, and distribute.
