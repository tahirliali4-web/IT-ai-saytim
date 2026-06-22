import streamlit as st

st.title("🤖 İT Dəstək AI")

# Bizim İT bilik bazamız (Bura istənilən qədər məlumat əlavə et)
bilik_bazasi = {
    "internet": "İnternet yoxdursa: Router-i söndürüb 10 saniyə sonra yandırın və kabeli yoxlayın.",
    "xeta 404": "404 xətası ünvanın yanlış olması deməkdir. URL-i dəqiqləşdirin.",
    "sistem donur": "Kompyuter donursa, 'Ctrl + Shift + Esc' ilə Task Manager-i açıb donan proqramı bağlayın.",
    "şifrə": "Şifrənizi unutmusunuzsa, 'Password Reset' bölməsindən e-poçtunuzla bərpa edin."
}

# Söhbət tarixçəsini yadda saxla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Əvvəlki mesajları ekrana çıxar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# İstifadəçidən sual al
if prompt := st.chat_input("İT haqqında nəyi bilmək istəyirsən?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI-nin cavabı
    response = "Bağışlayın, bu mövzuda məlumatım yoxdur. Zəhmət olmasa 'internet', 'şifrə' və ya '404' kimi açar sözlərlə soruşun."
    
    # Bazanı yoxla
    for key in bilik_bazasi:
        if key in prompt.lower():
            response = bilik_bazasi[key]
            break
            
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
