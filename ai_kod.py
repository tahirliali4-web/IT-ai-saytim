import streamlit as st

# Məlumat və Məsləhət Bazası
xeta_bazasi = {
    "404": {
        "izah": "Səhifə tapılmadı. URL düzgün deyil və ya səhifə silinib.",
        "meslehet": "URL-i iki dəfə yoxla, ola bilsin ki, bir hərfi səhv yazmısan."
    },
    "500": {
        "izah": "Server daxili xətası. Proqramın arxa planında bir şey səhv getdi.",
        "meslehet": "Səhifəni yenilə, əgər düzəlməsə, server loglarına bax."
    },
    "Port 22": {
        "izah": "SSH (Secure Shell) portu. Serverə uzaqdan qoşulmaq üçün istifadə olunur.",
        "meslehet": "Əgər qoşula bilmirsənsə, firewall parametrlərini yoxla."
    }
}

st.title("IT Texniki Məsləhətçi 🤖")

kod = st.text_input("Xəta kodunu və ya Portu daxil et (məs: 404):")

if st.button("Analiz et"):
    if kod in xeta_bazasi:
        st.subheader("İzahı:")
        st.info(xeta_bazasi[kod]["izah"])
        
        st.subheader("Məsləhətim:")
        st.success(xeta_bazasi[kod]["meslehet"])
    else:
        st.warning("Bu kod məlumat bazamda yoxdur. Zəhmət olmasa başqa bir kod yoxla.")
