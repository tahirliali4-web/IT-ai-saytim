import streamlit as st
import pandas as pd

st.title("🌐 Universal IT Xəta Diaqnoz Sistemi")
st.write("Axtardığınız xəta kodunu aşağıda qeyd edin və diaqnoz alın:")

# Xəta bazası
xeta_bazasi = {
    404: {"ad": "Not Found (Sayt tapılmadı)", "təsir": "Şəbəkə", "həll": "URL ünvanını yoxlayın."},
    500: {"ad": "Internal Server Error", "təsir": "Sistem", "həll": "Server tərəfində problem var, adminə yazın."},
    403: {"ad": "Forbidden (İcazə yoxdur)", "təsir": "Təhlükəsizlik", "həll": "İstifadəçi hüquqlarınızı yoxlayın."},
    503: {"ad": "Service Unavailable", "təsir": "Sistem", "həll": "Server yüklənib, bir az sonra cəhd edin."},
    200: {"ad": "OK (Xəta yoxdur)", "təsir": "Normal", "həll": "Hər şey qaydasındadır."}
}

# Axtarış üçün qutu (Yan panel əvəzinə əsas səhifədə)
kod = st.number_input("Xəta kodunu daxil edin:", value=404)

if st.button("Diaqnoz et"):
    if kod in xeta_bazasi:
        xeta = xeta_bazasi[kod]
        st.success(f"Tapıldı: {xeta['ad']}")
        st.write(f"**Təsir dairəsi:** {xeta['təsir']}")
        st.info(f"**Həll yolu:** {xeta['həll']}")
    else:
        st.error("Bu xəta kodu bazamızda yoxdur.")

st.write("---")
# Bütün siyahını görmək üçün cədvəl
st.write("### 📚 Mövcud Xətaların Tam Siyahısı")
df = pd.DataFrame.from_dict(xeta_bazasi, orient='index')
st.table(df)
