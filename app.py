import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Set page config
st.set_page_config(page_title="Language Translator", page_icon="")

st.title("Language Translator App")
st.write("Translate text between 100+ languages using Google Translate.")

# Language selection
languages = list(LANGUAGES.values())
lang_codes = dict(LANGUAGES)

source_lang = st.selectbox("Translate from (source language)", languages, index=languages.index("english"))
target_lang = st.selectbox("Translate to (target language)", languages, index=languages.index("hindi"))

# Text input
text = st.text_area("Enter text to translate:")

# Translate button
if st.button(" Translate"):
    try:
        # Get language codes
        src_code = [code for code, lang in LANGUAGES.items() if lang == source_lang][0]
        dest_code = [code for code, lang in LANGUAGES.items() if lang == target_lang][0]

        # Translate
        translated = translator.translate(text, src=src_code, dest=dest_code)
        st.success("✅ Translated Text:")
        st.text_area("Result:", translated.text, height=100)
    except Exception as e:
        st.error(f" Error: {str(e)}")
