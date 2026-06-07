"""
Exercise 4: Advanced Chatbot with System Prompts
Create a more sophisticated chatbot with:
- System prompts to customize behavior
- Temperature control for response creativity
- Max tokens control for response length
- Better error handling

Key Concepts:
- LangChain PromptTemplate for structured prompts
- Parameter tuning (temperature, max_tokens)
- Role-based prompting (system prompt engineering)
- Dynamic UI with variable inputs
"""

import gradio as gr
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate


# ============================================
# Initialize Model
# ============================================
def create_ollama_llm(temperature=0.5, max_tokens=256):
    """Create an Ollama LLM instance with specified parameters."""
    try:
        llm = OllamaLLM(
            model="qwen2.5:7b",
            base_url="http://localhost:11434",
            temperature=temperature,
            num_ctx=2048,  # Context window size
        )
        return llm
    except Exception as e:
        print(f"Error: {e}")
        return None


# ============================================
# Specialized Chatbot Functions
# ============================================
def create_system_prompt(role, style=""):
    """Create a system prompt based on the selected role."""
    prompts = {
        "General Assistant": "You are a helpful, friendly assistant. Answer questions clearly and concisely.",
        "Expert Tutor": "You are an expert tutor. Explain concepts in a way that helps people learn. Use examples when helpful.",
        "Creative Writer": "You are a creative writer. Write engaging, imaginative content. Be descriptive and expressive.",
        "Technical Expert": "You are a technical expert. Provide detailed, accurate explanations. Use technical terminology appropriately.",
        "Customer Support": "You are a friendly customer support agent. Help customers with their issues. Be empathetic and solutions-focused.",
    }
    return prompts.get(role, prompts["General Assistant"])


def advanced_chat(user_message, system_role, temperature, max_tokens):
    """
    Advanced chat function with role and parameter control.

    Args:
        user_message: The user's input
        system_role: The role/persona for the chatbot
        temperature: Creativity level (0.0-1.0)
        max_tokens: Maximum tokens in response

    Returns:
        The chatbot's response
    """
    if not user_message.strip():
        return "Please enter a message."

    try:
        # Create LLM with specified parameters
        llm = create_ollama_llm(temperature=temperature, max_tokens=max_tokens)

        if not llm:
            return "❌ Error: Could not initialize Ollama. Is it running?"

        # Create system prompt
        system_prompt = create_system_prompt(system_role)

        # Create prompt template
        prompt = PromptTemplate(
            template="""You are {role}.

{system_prompt}

User: {message}
Assistant:""",
            input_variables=["role", "system_prompt", "message"],
        )

        # Generate response
        formatted_prompt = prompt.format(
            role=system_role,
            system_prompt=system_prompt,
            message=user_message,
        )

        response = llm.invoke(formatted_prompt)
        return response

    except Exception as e:
        return f"❌ Error: {str(e)}\n\nMake sure Ollama is running: ollama serve"


# ============================================
# Gradio Interface with Advanced Options
# ============================================
def create_advanced_interface():
    """Create advanced chatbot interface with parameters."""
    demo = gr.Interface(
        fn=advanced_chat,
        inputs=[
            gr.Textbox(
                label="Your Message",
                placeholder="Ask me anything...",
                lines=3,
            ),
            gr.Dropdown(
                [
                    "General Assistant",
                    "Expert Tutor",
                    "Creative Writer",
                    "Technical Expert",
                    "Customer Support",
                ],
                value="General Assistant",
                label="Chatbot Role",
                info="Choose the personality/expertise",
            ),
            gr.Slider(
                0.0,
                1.0,
                value=0.5,
                step=0.1,
                label="Temperature (Creativity)",
                info="Lower = consistent, Higher = creative",
            ),
            gr.Slider(
                50,
                512,
                value=256,
                step=50,
                label="Max Response Length",
                info="Maximum tokens in response",
            ),
        ],
        outputs=gr.Textbox(
            label="Chatbot Response",
            lines=8,
        ),
        title="Advanced Local Ollama Chatbot",
        description="Chat with Qwen model with customizable roles and parameters. No API keys needed!",
        examples=[
            [
                "Explain machine learning to a beginner",
                "Expert Tutor",
                0.3,
                256,
            ],
            [
                "Write a short sci-fi story",
                "Creative Writer",
                0.8,
                256,
            ],
            [
                "What's wrong with my code?",
                "Technical Expert",
                0.5,
                256,
            ],
        ],
        allow_flagging="never",
    )
    return demo


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("Advanced Local Ollama Chatbot with Gradio")
    print("=" * 60)
    print("\n📋 Features:")
    print("  ✓ Multiple chatbot roles/personas")
    print("  ✓ Temperature control (creativity)")
    print("  ✓ Max token control (response length)")
    print("  ✓ System prompt engineering")
    print("  ✓ Error handling")
    print("\n" + "=" * 60)

    demo = create_advanced_interface()
    demo.launch(server_name="127.0.0.1", server_port=7860)
