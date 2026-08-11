# 🌍 AI Language Translator

A simple, fast, and user-friendly web-based language translator built with **Python and Streamlit**. The application allows users to enter text, select source and target languages, translate the text instantly, and listen to the translated result using text-to-speech.

## 🚀 Live Demo

**Try the application:**
[https://ai-language-translator-kysbmxaiwexx4hd6wh8mvt.streamlit.app/](https://ai-language-translator-kysbmxaiwexx4hd6wh8mvt.streamlit.app/)

---

## ✨ Features

- 🌍 Translate text between multiple languages
- 📝 Simple text-based input
- 🔄 Source and target language selection
- ⚡ Fast translation using `deep-translator`
- 🔊 Listen to translated text using text-to-speech
- 📱 Mobile-friendly web interface
- 🎨 Clean and simple Streamlit UI
- ⚠️ Error handling for invalid or failed translations
- ☁️ Deployed online using Streamlit Community Cloud

## 🌐 Supported Languages

The current version supports:

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇫🇷 French
- 🇩🇪 German
- 🇪🇸 Spanish
- 🇯🇵 Japanese
- 🇨🇳 Chinese (Simplified)
- 🇰🇷 Korean
- 🇸🇦 Arabic
- 🇷🇺 Russian

---

## 🛠️ Technologies Used

| Technology                | Purpose                         |
| ------------------------- | ------------------------------- |
| Python                    | Core programming language       |
| Streamlit                 | Web application framework       |
| Deep Translator           | Text translation                |
| Google Translate          | Translation service             |
| gTTS                      | Text-to-speech pronunciation    |
| GitHub                    | Version control and source code |
| Streamlit Community Cloud | Application deployment          |

---

## ⚙️ How It Works

The application follows a simple workflow:

```text
User enters text
       ↓
Selects source language
       ↓
Selects target language
       ↓
Clicks Translate
       ↓
Deep Translator processes the text
       ↓
Translated text is displayed
       ↓
User can listen to the translation
```

---

## 📂 Project Structure

```text
AI-Language-Translator/
│
├── app.py
├── translator.py
├── styles.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit user interface, language selection, translation workflow, and pronunciation functionality.

### `translator.py`

Handles the translation functionality using `deep-translator`.

### `styles.py`

Contains custom CSS used to improve the appearance and responsiveness of the application.

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/priyanshirastogi08-cmd/ai-language-translator.git
```

### 2. Open the project directory

```bash
cd ai-language-translator
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

## 📦 Requirements

The project uses:

```text
streamlit
deep-translator
gTTS
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**, making it accessible through a public web URL without requiring a local Python environment.

### Live Application

[https://ai-language-translator-kysbmxaiwexx4hd6wh8mvt.streamlit.app/](https://ai-language-translator-kysbmxaiwexx4hd6wh8mvt.streamlit.app/)

---

## 🎯 Future Improvements

Possible future enhancements include:

- 🎤 Voice input
- 🔄 Automatic language detection
- 📋 Copy translated text
- 📄 Download translations
- 🌐 Support for additional languages
- 🌓 Dark/light mode
- 💬 Translation history
- 📱 Further mobile UI optimization

---

## 👩‍💻 Author

**Priyanshi Rastogi**

B.Tech Computer Science Engineering Student at Indian Institute of Information Technology Pune

### Internship Project

Developed as part of an **AI Internship at CodeAlpha**.

---

## ❤️ Acknowledgements

- Streamlit
- Deep Translator
- Google Translate
- gTTS

---

⭐ If you find this project useful, consider giving the repository a star!
