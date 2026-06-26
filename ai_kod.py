import streamlit as st

# Məlumat bazası (Bütün köhnə və yeni məlumatlar buradadır)
it_bazasi = {
    # Web Xətaları
    "400": {"izah": "Bad Request (Yanlış sorğu).", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized (Giriş icazəsi yoxdur).", "meslehet": ["Login/Şifrəni yoxla", "Session-u yoxla"]},
    "403": {"izah": "Forbidden (Giriş qadağandır).", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found (Səhifə tapılmadı).", "meslehet": ["URL-i yoxla", "Səhifə silinib ola bilər"]},
    "405": {"izah": "Method Not Allowed.", "meslehet": ["GET/POST metodunu yoxla"]},
    "408": {"izah": "Request Timeout.", "meslehet": ["İnterneti yoxla", "Səhifəni yenilə"]},
    "429": {"izah": "Too Many Requests.", "meslehet": ["Bir az gözlə", "Limitləri yoxla"]},
    "500": {"izah": "Internal Server Error.", "meslehet": ["Server loglarına bax", "Kodu debug et"]},
    "502": {"izah": "Bad Gateway.", "meslehet": ["Serveri restart et", "Bir az gözlə"]},
    "503": {"izah": "Service Unavailable.", "meslehet": ["Server yükünü yoxla"]},
    "504": {"izah": "Gateway Timeout.", "meslehet": ["DNS-i yoxla", "Server cavabını gözlə"]},
    
    # Proqramlaşdırma
    "SyntaxError": {"izah": "Yazılış qaydası səhvi.", "meslehet": ["Mötərizəni yoxla", "Dırnağı bağla"]},
    "NameError": {"izah": "Dəyişən adı səhvi.", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu.", "meslehet": ["Str və Int-i toplama", "Tipə diqqət et"]},
    "IndexError": {"izah": "Siyahı indeksi səhvi.", "meslehet": ["Siyahı ölçüsünü yoxla"]},
    "KeyError": {"izah": "Lüğət açarı səhvi.", "meslehet": ["Açarın mövcudluğunu yoxla"]},
    "IndentationError": {"izah": "Boşluq xətası (Python).", "meslehet": ["Tab və ya boşluqları düzəlt"]},
    "AttributeError": {"izah": "Yanlış atribut.", "meslehet": ["Metodun adını yoxla"]},
    
    # Şəbəkə və Sistem
    "DNS": {"izah": "Ad həlli xətası.", "meslehet": ["8.8.8.8-ə keç", "İnterneti yoxla"]},
    "SSL": {"izah": "Təhlükəsizlik sertifikat səhvi.", "meslehet": ["Tarixi yoxla", "Sertifikatı yenilə"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı.", "meslehet": ["Lazımsız proqramı bağla", "Restart et"]},
    "CPU": {"izah": "Prosessor həddən artıq yükləndi.", "meslehet": ["Task Manager-ə bax"]},
    "HDD": {"izah": "Disk doludur.", "meslehet": ["Faylları sil", "Diski təmizlə"]},
    "FTP": {"izah": "Fayl ötürmə xətası.", "meslehet": ["Passiv rejimi yoxla", "Portu yoxla"]},
    "Firewall": {"izah": "Şəbəkə qoruma divarı.", "meslehet": ["Portun açıq olmasını yoxla"]},
    "BlueScreen": {"izah": "Windows sistem çökməsi.", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "AccessDenied": {"izah": "Giriş qadağandır.", "meslehet": ["Administrator kimi aç"]}
}

st.set_page_config(page_title="IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası")

axtaris = st.text_input("Axtarış (Xəta kodu və ya açar söz):").strip().lower()

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
        st.warning("Bu açar söz üzrə məlumat tapılmadı.")

st.write("---")
with st.expander("📂 Bazadakı bütün kodların siyahısı:"):
    st.write(list(it_bazasi.keys()))
