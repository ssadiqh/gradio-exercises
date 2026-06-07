"""
Exercise 3: Simple Chatbot with Local Ollama
Create a basic chatbot interface using local Ollama + Qwen model.

Key Concepts:
- Initializing OllamaLLM from LangChain
- Creating a simple prompt-response function
- Integrating LLM with Gradio Interface
- Error handling for connection issues
"""

import gradio as gr
from langchain_ollama import OllamaLLM


# ============================================
# Initialize the Local Ollama Model
# ============================================
def initialize_model():
    """Initialize the Ollama LLM with Qwen model."""
    try:
        llm = OllamaLLM(
            model="qwen2.5:7b",
            base_url="http://localhost:11434",
            temperature=0.5,
        )
        print("✅ Ollama model initialized successfully")
        return llm
    except Exception as e:
        print(f"❌ Error initializing model: {e}")
        print("Make sure Ollama is running: ollama serve")
        return None


# Initialize model globally
ollama_llm = initialize_model()


# ============================================
# Chatbot Function
# ============================================
def chat_with_ollama(user_message):
    """
    Send a message to the Ollama LLM and get a response.

    Args:
        user_message: The user's question or prompt

    Returns:
        The LLM's response
    """
    if not ollama_llm:
        return "❌ Error: Ollama model not initialized. Please start Ollama with: ollama serve"

    if not user_message.strip():
        return "Please enter a message."

    try:
        response = ollama_llm.invoke(user_message)
        return response
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nMake sure Ollama is running on http://localhost:11434"


# ============================================
# Gradio Interface
# ============================================
def create_chatbot_interface():
    """Create the Gradio interface for the chatbot."""
    demo = gr.Interface(
        fn=chat_with_ollama,
        inputs=gr.Textbox(
            label="Your Message",
            placeholder="Ask me anything...",
            lines=3,
        ),
        outputs=gr.Textbox(
            label="Chatbot Response",
            lines=5,
        ),
        title="Local Ollama Chatbot (Qwen2.5:7b)",
        description="Chat with Qwen model running locally via Ollama. No API keys needed!",
        examples=[
            ["What is machine learning?"],
            ["How do I learn Python?"],
            ["Explain quantum computing in simple terms"],
            ["What are the benefits of AI?"],
        ],
        allow_flagging="never",
    )
    return demo


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("Local Ollama Chatbot with Gradio")
    print("=" * 60)
    print("\n📋 Prerequisites:")
    print("  1. Ollama installed from https://ollama.ai")
    print("  2. Model downloaded: ollama pull qwen2.5:7b")
    print("  3. Ollama running: ollama serve (in another terminal)")
    print("\n" + "=" * 60)

    demo = create_chatbot_interface()
    demo.launch(server_name="127.0.0.1", server_port=7860)
