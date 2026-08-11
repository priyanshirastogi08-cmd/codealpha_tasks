import streamlit as st
from translator import (
    translate_text,
    get_supported_languages
)
from gtts import gTTS
from io import BytesIO
# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)
# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(
    """
    <style>
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 30px;
    }
    textarea {
        font-size: 17px !important;
    }
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
    }
    @media (max-width: 600px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }
        .main-title {
            font-size: 30px;
        }
        .subtitle {
            font-size: 15px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
# =========================================================
# SESSION STATE
# =========================================================
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "target_language" not in st.session_state:
    st.session_state.target_language = "Hindi"
# =========================================================
# TITLE
# =========================================================
st.markdown(
    '<div class="main-title">🌍 AI Language Translator</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Translate text between multiple languages instantly.</div>',
    unsafe_allow_html=True
)
# =========================================================
# LANGUAGES
# =========================================================
languages = get_supported_languages()
# =========================================================
# INPUT TEXT
# =========================================================
text = st.text_area(
    "📝 Enter Text",
    height=180,
    placeholder="Type something here..."
)
# =========================================================
# LANGUAGE SELECTION
# =========================================================
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox(
        "From",
        list(languages.keys())
    )
with col2:
    target = st.selectbox(
        "To",
        list(languages.keys()),
        index=1
    )
# =========================================================
# TRANSLATE BUTTON
# =========================================================
if st.button(
    "🚀 Translate",
    use_container_width=True
):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            with st.spinner("🌍 Translating..."):
                if source == target:
                    translated = text
                else:
                    translated = translate_text(
                        text,
                        languages[source],
                        languages[target]
                    )
            # Save result
            st.session_state.translated_text = translated
            st.session_state.target_language = target
            st.success("✅ Translation Completed!")
        except Exception as e:
            st.error(
                f"❌ Translation failed: {e}"
            )
# =========================================================
# TRANSLATED TEXT
# =========================================================
if st.session_state.translated_text:
    st.divider()
    st.subheader(
        f"🌍 {st.session_state.target_language}"
    )
    st.text_area(
        "Translated Text",
        value=st.session_state.translated_text,
        height=180,
        disabled=True
    )
    # =====================================================
    # PRONUNCIATION
    # =====================================================
    st.subheader("🔊 Pronunciation")
    if st.button(
        "🔊 Listen to Translation",
        use_container_width=True
    ):
        try:
            with st.spinner(
                "🔊 Generating pronunciation..."
            ):
                speech_code = languages[
                    st.session_state.target_language
                ]
                tts = gTTS(
                    text=st.session_state.translated_text,
                    lang=speech_code,
                    slow=False
                )
                audio = BytesIO()
                tts.write_to_fp(audio)
                audio.seek(0)
            st.audio(
                audio,
                format="audio/mp3"
            )
        except Exception as e:
            st.error(
                f"❌ Could not generate pronunciation: {e}"
            )
# =========================================================
# CLEAR
# =========================================================
if st.session_state.translated_text:
    if st.button(
        "🗑 Clear",
        use_container_width=True
    ):
        st.session_state.translated_text = ""
        st.rerun()
# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div style="
        text-align:center;
        color:#9ca3af;
        margin-top:40px;
        font-size:14px;
    ">
        🌍 AI Language Translator
    </div>
    """,
    unsafe_allow_html=True
)