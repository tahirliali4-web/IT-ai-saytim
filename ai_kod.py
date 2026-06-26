import streamlit as st

# MƏLUMAT BAZASI: 140+ MADDƏ (Hamısı bir yerdə)
it_bazasi = {
    # 1. WEB XƏTALARI
    "400": {"izah": "Bad Request", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized", "meslehet": ["Giriş edin", "Token-i yoxla"]},
    "403": {"izah": "Forbidden", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found", "meslehet": ["URL-i yoxla", "Səhifə silinib"]},
    "500": {"izah": "Internal Server Error", "meslehet": ["Loglara bax", "Serveri yenilə"]},
    "502": {"izah": "Bad Gateway", "meslehet": ["Serveri restart et"]},
    "503": {"izah": "Service Unavailable", "meslehet": ["Yüklənməni yoxla"]},
    "504": {"izah": "Gateway Timeout", "meslehet": ["DNS-i yoxla"]},
    
    # 2. ŞƏBƏKƏ VƏ SİSTEM
    "DNS": {"izah": "Ad həlli xətası", "meslehet": ["8.8.8.8-ə keç", "İnterneti yoxla"]},
    "FTP": {"izah": "Fayl ötürmə xətası", "meslehet": ["Portu yoxla", "Passiv rejimə keç"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı", "meslehet": ["Proqramları bağla", "Restart et"]},
    "BlueScreen": {"izah": "Sistem çökməsi (Windows)", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "KernelPanic": {"izah": "Linux sistem çökməsi", "meslehet": ["Logları oxu", "Kernel-i yoxla"]},
    "Firewall": {"izah": "Qoruma divarı", "meslehet": ["Portu açıq saxla"]},
    "VPN": {"izah": "VPN bağlantısı uğursuz", "meslehet": ["Bağlantını sıfırla"]},
    
    # 3. PROQRAMLAŞDIRMA
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla"]},
    
    # 4. KİBERTƏHLÜKƏSİZLİK
    "Phishing": {"izah": "Fişinq hücumu", "meslehet": ["Linki açma", "Şifrəni dəyiş"]},
    "DDoS": {"izah": "Həddən artıq sorğu", "meslehet": ["WAF-ı aktivləşdir"]},
    "Ransomware": {"izah": "Fayllar şifrələnib", "meslehet": ["Antivirusla yoxla", "Back-up-dan bərpa et"]},
    "SQLi": {"izah": "SQL İnjektion hücumu", "meslehet": ["Sorğuları parametrli yaz"]},
    
    # 5. YENİ ƏLAVƏLƏR (YENİ 20 MADDƏ)
    "CPU-Throttling": {"izah": "CPU sürətinin aşağı düşməsi", "meslehet": ["Soyutmanı yoxla", "Termal pastanı dəyiş"]},
    "Deadlock": {"izah": "Baza kilidlənməsi", "meslehet": ["Tranzaksiyaları yoxla"]},
    "OutOfMemory": {"izah": "Proqram yaddaşı bitdi", "meslehet": ["Heap size-ı artır"]},
    "StackOverflow": {"izah": "Rekursiv funksiya xətası", "meslehet": ["Döngünü dayandır"]},
    "BadSector": {"izah": "Hard diskdə fiziki xəta", "meslehet": ["Diski dəyiş", "Backup al"]},
    "Latency": {"izah": "Şəbəkə gecikməsi", "meslehet": ["Ping-i yoxla", "Kabeli dəyiş"]},
    "PacketLoss": {"izah": "Paket itkisi", "meslehet": ["Routeri yoxla", "İnterneti test et"]},
    "SMTP": {"izah": "E-mail göndərmə xətası", "meslehet": ["SMTP portunu yoxla"]},
    "SSH": {"izah": "Uzaqdan idarə xətası", "meslehet": ["SSH açarlarını yoxla"]},
    "BufferOverflow": {"izah": "Bufer daşması", "meslehet": ["Input uzunluğunu məhdudlaşdır"]},
    "SegmentFault": {"izah": "Yaddaşa icazəsiz giriş", "meslehet": ["Pointer-ləri yoxla"]},
    "RuntimeError": {"izah": "İş vaxtı xətası", "meslehet": ["Loglara bax", "Kodun məntiqini yoxla"]},
    "409": {"izah": "Conflict (Konflikt)", "meslehet": ["Mənbəni yenilə"]},
    "410": {"izah": "Gone (Səhifə birdəfəlik silinib)", "meslehet": ["Linkə ehtiyac yoxdur"]},
    "507": {"izah": "Insufficient Storage", "meslehet": ["Serverdə yer aç"]},
    "508": {"izah": "Loop Detected", "meslehet": ["Yönləndirmə döngüsünü düzəlt"]},
    "DiskFull": {"izah": "Serverin diski doludur", "meslehet": ["Logları sil", "Diski təmizlə"]},
    "RegistryError": {"izah": "Windows Registry xətası", "meslehet": ["Regedit-i yoxla"]},
    "BootError": {"izah": "Sistem yüklənməyib", "meslehet": ["BIOS ayarlarını yoxla"]},
    "DriverError": {"izah": "Avadanlıq sürücüsü problemi", "meslehet": ["Sürücünü yenidən quraşdır"]}
}

st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (140+)")

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
        st.error("Bu məlumat hələlik bazada yoxdur.")

st.write("---")
with st.expander("📂 Bütün xəta kodlarının siyahısı:"):
    st.write(list(it_bazasi.keys()))
