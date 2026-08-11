def load_css():
    return """
    <style>
    /* ================================
       MAIN PAGE
    ================================= */
    .stApp {
        background: #f8fafc;
    }
    .block-container {
        max-width: 1100px;
        padding-top: 45px;
        padding-bottom: 40px;
    }
    /* ================================
       TITLE
    ================================= */
    .translator-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }
    .translator-subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 35px;
    }
    /* ================================
       LANGUAGE AREA
    ================================= */
    .language-label {
        font-size: 14px;
        font-weight: 600;
        color: #374151;
    }
    /* ================================
       TEXT AREAS
    ================================= */
    textarea {
        background-color: #ffffff !important;
        color: #111827 !important;
        border: 1px solid #d1d5db !important;
        border-radius: 14px !important;
        font-size: 18px !important;
        line-height: 1.5 !important;
    }
    textarea::placeholder {
        color: #9ca3af !important;
    }
    textarea:focus {
        border: 2px solid #4285f4 !important;
        box-shadow: 0 0 0 2px rgba(66, 133, 244, 0.12) !important;
    }
    /* ================================
       SELECT BOX
    ================================= */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-radius: 10px !important;
        color: #111827 !important;
    }
    /* ================================
       BUTTONS
    ================================= */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #d1d5db;
        background: #ffffff;
        color: #374151;
        font-weight: 600;
        min-height: 42px;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        border-color: #4285f4;
        color: #4285f4;
        background: #f8fbff;
    }
    /* ================================
       TRANSLATE BUTTON
    ================================= */
    .translate-button button {
        background: #4285f4 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 17px !important;
        font-weight: 600 !important;
        height: 48px !important;
    }
    .translate-button button:hover {
        background: #3367d6 !important;
    }
    /* ================================
       DIVIDER
    ================================= */
    hr {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 25px 0;
    }
    /* ================================
       FOOTER
    ================================= */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 14px;
        margin-top: 45px;
    }
    </style>
    """