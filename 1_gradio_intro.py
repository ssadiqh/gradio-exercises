"""
Exercise 1: Introduction to Gradio
Learn the basics of Gradio by creating simple applications.

Key Concepts:
- gr.Interface() for creating simple interfaces
- Function mapping to inputs and outputs
- Launching a local server
"""

import gradio as gr


def add_numbers(num1, num2):
    """Simple function that adds two numbers."""
    return num1 + num2


def join_sentences(sentence1, sentence2):
    """Simple function that joins two sentences."""
    return f"{sentence1} {sentence2}"


# ============================================
# Exercise 1A: Sum Calculator
# ============================================
def demo_sum_calculator():
    """Create a simple sum calculator interface."""
    demo = gr.Interface(
        fn=add_numbers,
        inputs=[gr.Number(label="Number 1"), gr.Number(label="Number 2")],
        outputs=gr.Number(label="Sum"),
        title="Sum Calculator",
        description="Add two numbers together",
    )
    return demo


# ============================================
# Exercise 1B: Sentence Joiner
# ============================================
def demo_sentence_joiner():
    """Create a sentence joining interface."""
    demo = gr.Interface(
        fn=join_sentences,
        inputs=[
            gr.Textbox(label="First Sentence", placeholder="Enter first sentence..."),
            gr.Textbox(label="Second Sentence", placeholder="Enter second sentence..."),
        ],
        outputs=gr.Textbox(label="Combined Sentence"),
        title="Sentence Joiner",
        description="Combine two sentences together",
        examples=[
            ["Hello world", "How are you?"],
            ["The weather is", "beautiful today"],
        ],
    )
    return demo


# ============================================
# Main: Choose which demo to run
# ============================================
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "joiner":
        # Run sentence joiner demo
        demo = demo_sentence_joiner()
        print("🚀 Launching Sentence Joiner Demo...")
    else:
        # Run sum calculator demo (default)
        demo = demo_sum_calculator()
        print("🚀 Launching Sum Calculator Demo...")

    demo.launch(server_name="127.0.0.1", server_port=7860)
