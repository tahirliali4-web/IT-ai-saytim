import streamlit as st
import google.generativeai as genai

st.title("🤖 Hər şeyi Bilən İT Köməkçisi")

# Konfiqurasiya
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Ən stabil modeli seçirik (daha dəqiq adla)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Xəta: {e}")
    st.stop()

# Söhbət funksiyası
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("İT sualını yaz..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Sualı göndəririk
        response = model.generate_content(prompt)
        cavab = response.text
    except Exception as e:
        # Əgər 404 xətası alsaq, bura düşəcək
        cavab = f"Model xətası: {e}. Zəhmət olmasa API açarınızın Google AI Studio-da 'Gemini API' üçün aktiv olduğundan əmin olun."
    
    with st.chat_message("assistant"):
        st.markdown(cavab)
    st.session_state.messages.append({"role": "assistant", "content": cavab})
