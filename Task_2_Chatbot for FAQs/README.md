# 🎓 StudyBuddy — AI Study & Exam Preparation Assistant

**StudyBuddy** is an NLP-based FAQ chatbot designed to help students with common questions related to studying, exam preparation, revision, concentration, productivity, and learning techniques.

The application uses **TF-IDF vectorization and cosine similarity** to identify the FAQ question most similar to the user's query and return the corresponding answer.

## 🚀 Live Demo

🌐 **Try StudyBuddy online:**

[StudyBuddy — Live App](https://studybuddy-ai-faq-chatbot-dasvngkcqh27jordzzjajs.streamlit.app/)

The application is publicly deployed using **Streamlit Community Cloud** and can be accessed from a browser without installing Python or running the project locally.

---

## ✨ Features

* 🎓 Study and exam preparation assistance
* 🤖 NLP-based FAQ chatbot
* 🧠 TF-IDF-based text representation
* 🔍 Cosine similarity for FAQ matching
* 💬 Interactive chat interface
* 📚 20 predefined study-related FAQs
* 🛡️ Similarity threshold for unrelated questions
* 💡 Suggested questions for users
* 🗑️ Clear chat functionality
* ⏳ Loading indicator while processing questions
* 📱 Browser-based interface accessible from desktop and mobile devices
* ☁️ Public deployment using Streamlit Community Cloud

---

## 📚 Topics Covered

StudyBuddy currently provides answers related to:

* Effective studying
* Concentration and focus
* Pomodoro technique
* Procrastination
* Exam preparation
* Revision strategies
* Study schedules
* Memory improvement
* Note-taking
* Understanding difficult topics
* Study breaks
* Distractions
* Motivation
* Pre-exam preparation
* Programming exam preparation
* Mathematics exam preparation
* Problem-solving
* Active recall
* Learning strategies

The current knowledge base contains **20 predefined FAQs**.

---

## 🧠 How It Works

StudyBuddy uses a simple NLP-based information-retrieval approach.

```text
User enters a question
        ↓
Text preprocessing
        ↓
TF-IDF vectorization
        ↓
Cosine similarity calculation
        ↓
Find the most similar FAQ
        ↓
Check similarity threshold
        ↓
Return the relevant answer
```

### 1. User Input

The user enters a question through the Streamlit chat interface.

Example:

```text
How can I focus while studying?
```

### 2. Text Preprocessing

The chatbot preprocesses the input by:

* Converting text to lowercase
* Removing punctuation and special characters
* Removing unnecessary spaces

### 3. TF-IDF Vectorization

The FAQ questions and user query are converted into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

TF-IDF helps represent the importance of words and phrases within the FAQ dataset.

### 4. Cosine Similarity

The chatbot calculates the similarity between the user's question and the available FAQ questions using **cosine similarity**.

The FAQ with the highest similarity score becomes the candidate answer.

### 5. Similarity Threshold

A similarity threshold is used to prevent the chatbot from returning unrelated answers.

For example:

```text
User:
What is the capital of France?

StudyBuddy:
I'm sorry, I couldn't find a relevant answer to your question.
```

This keeps the chatbot focused on its intended **study-help domain**.

---

## 🛠️ Technologies Used

| Technology                | Purpose                            |
| ------------------------- | ---------------------------------- |
| Python                    | Core programming language          |
| Streamlit                 | Web application and chat interface |
| Scikit-learn              | TF-IDF and cosine similarity       |
| JSON                      | FAQ knowledge base                 |
| Regular Expressions       | Text preprocessing                 |
| Streamlit Community Cloud | Public deployment                  |
| GitHub                    | Source code and version control    |

---

## 📂 Project Structure

```text
StudyBuddy-AI-FAQ-Chatbot/
│
├── app.py
├── chatbot.py
├── faqs.json
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit interface, chat functionality, session state, user input handling, loading indicator, and sidebar.

### `chatbot.py`

Contains the NLP functionality, including:

* FAQ loading
* Text preprocessing
* TF-IDF vectorization
* Cosine similarity
* Similarity threshold
* Answer retrieval

### `faqs.json`

Contains the predefined study-related questions and their corresponding answers.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `README.md`

Contains the documentation and setup instructions for the project.

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/priyanshirastogi08-cmd/StudyBuddy-AI-FAQ-Chatbot.git
```

### 2. Open the project directory

```bash
cd StudyBuddy-AI-FAQ-Chatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Questions

Try asking StudyBuddy:

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
How can I improve my problem-solving skills?
```

StudyBuddy compares each query with its FAQ knowledge base and returns the most relevant response.

---

## 🎯 Project Objective

The objective of StudyBuddy is to demonstrate how **Natural Language Processing can be used to build a lightweight question-answering system** without relying on a generative AI API.

The project demonstrates practical concepts including:

* Text preprocessing
* Feature extraction
* TF-IDF
* Cosine similarity
* Information retrieval
* Similarity-based question matching
* Interactive chatbot development
* Web application deployment

---

## ☁️ Deployment

StudyBuddy is deployed using **Streamlit Community Cloud**.

### Public Application

[Open StudyBuddy](https://studybuddy-ai-faq-chatbot-dasvngkcqh27jordzzjajs.streamlit.app/?utm_source=chatgpt.com)

The deployed application allows users to access the chatbot directly through a web browser without requiring a local Python environment.

---

## 🔮 Future Improvements

Possible future enhancements include:

* 🎤 Voice input
* 🔊 Text-to-speech responses
* 📚 Larger and more diverse FAQ knowledge base
* 🌐 Multi-language support
* 🧠 Advanced NLP models
* 💾 Conversation history
* 📊 User analytics
* 🎯 Personalized study recommendations
* 📱 Further mobile UI optimization
* 📝 Study-plan generation
* ❓ Interactive quizzes
* 🧠 Flashcard generation

---

## 🎓 CodeAlpha Internship

This project was developed as part of the **CodeAlpha AI Internship**.

**Task:** FAQ Chatbot

The project demonstrates an NLP-based FAQ matching system using **TF-IDF and cosine similarity**, combined with an interactive Streamlit web interface and public cloud deployment.

---

## 👩‍💻 Author

**Priyanshi Rastogi**

B.Tech Computer Science Engineering Student
Indian Institute of Information Technology Pune

---

## ❤️ Acknowledgements

* Python
* Streamlit
* Scikit-learn
* Streamlit Community Cloud
* CodeAlpha
