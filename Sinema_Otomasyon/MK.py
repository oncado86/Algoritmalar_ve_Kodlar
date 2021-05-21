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
        if secim == 1:
            self.kayit_ol
        elif secim == 2:
            self.kullanici_girisi
        elif secim == 3:
            exit()
        else:
            self.f.mesaj_ver__(
                "Hatalı giriş, lütfen tekrar deneyiniz..")
            self.ana_ekran

    @property
    def kayit_ol(self):
        self.f.kayit_ol
        self.ana_ekran

    @property
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
        if secim == 1:
            self.rezervasyon_yap
        elif secim == 2:
            self.hasilati_gor
        else:
            exit()

    @property
    def rezervasyon_yap(self):
        self.f.rezervasyon_yap
        self.rez_secim

    @property
    def hasilati_gor(self):
        self.f.hasilati_goster
        s = input("\n\nDevam etmek için ENTER'e tuşa basınız..")
        self.rez_secim
