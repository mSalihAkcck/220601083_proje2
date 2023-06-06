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