# 🔧 Prompt Engineering Guide for LLMs

A hands-on repository showcasing **Prompt Engineering** techniques to optimize the performance of **Large Language Models (LLMs)**. This project includes structured prompt design, decoding strategies, and advanced reasoning techniques such as **Chain-of-Thought (CoT)** and **Self-Consistency**.

---

## 📌 What is Prompt Engineering?

**Prompt Engineering** is the process of crafting effective instructions or queries (prompts) to elicit accurate, relevant, and high-quality responses from LLMs like GPT, Gemini, Claude, or Mistral.

---

## 🚀 Project Highlights

- ✅ Experiment with **temperature**, **top-p**, **penalty**, **max_tokens**, and more decoding parameters  
- ✅ Apply **prompt templates** for different tasks: Q&A, summarization, classification, etc.  
- ✅ Test **short prompt techniques** like zero-shot, few-shot, and instruction-tuned prompts  
- ✅ Use **Chain-of-Thought (CoT)** reasoning to improve step-by-step thinking  
- ✅ Implement **Self-Consistency Decoding** for reliable results  
- ✅ Learn about **Out-of-Date Learning** limitations in LLMs

---

## 📚 Key Prompt Engineering Concepts

### 1. 📌 Prompt Elements
- **Instruction**: The command (e.g., *"Summarize the text below"*)
- **Context**: Background or additional data (e.g., a passage)
- **Input**: The user-provided query or task
- **Output Format**: Expected format of the result (e.g., JSON, bullet points)

> ✅ Tip: Be explicit, clear, and structured in your prompt.

---

### 2. 🧮 Decoding Parameters

| Parameter      | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `temperature`  | Controls randomness (0 = deterministic, 1+ = creative).                     |
| `top_p`        | Nucleus sampling – limits to top % of probable words (0.9 = focused).       |
| `max_tokens`   | Limits output length in tokens (e.g., 512, 2048).                           |
| `presence_penalty` | Discourages repetition of topics.                                       |
| `frequency_penalty`| Discourages repeating specific words.                                   |
| `model`        | The LLM used (e.g., `gpt-4`, `gemini-pro`, `claude-3`, `llama3`, etc.)      |

---

### 3. ⚡ Prompting Techniques

| Technique         | Description                                                                      |
|-------------------|----------------------------------------------------------------------------------|
| **Zero-Shot**      | Direct question without examples                                                |
| **Few-Shot**       | Add 1–3 examples to guide the model                                             |
| **Instruction Prompting** | Explicit tasks, e.g., "Write a Python function to..."                   |
| **Role Prompting** | Define roles, e.g., "You are an expert AI tutor..."                             |
| **Contextual Prompting** | Provide rich background or task-specific context                         |

---

## 🧠 Advanced Techniques

### ✅ Chain-of-Thought (CoT)
Encourages step-by-step reasoning to improve complex problem solving.

**Example Prompt:**
```text
Q: If there are 3 red balls and 2 blue balls in a bag, and I pick one at random, what’s the chance it's red?
A: Let’s think step by step.
