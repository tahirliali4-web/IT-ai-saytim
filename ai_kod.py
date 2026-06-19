import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Səni məlumatların
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12]]
y_cavablar = [0, 0, 0, 1, 1, 1] 

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

# Yeni problemi yoxlayırıq
yeni_problem = [8, 80]
texmin = model.predict([yeni_problem])

# Ekranda göstərmək üçün st.write istifadə edirik
if texmin[0] == 0:
    st.write(f"Giris {yeni_problem} ucun AI Texmini: Bu bir SEBEKE xetasidir!")
else:
    st.write(f"Giris {yeni_problem} ucun AI Texmini: Bu bir SISTEM xetasidir!")
