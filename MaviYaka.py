import Calisan

class MaviYaka(Calisan.Calisan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, sektor, yipranma_payi):
        Calisan.Calisan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, sektor)
        self.__yipranma_payi = yipranma_payi
        self.__yeni_maas = None

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            maas = Calisan.Calisan.get_maas(self)
            tecrube = Calisan.Calisan.get_tecrube(self)

            if tecrube < 24:
                zam_orani = self.get_yipranma_payi()*10
                yeni_maas = int(maas + maas*zam_orani/100)
                self.set_yeni_maas(yeni_maas)
            elif 24 <= tecrube <= 48 and maas < 15000:
                zam_orani = (maas % tecrube) / 2 + self.get_yipranma_payi()*10
                yeni_maas = int(maas + maas*zam_orani/100)
                self.set_yeni_maas(yeni_maas)
            elif tecrube > 48 and maas < 25000:
                zam_orani = (maas % tecrube) / 3 + self.get_yipranma_payi()*10
                yeni_maas = int(maas + maas*zam_orani/100)
                self.set_yeni_maas(yeni_maas)

        except Exception:
            print("Bir hata oluştu işlem adımlarını kontrol ediniz.")

    def __str__(self):
        MaviYaka.zam_hakki(self)
        return f"Ad: {Calisan.Calisan.get_ad(self)}\n" \
               f"Soyad: {Calisan.Calisan.get_soyad(self)}\n" \
               f"Tecrübe: {Calisan.Calisan.get_tecrube(self)} ay\n" \
               f"Yeni maaş: {self.get_yeni_maas()} TL\n"