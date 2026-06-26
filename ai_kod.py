import streamlit as st

# MƏLUMAT BAZASI: 100+ MADDƏ (Köhnələr + Yeni 20 əlavə)
it_bazasi = {
    # 1. WEB XƏTALARI
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
    
    # 3. PROQRAMLAŞDIRMA
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "IndexError": {"izah": "Siyahı indeksi xətası", "meslehet": ["Ölçünü yoxla"]},
    "KeyError": {"izah": "Lüğət açarı xətası", "meslehet": ["Açarın mövcudluğunu yoxla"]},
    "IndentationError": {"izah": "Boşluq xətası", "meslehet": ["Tab-ı yoxla"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla"]},
    "ConnectionError": {"izah": "Baza qoşulma xətası", "meslehet": ["Host adını yoxla"]},
    
    # 4. KİBER TƏHLÜKƏSİZLİK
    "Phishing": {"izah": "Fişinq hücumu", "meslehet": ["Linki açma", "Şifrəni dəyiş"]},
    "DDoS": {"izah": "Həddən artıq sorğu", "meslehet": ["WAF-ı aktivləşdir"]},
    "Ransomware": {"izah": "Fayllar şifrələnib", "meslehet": ["Antivirusla yoxla", "Back-up-dan bərpa et"]},
    "BruteForce": {"izah": "Şifrənin sındırılması", "meslehet": ["İki faktorlu doğrulamanı aç"]},
    "Malware": {"izah": "Zərərli proqram", "meslehet": ["Tam sistem skan et"]},
    "ZeroDay": {"izah": "Naməlum boşluq", "meslehet": ["Patch-ləri yenilə"]},
    "SQLi": {"izah": "SQL İnjektion hücumu", "meslehet": ["Sorğuları parametrli yaz"]},
    "XSS": {"izah": "Cross-site scripting", "meslehet": ["Input-ları filtrlə"]},
    "ManInTheMiddle": {"izah": "Ortadakı adam hücumu", "meslehet": ["VPN istifadə et"]},
    "DataBreach": {"izah": "Məlumat sızması", "meslehet": ["Bütün şifrələri dəyiş"]},

    # 5. ƏLAVƏLƏR
    "Timeout": {"izah": "Əlaqə vaxtı bitdi", "meslehet": ["Server cavabını gözlə"]},
    "Cache": {"izah": "Köhnə məlumatlar", "meslehet": ["Brauzer cache-ini təmizlə"]},
    "SSL": {"izah": "Təhlükəsizlik sertifikat səhvi", "meslehet": ["Tarixi yoxla"]},
    "AccessDenied": {"izah": "Giriş qadağandır", "meslehet": ["Admin hüququ ilə aç"]},
    "Port 80": {"izah": "HTTP portu məşğuldur", "meslehet": ["Servisi dayandır"]},
    "Port 3306": {"izah": "MySQL portu bağlıdır", "meslehet": ["Bazanı başlat"]},
    "KernelPanic": {"izah": "Linux sistem çökməsi", "meslehet": ["Logları oxu"]},
    "Deadlock": {"izah": "Baza kilidlənməsi", "meslehet": ["Tranzaksiyaları yoxla"]},
    "OutOfMemory": {"izah": "Proqram yaddaşı bitdi", "meslehet": ["Heap size-ı artır"]},
    "StackOverflow": {"izah": "Rekursiv funksiya xətası", "meslehet": ["Döngünü dayandır"]},
    "BadSector": {"izah": "Hard diskdə fiziki xəta", "meslehet": ["Diski dəyiş", "Backup al"]},
    "Latency": {"izah": "Şəbəkə gecikməsi", "meslehet": ["Ping-i yoxla", "Kabeli dəyiş"]},
    "PacketLoss": {"izah": "Paket itkisi", "meslehet": ["Routeri yoxla"]},
    "SMTP": {"izah": "E-mail göndərmə xətası", "meslehet": ["SMTP portunu yoxla"]},
    "SSH": {"izah": "Uzaqdan idarə xətası", "meslehet": ["SSH açarlarını yoxla"]},
    "BufferOverflow": {"izah": "Bufer daşması", "meslehet": ["Input uzunluğunu məhdudlaşdır"]},
    "SegmentFault": {"izah": "Yaddaşa icazəsiz giriş", "meslehet": ["Pointer-ləri yoxla"]},
    "RuntimeError": {"izah": "İş vaxtı xətası", "meslehet": ["Loglara bax", "Kodun məntiqini yoxla"]},
    "409": {"izah": "Conflict (Konflikt)", "meslehet": ["Mənbəni yenilə"]},
    "DiskFull": {"izah": "Serverin diski doludur", "meslehet": ["Logları sil", "Diski təmizlə"]},

    # 6. YENİ 20 MADDƏ
    "418": {"izah": "I'm a teapot", "meslehet": ["Bu bir zarafat kodudur, ciddi deyil"]},
    "422": {"izah": "Unprocessable Entity", "meslehet": ["JSON formatını yoxla"]},
    "508": {"izah": "Loop Detected", "meslehet": ["Yönləndirmə döngüsünü düzəlt"]},
    "InvalidToken": {"izah": "Token yararsızdır", "meslehet": ["Yenidən giriş edin"]},
    "SessionExpired": {"izah": "Sessiya müddəti bitdi", "meslehet": ["Səhifəni yenilə"]},
    "HardwareFailure": {"izah": "Avadanlıq nasazlığı", "meslehet": ["Servisə müraciət et"]},
    "Overheating": {"izah": "Həddən artıq qızma", "meslehet": ["Ventilyatoru yoxla"]},
    "BIOS-Error": {"izah": "BIOS/UEFI xətası", "meslehet": ["Batareyanı yoxla"]},
    "AP-Isolation": {"izah": "Wi-Fi cihazları bir-birini görmür", "meslehet": ["Router ayarını dəyiş"]},
    "BandwidthLimit": {"izah": "İnternet limiti aşıldı", "meslehet": ["Provayderlə əlaqə saxla"]},
    "DatabaseLocked": {"izah": "Baza kilidli", "meslehet": ["Prosesləri öldür"]},
    "FileCorrupted": {"izah": "Fayl xarab olub", "meslehet": ["Faylı yenidən yüklə"]},
    "MissingDLL": {"izah": "Kitabxana faylı çatışmır", "meslehet": ["Driveri yenilə"]},
    "DiskWriteError": {"izah": "Diskə yazmaq olmur", "meslehet": ["İcazələri yoxla"]},
    "NoRouteToHost": {"izah": "Host tapılmadı", "meslehet": ["İnterneti yoxla"]},
    "ConnectionRefused": {"izah": "Qoşulma rədd edildi", "meslehet": ["Portu yoxla"]},
    "RegistryLocked": {"izah": "Registry kilidli", "meslehet": ["Admin kimi aç"]},
    "ServiceTimeout": {"izah": "Servis gecikir", "meslehet": ["Serveri restart et"]},
    "SSLHandshake": {"izah": "SSL əlaqə qurulmadı", "meslehet": ["Sertifikatı yoxla"]},
    "PermissionDenied": {"izah": "İcazə yoxdur", "meslehet": ["Sudo/Admin hüququnu yoxla"]},
    
    # 7. DAHA 20 YENİ MADDƏ
    "406": {"izah": "Not Acceptable", "meslehet": ["Header məlumatını yoxla"]},
    "407": {"izah": "Proxy Authentication Required", "meslehet": ["Proxy şifrəsini daxil et"]},
    "410": {"izah": "Gone", "meslehet": ["Resurs birdəfəlik silinib"]},
    "411": {"izah": "Length Required", "meslehet": ["Content-Length əlavə et"]},
    "413": {"izah": "Payload Too Large", "meslehet": ["Fayl ölçüsünü kiçilt"]},
    "414": {"izah": "URI Too Long", "meslehet": ["URL-i qısalt"]},
    "415": {"izah": "Unsupported Media Type", "meslehet": ["Fayl formatını yoxla"]},
    "501": {"izah": "Not Implemented", "meslehet": ["Server metodu dəstəkləmir"]},
    "505": {"izah": "HTTP Version Not Supported", "meslehet": ["Protokolu yoxla"]},
    "507": {"izah": "Insufficient Storage", "meslehet": ["Serverdə yer boşalt"]},
    "511": {"izah": "Network Authentication Required", "meslehet": ["Wi-Fi girişini təsdiqlə"]},
    "Cloudflare-520": {"izah": "Web server boş cavab verdi", "meslehet": ["Server loglarına bax"]},
    "Cloudflare-521": {"izah": "Server əlaqəni rədd etdi", "meslehet": ["Firewall-ı yoxla"]},
    "Cloudflare-522": {"izah": "Connection Timed Out", "meslehet": ["Serveri yoxla"]},
    "Cloudflare-523": {"izah": "Origin is Unreachable", "meslehet": ["DNS-i yoxla"]},
    "Cloudflare-524": {"izah": "A Timeout Occurred", "meslehet": ["Sorğunun müddətinə bax"]},
    "Docker-Pull-Error": {"izah": "İmage yüklənmədi", "meslehet": ["Docker login et"]},
    "Git-Merge-Conflict": {"izah": "Fayllar toqquşdu", "meslehet": ["Kodları manuel birləşdir"]},
    "Jenkins-Build-Fail": {"izah": "Build uğursuz oldu", "meslehet": ["Pipeline koduna bax"]},
    "K8s-CrashLoop": {"izah": "Pod daim yenilənir", "meslehet": ["Pod loglarını yoxla"]}
}

st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (100+)")

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

st.write("---")
st.write("### Problemin diaqnostika prosesi:")
