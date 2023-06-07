import Insan

class Calisan(Insan.Insan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, sektor):
        Insan.Insan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__sektor = sektor
        self.__yeni_maas = None

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas
    def set_maas(self, maas):
        self.__maas = maas
    def get_maas(self):
        return self.__maas
    def get_tecrube(self):
        return self.__tecrube
    def get_sektor(self):
        return self.__sektor

    def zam_hakki(self):
        try:
            while self.__sektor not in ["Teknoloji", "muhasebe", "insaat", "diger"]:
                print(f"{Insan.Insan.get_ad(self)} çalışanının sektörü hatalı girilmiştir.")
                break

            if self.get_tecrube() < 24:
                self.set_yeni_maas(self.get_maas())
            elif (24 <= self.get_tecrube() <= 48) and self.get_maas() < 15000:
                zam_orani = self.get_maas() % self.get_tecrube()
                yeni_maas = int(self.get_maas() + (self.get_maas()*zam_orani/100))
                self.set_yeni_maas(yeni_maas)
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2
                yeni_maas = int(self.get_maas() + (self.get_maas()*zam_orani/100))
                self.set_yeni_maas(yeni_maas)

        except Exception:
            print("Zam hesaplanırken hata oluştu işlem adımlarını kontrol ediniz.")

    def __str__(self):
        Calisan.zam_hakki(self)
        return f"Ad: {Insan.Insan.get_ad(self)}\n" \
               f"Soyad: {Insan.Insan.get_soyad(self)}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni maaş: {self.get_yeni_maas()} TL\n"