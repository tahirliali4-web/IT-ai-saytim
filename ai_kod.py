import streamlit as st

# Tam IT Məlumat Bazası
it_bazasi = {
    # Web Xətaları
    "400": {"izah": "Bad Request (Səhv sorğu).", "meslehet": ["URL-i yoxla", "Sorğu formatını düzəlt"]},
    "401": {"izah": "Unauthorized (İcazəsiz giriş).", "meslehet": ["Şifrəni yoxla", "Login ol"]},
    "403": {"izah": "Forbidden (Giriş qadağandır).", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found (Səhifə tapılmadı).", "meslehet": ["URL-i yoxla", "Səhifənin mövcudluğunu yoxla"]},
    "500": {"izah": "Internal Server Error (Server xətası).", "meslehet": ["Serveri yenilə", "Loglara bax"]},
    "502": {"izah": "Bad Gateway (Keçid xətası).", "meslehet": ["Bir az gözlə", "Serveri restart et"]},
    "503": {"izah": "Service Unavailable (Xidmət yoxdur).", "meslehet": ["Serverin yüklənməsini yoxla"]},
    
    # Şəbəkə və Portlar
    "DNS": {"izah": "DNS xətası (Ad həlli mümkün olmadı).", "meslehet": ["İnterneti yoxla", "DNS-i 8.8.8.8 et"]},
    "Port 21": {"izah": "FTP (Fayl köçürmə).", "meslehet": ["Portun açıq olmasını yoxla", "İstifadəçi adını yoxla"]},
    "Port 22": {"izah": "SSH (Uzaqdan idarə).", "meslehet": ["Firewall-u yoxla", "Serverin açıq olduğundan əmin ol"]},
    "Port 3306": {"izah": "MySQL (Verilənlər bazası).", "meslehet": ["Bazanın işlədiyini yoxla", "Host adını yoxla"]},
    
    # Sistem Xətaları
    "RAM": {"izah": "Yaddaş çatışmazlığı.", "meslehet": ["Lazımsız proqramları bağla", "RAM-ı yoxla"]},
    "CPU": {"izah": "Prosessorun həddindən artıq yüklənməsi.", "meslehet": ["Arxa plan proseslərinə bax", "Sistemə restart ver"]}
}

st.set_page_config(page_title="IT Bütün Xətalar Mərkəzi", page_icon="🌐")
st.title("🌐 IT Bütün Xətalar Mərkəzi")

axtaris = st.text_input("Xəta kodunu və ya mövzunu yazın (məs: 403, DNS, RAM):").strip()

if axtaris:
    if axtaris in it_bazasi:
        data = it_bazasi[axtaris]
        st.subheader(f"İzahı: {data['izah']}")
        st.subheader("💡 Həll yolları:")
        for m in data['meslehet']:
            st.success(m)
    else:
        st.error(f"'{axtaris}' bazada tapılmadı. Zəhmət olmasa siyahıdan birini yoxlayın.")

with st.expander("Bazada olan bütün kodlar:"):
    st.write(list(it_bazasi.keys()))
