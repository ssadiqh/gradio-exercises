# Gradio Exercises - Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Setup (One Time)

**Windows - Run in PowerShell:**
```powershell
cd "C:\Ai Projects\gradio-exercises"
.\install.bat
```

**macOS/Linux - Run in Terminal:**
```bash
cd gradio-exercises
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This creates a virtual environment and installs all dependencies.

## Step 2: Run From VS Code (Easiest!)

1. **Open the project in VS Code**
   ```
   File → Open Folder → Select gradio-exercises
   ```

2. **Wait for VS Code to recognize the venv** (first time takes 10 seconds)

3. **Run any exercise:**
   - Press `Ctrl+Shift+D` to open Debug/Run menu
   - Select the exercise you want (e.g., "Exercise 4: Advanced Chatbot")
   - Press `F5` or click the Play button

4. **Open your browser:** http://localhost:7860

## Step 3: Or Run From Terminal

```bash
python 4_advanced_chatbot.py
```

Then open: http://localhost:7860

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
