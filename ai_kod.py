import streamlit as st

# MƏLUMAT BAZASI (Buraya heç vaxt silinməyən 100+ maddəni yerləşdirəcəyik)
it_bazasi = {
    # 1. WEB XƏTALARI
    "400": {"izah": "Bad Request", "meslehet": ["URL-i yoxla", "Sorğu formatını düzəlt"]},
    "401": {"izah": "Unauthorized", "meslehet": ["Giriş edin", "Token-i yoxla"]},
    "403": {"izah": "Forbidden", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found", "meslehet": ["URL-i yoxla", "Səhifə silinib"]},
    "500": {"izah": "Internal Server Error", "meslehet": ["Serveri yenilə", "Loglara bax"]},
    "502": {"izah": "Bad Gateway", "meslehet": ["Serveri restart et", "Bir az gözlə"]},
    "503": {"izah": "Service Unavailable", "meslehet": ["Yüklənməni yoxla"]},
    "504": {"izah": "Gateway Timeout", "meslehet": ["DNS-i yoxla", "Server cavabını gözlə"]},
    
    # 2. ŞƏBƏKƏ VƏ SİSTEM
    "DNS": {"izah": "Ad həlli xətası", "meslehet": ["DNS-i 8.8.8.8 et", "İnterneti yoxla"]},
    "FTP": {"izah": "Fayl ötürmə xətası", "meslehet": ["Portu yoxla", "Passiv rejimə keç"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı", "meslehet": ["Proqramları bağla", "Restart et"]},
    "BlueScreen": {"izah": "Sistem çökməsi (Windows)", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "Ping": {"izah": "Bağlantı kəsilib", "meslehet": ["IP ünvanını yoxla"]},
    "Firewall": {"izah": "Qoruma divarı", "meslehet": ["Portu açıq saxla"]},
    
    # 3. PROQRAMLAŞDIRMA (PYTHON & SQL)
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla", "Sorğunu düzəlt"]},
    "ConnectionError": {"izah": "Bazaya qoşula bilmir", "meslehet": ["Host adını yoxla", "Şifrəni bax"]},
    
    # 4. ƏLAVƏ TERMİNLƏR
    "API": {"izah": "İnterfeys xətası", "meslehet": ["Endpoint-i yoxla", "Token-i yenilə"]},
    "Git": {"izah": "Versiya xətası", "meslehet": ["Merge konfliktini həll et"]},
    "Docker": {"izah": "Konteyner işə düşmür", "meslehet": ["Docker loglarına bax"]},
    "Cache": {"izah": "Köhnə məlumatlar", "meslehet": ["Brauzer cache-ini təmizlə"]}
}

# PROQRAM MƏNTİQİ
st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (Bütün məlumatlar bir yerdə)")

axtaris = st.text_input("Axtarış üçün xəta kodu və ya açar söz yazın:").strip().lower()

if axtaris:
    tapildi = False
    for kod, melumat in it_bazasi.items():
        if axtaris in kod.lower() or axtaris in melumat['izah'].lower():
            st.subheader(f"✅ Tapıldı: {kod}")
            st.info(f"İzahı: {melumat['izah']}")
            st.subheader("💡 Məsləhətlər:")
            for m in melumat['meslehet']:
                st.success(m)
            tapildi = True
    
    if not tapildi:
        st.error("Bu məlumat bazada yoxdur. Zəhmət olmasa aşağıdakı siyahıya baxın.")

st.write("---")
with st.expander("📂 Bazadakı bütün mövcud xəta kodları:"):
    st.write(list(it_bazasi.keys()))
