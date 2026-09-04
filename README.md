# AI Chatbot (LangChain + Streamlit + OpenRouter)

An interactive, multi-model AI chatbot built in **Python** using **LangChain** for orchestration and **Streamlit** for the web interface, seamlessly connected to **OpenRouter**.

## Features

- 🔄 **Model Switcher**: Switch between top open models dynamically before any question:
  - **DeepSeek**: DeepSeek V3 (`deepseek/deepseek-chat`), DeepSeek R1 (`deepseek/deepseek-r1`)
  - **Meta Llama**: Llama 3.3 70B (`meta-llama/llama-3.3-70b-instruct`), Llama 3.1 8B (`meta-llama/llama-3.1-8b-instruct`)
  - **Qwen**: Qwen 2.5 72B (`qwen/qwen-2.5-72b-instruct`), Qwen 2.5 Coder 32B (`qwen/qwen-2.5-coder-32b-instruct`)
- ⚡ **Real-time Streaming**: Token-by-token streaming responses powered by LangChain.
- 🔑 **Flexible API Configuration**: Reads `OPENROUTER_API_KEY` from `.env` or from sidebar UI input.
- 🎛️ **Customization**: Temperature tuning and editable system instructions.
- 🗑️ **Session Management**: Clear chat history at any time.

---

## Project Structure

```
AI-CHATBOT/
├── .env                # Local API keys (ignored by git)
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules (.env, __pycache__, venv, etc.)
├── main.py             # Streamlit application script
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## Getting Started

### 1. Prerequisites
- Python 3.10+ installed
- OpenRouter API key (get one from [OpenRouter](https://openrouter.ai/keys))

### 2. Setup Environment

Activate your virtual environment (or create one):
```powershell
# In PowerShell (Windows):
.\venv\Scripts\Activate.ps1
```

Install the dependencies:
```powershell
pip install -r requirements.txt
```

### 3. Configure API Key

Open `.env` in the root directory and add your key:
```env
OPENROUTER_API_KEY=sk-or-v1-your-actual-api-key-here
```
*(Alternatively, you can paste the API key directly in the Streamlit sidebar).*

### 4. Run the Chatbot

Start the Streamlit application:
```powershell
streamlit run main.py
```

Then open your browser at `http://localhost:8501`.
