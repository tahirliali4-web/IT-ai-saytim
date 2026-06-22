import streamlit as st
import google.generativeai as genai

st.title("🤖 Hər şeyi Bilən İT Köməkçisi")

# 1. API Açarını quraşdırırıq
# QEYD: API açarını Streamlit-in "Secrets" bölməsinə əlavə etməlisən
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("API açarı tapılmadı! Lütfən Streamlit Secrets-ə GEMINI_API_KEY əlavə edin.")

# 2. Söhbət tarixçəsini saxlayaq
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. İstifadəçidən sual alaq
if prompt := st.chat_input("İT və ya proqramlaşdırma ilə bağlı sualını yaz..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI-yə sualı göndər
    try:
        response = model.generate_content(f"Sən bir İT mütəxəssisisən. Bu suala ətraflı cavab ver: {prompt}")
        cavab = response.text
    except Exception as e:
        cavab = "Bağışlayın, hazırda cavab verə bilmirəm. API açarını yoxlayın."
    
    with st.chat_message("assistant"):
        st.markdown(cavab)
    st.session_state.messages.append({"role": "assistant", "content": cavab})
