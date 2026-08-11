from deep_translator import GoogleTranslator
# =========================================================
# SUPPORTED LANGUAGES
# =========================================================
def get_supported_languages():
    """
    Returns the languages supported by the translator.
    """
    return {
        "English": "en",
        "Hindi": "hi",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Japanese": "ja",
        "Chinese (Simplified)": "zh-CN",
        "Korean": "ko",
        "Arabic": "ar",
        "Russian": "ru",
    }
# =========================================================
# TRANSLATE TEXT
# =========================================================
def translate_text(text, source, target):
    """
    Translate text using GoogleTranslator.
    """
    if not text or not text.strip():
        raise ValueError("Please enter some text.")
    if source == target:
        return text
    try:
        translator = GoogleTranslator(
            source=source,
            target=target
        )
        translated = translator.translate(text)
        if not translated:
            raise Exception("No translation was returned.")
        return translated
    except Exception as e:
        raise Exception(f"Translation failed: {e}")