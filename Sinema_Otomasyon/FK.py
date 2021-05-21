from os import name, system
from time import sleep
import shutil
from VEK import VEK


class FK():
    # Develped by OnCaDo
    def __init__(self) -> None:
        self.v = VEK()
        self.e_t
        self.klist, self.slist = [], []

    @property
    def e_t(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def mesaj_ver__(self, msj):
        self.e_t
        self.center("~~~~~~~~~~~~~~~~~~~~~~OnCaDo~~~~~~~~~~~~~~~~~~~~~~\n\n")
        self.center(f"{msj}")
        self.center("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        sleep(3)

    def menu_baslik__(self, baslik_mesaji):
        self.e_t
        self.center("~~~~~~~~~~~~~~~~~~~~~~OnCaDo~~~~~~~~~~~~~~~~~~~~~~\n\n")
        self.center(f"{baslik_mesaji}")

    def secim_al__(self, snr_dgr):
        scm = None
        while not scm:
            scm = input("\n\t--> ")
        else:
            try:
                scm = int(scm)
                if 1 <= scm <= snr_dgr:
                    return scm
                else:
                    print("\nHatalı giriş..\n")
                    return self.secim_al__(snr_dgr)
            except Exception:
                print("\nHatalı giriş..\n")
                return self.secim_al__(snr_dgr)

    def kullanici_ekle__(self, ad, sifre):
        usr = [self.v.genel.sifrele__(ad), self.v.genel.sifrele__(sifre)]
        self.v.kullanici.ekle__(usr)

    @property
    def ilk_acilis(self):
        if self.v.kullanici.sayisi < 1:
            self.e_t
            msj = """Programı ilk defa kullanıyorsunuz. Kullanıcı oluşturmalısınız.
            """
            self.mesaj_ver__(msj)
            ad, sif = None, None
            while not ad:
                ad = input("\nKullanıcı adı: ")

            while not sif:
                sif = input("\nŞifreniz: ")
            self.kullanici_ekle__(ad, sif)
            self.mesaj_ver__(
                "Kayıt işlemi başarılı.\nYönlendiriliyorsunuz..")

    def usr_kntrl__(self, user):
        usr = self.v.id.yok
        self.v.genel.verileri_cek
        self.klist, self.slist = self.cozumle
        for i, d in enumerate(self.klist):
            if d == user:
                usr = self.v.id.var
                self.v.kullanici.id_ = i
                break
        return usr

    @property
    def ana_ekran(self):
        self.v.genel.dosyalari_olustur
        self.ilk_acilis

    @property
    def kayit_ol(self):
        self.menu_baslik__("Kullanıcı Kaydı")
        self.v.genel.verileri_cek
        ad, sf = None, None
        while not ad:
            ad = input("Kullanıcı Adı: ")
        u = self.usr_kntrl__(ad)

        if self.v.kullanici.sayisi < 10:
            if u == self.v.id.yok:
                while not sf:
                    sf = input("Şifre: ")
                self.kullanici_ekle__(ad, sf)
                self.mesaj_ver__(
                    "Kayıt işlemi başarılı. Yönlendiriliyorsunuz..")
                # ana ekrana git
            else:
                self.mesaj_ver__(
                    "Böyle bir kullanıcı bulunmakta. Yönlendiriliyorsunuz..")
                # ana ekrana git
        else:
            self.mesaj_ver__(
                "KULLANICI SINIRINA ULAŞILDI!!\nÜcretsiz sürüm 10 adet kullanıcıyı desteklemektedir.\nLütfen yetkiliyle görüşün.")
            # ana ekrana git

    @property
    def kullanici_girisi(self):
        self.menu_baslik__("Kullanıcı Girişi")
        self.v.genel.verileri_cek
        ad, sf = None, None
        while not ad:
            ad = input("Kullanıcı Adı: ")

        u = self.usr_kntrl__(ad)
        if u == self.v.id.var:
            while not sf:
                sf = input("Şifreniz: ")

            if sf == self.slist[self.v.kullanici.id_]:
                self.mesaj_ver__(
                    "Giriş başarılı.. Yönlediriliyorsunuz..")
                return self.v.id.var

            else:
                self.mesaj_ver__(
                    "Kullanıcı adı ya da şifre yanlış. Yönlediriliyorsunuz..")
                return self.v.id.yok

        else:
            self.mesaj_ver__(
                "Böyle bir kullanıcı yok. Yönlediriliyorsunuz..")
            return self.v.id.yok

    @property
    def rezervasyon_yap(self):
        self.e_t
        self.menu_baslik__("Rezervasyon Yap")
        self.v.genel.verileri_cek

        print(f"""
        1- {self.v.salon.isim__(self.v.id.red)} Salonu\t\t-> {self.v.salon.film_ismi__(self.v.id.star_wars)} Filmi
        2- {self.v.salon.isim__(self.v.id.green)} Salonu\t\t-> {self.v.salon.film_ismi__(self.v.id.lotr)} Filmi
        3- {self.v.salon.isim__(self.v.id.blue)} Salonu\t\t-> {self.v.salon.film_ismi__(self.v.id.mtr)} Filmi""")

        salon_secim = self.secim_al__(3)-1

        print("\nKaç numaralı matinede rezervasyon yapmak istersiniz? (1/2/3/4/5)")
        matine_secim = self.secim_al__(5)-1

        bos_koltuk = self.v.salon.izleme.bos_koltuk__(
            salon_secim, matine_secim)

        if bos_koltuk < 50:
            print(
                f"\nÖdeme türünü seçiniz.\n1- {self.v.salon.bilet.tur__(self.v.id.ogrenci)} ({self.v.salon.bilet.ucret__(self.v.id.ogrenci_ucret)} TL)\n2- {self.v.salon.bilet.tur__(self.v.id.tam)} ({self.v.salon.bilet.ucret__(self.v.id.tam_ucret)} TL)")
            odeme_sekli = (self.secim_al__(2)-1)

            self.v.salon.izleme.artir__(salon_secim, matine_secim, odeme_sekli)

            print("\n\nRezervasyon Bilgileri:\n")
            print(f"--> {self.v.salon.isim__(salon_secim)} salonundaki {matine_secim + 1} matinesinde: {bos_koltuk +1 } numaralı koltuk\n--> Bilet Ücreti: {self.v.salon.bilet.ucret__(odeme_sekli)} ₺.")
            sleep(2)
            self.v.genel.verileri_kaydet
            print("\nRezervasyonunuz Başarıyla gerçekleştirildi.\nİyi seyirler Dileriz.")
        else:
            self.mesaj_ver__("\nBu matinede boş koltuk kalmadı..\n")

    @property
    def hasilati_goster(self):
        self.e_t
        self.v.genel.verileri_cek
        self.v.genel.verileri_goster

    @property
    def cozumle(self):
        klist = []

        for i in self.v.kullanici.listesi[0]:
            klist.append(self.v.genel.cozumle__(i))
        slist = []
        for i in self.v.kullanici.listesi[1]:
            slist.append(self.v.genel.cozumle__(i))
        return klist, slist

    def center(self, msj):
        print(msj.center(shutil.get_terminal_size().columns))
