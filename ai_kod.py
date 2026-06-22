import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.title("🛡️ AI İntellektual Xəta Diaqnozu Pro")

# Məlumat bazası
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12], [404, 80], [503, 8080]]
y_cavablar = [0, 0, 0, 1, 1, 1, 0, 1] 

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

# Tarixçəni yadda saxlamaq üçün
if 'history' not in st.session_state:
    st.session_state.history = []

# Yan panel
st.sidebar.header("Xəta Parametrləri")
xata_kodu = st.sidebar.number_input("Xəta Kodu:", value=10)
port = st.sidebar.number_input("Port:", value=80)

if st.sidebar.button("Analiz et"):
    texmin = model.predict([[xata_kodu, port]])
    
    if texmin[0] == 0:
        sonuc = "ŞƏBƏKƏ XƏTASI"
        meslehet = "Router-i yoxlayın, internet kabelini çıxarıb taxın."
    elif texmin[0] == 1:
        sonuc = "SİSTEM XƏTASI"
        meslehet = "Kompüteri yenidən başladın və RAM yaddaşını yoxlayın."
    else:
        sonuc = "GİRİŞ/İCAZƏ XƏTASI"
        meslehet = "Şifrənizi yoxlayın və ya administratorla əlaqə saxlayın."
    
    # Nəticəni ekranda göstər
    st.success(f"Diaqnoz: {sonuc}")
    st.write(f"**Məsləhət:** {meslehet}")
    
    # Tarixçəyə əlavə et
    st.session_state.history.append({"Xəta": xata_kodu, "Port": port, "Nəticə": sonuc})

# Yalnız cədvəli göstər
st.write("---")
st.write("### 📜 Son Axtarışlar Tarixçəsi")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.table(df)
