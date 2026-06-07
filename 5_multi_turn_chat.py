"""
Exercise 5: Multi-Turn Conversational Chatbot
Create a chatbot with conversation memory that maintains context.

Key Concepts:
- Maintaining conversation history
- Conversation memory in LangChain
- gr.Chatbot component for chat interface
- Context-aware responses
- Clearing conversation history
"""

import gradio as gr
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage


# ============================================
# Initialize Model
# ============================================
def create_ollama_llm():
    """Create an Ollama LLM instance."""
    try:
        llm = OllamaLLM(
            model="qwen2.5:7b",
            base_url="http://localhost:11434",
            temperature=0.5,
        )
        return llm
    except Exception as e:
        print(f"Error: {e}")
        return None


# ============================================
# Conversation State Manager
# ============================================
class ConversationManager:
    """Manages conversation history and context."""

    def __init__(self, system_prompt="You are a helpful assistant."):
        self.system_prompt = system_prompt
        self.conversation_history = []
        self.llm = create_ollama_llm()

    def add_message(self, role, content):
        """Add a message to conversation history."""
        self.conversation_history.append({"role": role, "content": content})

    def get_formatted_history(self):
        """Format conversation history for the prompt."""
        formatted = []
        for msg in self.conversation_history:
            if msg["role"] == "user":
                formatted.append(HumanMessage(content=msg["content"]))
            else:
                formatted.append(AIMessage(content=msg["content"]))
        return formatted

    def generate_response(self, user_message):
        """Generate a response based on conversation history."""
        if not self.llm:
            return "Error: Ollama not initialized"

        try:
            # Add user message to history
            self.add_message("user", user_message)

            # Create prompt with history
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", self.system_prompt),
                    *[(m.type, m.content) for m in self.get_formatted_history()],
                ]
            )

            # Build full conversation string for Ollama
            history_text = "\n".join(
                [f"User: {msg['content']}" if msg["role"] == "user"
                 else f"Assistant: {msg['content']}"
                 for msg in self.conversation_history[:-1]]
            )

            full_prompt = f"""System: {self.system_prompt}

{history_text}
User: {user_message}
Assistant:"""

            response = self.llm.invoke(full_prompt)

            # Add assistant response to history
            self.add_message("assistant", response)

            return response

        except Exception as e:
            return f"Error: {str(e)}"

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []

    def get_history_for_display(self):
        """Get conversation history formatted for Gradio Chatbot."""
        history = []
        for msg in self.conversation_history:
            if msg["role"] == "user":
                history.append((msg["content"], None))
            else:
                # Fill in the previous user message with assistant response
                if history:
                    user_msg, _ = history[-1]
                    history[-1] = (user_msg, msg["content"])
        return history


# ============================================
# Initialize Conversation Manager
# ============================================
conversation_manager = ConversationManager(
    system_prompt="You are a helpful, friendly assistant. Keep responses concise and clear."
)


# ============================================
# Chat Function for Gradio
# ============================================
def chat_function(message, history):
    """
    Chat function that maintains conversation context.

    Args:
        message: The user's current message
        history: Previous conversation history from Gradio Chatbot

    Returns:
        The assistant's response
    """
    if not message.strip():
        return ""

    response = conversation_manager.generate_response(message)
    return response


# ============================================
# Gradio Interface with Chatbot Component
# ============================================
def create_chat_interface():
    """Create the multi-turn chatbot interface."""
    demo = gr.ChatInterface(
        fn=chat_function,
        examples=[
            "What is artificial intelligence?",
            "How do neural networks work?",
            "Tell me a joke",
            "What's the weather like? (I'm in New York)",
        ],
        title="Multi-Turn Conversational Chatbot",
        description="Chat with Qwen model. Conversation history is maintained across turns.",
        concurrency_limit=1,
    )
    return demo


# ============================================
# Alternative: Custom Interface with Clear Button
# ============================================
def create_custom_interface():
    """Create interface with manual clear button."""

    def clear_conversation():
        """Clear the conversation history."""
        conversation_manager.clear_history()
        return [], ""

    def respond(message, chat_history):
        """Process message and update chat history."""
        if not message.strip():
            return chat_history, ""

        # Generate response
        response = conversation_manager.generate_response(message)

        # Add to chat history
        chat_history.append([message, response])
        return chat_history, ""

    with gr.Blocks() as demo:
        gr.Markdown("# Multi-Turn Conversational Chatbot")
        gr.Markdown(
            "Chat with Qwen model. The chatbot remembers previous messages in the conversation."
        )

        chatbot = gr.Chatbot(label="Conversation", height=400)
        message_input = gr.Textbox(
            label="Your Message",
            placeholder="Type your message here...",
            lines=2,
        )

        with gr.Row():
            submit_btn = gr.Button("Send", variant="primary")
            clear_btn = gr.Button("Clear History", variant="secondary")

        # Submit button action
        submit_btn.click(
            respond,
            inputs=[message_input, chatbot],
            outputs=[chatbot, message_input],
        )

        # Clear button action
        clear_btn.click(
            clear_conversation,
            outputs=[chatbot, message_input],
        )

        # Allow Enter key to submit
        message_input.submit(
            respond,
            inputs=[message_input, chatbot],
            outputs=[chatbot, message_input],
        )

    return demo


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    import sys

    print("=" * 60)
    print("Multi-Turn Conversational Chatbot with Gradio")
    print("=" * 60)
    print("\nFeatures:")
    print("  * Conversation memory (remembers previous messages)")
    print("  * Context-aware responses")
    print("  * Multi-turn dialogue")
    print("  * Clear history button")
    print("\n" + "=" * 60)

    # Choose interface style
    if len(sys.argv) > 1 and sys.argv[1] == "custom":
        print("\n[LAUNCH] Launching Custom Interface...")
        demo = create_custom_interface()
    else:
        print("\n[LAUNCH] Launching ChatInterface...")
        demo = create_chat_interface()

    demo.launch(server_name="127.0.0.1", server_port=7860)
