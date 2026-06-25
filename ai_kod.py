import streamlit as st

# Çox geniş IT məlumat bazası
it_bazasi = {
    "404": {"izah": "Səhifə tapılmadı.", "meslehet": ["URL-i yoxla", "Cache-i təmizlə", "Saytın baş səhifəsinə qayıt"]},
    "500": {"izah": "Server xətası.", "meslehet": ["Saytı yenilə", "Loglara bax", "Administratora yaz"]},
    "DNS": {"izah": "Ad həlli xətası.", "meslehet": ["İnterneti yoxla", "DNS 8.8.8.8-ə keç", "Flushdns et"]},
    "Port 22": {"izah": "SSH bağlantı xətası.", "meslehet": ["Serveri yoxla", "Firewall-u aç", "Key-ləri yoxla"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı.", "meslehet": ["Proqramları bağla", "RAM-ı artır", "Restart et"]},
    "CPU": {"izah": "Prosessor həddən artıq yüklənib.", "meslehet": ["Task Manager-ə bax", "İşə düşən proqramları yoxla", "Soyutma sistemini yoxla"]},
    "Wi-Fi": {"izah": "İnternet bağlantısı kəsilib.", "
