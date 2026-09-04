# 🤖 Multi-Model AI Chatbot

A simple **multi-model AI chatbot** built with **Python, Streamlit, LangChain, and OpenRouter**.  
It allows users to switch between multiple AI models and chat with the selected model.

## ✨ Features

- 🤖 Chat with multiple AI models
- 🔄 Switch between models easily
- 💬 Maintains conversation history
- ⚡ Streaming AI responses
- 🧠 LangChain integration
- 🌐 OpenRouter API
- 🗑️ Clear conversation functionality
- 🔐 Secure API key management using `.env`

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web interface
- **LangChain** – LLM integration
- **OpenRouter** – AI model API
- **python-dotenv** – Environment variable management

## 🧠 Supported Models

| Model | Provider |
|-------|----------|
| DeepSeek V3 | DeepSeek |
| DeepSeek R1 | DeepSeek |
| Llama 3.3 70B Instruct | Meta |
| Llama 3.1 8B Instruct | Meta |
| Qwen 2.5 72B Instruct | Qwen |
| Qwen 2.5 Coder 32B Instruct | Qwen |

## 📁 Project Structure

```text
AI-Chatbot/
│
├── 📁 venv
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenRouter API key

Create a `.env` file in the project directory:

```env
OPENROUTER_API_KEY=your_api_key_here
```

> **Important:** Never commit your `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 Requirements

```
pip install -r requirements.txt
```

## 🔄 How It Works

```text
User
  ↓
Streamlit Interface
  ↓
Select AI Model
  ↓
LangChain
  ↓
OpenRouter API
  ↓
Selected AI Model
  ↓
Streaming Response
  ↓
Chat Interface
```

## 🚀 Future Improvements

- Add more AI models
- Add model-specific settings
- Add chat export functionality
- Add persistent conversation storage
- Add file/PDF chat support
- Improve UI customization

## 👨‍💻 Author & Developer

**Jaidev S**

⭐ If you like the project, consider giving the repository a star !