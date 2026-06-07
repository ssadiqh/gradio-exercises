"""
Exercise 2: Gradio Inputs and Outputs
Learn to use various Gradio input and output types.

Key Concepts:
- Common input types: Textbox, Slider, Dropdown, Checkbox, Radio, etc.
- Common output types: Textbox, Label, Markdown
- Examples parameter for pre-loaded examples
- Customizing input/output properties
"""

import gradio as gr


def story_builder(
    num_characters, character_type, locations, activity, time_of_day, is_adventure
):
    """Build a story based on user inputs."""
    locations_str = " and ".join(locations) if locations else "unknown place"
    activities_str = " and ".join(activity) if activity else "rested"

    story = f"""
Once upon a time, {num_characters} {character_type}s went to the {locations_str}.
They {activities_str} throughout the {time_of_day}.
{"This was quite an adventure!" if is_adventure else "It was a peaceful day."}
"""
    return story.strip()


def text_analyzer(text):
    """Analyze text and return statistics."""
    word_count = len(text.split())
    char_count = len(text)
    sentence_count = text.count(".") + text.count("!") + text.count("?")

    return {
        "Word Count": word_count,
        "Character Count": char_count,
        "Sentence Count": max(1, sentence_count),
        "Average Word Length": round(char_count / max(1, word_count), 2),
    }


# ============================================
# Exercise 2A: Story Builder with Multiple Input Types
# ============================================
def demo_story_builder():
    """Create an interface with various input types."""
    demo = gr.Interface(
        fn=story_builder,
        inputs=[
            gr.Slider(
                1, 10, value=3, step=1,
                label="Number of Characters",
                info="Choose between 1 and 10"
            ),
            gr.Dropdown(
                ["Wizard", "Knight", "Merchant", "Scholar"],
                value="Knight",
                label="Character Type",
                info="What type of character?"
            ),
            gr.CheckboxGroup(
                ["Forest", "Castle", "Village", "Mountain"],
                value=["Forest"],
                label="Locations",
                info="Where do they go? (Select multiple)"
            ),
            gr.Dropdown(
                ["Explored", "Battled", "Discovered", "Celebrated"],
                value=["Explored", "Discovered"],
                multiselect=True,
                label="Activities",
                info="What do they do? (Select multiple)"
            ),
            gr.Radio(
                ["Morning", "Afternoon", "Evening", "Night"],
                value="Afternoon",
                label="Time of Day",
                info="When does it happen?"
            ),
            gr.Checkbox(
                value=True,
                label="Is Adventure?",
                info="Is it an adventure story?"
            ),
        ],
        outputs=gr.Textbox(label="Your Story", lines=6),
        title="Story Builder",
        description="Create your own adventure story!",
        examples=[
            [3, "Knight", ["Castle", "Forest"], ["Battled", "Discovered"], "Evening", True],
            [5, "Wizard", ["Mountain"], ["Explored", "Celebrated"], "Night", False],
            [2, "Merchant", ["Village"], ["Discovered"], "Morning", False],
        ],
    )
    return demo


# ============================================
# Exercise 2B: Text Analyzer with Label Output
# ============================================
def demo_text_analyzer():
    """Create an interface with text analysis and label output."""
    demo = gr.Interface(
        fn=text_analyzer,
        inputs=gr.Textbox(
            label="Input Text",
            placeholder="Enter or paste your text here...",
            lines=5,
        ),
        outputs=gr.Label(label="Text Statistics"),
        title="Text Analyzer",
        description="Analyze text and get statistics",
        examples=[
            ["The quick brown fox jumps over the lazy dog."],
            ["Machine learning is fascinating. It powers many applications today!"],
        ],
    )
    return demo


# ============================================
# Main: Choose which demo to run
# ============================================
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "analyzer":
        # Run text analyzer demo
        demo = demo_text_analyzer()
        print("[LAUNCH] Launching Text Analyzer Demo...")
    else:
        # Run story builder demo (default)
        demo = demo_story_builder()
        print("[LAUNCH] Launching Story Builder Demo...")

    demo.launch(server_name="127.0.0.1", server_port=7860)
