import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title = "AI Chatbot",
    page_icon = "🤖",
    layout = "centered"
)

# Simplified Supported Models Dictionary (Only Display Names -> IDs)
AVAILABLE_MODELS = {
    "DeepSeek V3": "deepseek/deepseek-chat",
    "Llama 3.3 70B Instruct": "meta-llama/llama-3.3-70b-instruct",
    "Llama 3.1 8B Instruct": "meta-llama/llama-3.1-8b-instruct",
    "Qwen 2.5 72B Instruct": "qwen/qwen-2.5-72b-instruct",
    "Qwen 2.5 Coder 32B Instruct": "qwen/qwen-2.5-coder-32b-instruct",
}

# Constants
TEMPERATURE = 0.7
SYSTEM_PROMPT = "You are a helpful, knowledgeable, and polite AI assistant. Provide concise and well-structured answers."
API_KEY = os.getenv("OPENROUTER_API_KEY")

# --- Main Application ---
st.title("🤖 Multi-Model AI Chatbot")

# Check for API Key early
if not API_KEY: 
    st.error("❌ OpenRouter API Key not found. Please add `OPENROUTER_API_KEY` to your `.env` file.")
    st.stop()

# Model Selection at the top
col1, col2 = st.columns([3, 1], vertical_alignment = "bottom")
with col1:
    selected_model_name = st.selectbox(
        "Select AI Model:",
        options = list(AVAILABLE_MODELS.keys()),
        index = 0
    )
with col2:
    if st.button("🗑️ Clear Conversation", use_container_width = True):
        st.session_state.messages = []
        st.rerun()

model_id = AVAILABLE_MODELS[selected_model_name]

# Intimate the user about the currently selected model
st.info(f"Currently chatting with: **{selected_model_name}**")
st.markdown("---")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to initialize LangChain ChatOpenAI configured for OpenRouter
def get_langchain_model(api_key: str, model_name: str, temp = float):
    return ChatOpenAI(
        model = model_name,
        api_key = api_key,
        base_url = "https://openrouter.ai/api/v1",
        temperature = 0.7,
        streaming = True
    )

# React to user input
prompt = st.chat_input("Ask a question...")

if prompt:
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using LangChain
    with st.chat_message("assistant"):
        try:
            # Initialize LangChain LLM
            llm = get_langchain_model(API_KEY, model_id, TEMPERATURE)
            
            # Build LangChain message list System Message + Conversational History
            langchain_messages = [SystemMessage(content=SYSTEM_PROMPT)]

            # Only send last 6 messages
            recent_messages = st.session_state.messages[-6:]

            for msg in recent_messages:
                if msg["role"] == "user":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    langchain_messages.append(AIMessage(content=msg["content"]))


            ''' # Build LangChain message list with System Message + Conversation History
            langchain_messages = [SystemMessage(content=SYSTEM_PROMPT)]
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    langchain_messages.append(AIMessage(content=msg["content"])) '''

            # Stream response token by token
            def stream_response():
                for chunk in llm.stream(langchain_messages):
                    if chunk.content:
                        yield chunk.content

            # Add the spinner while waiting for/generating the stream
            with st.spinner("Generating response..."):
                full_response = st.write_stream(stream_response())

            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error communicating with OpenRouter: {str(e)}")