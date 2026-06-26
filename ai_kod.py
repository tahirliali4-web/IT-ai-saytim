import streamlit as st

# Genişləndirilmiş IT Məlumat Bazası (Bura istədiyin qədər xəta əlavə edə bilərsən)
it_bazasi = {
    # 1xx - İnformasiya xarakterli
    "100": {"izah": "Continue (Davam et).", "meslehet": ["Sorğu qəbul edilib, davam edin."]},
    "101": {"izah": "Switching Protocols.", "meslehet": ["Protokol dəyişdirilir."]},
    
    # 2xx - Uğurlu
    "200": {"izah": "OK (Uğurlu).", "meslehet": ["Hər şey qaydasındadır."]},
    
    # 3xx - Yönləndirmə
    "301": {"izah": "Moved Permanently.", "meslehet": ["Yeni linkə keçin."]},
    
    # 4xx - Müştəri xətaları
    "400": {"izah": "Bad Request.", "meslehet": ["Sorğunu yoxlayın."]},
    "401": {"izah": "Unauthorized.", "meslehet": ["Giriş edin."]},
    "403": {"izah": "Forbidden.", "meslehet": ["İcazəniz yoxdur."]},
    "404": {"izah": "Not Found.", "meslehet": ["Linkə diqqət edin."]},
    "408": {"izah": "Request Timeout.", "meslehet": ["Bağlantını yoxlayın."]},
    
    # 5xx - Server xətaları
    "500": {"izah": "Internal Server Error.", "meslehet": ["Serveri yeniləyin."]},
    "502": {"izah": "Bad Gateway.", "meslehet": ["Serveri yoxlayın."]},
    "503": {"izah": "Service Unavailable.", "meslehet": ["Bir az sonra yoxlayın."]},
    "504": {"izah": "Gateway Timeout.", "meslehet": ["Serverin cavabını gözləyin."]},
    
    # Proqramlaşdırma və Sistem
    "SyntaxError": {"izah": "Sintaksis səhvi.", "meslehet": ["Yazılışı yoxlayın."]},
    "NameError": {"izah": "Dəyişən adı səhvi.", "meslehet": ["Dəyişəni təyin edin."]},
    "BlueScreen": {"izah": "Windows çökdü.", "meslehet": ["RAM və Sürücüləri yoxlayın."]}
}

st.set_page_config(page_title="IT Ensklopediyası", page_icon="🌐")
st.title("🌐 IT Mütəxəssis Aləti")

axtaris = st.text_input("Xəta kodunu və ya xəta adını yazın:").strip()

if axtaris:
    if axtaris in it_bazasi:
        data = it_bazasi[axtaris]
        st.subheader(f"🔍 İzahı: {data['izah']}")
        st.subheader("💡 Məsləhətlər:")
        for m in data['meslehet']:
            st.success(m)
    else:
        st.error(f"'{axtaris}' hələlik bazada yoxdur. Bazanı genişləndirməyə davam edə bilərik.")

with st.expander("Bazada olan bütün kodlar:"):
    st.write(list(it_bazasi.keys()))
