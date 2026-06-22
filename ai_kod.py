import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.title("🛡️ AI İntellektual Xəta Diaqnozu Pro")

# Məlumat bazası
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12], [404, 80], [503, 8080]]
y_cavablar = [0, 0, 0, 1, 1, 1, 0, 1] 

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

# Tarixçəni yadda saxlamaq üçün 'session_state' (sayt yenilənəndə məlumatı qoruyur)
if 'history' not in st.session_state:
    st.session_state.history = []

# Yan panel
st.sidebar.header("Xəta Parametrləri")
xata_kodu = st.sidebar.number_input("Xəta Kodu:", value=10)
port = st.sidebar.number_input("Port:", value=80)

if st.sidebar.button("Analiz et"):
    texmin = model.predict([[xata_kodu, port]])
    
    # Nəticəni müəyyən edirik
    if texmin[0] == 0:
        sonuc = "ŞƏBƏKƏ XƏTASI"
    elif texmin[0] == 1:
        sonuc = "SİSTEM XƏTASI"
    else:
        sonuc = "GİRİŞ XƏTASI"
    
    # Nəticəni tarixçəyə əlavə edirik
    st.session_state.history.append({"Xəta": xata_kodu, "Port": port, "Nəticə": sonuc})
    
    st.subheader("Diaqnoz Nəticəsi:")
    st.success(f"{sonuc} aşkarlandı!")

# Tarixçəni cədvəl şəklində göstər
st.write("---")
st.write("### 📜 Son Axtarışlar Tarixçəsi")
if st.session_state.history:
    df_history = pd.DataFrame(st.session_state.history)
    st.table(df_history)
else:
    st.write("Hələ ki, heç bir axtarış edilməyib.")
