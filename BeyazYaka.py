import Calisan

class BeyazYaka(Calisan.Calisan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, sektor, tesvik_ptimi):
        Calisan.Calisan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, sektor)
        self.__tesvik_primi = tesvik_ptimi
        self.__yeni_maas = None

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas
    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            maas = Calisan.Calisan.get_maas(self)
            tecrube = Calisan.Calisan.get_tecrube(self)

            if tecrube < 24:
                zam_onerisi = self.get_tesvik_primi()
                yeni_maas = int(maas + zam_onerisi)
                self.set_yeni_maas(yeni_maas)
            elif 24 <= tecrube <= 48 and maas < 15000:
                zam_onerisi = (maas % tecrube) * 5 + self.get_tesvik_primi()
                yeni_maas = int(maas + zam_onerisi)
                self.set_yeni_maas(yeni_maas)
            elif tecrube > 48 and maas < 25000:
                zam_onerisi = (maas % tecrube) * 4 + self.get_tesvik_primi()
                yeni_maas = int(maas + zam_onerisi)
                self.set_yeni_maas(yeni_maas)

        except Exception:
            print("Bir hata oluştu işlem adımlarını kontrol ediniz.")

    def __str__(self):
        BeyazYaka.zam_hakki(self)
        return f"Ad: {Calisan.Calisan.get_ad(self)}\n" \
               f"Soyad: {Calisan.Calisan.get_soyad(self)}\n" \
               f"Tecrübe: {Calisan.Calisan.get_tecrube(self)} ay\n" \
               f"Yeni maaş: {self.get_yeni_maas()} TL\n"