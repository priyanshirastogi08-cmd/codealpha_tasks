import streamlit as st
from chatbot import get_best_answer
# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="StudyBuddy - AI Study Assistant",
    page_icon="🎓",
    layout="centered"
)
# =========================================================
# TITLE
# =========================================================
st.title("🎓 StudyBuddy")
st.caption("AI Study & Exam Preparation Assistant")
st.write(
    "Ask questions about study techniques, exam preparation, "
    "revision, concentration, productivity, and learning."
)
# =========================================================
# SESSION STATE
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []
# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# =========================================================
# USER INPUT
# =========================================================
user_question = st.chat_input(
    "Ask StudyBuddy a study-related question..."
)
# =========================================================
# PROCESS QUESTION
# =========================================================
if user_question:
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            answer = get_best_answer(user_question)
        st.write(answer)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.header("📚 StudyBuddy")
    st.write(
        "StudyBuddy uses NLP-based FAQ matching "
        "to find the most relevant answer to your question."
    )
    st.divider()
    st.subheader("💡 Try asking")
    st.write("• How can I study effectively?")
    st.write("• How can I concentrate while studying?")
    st.write("• What is the Pomodoro technique?")
    st.write("• How should I prepare for exams?")
    st.write("• How can I stop procrastinating?")
    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()