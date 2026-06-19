import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# 1. Başlıq əlavə edirik
st.title("Süni İntellektlə Xəta Diaqnozu")

# 2. Məlumatlar (Modeli öyrədirik)
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12]]
y_cavablar = [0, 0, 0, 1, 1, 1] 

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

# 3. İstifadəçidən məlumat alırıq
xata_kodu = st.number_input("Xəta Kodu:", value=8)
port = st.number_input("Port:", value=80)

# 4. Düyməyə basanda proqnoz versin
if st.button("Analiz et"):
    yeni_problem = [[xata_kodu, port]]
    texmin = model.predict(yeni_problem)
    
    if texmin[0] == 0:
        st.error(f"Giriş {yeni_problem[0]} üçün AI Texmini: Bu bir ŞƏBƏKƏ xətasıdır!")
    else:
        st.success(f"Giriş {yeni_problem[0]} üçün AI Texmini: Bu bir SİSTEM xətasıdır!")
