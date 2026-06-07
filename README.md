# Gradio Exercises - Interactive AI Interfaces

**Beginner-friendly hands-on exercises for building interactive web interfaces with Gradio and local LLMs**

Learn to create web-based interfaces for AI models using Gradio, from simple calculators to multi-turn conversational chatbots powered by local Ollama.

## What is Gradio?

Gradio is a Python library that lets you quickly create web-based interfaces for machine learning models and functions without needing to learn web development. It's perfect for:

- 🎯 Creating prototypes quickly
- 🤖 Sharing ML models with non-technical users
- 💬 Building chatbots and conversational interfaces
- 📊 Creating data analysis tools
- 🚀 Deploying models locally or to the cloud

## Prerequisites

### Required
- **Python 3.8+**
- **Ollama** installed from https://ollama.ai
- **Qwen2.5:7b** model: `ollama pull qwen2.5:7b`
- **Ollama running** in the background: `ollama serve`

### Verify Setup
```bash
# Test Ollama is running (in a new terminal)
curl http://localhost:11434/api/generate -d '{"model":"qwen2.5:7b","prompt":"hello"}'
```

## Quick Start

### 1. Setup (One Time)

**Windows:**
```powershell
cd "C:\Ai Projects\gradio-exercises"
.\install.bat
```

**macOS/Linux:**
```bash
cd gradio-exercises
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This creates a virtual environment and installs:
- **gradio** - Web interface framework
- **langchain** - LLM orchestration
- **langchain-ollama** - Local LLM integration
- **pydantic** - Data validation

### 2. Run Exercises

Make sure Ollama is running:
```bash
ollama serve
```

Then run any exercise:
```bash
python 1_gradio_intro.py
python 2_gradio_inputs_outputs.py
python 3_simple_chatbot.py
python 4_advanced_chatbot.py
python 5_multi_turn_chat.py
```

Open your browser to: **http://localhost:7860**

## Exercises Overview

### Exercise 1: Introduction to Gradio
**File:** `1_gradio_intro.py`

Learn the basics of creating Gradio interfaces.

**Concepts:**
- `gr.Interface()` for simple interfaces
- Mapping functions to inputs/outputs
- Running a local server
- Launching and testing

**Demos:**
- Sum Calculator: Add two numbers
- Sentence Joiner: Combine two sentences

**Run:**
```bash
# Sum calculator (default)
python 1_gradio_intro.py

# Or sentence joiner
python 1_gradio_intro.py joiner
```

---

### Exercise 2: Gradio Inputs and Outputs
**File:** `2_gradio_inputs_outputs.py`

Master common Gradio input and output types.

**Concepts:**
- Input types: Textbox, Slider, Dropdown, Checkbox, Radio, CheckboxGroup
- Output types: Textbox, Label, Markdown
- Examples parameter for pre-loaded samples
- Input customization and labeling

**Demos:**
- Story Builder: Create stories with multiple input types
- Text Analyzer: Analyze text and display statistics

**Input Types Used:**
| Input | Purpose | Example |
|-------|---------|---------|
| `Textbox` | Free text input | Questions, messages |
| `Slider` | Numeric range | Counts, ratings |
| `Dropdown` | Single/multi choice | Categories, selections |
| `Checkbox` | True/False toggle | Features, options |
| `Radio` | Exclusive choice | Single selection |
| `CheckboxGroup` | Multiple selection | Multiple choices |

**Run:**
```bash
# Story builder (default)
python 2_gradio_inputs_outputs.py

# Or text analyzer
python 2_gradio_inputs_outputs.py analyzer
```

---

### Exercise 3: Simple Chatbot with Local Ollama
**File:** `3_simple_chatbot.py`

Create your first LLM-powered chatbot with Gradio.

**Concepts:**
- Initializing OllamaLLM from LangChain
- Creating a prompt-response function
- Integrating LLM with Gradio
- Error handling for connection issues

**Features:**
- Clean, simple interface
- Pre-loaded example questions
- Error messages if Ollama isn't running
- No API keys required

**Run:**
```bash
python 3_simple_chatbot.py
```

**Ask It:**
- "What is machine learning?"
- "How do I learn Python?"
- "Explain quantum computing in simple terms"

---

### Exercise 4: Advanced Chatbot with System Prompts
**File:** `4_advanced_chatbot.py`

Build a sophisticated chatbot with role customization.

**Concepts:**
- System prompts for behavior control
- Role-based prompting (Expert Tutor, Creative Writer, etc.)
- Temperature control (creativity vs. consistency)
- Max tokens control (response length)
- LangChain PromptTemplate

**Features:**
- 5 selectable roles: General Assistant, Expert Tutor, Creative Writer, Technical Expert, Customer Support
- Temperature slider: 0.0 (consistent) to 1.0 (creative)
- Max response length control
- Role-specific system prompts

**Temperature Guide:**
| Temperature | Behavior | Use Case |
|---|---|---|
| 0.0 - 0.3 | Deterministic, focused | Factual answers, facts |
| 0.4 - 0.6 | Balanced | General questions |
| 0.7 - 1.0 | Creative, varied | Creative writing, ideas |

**Run:**
```bash
python 4_advanced_chatbot.py
```

**Try Different Roles:**
- Role: "Expert Tutor", Message: "Explain machine learning to a beginner"
- Role: "Creative Writer", Message: "Write a short sci-fi story"
- Role: "Technical Expert", Message: "What's wrong with my code?"

---

### Exercise 5: Multi-Turn Conversational Chatbot
**File:** `5_multi_turn_chat.py`

Create a chatbot that remembers conversation history.

**Concepts:**
- Conversation memory management
- Maintaining context across multiple turns
- `gr.ChatInterface` vs. custom `gr.Blocks` interface
- Conversation history formatting
- Clear history functionality

**Features:**
- Maintains conversation context
- Remembers previous messages
- Two interface styles (choose with argument)
- Clear history button
- Examples in the interface

**Run:**
```bash
# ChatInterface style (default)
python 5_multi_turn_chat.py

# Or custom interface with explicit clear button
python 5_multi_turn_chat.py custom
```

**Example Conversation:**
```
You: "What is AI?"
Bot: "AI is artificial intelligence..."

You: "Can you explain more?"
Bot: "Sure! Building on what I said..." (remembers context)

You: "Now explain deep learning"
Bot: "Deep learning is a subset of machine learning..." (uses conversation context)
```

---

## Gradio Components Reference

### Input Components

```python
import gradio as gr

# Text input
gr.Textbox(label="Name", placeholder="Enter name...")

# Numeric input
gr.Number(label="Age")

# Slider
gr.Slider(0, 100, value=50, step=1, label="Score")

# Dropdown (single selection)
gr.Dropdown(["Option A", "Option B"], label="Choice")

# Dropdown (multiple selection)
gr.Dropdown(["A", "B", "C"], multiselect=True, label="Choices")

# Checkbox
gr.Checkbox(label="Agree?")

# Radio (exclusive selection)
gr.Radio(["Yes", "No"], label="Answer")

# CheckboxGroup (multiple selection)
gr.CheckboxGroup(["A", "B", "C"], label="Select Multiple")
```

### Output Components

```python
# Text output
gr.Textbox(label="Result")

# Label (for classification)
gr.Label(label="Prediction")

# Markdown formatted output
gr.Markdown("# Title\n\nFormatted text")

# JSON display
gr.JSON()
```

### Interface Creation

```python
# Simple interface
demo = gr.Interface(
    fn=my_function,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
)

# Chat interface
demo = gr.ChatInterface(fn=chat_function)

# Custom blocks interface
with gr.Blocks() as demo:
    gr.Markdown("# Title")
    textbox = gr.Textbox(label="Input")
    button = gr.Button("Submit")
    output = gr.Textbox(label="Output")
    button.click(fn=my_function, inputs=textbox, outputs=output)
```

## Architecture Overview

```
User (Browser)
    ↓
Gradio Interface (gr.Interface / gr.ChatInterface)
    ↓
Python Function
    ↓
LangChain (PromptTemplate)
    ↓
OllamaLLM (Local HTTP Client)
    ↓
Ollama Server (localhost:11434)
    ↓
Qwen2.5:7b Model
    ↓
Response Back Through Stack
```

## Performance Tips

1. **Qwen2.5:7b Speed:** Expect 2-5 seconds per response on typical hardware
2. **Lower Temperature:** Faster with lower temperature (less sampling)
3. **Reduce Max Tokens:** Shorter max_tokens = faster responses
4. **Batch Requests:** Process multiple requests in sequence
5. **CPU vs GPU:** GPU acceleration significantly faster (if available)

## Common Issues and Solutions

### "Connection refused on port 11434"
**Solution:** Start Ollama in another terminal
```bash
ollama serve
```

### "Model not found: qwen2.5:7b"
**Solution:** Download the model
```bash
ollama pull qwen2.5:7b
```

### Port 7860 Already in Use
**Solution:** Change port in the code
```python
demo.launch(server_port=7861)  # Use different port
```

### Slow Responses
**Normal!** Qwen2.5:7b is a 7B parameter model. Responses take 2-5 seconds.
- If very slow, ensure Ollama has sufficient resources
- Try lower temperature (0.3 instead of 0.7)
- Reduce max_tokens

### Incomplete Responses (Exercise 4)
**Solution:** Increase max_tokens in the slider
- In Exercise 4, increase max_tokens to 512
- This allows longer responses before cutoff

## Understanding Temperature and Creativity

```
Temperature = 0.2 (Precise)
User: "Explain AI"
Response: "AI is artificial intelligence, a field of computer science..."

Temperature = 0.7 (Creative)
User: "Explain AI"
Response: "Imagine a digital mind learning from the world around it..."
```

## Next Steps After Exercises

### Basic Enhancements
1. **Add persistence:** Save conversations to file
2. **Add multiple models:** Switch between Qwen and other models
3. **Add response formatting:** Parse structured outputs

### Intermediate Enhancements
4. **Add RAG:** Retrieve documents before answering
5. **Add feedback system:** Thumbs up/down on responses
6. **Add analytics:** Track questions and response times

### Advanced Enhancements
7. **Multi-model comparison:** Compare responses from different models
8. **Add streaming:** Show responses as they generate
9. **Deploy to cloud:** Share publicly with Gradio Share

## Key Learning Outcomes

By completing these exercises, you'll understand:

✅ How to create web interfaces without HTML/CSS/JavaScript
✅ Gradio's input and output components
✅ Integrating local LLMs with interfaces
✅ System prompts and role-based prompting
✅ Maintaining conversation state
✅ Error handling in AI applications
✅ Parameter tuning (temperature, max_tokens)
✅ Deploying AI models for users to interact with

## Gradio vs. Flask (from genai_flask_app_local)

| Feature | Gradio | Flask |
|---------|--------|-------|
| Setup Time | 5 minutes | 30+ minutes |
| Learning Curve | Very easy | Moderate |
| Customization | Limited (good for prototypes) | Unlimited |
| Built-in Components | Yes (UI pre-built) | No (build your own) |
| Best For | Quick prototypes, demos | Production apps |

**Use Gradio for:** Quick demos, research prototypes, user testing
**Use Flask for:** Production applications, custom UX, complex workflows

## Further Reading

- [Gradio Documentation](https://www.gradio.app/)
- [Gradio Blocks Guide](https://www.gradio.app/guides/blocks-and-components)
- [LangChain Documentation](https://python.langchain.com/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Qwen Model Card](https://huggingface.co/Qwen/Qwen2.5-7B)

## Learning Checklist

After completing all 5 exercises, you should be able to:

- [ ] Create a simple Gradio interface with basic inputs/outputs
- [ ] Use different input types (Slider, Dropdown, Checkbox, etc.)
- [ ] Display different output types
- [ ] Integrate a local LLM (Ollama) with Gradio
- [ ] Use system prompts to customize chatbot behavior
- [ ] Control temperature and max_tokens for response quality
- [ ] Build a multi-turn conversational chatbot with memory
- [ ] Handle errors gracefully
- [ ] Explain the difference between prompt engineering and LLM selection
- [ ] Deploy a simple AI interface for others to use

## Exercise Difficulty Progression

```
Beginner → Intermediate → Advanced
    ↓
1. Gradio Intro (Simple interfaces)
    ↓
2. Inputs/Outputs (UI components)
    ↓
3. Simple Chatbot (LLM integration)
    ↓
4. Advanced Chatbot (Prompt engineering)
    ↓
5. Multi-Turn Chat (Conversation memory)
```

## Tips for Learning

1. **Run exercises sequentially** — Each builds on previous concepts
2. **Experiment with parameters** — Change temperature, max_tokens, roles
3. **Try different inputs** — Test edge cases and variations
4. **Read the code comments** — Each file has detailed explanations
5. **Modify examples** — Create your own input types and functions
6. **Break things intentionally** — Understand errors and solutions

## Important Notes

These exercises teach **learning and prototyping**. For production deployment, consider:

- ✅ Error handling and validation
- ✅ Rate limiting
- ✅ User authentication
- ✅ Response caching
- ✅ Monitoring and logging
- ✅ Scalable infrastructure
- ✅ Security hardening

## License

Educational - MIT License - Free to use and modify

## Notes

- All exercises run locally with no API keys
- Exercises 1-2 work without Ollama (pure Gradio)
- Exercises 3-5 require Ollama running
- Each exercise is self-contained and can be run independently
- Gradio interfaces auto-reload if you modify the code
- Stop any running exercise with `Ctrl+C`

---

**Start with Exercise 1 and work through sequentially for best learning outcomes!**

Last Updated: June 2026
Model: Qwen 2.5:7b (Local)
Framework: Gradio + LangChain
