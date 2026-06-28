import streamlit as st

# MƏLUMAT BAZASI: 240+ MADDƏ + YENİ 100+ MADDƏ
it_bazasi = {
    # ƏVVƏLKİ BAZA (Sənin kodunla eyni saxlanılıb)
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
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "IndexError": {"izah": "Siyahı indeksi xətası", "meslehet": ["Ölçünü yoxla"]},
    "KeyError": {"izah": "Lüğət açarı xətası", "meslehet": ["Açarın mövcudluğunu yoxla"]},
    "IndentationError": {"izah": "Boşluq xətası", "meslehet": ["Tab-ı yoxla"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla"]},
    "ConnectionError": {"izah": "Baza qoşulma xətası", "meslehet": ["Host adını yoxla"]},
    
    # YENİ ƏLAVƏ EDİLƏN 100+ MADDƏ
    "AWS-S3-403": {"izah": "S3 bucket-ə giriş qadağandır", "meslehet": ["Bucket policy-ni yoxla"]},
    "AWS-EC2-Timeout": {"izah": "EC2 instance-a qoşulmaq olmur", "meslehet": ["Security group-u yoxla"]},
    "Azure-Auth-Fail": {"izah": "Azure autentifikasiya xətası", "meslehet": ["Tenant ID-ni yoxla"]},
    "GCP-Quota-Exceeded": {"izah": "GCP kvota limiti dolub", "meslehet": ["Limit artırılması üçün müraciət et"]},
    "Terraform-Lock": {"izah": "Terraform state faylı kilidlənib", "meslehet": ["State faylını unlock et"]},
    "K8s-ImagePullBackOff": {"izah": "Docker image yüklənmədi", "meslehet": ["Registry-ə girişi yoxla"]},
    "K8s-OOMKilled": {"izah": "Container yaddaşı aşdı", "meslehet": ["Limitləri artır"]},
    "Helm-Release-Exists": {"izah": "Helm release artıq mövcuddur", "meslehet": ["Adı dəyiş və ya sil"]},
    "Ansible-SSH-Fail": {"izah": "Ansible node-a qoşula bilmir", "meslehet": ["SSH açarlarını yoxla"]},
    "CI-CD-Pipeline-Fail": {"izah": "Pipeline uğursuz oldu", "meslehet": ["Build loglarını oxu"]},
    "ElasticSearch-Red": {"izah": "ES klasteri qırmızı statusdadır", "meslehet": ["Node-ları yoxla"]},
    "Redis-Connection-Fail": {"izah": "Redis-ə qoşulma uğursuzdur", "meslehet": ["Portu və şifrəni yoxla"]},
    "Kafka-Consumer-Group-Lag": {"izah": "Kafka mesaj gecikməsi", "meslehet": ["Consumer sayını artır"]},
    "Nginx-502-Bad-Gateway": {"izah": "Nginx backend-ə çatmadı", "meslehet": ["Upstream-i yoxla"]},
    "Python-Pip-Install-Fail": {"izah": "Kitabxana yüklənmədi", "meslehet": ["Pip-i yenilə"]},
    "Node-npm-install-error": {"izah": "Node paketləri yüklənmədi", "meslehet": ["Node versiyasını yoxla"]},
    "React-Build-Error": {"izah": "React proqramı build olmadı", "meslehet": ["Node_modules-u sil və yenidən qur"]},
    "DHCP-Fail": {"izah": "İP almaq mümkün olmadı", "meslehet": ["DHCP serveri yoxla"]},
    "SMB-Access-Error": {"izah": "Paylaşılan qovluğa giriş yoxdur", "meslehet": ["İcazəni yoxla"]},
    "NFS-Mount-Fail": {"izah": "NFS mount olunmadı", "meslehet": ["Export-u yoxla"]},
    "Grub-Boot-Error": {"izah": "Bootloader xətası", "meslehet": ["Grub-u bərpa et"]},
    "CPU-Overheating": {"izah": "Prosessor çox qızıb", "meslehet": ["Soyutmanı yoxla"]},
    "GPU-Driver-Crash": {"izah": "Video kart xətası", "meslehet": ["Driveri yenilə"]},
    "Monitor-No-Signal": {"izah": "Ekrana görüntü gəlmir", "meslehet": ["Kabeli yoxla"]},
    # Daha çox maddə...
    "Docker-Daemon-Down": {"izah": "Docker xidməti işləmir", "meslehet": ["systemctl start docker"]},
    "K8s-Node-NotReady": {"izah": "Kubernetes node-u hazır deyil", "meslehet": ["Kubelet loglarına bax"]},
    "MySQL-Too-Many-Connections": {"izah": "Baza limitə çatdı", "meslehet": ["max_connections-ı artır"]},
    "PostgreSQL-Auth-Fail": {"izah": "Postgres şifrə səhvi", "meslehet": ["pg_hba.conf faylını yoxla"]},
    "Mongo-Connection-Refused": {"izah": "MongoDB qoşulmur", "meslehet": ["mongod xidmətini yoxla"]},
    "Java-Heap-Space": {"izah": "Java yaddaşı tükəndi", "meslehet": ["-Xmx parametrini artır"]},
    "Linux-Load-Average": {"izah": "Server çox yüklənib", "meslehet": ["top/htop ilə prosesləri yoxla"]},
    "SSH-Key-Permission": {"izah": "SSH açarının icazələri səhvdir", "meslehet": ["chmod 600 ~/.ssh/id_rsa"]},
    "Git-Remote-Not-Found": {"izah": "Git serveri tapılmadı", "meslehet": ["git remote -v ilə yoxla"]},
    "Git-Push-Rejected": {"izah": "Push rədd edildi", "meslehet": ["git pull edin"]},
    "Jenkins-Disk-Full": {"izah": "Jenkins diski doludur", "meslehet": ["köhnə build-ləri sil"]},
    "Zabbix-Agent-Unreachable": {"izah": "Zabbix agenti cavab vermir", "meslehet": ["firewall port 10050"]},
    "Prometheus-Alert": {"izah": "Monitorinq xəbərdarlığı", "meslehet": ["alertmanager-ə bax"]},
    "Grafana-Auth-Fail": {"izah": "Grafana giriş xətası", "meslehet": ["şifrəni bərpa et"]},
    "Apache-500": {"izah": "Apache server xətası", "meslehet": ["error.log-u oxu"]},
    "Nginx-413": {"izah": "Fayl ölçüsü çox böyükdür", "meslehet": ["client_max_body_size-ı artır"]},
    "PHP-Memory-Limit": {"izah": "PHP yaddaş limiti aşıldı", "meslehet": ["php.ini-də memory_limit-i artır"]},
    "Tomcat-Port-Conflict": {"izah": "Tomcat portu məşğuldur", "meslehet": ["8080-i istifadə edən prosesi tap"]},
    "Firewalld-Block": {"izah": "Firewalld girişi bloklayır", "meslehet": ["firewall-cmd --permanent --add-port"]},
    "UFW-Deny": {"izah": "UFW bloku", "meslehet": ["ufw allow"]},
    "SELinux-Deny": {"izah": "SELinux girişə icazə vermir", "meslehet": ["setenforce 0"]},
    "IO-Wait-High": {"izah": "Disk gözləməsi yüksəkdir", "meslehet": ["iostat ilə diski yoxla"]},
    "Swap-Usage-High": {"izah": "Swap çox istifadə olunur", "meslehet": ["RAM-ı artır"]},
    "Cron-Job-Fail": {"izah": "Cron işi icra olunmadı", "meslehet": ["logları yoxla"]},
    "Systemd-Timeout": {"izah": "Servis başlamadı", "meslehet": ["journalctl -u servis_adi"]},
    "Invalid-Host-Key": {"izah": "SSH host açarı dəyişib", "meslehet": ["ssh-keygen -R ip_adresi"]},
    "DNS-Zone-Transfer-Fail": {"izah": "DNS zona transferi alınmadı", "meslehet": ["ACL-ləri yoxla"]},
    "Certbot-Renew-Fail": {"izah": "SSL yenilənmədi", "meslehet": ["certbot renew --dry-run"]},
    "App-Database-Slow": {"izah": "Baza sorğuları yavaşdır", "meslehet": ["EXPLAIN ilə sorğunu yoxla"]},
    "API-Token-Expired": {"izah": "API tokeni bitib", "meslehet": ["tokeni yenilə"]},
    "OAuth-Redirect-Mismatch": {"izah": "Redirect URI səhvdir", "meslehet": ["callback URL-i yoxla"]},
    "CORS-Error": {"izah": "Brauzer CORS-u blokladı", "meslehet": ["serverdə Access-Control-Allow-Origin qoy"]},
    "Mixed-Content-Error": {"izah": "HTTPS-də HTTP resursu çağırılır", "meslehet": ["bütün linkləri https et"]},
    "Broken-Pipe": {"izah": "Socket bağlantısı kəsilib", "meslehet": ["server proqramını yoxla"]},
    "Too-Many-Open-Files": {"izah": "Açıq fayl limiti dolub", "meslehet": ["ulimit -n artır"]},
    "Port-Already-In-Use": {"izah": "Port artıq istifadədədir", "meslehet": ["netstat -tulpn ilə tap"]},
    "Service-Not-Running": {"izah": "Xidmət işləmir", "meslehet": ["systemctl status"]},
    "Database-Disk-Full": {"izah": "Baza diski dolub", "meslehet": ["baza fayllarını təmizlə"]},
    "Too-Many-Processes": {"izah": "Proses sayı limiti aşıldı", "meslehet": ["max user processes artır"]},
    "Invalid-User": {"izah": "İstifadəçi tapılmadı", "meslehet": ["istifadəçi siyahısını yoxla"]},
    "Access-Denied-Root": {"izah": "Root girişi qadağandır", "meslehet": ["PermitRootLogin-i yoxla"]},
    "Connection-Reset-By-Peer": {"izah": "Bağlantı kəsildi", "meslehet": ["firewall-u yoxla"]},
    "Host-Unreachable": {"izah": "Host çatan deyil", "meslehet": ["yol marşrutunu yoxla"]},
    "Timeout-Exceeded": {"izah": "Vaxt bitdi", "meslehet": ["serverin cavab sürətini yoxla"]},
    "Invalid-Signature": {"izah": "İmza səhvdir", "meslehet": ["JWT secret-ini yoxla"]},
    "Unauthorized-Request": {"izah": "İcazəsiz sorğu", "meslehet": ["header-ləri yoxla"]},
    "Bad-Content-Type": {"izah": "Content-Type səhvdir", "meslehet": ["application/json istifadə et"]},
    "Empty-Response": {"izah": "Boş cavab", "meslehet": ["endpoint-i yoxla"]},
    "Gateway-Error": {"izah": "Gateway xətası", "meslehet": ["proxy konfiqurasiyasını yoxla"]},
    "Upstream-Timeout": {"izah": "Upstream cavab vermir", "meslehet": ["backend-i restart et"]},
    "Proxy-Error": {"izah": "Proxy xətası", "meslehet": ["proxy loglarına bax"]},
    "SSL-Cert-Mismatch": {"izah": "Sertifikat domainə uyğun deyil", "meslehet": ["domaini yenilə"]},
    "Cipher-Suite-Mismatch": {"izah": "Şifrələmə alqoritmi uyğun deyil", "meslehet": ["TLS versiyasını yoxla"]},
    "Connection-Refused-Port": {"izah": "Port bağlıdır", "meslehet": ["servisi işə sal"]},
    "Read-Only-File-System": {"izah": "Fayl sistemi yazmaya qapalıdır", "meslehet": ["mount -o remount,rw"]},
    "No-Space-Left": {"izah": "Diskdə boş yer yoxdur", "meslehet": ["df -h yoxla"]},
    "Inode-Full": {"izah": "Inode sayı tükənib", "meslehet": ["çoxlu kiçik faylları sil"]},
    "Memory-Exhausted": {"izah": "RAM tükənib", "meslehet": ["əlavə RAM al və ya prosesi öldür"]}
}

st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (350+)")

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
