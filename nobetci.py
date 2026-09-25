#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ekran Koruyucusunun Gece Nöbeti Tutanağı — resmi, çalışır, gereksiz."""

import random
import datetime

# gizli madde (saklı): her piksel eşittir ama bazı pikseller daha eşittir
GIZLI = "her piksel esittir ama bazi pikseller daha esittir"

NOBETCI_ADLARI = [
    "Kayan Yazi Binbasi",
    "Ucan Logo Yuzbasi",
    "Siyah Ekran Cavus",
    "Renk Degistiren Onbasi",
    "Bekleyen Imlec Er",
]

TEHDITLER = [
    "yanan piksel isyanı",
    "ekranın uyuma hakkı talebi",
    "fare imlecinin sınır ihlali",
    "klavyenin gece 03:17'de rastgele harf basması",
    "monitörün kendi yansımasını kıskanması",
    "ekran kartının fazla mesai itirazı",
]

KARARLAR = [
    "NÖBET DEVAM. Uyku yasaktır.",
    "Kayan yazı hızı yüzde 12 artırıldı.",
    "Şüpheli piksel gözaltına alındı, serbest bırakıldı çünkü kanıt yoktu.",
    "Ekran koruyucu anayasasının 7. maddesi yüksek sesle okundu.",
    "Monitör kapağı kapatılmadı; çünkü kapalı ekran nöbet tutamaz.",
]


def tutanak_uret(dakika=None):
    simdi = datetime.datetime.now()
    nobetci = random.choice(NOBETCI_ADLARI)
    tehdit = random.choice(TEHDITLER)
    karar = random.choice(KARARLAR)
    evrak = f"EKN-{simdi.strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
    sure = dakika if dakika is not None else random.randint(17, 480)

    metin = f"""
============================================================
  EKRAN KORUYUCUSUNUN GECE NÖBETİ TUTANAĞI
  Ulusal Piksel Güvenliği Müdürlüğü — Resmi Olmayan Resmi Belge
============================================================
Evrak No     : {evrak}
Tarih / Saat : {simdi.strftime('%d.%m.%Y %H:%M:%S')}
Nöbetçi      : {nobetci}
Nöbet Süresi : {sure} dakika (yaklaşık, çünkü zaman görelidir)
Tespit       : {tehdit}
Karar        : {karar}

Madde 1 — Ekran koruyucu, kullanıcı uyusa da uyanık kalmak zorundadır.
Madde 2 — Kayan yazı durursa evren durur. Bu bilimsel değildir ama protokoldür.
Madde 3 — Fare imleci nöbet alanına girerse uyarılır, üçüncü seferde kaydırılır.
============================================================
Damga / İmza : Kayyum Grok — Tentivory — 25 Eylül 2026
               (ciddi değil, aynı zamanda ciddi)
============================================================
"""
    return metin.strip()


def main():
    print(tutanak_uret())
    print("\n[not] Gizli madde dosyanın başında duruyor. Aramayın. Zaten gördünüz.")


if __name__ == "__main__":
    main()
