import Insan

class Issiz(Insan.Insan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, mavi_yaka_yili, beyaz_yaka_yili, yonetici_yili):
        Insan.Insan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__mavi_yaka = mavi_yaka_yili
        self.__beyaz_yaka = beyaz_yaka_yili
        self.__yonetici = yonetici_yili
        self.__tecrube = {"Mavi yaka": mavi_yaka_yili, "Beyaz yaka": beyaz_yaka_yili, "Yonetici": yonetici_yili}
        self.__statu_onerisi = None
        # tüm değişkenleri private tanımlıyoruz
        # gerekli değişkenler için get/set metotlarını tanımlıyoruz

    def get_mavi_yaka(self):
        return self.__mavi_yaka
    def get_beyaz_yaka(self):
        return self.__beyaz_yaka
    def get_yonetici(self):
        return self.__yonetici
    def get_tecrube(self):
        return self.__tecrube
    def get_statu_onerisi(self):
        return self.__statu_onerisi
    def set_statu_onerisi(self, statu):
        self.__statu_onerisi = statu

    def statu_bul(self):        # statü önerisinde bulunabilmek için gerekli işlemleri yapıyoruz
        try:
            mavi_yaka = self.__tecrube["Mavi yaka"]*20/100
            beyaz_yaka = self.__tecrube["Beyaz yaka"]*35/100
            yonetici = self.__tecrube["Yonetici"]*45/100

            if mavi_yaka > beyaz_yaka and mavi_yaka > yonetici:
                self.set_statu_onerisi("Mavi yaka")
            elif beyaz_yaka > mavi_yaka and beyaz_yaka > yonetici:
                self.set_statu_onerisi("Beyaz yaka")
            else:
                self.set_statu_onerisi("Yonetici")

        except Exception:
            print("Statü önerme işlemi yapılırken hata oluştu işlem adımlarını kontrol ediniz.")

    # bilgileri str metodu ile yazdırıyoruz
    def __str__(self):
        Issiz.statu_bul(self)
        return f"Ad: {Insan.Insan.get_ad(self)}\n" \
               f"Soyad: {Insan.Insan.get_soyad(self)}\n" \
               f"Kişiye önerilen en uygun statü: {self.get_statu_onerisi()}\n"