# 🎓 StudyBuddy — AI Study & Exam Preparation Assistant

StudyBuddy is an **NLP-based FAQ chatbot** designed to help students with common questions related to studying, exam preparation, revision, concentration, productivity, and learning techniques.

The chatbot uses **TF-IDF vectorization and cosine similarity** to identify the FAQ question that is most similar to the user's query and returns the corresponding answer.

---

## 🚀 Live Demo

The application can be run locally using Streamlit.

```bash
streamlit run app.py
```

---

## ✨ Features

* 🤖 AI-based FAQ chatbot
* 🎓 Study and exam preparation assistance
* 🧠 NLP-based question matching
* 📊 TF-IDF text vectorization
* 🔍 Cosine similarity for finding the closest FAQ
* 💬 Interactive chat interface
* 📝 Predefined study FAQ knowledge base
* 🛡️ Similarity threshold to handle unrelated questions
* 💡 Suggested questions for users
* 🗑️ Clear chat functionality
* ⏳ Loading indicator while processing questions
* 📱 Responsive Streamlit interface

---

## 📚 Topics Covered

StudyBuddy currently provides answers related to:

* Effective studying
* Concentration
* Pomodoro technique
* Procrastination
* Exam preparation
* Study timetables
* Revision strategies
* Memory improvement
* Note-taking
* Understanding difficult topics
* Study breaks
* Distractions
* Motivation
* Pre-exam preparation
* Programming exam preparation
* Mathematics exam preparation
* Problem-solving skills
* Active recall

The chatbot currently contains **20 predefined FAQs**.

---

## 🧠 How It Works

StudyBuddy follows an NLP-based question-matching process.

```text
User enters a question
        ↓
Text preprocessing
        ↓
TF-IDF vectorization
        ↓
Cosine similarity calculation
        ↓
Find most similar FAQ
        ↓
Check similarity threshold
        ↓
Return the relevant answer
```

### 1. User Input

The user enters a study-related question through the Streamlit chat interface.

Example:

```text
How can I focus while studying?
```

### 2. Text Preprocessing

The chatbot:

* Converts text to lowercase
* Removes punctuation and special characters
* Removes unnecessary spaces

### 3. TF-IDF Vectorization

The FAQ questions and the user's question are converted into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

This allows the system to represent text numerically and compare the importance of words between questions.

### 4. Cosine Similarity

The system calculates the cosine similarity between the user's question and every FAQ question.

The FAQ with the highest similarity score is selected as the potential match.

### 5. Similarity Threshold

A similarity threshold is used to prevent the chatbot from returning an unrelated answer.

For example:

```text
User:
What is the capital of France?

StudyBuddy:
I'm sorry, I couldn't find a relevant answer to your question.
```

This makes the chatbot more reliable for its intended study-help domain.

---

## 🛠️ Technologies Used

| Technology          | Purpose                            |
| ------------------- | ---------------------------------- |
| Python              | Core programming language          |
| Streamlit           | Web application and chat interface |
| Scikit-learn        | TF-IDF and cosine similarity       |
| JSON                | FAQ knowledge base                 |
| Regular Expressions | Text preprocessing                 |

---

## 📂 Project Structure

```text
Task_2_StudyBuddy/
│
├── app.py
├── chatbot.py
├── faqs.json
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit user interface, chat history, user input handling, loading indicator, and sidebar.

### `chatbot.py`

Contains the main NLP functionality, including:

* FAQ loading
* Text preprocessing
* TF-IDF vectorization
* Cosine similarity
* Similarity threshold
* Answer retrieval

### `faqs.json`

Contains the predefined study-related questions and their corresponding answers.

### `requirements.txt`

Contains the Python libraries required to run the project.

### `README.md`

Contains project documentation and usage instructions.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/priyanshirastogi08-cmd/codealpha_tasks.git
```

### 2. Navigate to the StudyBuddy project

```bash
cd codealpha_tasks/Task_2_StudyBuddy
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The StudyBuddy chatbot will open in your web browser.

---

## 💬 Example Questions

Users can ask questions such as:

```text
How can I study effectively?
```

```text
How can I concentrate while studying?
```

```text
What is the Pomodoro technique?
```

```text
How can I stop procrastinating?
```

```text
How should I prepare for exams?
```

```text
How can I remember what I study?
```

```text
How can I improve my problem solving skills?
```

The chatbot identifies the most relevant FAQ and returns its predefined answer.

---

## 🎯 Project Objective

The objective of StudyBuddy is to demonstrate how **Natural Language Processing can be used to build a simple question-answering system** without requiring a generative language model.

The project focuses on:

* Text preprocessing
* Feature extraction
* NLP-based similarity
* Information retrieval
* Interactive chatbot development

---

## 🔮 Future Improvements

Possible future improvements include:

* 🎤 Voice input
* 🔊 Text-to-speech responses
* 📚 Larger FAQ knowledge base
* 🌐 Multi-language support
* 🧠 Advanced NLP models
* 💾 Conversation history
* 📊 User analytics
* 🎯 Personalized study recommendations
* 📱 Further mobile optimization
* 🔐 User accounts and personalized learning profiles

---

## 🎓 CodeAlpha Internship

This project was developed as part of the **CodeAlpha AI Internship**.

**Task:** FAQ Chatbot

The project demonstrates an NLP-based approach to FAQ matching using **TF-IDF and cosine similarity**.

---

## 👩‍💻 Author

**Priyanshi Rastogi**

B.Tech Computer Science Engineering Student
Indian Institute of Information Technology Pune

---

## ❤️ Acknowledgements

* Streamlit
* Scikit-learn
* Python
* CodeAlpha
