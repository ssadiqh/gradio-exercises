# Gradio Exercises - Quick Start Guide

Get up and running in 5 minutes! 🚀

## 1️⃣ Prerequisites Check (1 min)

Make sure you have:
```bash
# Check Python version
python --version  # Should be 3.8+

# Check Ollama is installed
ollama --version

# Check Qwen model is available
ollama list  # Should show qwen2.5:7b
```

If Ollama or Qwen isn't installed:
```bash
# Install Ollama from https://ollama.ai
# Then download the model:
ollama pull qwen2.5:7b
```

## 2️⃣ Setup Virtual Environment (1 min)

**Windows:**
```bash
cd "C:\Ai Projects\gradio-exercises"
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
cd ~/path/to/gradio-exercises
python -m venv .venv
source .venv/bin/activate
```

## 3️⃣ Install Dependencies (1 min)

```bash
pip install -r requirements.txt
```

## 4️⃣ Start Ollama Server (In Separate Terminal)

Keep this running while you work:
```bash
ollama serve
```

You should see:
```
listening on 127.0.0.1:11434
```

## 5️⃣ Run Your First Exercise (2 min)

In your original terminal (with `.venv` activated):

```bash
python 1_gradio_intro.py
```

You should see:
```
🚀 Launching Sum Calculator Demo...
Running on http://127.0.0.1:7860
```

**Open your browser to:** http://localhost:7860

Try adding two numbers! 🧮

## Exercises at a Glance

| Exercise | File | Focus | Time |
|----------|------|-------|------|
| 1 | `1_gradio_intro.py` | Basic interfaces | 5 min |
| 2 | `2_gradio_inputs_outputs.py` | UI components | 10 min |
| 3 | `3_simple_chatbot.py` | LLM integration | 10 min |
| 4 | `4_advanced_chatbot.py` | System prompts | 15 min |
| 5 | `5_multi_turn_chat.py` | Conversation memory | 15 min |

## Common Commands

```bash
# Run exercise 1 (default: sum calculator)
python 1_gradio_intro.py

# Run exercise 1 sentence joiner variant
python 1_gradio_intro.py joiner

# Run exercise 2 (default: story builder)
python 2_gradio_inputs_outputs.py

# Run exercise 2 text analyzer variant
python 2_gradio_inputs_outputs.py analyzer

# Run exercise 3 (simple chatbot)
python 3_simple_chatbot.py

# Run exercise 4 (advanced chatbot)
python 4_advanced_chatbot.py

# Run exercise 5 ChatInterface style
python 5_multi_turn_chat.py

# Run exercise 5 custom blocks style
python 5_multi_turn_chat.py custom
```

## Stop an Exercise

Press `Ctrl+C` in the terminal running the script.

## Troubleshooting

### "Connection refused: http://localhost:11434"
→ Start Ollama in another terminal: `ollama serve`

### "Model not found: qwen2.5:7b"
→ Download the model: `ollama pull qwen2.5:7b`

### Port 7860 already in use
→ Edit the `.py` file, change `server_port=7860` to `server_port=7861`

### Virtual environment not activating
**Windows:** If you get a script execution error, run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

## Next Steps

1. ✅ Run Exercise 1 to see basic Gradio functionality
2. ✅ Run Exercise 2 to explore input/output types
3. ✅ Run Exercise 3 to see your first AI interface
4. ✅ Run Exercise 4 to learn prompt engineering
5. ✅ Run Exercise 5 to build conversational AI

Read `README.md` for detailed explanations of each exercise!

## Pro Tips

💡 **Experiment:** Change values in exercises (temperature, max_tokens) to see effects
💡 **Modify Code:** Add new input types or change system prompts
💡 **Read Comments:** Each exercise has detailed code comments explaining concepts
💡 **Test Edge Cases:** Try empty inputs, very long text, special characters

## Performance Expectations

- Exercise 1-2: Instant (no LLM)
- Exercise 3-5: 2-5 seconds per response (normal for Qwen2.5:7b)
  - If slower: Ensure Ollama has enough resources
  - If responses incomplete: Increase `max_tokens`

---

**Ready? Start with:** `python 1_gradio_intro.py`

For detailed learning, read `README.md` after running each exercise!
