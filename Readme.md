# AI Flowchart Maker

An interactive web application built with **Streamlit** that generates Mermaid syntax flowcharts from natural language prompts using a local **Ollama** LLM (Llama 3).

---

## Project Structure

* **`app.py`**: The main Streamlit web application interface.
* **`llm.py`**: Handles communication with the local Ollama API to generate flowchart code[cite: 2].
* **`prompts.py`**: Formats and structures prompts to enforce strict Mermaid syntax rules[cite: 3].
* **`chk.py`**: Utility script for handling Mermaid code rendering[cite: 1].
* **`requirements.txt`**: Lists all necessary Python package dependencies[cite: 2, 4].

---

## Prerequisites

1. **Python 3.8+** installed on your system.
2. **Ollama** installed locally ([Download Ollama](https://ollama.com/)).
3. The Llama 3 model pulled in Ollama:
   ```bash
   ollama pull llama3