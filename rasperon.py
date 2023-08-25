# main.py
import os
import json
from filigran import yazdir_logo  # filigran dosyasındaki yazdir_logo fonksiyonunu içe aktarıyoruz

# Veritabanı dosyası kontrolü
veritabani_dosyasi = "ornek.json"

if not os.path.exists(veritabani_dosyasi):
    with open(veritabani_dosyasi, 'w', encoding='utf-8') as dosya:
        json.dump({}, dosya, indent=4, ensure_ascii=False)  # JSON verisini daha okunaklı hale getir ve özel karakterleri koruma işlemi

# Veritabanı yükleme
with open(veritabani_dosyasi, 'r', encoding='utf-8') as dosya:
    veritabani = json.load(dosya)

# Bot ismini ayarlama
if "bot_adi" not in veritabani:
    bot_adi = input("Sohbet botunun ismini belirleyin: ")
    veritabani["bot_adi"] = bot_adi
    with open(veritabani_dosyasi, 'w', encoding='utf-8') as dosya:
        json.dump(veritabani, dosya, indent=4, ensure_ascii=False)  # JSON verisini daha okunaklı hale getir ve özel karakterleri koruma işlemi
else:
    bot_adi = veritabani["bot_adi"]

# ASCII logo yazdırma işlevini çağırıyoruz
yazdir_logo()

# Botun ilk selamını yazdırıyoruz
print(f"{bot_adi}: Merhaba! Size nasıl yardımcı olabilirim?")

# Sonsuz bir döngü başlatıyoruz, kullanıcı çıkış yapana kadar devam edecek
while True:
    # Kullanıcıdan bir soru veya mesaj alıyoruz
    soru = input("Siz: ")

    # Eğer kullanıcı "çıkış yap" derse programdan çıkış yapıyoruz
    if soru.lower() == "çıkış yap":
        print(f"{bot_adi}: Güle güle! Program kapatılıyor.")
        break  # Programdan çıkış yap

    # Eğer kullanıcının sorduğu sorunun cevabı veritabanında varsa cevabı yazdırıyoruz
    if soru.lower() in veritabani:
        print(f"{bot_adi}: {veritabani[soru.lower()]}")
    else:
        # Eğer sorunun cevabı yoksa, kullanıcıya öğretebilir miyiz sorusu soruyoruz
        cevap = input(f"{bot_adi}: Üzgünüm, bu sorunun cevabını bilmiyorum. Size öğretebilir miyim? (e/h) ").lower()
        if cevap == "e" or cevap == "evet":
            # Eğer öğretmek istiyorsa yeni cevabı kaydediyoruz
            yeni_cevap = input(f"{bot_adi}: Peki, bu sorunun doğru cevabını girin: ")
            veritabani[soru.lower()] = yeni_cevap
            with open(veritabani_dosyasi, 'w', encoding='utf-8') as dosya:
                json.dump(veritabani, dosya, indent=4, ensure_ascii=False)  # JSON verisini daha okunaklı hale getir ve UTF-8 karakterleri destekle
                print(f"{bot_adi}: Teşekkür ederim, bu bilgiyi öğrendim.")
        else:
            # Eğer öğretmek istemiyorsa başka nasıl yardımcı olabileceğimizi soruyoruz
            print(f"{bot_adi}: Üzgünüm, size nasıl başka yardımcı olabilirim?")
