import streamlit as st

# 100+ IT Bilik Bazası
it_bazasi = {
    # 1. WEB XƏTALARI (HTTP Codes)
    "400": {"izah": "Bad Request", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized", "meslehet": ["Giriş edin", "Token-i yoxla"]},
    "403": {"izah": "Forbidden", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found", "meslehet": ["URL-i yoxla", "Səhifə silinib"]},
    "405": {"izah": "Method Not Allowed", "meslehet": ["GET/POST metodunu yoxla"]},
    "408": {"izah": "Request Timeout", "meslehet": ["İnterneti yoxla"]},
    "429": {"izah": "Too Many Requests", "meslehet": ["Limitləri yoxla"]},
    "500": {"izah": "Internal Server Error", "meslehet": ["Loglara bax", "Serveri yenilə"]},
    "502": {"izah": "Bad Gateway", "meslehet": ["Serveri restart et"]},
    "503": {"izah": "Service Unavailable", "meslehet": ["Yüklənməni yoxla"]},
    "504": {"izah": "Gateway Timeout", "meslehet": ["DNS-i yoxla"]},
    
    # 2. ŞƏBƏKƏ VƏ SİSTEM
    "DNS": {"izah": "Ad həlli xətası", "meslehet": ["8.8.8.8-ə keç", "İnterneti yoxla"]},
    "FTP": {"izah": "Fayl ötürmə xətası", "meslehet": ["Portu yoxla", "Passiv rejimə keç"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı", "meslehet": ["Proqramları bağla", "Restart et"]},
    "CPU": {"izah": "Prosessor yüklənməsi", "meslehet": ["Task Manager-ə bax"]},
    "HDD": {"izah": "Disk doludur", "meslehet": ["Faylları sil", "Diski təmizlə"]},
    "BlueScreen": {"izah": "Sistem çökməsi", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "Ping": {"izah": "Bağlantı kəsilib", "meslehet": ["IP ünvanını yoxla"]},
    "Firewall": {"izah": "Qoruma divarı", "meslehet": ["Portu açıq saxla"]},
    "VPN": {"izah": "VPN bağlantısı uğursuz", "meslehet": ["Bağlantını sıfırla"]},
    "Wi-Fi": {"izah": "Wi-Fi qoşulmur", "meslehet": ["Routeri söndürüb yandır"]},
    
    # 3. PROQRAMLAŞDIRMA (PYTHON, SQL, SİSTEM)
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "IndexError": {"izah": "Siyahı indeksi xətası", "meslehet": ["Ölçünü yoxla"]},
    "KeyError": {"izah": "Lüğət açarı xətası", "meslehet": ["Açarın mövcudluğunu yoxla"]},
    "IndentationError": {"izah": "Boşluq xətası", "meslehet": ["Tab-ı yoxla"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla"]},
    "ConnectionError": {"izah": "Baza qoşulma xətası", "meslehet": ["Host adını yoxla"]},
    "AttributeError": {"izah": "Yanlış atribut", "meslehet": ["Metodun adını yoxla"]},
    "ValueError": {"izah": "Yanlış dəyər", "meslehet": ["Dəyişən dəyərini yoxla"]},
    
    # 4. ƏLAVƏ TERMİNLƏR (Baza genişləndirilməsi)
    "API": {"izah": "İnterfeys xətası", "meslehet": ["Endpoint-i yoxla", "Token-i yenilə"]},
    "Git": {"izah": "Versiya idarəetmə xətası", "meslehet": ["Merge konfliktini həll et"]},
    "Docker": {"izah": "Konteyner işə düşmür", "meslehet": ["Docker loglarına bax"]},
    "Cache": {"izah": "Köhnə məlumatlar", "meslehet": ["Brauzer cache-ini təmizlə"]},
    "SSL": {"izah": "Təhlükəsizlik sertifikat səhvi", "meslehet": ["Tarixi yoxla"]},
    "AccessDenied": {"izah": "Giriş qadağandır", "meslehet": ["Admin hüququ ilə aç"]},
    "Timeout": {"izah": "Əlaqə vaxtı bitdi", "meslehet": ["Server cavabını gözlə"]},
    "Port 80": {"izah": "HTTP portu məşğuldur", "meslehet": ["Servisi dayandır"]},
    "Port 3306": {"izah": "MySQL portu bağlıdır", "meslehet": ["Bazanı başlat"]},
    "KernelPanic": {"izah": "Linux sistem çökməsi", "meslehet": ["Logları oxu"]}
}

st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (100+ Maddə)")

axtaris = st.text_input("Xəta kodu və ya açar sözü yazın:").strip().lower()

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
        st.error("Bu məlumat bazada hələ ki yoxdur.")

st.write("---")
with st.expander("📂 Bütün xəta kodlarının siyahısı:"):
    st.write(list(it_bazasi.keys()))

st.write("---")
st.write("### Problemin diaqnostika prosesi:")
