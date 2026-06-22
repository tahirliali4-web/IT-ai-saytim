import streamlit as st

st.title("🤖 İT Dəstək AI")

# Bilik bazası
bilik_bazasi = {
    "internet": "İnternet yoxdursa: Router-i yoxlayın, kabeli çıxarıb taxın.",
    "404": "404 xətası: Səhifə tapılmadı. URL ünvanını yoxlayın.",
    "donur": "Kompüter donursa, 'Ctrl + Shift + Esc' ilə Task Manager-i açıb proqramı bağlayın.",
    "şifrə": "Şifrəni unutmusunuzsa, 'Password Reset' bölməsindən bərpa edin."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("İT sualını yaz (məsələn: '404 xətası nədir?'):"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Ağıllı axtarış: Cümlənin içində açar sözləri axtarır
    cavab = "Bağışlayın, bu mövzuda məlumatım yoxdur."
    for acarsoz, melumat in bilik_bazasi.items():
        if acarsoz in prompt.lower():
            cavab = melumat
            break
            
    with st.chat_message("assistant"):
        st.markdown(cavab)
    st.session_state.messages.append({"role": "assistant", "content": cavab})
