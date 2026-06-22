import streamlit as st
import google.generativeai as genai

# 1. Tətbiqə ad ver
st.title("Gemini AI Tətbiqi")

# 2. Açarın Secrets-də olub-olmadığını yoxla
if "GEMINI_API_KEY" in st.secrets:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        
        # Açarın 'AIza' ilə başlayıb-başlamadığını yoxlayan kiçik qoruyucu
        if not api_key.startswith("AIza"):
            st.error("Xəta: Açar 'AIza' ilə başlamalıdır! Sən hazırda düzgün olmayan bir açar (yəqin ki, 'AQ.' ilə başlayan) istifadə edirsən.")
        else:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            st.success("API açarı uğurla qəbul edildi!")
            
            # İndi botun işləməsi üçün kodunu bura yaza bilərsən
            user_input = st.text_input("Sualını yaz:")
            if user_input:
                response = model.generate_content(user_input)
                st.write(response.text)
                
    except Exception as e:
        st.error(f"Sistem xətası: {e}")
else:
    st.warning("Secrets-də 'GEMINI_API_KEY' tapılmadı. Lütfən, Streamlit-in 'Secrets' bölməsinə açarını əlavə et.")
