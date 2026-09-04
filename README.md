# 🤖 Multi-Model AI Chatbot

A simple **Multi - Model AI Chatbot** built with **Python, Streamlit, LangChain and OpenRouter**.  
It allows users to switch between multiple AI models and chat with the selected model.

## ✨ Features

- 🤖 Chat with multiple AI models
- 🔄 Switch between models easily
- 💬 Maintains conversation history
- ⚡ Streaming AI responses
- 🗑️ Clear conversation functionality
- 🔐 Secure API key management

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **OpenRouter**

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
git clone https://github.com/JD-Jaidev/AI-CHATBOT
cd AI-CHATBOT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Add your OpenRouter API key

Create a `.env` file in the project directory:

```env
OPENROUTER_API_KEY = your_api_key_here
```

### 4. Run the application

```bash
streamlit run main.py
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