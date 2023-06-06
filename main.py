import pandas as pd
import Insan
import Issiz
import Calisan
import MaviYaka
import BeyazYaka

insan1 = Insan.Insan(52695316528, "Salih", "Akcicek", 24, "Erkek", "Turkiye")
print(insan1.__str__())
insan2 = Insan.Insan(26531296584, "Seher", "Yılmaz", 28, "Kadın", "Turkiye")
print(insan2.__str__())

issiz1 = Issiz.Issiz(56321874638, "Selen", "Celik", 35, "Kadın", "Turkiye", 8, 4, 3)
print(issiz1.__str__())
issiz2 = Issiz.Issiz(94531516546, "Ahmet", "Kanbaz", 30, "Erkek", "Turkiye", 4, 3, 1)
print(issiz2.__str__())
issiz3 = Issiz.Issiz(46468974562, "Ersoy", "Camur", 46, "Erkek", "Turkiye", 7, 5, 4)
print(issiz3.__str__())

calisan1 = Calisan.Calisan(50022603714, "Ece", "Seckin", 27, "Kadın", "Turkiye", 30, 8500, "muhasebe")
print(calisan1.__str__())
calisan2 = Calisan.Calisan(21032551692, "Emrah", "Yasar", 33, "Erkek", "Turkiye", 38, 12500, "Teknoloji")
print(calisan2.__str__())
calisan3 = Calisan.Calisan(21032551692, "Yasin", "Cakmak", 40, "Erkek", "Turkiye", 55, 24500, "insaat")
print(calisan3.__str__())

maviyaka1 = MaviYaka.MaviYaka(86321569845, "Kemal", "Karaman", 29, "Erkek", "Turkiye", 30, 9000, "muhasebe", 0.5)
print(maviyaka1.__str__())
maviyaka2 = MaviYaka.MaviYaka(50306972413, "Fatma", "Konan", 35, "Kadın", "Turkiye", 39, 13500, "diger", 0.8)
print(maviyaka2.__str__())
maviyaka3 = MaviYaka.MaviYaka(86321569845, "Meltem", "Bayir", 23, "Kadın", "Turkiye", 16, 8500, "diger", 0.3)
print(maviyaka3.__str__())

beyazyaka1 = BeyazYaka.BeyazYaka(60321269873, "Leyla", "Semen", 36, "Kadın", "Turkiye", 26, 14000, "Teknoloji", 1000)
print(beyazyaka1.__str__())
beyazyaka2 = BeyazYaka.BeyazYaka(30440751231, "Sinem", "Kobal", 35, "Kadın", "Turkiye", 49, 22500, "diger", 2000)
print(beyazyaka2.__str__())
beyazyaka3 = BeyazYaka.BeyazYaka(81924007632, "Murat", "Boz", 43, "Erkek", "Turkiye", 56, 24500, "insaat", 1500)
print(beyazyaka3.__str__())

veriler = {"Kategori": ["Calisan", "Calisan", "Calisan", "Mavi yaka", "Mavi yaka", "Mavi yaka", "Beyaz yaka", "Beyaz yaka", "Beyaz yaka"],
        "Tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
        "Yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
        "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
        "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
        "Sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(), maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(), beyazyaka3.get_sektor()],
        "Tecrube": [calisan1.get_tecrube()//12, calisan2.get_tecrube()//12, calisan3.get_tecrube()//12, maviyaka1.get_tecrube()//12, maviyaka2.get_tecrube()//12, maviyaka3.get_tecrube()//12, beyazyaka1.get_tecrube()//12, beyazyaka2.get_tecrube()//12, beyazyaka3.get_tecrube()//12],
        "Maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],
        "Yipranma payi": [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(), 0, 0, 0],
        "Tesvik primi": [0, 0, 0, 0, 0, 0, beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(), beyazyaka3.get_tesvik_primi()],
        "Yeni maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()]
        }

df = pd.DataFrame(veriler)
print(df.to_string(), "\n")

grup = df.groupby(["Kategori"]).agg({"Yeni maas": "mean", "Tecrube": "mean"})
print(grup, "\n")             # kategoriye göre gruplandırılmıs yeni maas ve tecrubenin ortalaması