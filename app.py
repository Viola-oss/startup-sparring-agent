import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Startup Sparring Agent", layout="centered")
st.title("🚀 KI Startup Sparring Agent")

st.markdown("Beschreibe deine **Geschäftsidee** oder dein **Business Model** unten. Die KI gibt dir Feedback, stellt kritische Fragen und schlägt ein MVP vor.")

user_input = st.text_area("📌 Deine Idee", height=200)

if st.button("💡 Analyse starten"):
    with st.spinner("KI denkt nach..."):
        prompt = f"""
Du bist ein erfahrener Startup-Mentor. Analysiere folgende Geschäftsidee:

\"{user_input}\"

1. Was sind die Stärken und Schwächen dieser Idee?
2. Welche kritischen Fragen sollte man stellen?
3. Was wäre ein konkreter MVP-Vorschlag?

Strukturiere deine Antwort in 3 Abschnitten.
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )

        output = response["choices"][0]["message"]["content"]
        st.markdown("### 🧠 KI-Feedback:")
        st.markdown(output)
