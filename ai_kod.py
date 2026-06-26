import streamlit as st

# Məlumat bazası: İndi strukturu daha etibarlı etdik
# Bura istədiyin qədər yeni sətir əlavə edə bilərsən
it_bazasi = {
    # 1xx - 3xx
    "200": {"izah": "Uğurlu (OK).", "meslehet": ["Sistem normal işləyir."]},
    "301": {"izah": "Daimi yönləndirmə.", "meslehet": ["Yeni linkə keçid edin."]},
    
    # 4xx - 5xx (Köhnə və yenilər bir yerdə)
    "400": {"izah": "Bad Request.", "meslehet": ["Sorğunu yoxlayın", "Parametrləri düzəldin"]},
    "401": {"izah": "Giriş icazəsi yoxdur.", "meslehet": ["Login və şifrəni yoxlayın"]},
    "403": {"izah": "Giriş qadağandır.", "meslehet": ["İcazələri yoxlayın"]},
    "404": {"izah": "Səhifə tapılmadı.", "meslehet": ["URL-i yoxlayın", "Səhifə silinib"]},
    "408": {"izah": "Sorğu vaxtı bitdi.", "meslehet": ["İnterneti yoxlayın"]},
    "429": {"izah": "Çoxsaylı sorğu.", "meslehet": ["Bir az gözləyin"]},
    "500": {"izah": "Server daxili xətası.", "meslehet": ["Loglara baxın", "Serveri yeniləyin"]},
    "502": {"izah": "Bad Gateway.", "meslehet": ["Serveri restart edin"]},
    "503": {"izah": "Xidmət əlçatan deyil.", "meslehet": ["Yüklənməni yoxlayın"]},
    
    # Sistem və Şəbəkə
    "DNS": {"izah": "Ad həlli xətası.", "meslehet": ["DNS 8.8.8.8-ə keçin", "İnterneti yoxlayın"]},
    "FTP": {"izah": "Fayl ötürmə xətası.", "meslehet": ["Portu və istifadəçi adını yoxlayın"]},
    "Wi-Fi": {"izah": "İnternet bağlantısı kəsilib.", "meslehet": ["Routeri restart edin"]},
    "BlueScreen": {"izah": "Windows çökdü.", "meslehet": ["RAM-ı yoxlayın", "Driverləri yeniləyin"]},
    
    # Proqramlaşdırma
    "SyntaxError": {"izah": "Yazılış səhvi.", "meslehet": ["Mötərizələri və iki nöqtəni yoxlayın"]},
    "NameError": {"izah": "Dəyişən adı tapılmadı.", "meslehet": ["Dəyişənin adını düzgün yazdığınızdan əmin olun"]}
}

st.set_page_config(page_title="IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası")

# Axtarış
axtaris = st.text_input("Axtarış üçün xəta kodunu və ya açar sözü daxil edin:").strip().lower()

if axtaris:
    tapildi = False
    for kod, melumat in it_bazasi.items():
        if axtaris in kod.lower() or axtaris in melumat['izah'].lower():
            st.subheader(f"✅ Nəticə: {kod}")
            st.info(f"İzahı: {melumat['izah']}")
            st.subheader("💡 Məsləhətlər:")
            for m in melumat['meslehet']:
                st.success(m)
            tapildi = True
    
    if not tapildi:
        st.warning("Bu mövzuda hələlik məlumat yoxdur. Bazanı genişləndirməyə davam edirik.")

st.write("---")
with st.expander("📂 Bazadakı bütün açar sözlər (Kodlar):"):
    st.write(list(it_bazasi.keys()))
