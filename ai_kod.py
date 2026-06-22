import streamlit as st
from sklearn.tree import DecisionTreeClassifier

st.title("🛡️ AI İntellektual Xəta Diaqnozu")

# Məlumat bazasını genişləndiririk (Daha çox nümunə = Daha çox dəqiqlik)
# [Xəta_Kodu, Port]
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12], [404, 80], [503, 8080]]
# 0 = Şəbəkə, 1 = Sistem, 2 = Giriş/İcazə xətası
y_cavablar = [0, 0, 0, 1, 1, 1, 0, 1] 

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

# Yan panel (Sidebar) - Proqramı daha peşəkar edir
st.sidebar.header("Xəta Parametrləri")
xata_kodu = st.sidebar.number_input("Xəta Kodu:", value=10)
port = st.sidebar.number_input("Port:", value=80)

if st.sidebar.button("Analiz et"):
    texmin = model.predict([[xata_kodu, port]])
    
    st.subheader("Diaqnoz Nəticəsi:")
    
    if texmin[0] == 0:
        st.error("Nəticə: ŞƏBƏKƏ XƏTASI")
        st.write("Məsləhət: Router-i yoxlayın, internet kabelini çıxarıb taxın.")
    elif texmin[0] == 1:
        st.warning("Nəticə: SİSTEM XƏTASI")
        st.write("Məsləhət: Kompüteri yenidən başladın və RAM yaddaşını yoxlayın.")
    else:
        st.info("Nəticə: GİRİŞ/İCAZƏ XƏTASI")
        st.write("Məsləhət: Şifrənizi yoxlayın və ya administratorla əlaqə saxlayın.")

# Vizualizasiya - AI necə düşünür?
st.write("---")
st.write("Süni intellektin qərarvermə məntiqi:")
[attachment_0](attachment)
