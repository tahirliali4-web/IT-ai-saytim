import streamlit as st

# Genişləndirilmiş IT məlumat bazası
it_bazasi = {
    "404": {"izah": "Səhifə tapılmadı.", "meslehet": ["URL-i yoxla", "Cache-i təmizlə", "Ana səhifəyə qayıt"]},
    "500": {"izah": "Server xətası.", "meslehet": ["Saytı yenilə", "Loglara bax", "Adminə yaz"]},
    "DNS": {"izah": "Ad həlli xətası.", "meslehet": ["İnterneti yoxla", "DNS 8.8.8.8-ə keç", "Flushdns et"]},
    "Port 22": {"izah": "SSH bağlantı xətası.", "meslehet": ["Serveri yoxla", "Firewall-u aç", "Key-ləri yoxla"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı.", "meslehet": ["Proqramları bağla", "RAM-ı artır", "Restart et"]},
    "CPU": {"izah": "Prosessor həddən artıq yüklənib.", "meslehet": ["Task Manager-ə bax", "İşə düşən proqramları yoxla"]},
    "Wi-Fi": {"izah": "İnternet bağlantısı kəsilib.", "meslehet": ["Routeri söndürüb yandır", "Wi-Fi parametrlərini yoxla", "Modemi resetlə"]}
}

st.set_page_config(page_title="IT Məsləhətçi Pro", page_icon="⚙️")
st.title("⚙️ IT Məsləhətçi Pro")

# Axtarış və ya Seçim
secim = st.selectbox("Xəta kodunu və ya mövzunu seçin:", list(it_bazasi.keys()))

if st.button("Analiz et"):
    data = it_bazasi[secim]
    st.subheader(f"🔍 İzahı: {data['izah']}")
    st.subheader("💡 Məsləhətlər:")
    for m in data['meslehet']:
        st.success(m)
