class Insan:

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
        # tüm değişkenleri private tanımlıyoruz
        # gerekli değişkenler için get/set metotlarını tanımlıyoruz

    def get_tc_no(self):
        return self.__tc_no
    def get_ad(self):
        return self.__ad
    def get_soyad(self):
        return self.__soyad
    def get_yas(self):
        return self.__yas
    def get_cinsiyet(self):
        return self.__cinsiyet
    def get_uyruk(self):
        return self.__uyruk

    # bilgileri str metodu ile yazdırıyoruz
    def __str__(self):
        return f"TC no: {self.get_tc_no()}\n" \
               f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Yaş: {self.get_yas()}\n" \
               f"Cinsyet: {self.get_cinsiyet()}\n" \
               f"Uyruk: {self.get_uyruk()}\n"