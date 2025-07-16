# AI Agent Automation with LangGraph, LangChain, and Groq

This project is an AI-powered automation system that uses `LangGraph` to orchestrate a workflow of modular AI agents for tasks like query classification, data retrieval, and response generation.  
The project demonstrates a **customer support assistant** as a use case, answering user queries with context-aware responses using Groq’s blazing-fast LLM API (e.g., Llama 3 70B).

---

## Features
- Modular AI agents:
  - Query classification (billing, technical, general)
  - Data retrieval based on query category
  - Response generation using `langchain_groq.ChatGroq`
- Workflow orchestration via `LangGraph` and `StateGraph`
- Async support for fast and concurrent execution
- Robust logging and easy extensibility

---

## Project structure

```plaintext
ai_agent_automation/
├── agents/                   # Modular agents
│   ├── classify_query.py
│   ├── retrieve_data.py
│   └── generate_response.py
├── workflows/                # Workflow graph definition
│   └── customer_support_graph.py
├── utils/                    # Logger utility
│   └── logger.py
├── tests/                    # Unit tests
├── main.py                   # Application entry point
├── .env                      # Environment variables (Groq API key)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## Prerequisites
- Python 3.10 or higher
- Groq API key: [Sign up at Groq Cloud](https://console.groq.com/)

---

## Setup instructions

1️⃣ **Clone the project:**
```bash
git clone https://github.com/masumbillah21/ai_agent_automation.git
cd ai_agent_automation
```

2️⃣ Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\\Scripts\\activate   # Windows
source venv/bin/activate  # Linux/macOS
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Add your Groq API key to .env:

```
GROQ_API_KEY=your_groq_api_key_here
```


▶️ Usage
Run the application:

```bash
python main.py
```
You’ll see a prompt:


Enter customer query:
Example queries:

I want a refund for my last order.

I’m getting an error when I try to log in.

What are your business hours?

The system will classify your query, retrieve a relevant response, and generate a concise AI-powered reply using Groq's Llama 3 model.

### Running tests
Unit tests are included for key agents and the workflow:

```bash
python -m pytest tests
```

### Notes
Ensure .env is properly loaded (main.py handles this using python-dotenv).

Uses latest StateGraph API from LangGraph >=0.0.40.

ResponseGeneratorAgent is async; ensure you run graph.ainvoke() in your workflow.

### License
MIT License — feel free to use, modify, and distribute.
