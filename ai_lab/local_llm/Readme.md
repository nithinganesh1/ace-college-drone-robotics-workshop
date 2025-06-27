# 🧠 Running Local LLMs with Ollama
This folder contains demos and notes on how to run **Large Language Models (LLMs)** locally using [Ollama](https://ollama.com).
Participants explored various open-source models and compared their performance directly on their own systems.

---

## 🛠️ What is Ollama?

**Ollama** is a powerful tool for running LLMs locally on CPU/GPU.
It supports models like:

* LLaMA 2
* Mistral
* Gemma
* Phi
* Code LLMs (like `code-llama`)

---

## 🔧 Installing Ollama (Linux)

1. Open your terminal and run:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Then start Ollama service:

```bash
ollama serve
```

> If the service does not start automatically, you can manually start it using:

```bash
sudo systemctl start ollama
```

---

## 🚀 Running a Model

To run your first LLM (e.g., LLaMA 2):

```bash
ollama run llama2
```

This will download the model and start a chat session.

---

## 📦 Example Models Tested

We tested and compared these models in the workshop:

* `llama2`
* `mistral`
* `gemma`
* `deepseek`
* `phi`
* `codellama` (for code generation) ...

You can run any of them by:

```bash
ollama run mistral
ollama run deepseek-rf
ollama run gemma
ollama run phi
```

---

## 🔍 Comparing LLMs

We compared the models based on:

* Response speed
* Language understanding
* Code generation ability
* Accuracy on follow-up questions
* Resource usage (RAM/CPU)

---

## 🛠️ Useful Ollama Commands

### 🔍 List all available local models

```bash
ollama list
```

### ⬇️ Pull a new model from Ollama hub

```bash
ollama pull <model_name>
# Example:
ollama pull mistral
```

### ❌ Remove a model

```bash
ollama rm <model_name>
```

### 🧠 Show model info

```bash
ollama show <model_name>
```

### 📝 Run in one-shot mode (single message)

```bash
ollama run mistral -p "Explain what is cosine similarity in ML"
```

---

## 🤖 Advanced: Run Ollama via API

You can also access models using Python with the Ollama REST API or tools like `llama-cpp-python`.

---

## ✅ Learning Outcomes

* Understand how LLMs work offline
* Run and test open-source models without cloud dependency
* Compare performance across different architectures
* Use command-line and API-based interaction with LLMs

---

Ready to explore the world of open models on your own hardware! 💻🔥
