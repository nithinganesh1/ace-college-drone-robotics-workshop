# 🧠 Chatbot with NLP 
This module introduces how to build a basic chatbot using **AI, Machine Learning**, and **Natural Language Processing (NLP)** techniques.

---

## 🤖 What is AI and ML?

- **Artificial Intelligence (AI)** is the simulation of human intelligence by machines.
- **Machine Learning (ML)** is a subset of AI that allows systems to **learn from data** without being explicitly programmed.

---

## 🧩 Types of Machine Learning

1. **Supervised Learning** – Model is trained on labeled data.  
   _Example: Sentiment classification, spam detection_

2. **Unsupervised Learning** – Model finds patterns in data without labels.  
   _Example: Clustering, topic modeling_

3. **Reinforcement Learning** – Agent learns to make decisions through rewards and penalties.  
   _Example: Game AI, robotics movement control_

---

## 🗣️ What is NLP?

**Natural Language Processing (NLP)** is a field of AI that focuses on the interaction between computers and human languages.

Used for:
- Chatbots
- Language translation
- Sentiment analysis
- Voice assistants

---

## 🧹 NLP Preprocessing Steps

Text preprocessing is important before feeding text into an ML model.

### Basic Steps:
1. **Lowercasing** – Converts all characters to lowercase.
2. **Remove Punctuation** – Strips symbols like `!`, `?`, `.` etc.
3. **Tokenization** – Splits text into individual words or tokens.
4. **Stopword Removal** – Removes common words like "is", "the", "a", etc.
5. **Stemming** – Cuts words to their root form.  
   _Example: “running” → “run” (can be crude)_
6. **Lemmatization** – Converts word to dictionary form using context.  
   _Example: “better” → “good”_
7. **Named Entity Recognition (NER)** – Identifies names, dates, locations in text.  
   _Example: “Elon Musk founded Tesla in 2003.”_

---

## 📚 Intent Classification (for Chatbots)

- Every user message (input) is matched to an **intent** (like greeting, asking help, etc.)
- Intents are defined in a structured format (like txt)
- Machine Learning model is trained to classify messages into intents

---

## 🔍 Text Vectorization

Text needs to be converted into numerical format for training.

### Common Methods:

- **Bag of Words (BoW)** – Simple word count
- **TF-IDF (Term Frequency – Inverse Document Frequency)**  
  - Scores words based on their importance in a sentence vs entire dataset

---

## 📏 Matching Input & Response

Once text is vectorized, we can:
- Train a classifier (e.g., SVM, Logistic Regression)
- Or use **cosine similarity** to measure similarity between user input and stored examples

---

## 🛠️ This Project Includes:

- A chatbot using:
  - Rule-based + ML-based logic
  - NLP preprocessing (with `nltk`)
  - TF-IDF + cosine similarity for response selection

- Intent data in `ML.txt`
- Simple interface via command line

---

## ✅ Learning Outcomes

- Understand how chatbots use NLP
- Learn the core steps in processing human language
- Build your own intent-based assistant

---

## 📦 Requirements

Install with:

```bash
pip install nltk scikit-learn
