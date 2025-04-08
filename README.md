# 🔧 Gemma Code Generator

This is a command-line Python application that uses Google's **Gemma** (via `google.generativeai`) to generate code from natural language descriptions. Just type what kind of code you want, and the tool will generate it in real-time using the selected Gemma model.

## 🚀 Features

* Uses **Gemma (gemma-3-27b-it)** for high-quality code generation.
* Accepts natural language descriptions and generates structured code in response.
* Streamed output for real-time generation experience.
* Built-in prompt formatting and error handling.

## 📦 Requirements

* Python 3.7+
* Google Generative AI SDK (`google-generativeai`)

Install dependencies with:

```bash
pip install google-generativeai
```

## 🔑 API Key Setup

You must set your Google Generative AI API key as an environment variable:

```bash
export GEMINI_API_KEY=your_api_key_here
```

On Windows (Command Prompt):

```cmd
set GEMINI_API_KEY=your_api_key_here
```

## 🧠 Model Used

* **Model Name**: `gemma-3-27b-it`
* **Temperature**: `0.2` (for more deterministic output)

## 🛠️ How to Use

Run the script in a terminal:

```bash
python gemma_code_generator.py
```

Then follow the prompt and enter a code description like:

```
a function to check if a number is prime
```

Example output:

```
--- Gemma's Generated Code (gemma-3-27b-it) ---
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
--- End of Generation ---
```

---

## 📁 File Structure

```
gemma_code_generator.py # Main executable script
README.md # Project documentation
```

---

## 🧩 Functions Breakdown

- `generate_with_gemma(prompt_text)`: Handles the API call, streams, and prints the response.
- `build_code_generation_prompt(description, language)`: Formats the prompt with language-specific markdown.
- `__main__`: CLI input loop and generation orchestration.

---

## 🧪 Example Use Cases

- Prototype code snippets quickly
- Assist with boilerplate generation
- Learning assistant for beginners
- Idea-to-code conversion

---

## 🛡️ Error Handling

- Checks if the `GEMINI_API_KEY` is set.
- Handles stream interruptions or API issues gracefully.
- Displays appropriate messages when input is missing or invalid.

---

## 📄 License

MIT License. Feel free to use, modify, and contribute!

---

Let me know if you'd like a version with a badge setup (build status, version, etc.) or instructions for converting this into a GUI or web app!
