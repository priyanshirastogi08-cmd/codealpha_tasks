import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# =========================================================
# LOAD FAQ DATA
# =========================================================
def load_faqs():
    """
    Load FAQ questions and answers from faqs.json.
    """
    with open("faqs.json", "r", encoding="utf-8") as file:
        return json.load(file)
# =========================================================
# TEXT PREPROCESSING
# =========================================================
def preprocess_text(text):
    """
    Clean and normalize text before vectorization.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
# =========================================================
# FIND BEST FAQ MATCH
# =========================================================
def get_best_answer(user_question, threshold=0.20):
    """
    Find the FAQ most similar to the user's question
    using TF-IDF and cosine similarity.
    """
    faqs = load_faqs()
    if not user_question or not user_question.strip():
        return "Please enter a question."
    questions = [
        preprocess_text(faq["question"])
        for faq in faqs
    ]
    user_question = preprocess_text(user_question)
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        sublinear_tf=True
        )
    tfidf_matrix = vectorizer.fit_transform(
        questions + [user_question]
    )
    similarities = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )[0]
    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]
    if best_score < threshold:
        return (
            "I'm sorry, I couldn't find a relevant answer "
            "to your question. Try asking about study techniques, "
            "exam preparation, revision, concentration, "
            "time management, or learning strategies."
        )
    return faqs[best_match_index]["answer"]
# =========================================================
# TESTING
# =========================================================
if __name__ == "__main__":
    test_questions = [
        "How do I study better?",
        "How can I focus when studying?",
        "What is pomodoro?",
        "How do I stop wasting time?",
        "How should I prepare for exams?"
    ]
    for question in test_questions:
        answer = get_best_answer(question)
        print("\nQuestion:", question)
        print("Answer:", answer)