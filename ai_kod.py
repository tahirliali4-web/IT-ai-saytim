import streamlit as st

# 30+ IT məlumatı olan nəhəng baza
it_bazasi = {
    "400": {"izah": "Bad Request (Yanlış sorğu).", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized (Giriş icazəsi yoxdur).", "meslehet": ["Düzgün şifrə daxil et", "Session-u yoxla"]},
    "403": {"izah": "Forbidden (Giriş qadağandır).", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found (Səhifə tapılmadı).", "meslehet": ["URL-i yoxla", "Səhifə silinib ola bilər"]},
    "405": {"izah": "Method Not Allowed (Metod qadağandır).", "meslehet": ["GET/POST metodunu yoxla"]},
    "408": {"izah": "Request Timeout (Sorğu vaxtı bitdi).", "meslehet": ["İnterneti yoxla", "Səhifəni yenilə"]},
    "500": {"izah": "Internal Server Error (Server xətası).", "meslehet": ["Serveri yenilə", "Loglara bax"]},
    "502": {"izah": "Bad Gateway (Keçid xətası).", "meslehet": ["Serveri restart et", "Bir az gözlə"]},
    "503": {"izah": "Service Unavailable (Xidmət yoxdur).", "meslehet": ["Serverin yüklənməsini yoxla"]},
    "504": {"izah": "Gateway Timeout (Keçid vaxtı bitdi).", "meslehet": ["DNS-i yoxla", "Serverin cavabını gözlə"]},
    "DNS": {"izah": "Ad həlli xətası (DNS Error).", "meslehet": ["DNS-i 8.8.8.8 et", "İnterneti yoxla"]},
    "SSL": {"izah": "SSL sertifikat xətası.", "meslehet": ["Tarixi yoxla", "Sertifikatı yenilə"]},
    "SyntaxError": {"izah": "Python Sintaksis səhvi.", "meslehet": ["Mötərizəni yoxla", "Dırnağı bağla"]},
    "NameError": {"izah": "Python dəyişən adı tapılmadı.", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Python tip uyğunsuzluğu.", "meslehet": ["Str və Int-i toplama", "Tipə diqqət et"]},
    "IndexError": {"izah": "Python siyahı indeksi səhvi.", "meslehet": ["Siyahının ölçüsünü yoxla"]},
    "KeyError": {"izah": "Python lüğət açarı xətası.", "meslehet": ["Açarın mövcudluğunu yoxla"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı.", "meslehet": ["Lazımsız proqramı bağla", "Restart et"]},
    "CPU": {"izah": "Prosessor həddən artıq yükləndi.", "meslehet": ["Task Manager-ə bax", "Soyutmanı yoxla"]},
    "HDD": {"izah": "Disk doludur.", "meslehet": ["Faylları sil", "Diski təmizlə"]},
    "Port 21": {"izah": "FTP bağlantı portu.", "meslehet": ["Firewall-u yoxla"]},
    "Port 22": {"izah": "SSH uzaqdan idarə portu.", "meslehet": ["Serverin açıq olduğundan əmin ol"]},
    "Port 80": {"izah": "HTTP web portu.", "meslehet": ["Server servisinin işlədiyini yoxla"]},
    "Port 3306": {"izah": "MySQL verilənlər bazası portu.", "meslehet": ["Bazanın işlədiyini yoxla"]},
    "BlueScreen": {"izah": "Windows sistem çökməsi.", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "AccessDenied": {"izah": "Fayla giriş qadağandır.", "meslehet": ["Administrator hüququ ilə aç"]},
    "Timeout": {"izah": "Əlaqə vaxtı bitdi.", "meslehet": ["İnterneti yoxla", "Serverin cavabını gözlə"]},
    "429": {"izah": "Too Many Requests (Həddən artıq sorğu).", "meslehet": ["Bir az gözlə", "Limitləri yoxla"]},
    "SQL-1064": {"izah": "SQL sintaksis xətası.", "meslehet": ["Sorğunu yoxla", "Dırnaqlara diqqət et"]},
    "Ping": {"izah": "Bağlantı yoxlanışı.", "meslehet": ["Serverin IP ünvanını yoxla"]},
    "Cache": {"izah": "Köhnə məlumatların saxlanması.", "meslehet": ["Brauzer cache-ini təmizlə"]}
}

st.set_page_config(page_title="IT Ensiklopediyası", page_icon="🌐")
st.title("🌐 IT Ensiklopediyası")

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
            break
    if not tapildi:
        st.error("Nəticə tapılmadı.")

st.write("---")
with st.expander("📂 Bazadakı 30+ kodun siyahısı:"):
    st.write(list(it_bazasi.keys()))

st.write("---")
st.write("### Problemin diaqnostika prosesi:")
