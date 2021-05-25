from FK import FK


class MN():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self.f = FK()

    @property
    def ana_ekran(self):
        self.f.ana_ekran
        self.f.menu_baslik__("Lütfen bir işlem seçiniz.")
        print("\n\n1- Kayıt Ol\n2- Oturum Aç\n3- Çıkış")
        secim = self.f.secim_al__(3)
        secenek = [self.kayit_ol, self.kullanici_girisi, exit]
        self.f.menu_secim__(secenek, secim)

    def kayit_ol(self):
        self.f.kayit_ol
        self.ana_ekran

    def kullanici_girisi(self):
        usr = self.f.kullanici_girisi
        if usr == 1:
            self.rez_secim
        else:
            self.ana_ekran

    @property
    def rez_secim(self):
        self.f.e_t
        self.f.menu_baslik__("Lütfen yapmak istediğiniz işlemi seçiniz.")
        print(
            f"""Merhaba sayın {self.f.klist[self.f.v.kullanici.id_].upper()},\nYapabileceğiniz işlemler listelendi
            
            1- Rezervasyon Yap
            2- Hasılatı Gör
            3- Çıkış""")
        secim = self.f.secim_al__(3)
        secenek = [self.rezervasyon_yap, self.hasilati_gor, exit]
        self.f.menu_secim__(secenek, secim)

    def rezervasyon_yap(self):
        self.f.rezervasyon_yap
        self.rez_secim

    def hasilati_gor(self):
        self.f.hasilati_goster
        s = input("\n\nDevam etmek için ENTER'e tuşa basınız..")
        self.rez_secim
