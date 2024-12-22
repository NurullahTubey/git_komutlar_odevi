import json

# JSON dosyasını kaydetme fonksiyonu
def save_to_json(data, filename="ogrenciler.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# JSON dosyasını yükleme fonksiyonu
def load_from_json(filename="ogrenciler.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Ana program
ogrenciler = load_from_json()  # Önceki veriler varsa yükle

while True:
    print("\n1. Yeni öğrenci ekle")
    print("2. Kayıtlı öğrencileri göster")
    print("3. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        try:
            ogrenci_sayisi = int(input("Kaç öğrenci eklemek istiyorsunuz? "))
            for _ in range(ogrenci_sayisi):
                ad = input("Öğrencinin adını girin: ")
                vize = float(input(f"{ad} için vize notunu girin: "))
                final = float(input(f"{ad} için final notunu girin: "))
                ortalama = round((vize * 0.4) + (final * 0.6), 2)

                ogrenciler.append({
                    "Ad": ad,
                    "Vize": vize,
                    "Final": final,
                    "Ortalama": ortalama
                })

            save_to_json(ogrenciler)  # Yeni verileri JSON dosyasına kaydet
            print("Öğrenciler başarıyla kaydedildi!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    elif secim == "2":
        if not ogrenciler:
            print("Kayıtlı öğrenci bulunmamaktadır.")
        else:
            print("\nKayıtlı Öğrenciler:")
            print("{:<20} {:<10} {:<10} {:<10}".format("Ad", "Vize", "Final", "Ortalama"))
            print("-" * 50)
            for ogrenci in ogrenciler:
                print("{:<20} {:<10} {:<10} {:<10}".format(ogrenci["Ad"], ogrenci["Vize"], ogrenci["Final"], ogrenci["Ortalama"]))

    elif secim == "3":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Lütfen geçerli bir seçenek girin.")
