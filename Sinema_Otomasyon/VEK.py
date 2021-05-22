from VK import VERILER

_v_ = VERILER()


class Genel():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    @property
    def dosyalari_olustur(self):
        _v_._dosyalari_olustur

    @property
    def verileri_cek(self):
        _v_._verileri_cek

    @property
    def verileri_goster(self):
        _v_._verileri_goster

    @property
    def verileri_kaydet(self):
        _v_._verileri_kaydet

    def sifrele__(self, metin, ilerleme=9):
        return _v_._kripto__(metin, _v_._sifrele_ID, ilerleme)

    def cozumle__(self, metin, ilerleme=9):
        return _v_._kripto__(metin, _v_._cozumle_ID, ilerleme)


class iD():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    @property
    def var(self):
        return _v_._var

    @property
    def yok(self):
        return _v_._yok

    @property
    def toplam_izlenme(self):
        return _v_._sb__toplam_izlenme__ID

    @property
    def ogrenci_izlenme(self):
        return _v_._sb__ogrenci_izleme__ID

    @property
    def tam_izlenme(self):
        return _v_._sb__tam_izleme__ID

    @property
    def toplam_gelir(self):
        return _v_._sb__toplam_gelir__ID

    @property
    def ogrenci_gelir(self):
        return _v_._sb__ogrenci_gelir__ID

    @property
    def tam_gelir(self):
        return _v_._sb__tam_gelir__ID

    @property
    def red(self):
        return _v_._red_ID

    @property
    def green(self):
        return _v_._green_ID

    @property
    def blue(self):
        return _v_._blue_ID

    @property
    def star_wars(self):
        return _v_._sw_ID

    @property
    def lotr(self):
        return _v_._ltr_ID

    @property
    def mtr(self):
        return _v_._mtr_ID

    @property
    def yaz(self):
        return _v_._yaz_ID

    @property
    def ekle(self):
        return _v_._ekle_ID

    @property
    def txt_sifre(self):
        return _v_._txt_sifre_ID

    @property
    def txt_log(self):
        return _v_._txt_log_ID

    @property
    def kullanici_ad(self):
        return _v_._kullanici_ad_ID

    @property
    def kullanici_sifre(self):
        return _v_._kullanici_sifre_ID

    @property
    def ogrenci(self):
        return _v_._ogrenci_ID

    @property
    def ogrenci_ucret(self):
        return _v_._ogrenci_ucret_ID

    @property
    def tam(self):
        return _v_._tam_ID

    @property
    def tam_ucret(self):
        return _v_._tam_ucret_ID


class Bilet():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def tur__(self, tur_ID):
        return _v_._bilet_bilgisi__(tur_ID)

    def ucret__(self, ucret_ID):
        return _v_._bilet_bilgisi__(ucret_ID)


#------------------------- IZLEME
class Izleme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self.red = Red_Izlenme()
        self.green = Green_Izlenme()
        self.blue = Blue_Izlenme()

    def artir__(self, salon_ID, matine_bilgisi, odeme_sekli):
        # toplam izleme
        _v_._bilgi_guncelle__(salon_ID, matine_bilgisi, _v_._sb__toplam_izlenme__ID, _v_._salon_bilgisi_getir__(
            salon_ID, matine_bilgisi, _v_._sb__toplam_izlenme__ID)+1)

        if odeme_sekli == 0:
            # toplam gelir
            _v_._bilgi_guncelle__(salon_ID, 0, _v_._sb__toplam_gelir__ID,
                                  _v_._salon_bilgisi_getir__(salon_ID, 0, _v_._sb__toplam_gelir__ID) + _v_._bilet_bilgisi__(_v_._ogrenci_ucret_ID))

            # ogrenci izlenme
            _v_._bilgi_guncelle__(salon_ID, matine_bilgisi, _v_._sb__ogrenci_izleme__ID,
                                  _v_._salon_bilgisi_getir__(salon_ID, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)+1)
            # ogrenci gelir
            _v_._bilgi_guncelle__(salon_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID,
                                  _v_._salon_bilgisi_getir__(salon_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID) + _v_._bilet_bilgisi__(_v_._ogrenci_ucret_ID))

        else:
            # toplam gelir
            _v_._bilgi_guncelle__(salon_ID, 0, _v_._sb__toplam_gelir__ID,
                                  _v_._salon_bilgisi_getir__(salon_ID, 0, _v_._sb__toplam_gelir__ID) + _v_._bilet_bilgisi__(_v_._tam_ucret_ID))
            # tam izlenme
            _v_._bilgi_guncelle__(salon_ID, matine_bilgisi, _v_._sb__tam_izleme__ID,
                                  _v_._salon_bilgisi_getir__(salon_ID, matine_bilgisi, _v_._sb__tam_izleme__ID)+1)
            # tam gelir
            _v_._bilgi_guncelle__(salon_ID, matine_bilgisi, _v_._sb__tam_gelir__ID,
                                  _v_._salon_bilgisi_getir__(salon_ID, matine_bilgisi, _v_._sb__tam_gelir__ID) + _v_._bilet_bilgisi__(_v_._tam_ucret_ID))

    def bos_koltuk__(self, salon_ID, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(salon_ID, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


class Red_Izlenme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.red, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.red, matine_bilgisi, _v_._sb__tam_izleme__ID)

    def toplam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.red, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


class Green_Izlenme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.green, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.green, matine_bilgisi, _v_._sb__tam_izleme__ID)

    def toplam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.green, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


class Blue_Izlenme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.blue, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.blue, matine_bilgisi, _v_._sb__tam_izleme__ID)

    def toplam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.blue, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


#------------------------- GELIR
class Gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self.red = Red_Gelir()
        self.green = Green_Gelir()
        self.blue = Blue_Gelir()

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._red_ID, 0, _v_._sb__toplam_gelir__ID) + _v_._salon_bilgisi_getir__(_v_._green_ID, 0, _v_._sb__toplam_gelir__ID) + _v_._salon_bilgisi_getir__(_v_._blue_ID, 0, _v_._sb__toplam_gelir__ID)


class Red_Gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._red_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._red_ID, matine_bilgisi, _v_._sb__tam_gelir__ID)

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._red_ID, 0, _v_._sb__toplam_gelir__ID)


class Green_Gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._green_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._green_ID, matine_bilgisi, _v_._sb__tam_gelir__ID)

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._green_ID, 0, _v_._sb__toplam_gelir__ID)


class Blue_Gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._blue_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._blue_ID, matine_bilgisi, _v_._sb__tam_gelir__ID)

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._blue_ID, 0, _v_._sb__toplam_gelir__ID)


class Kullanici():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    @property
    def listesi(self):
        return _v_._kullanicilar_list

    @property
    def sayisi(self):
        return _v_._kullanici_sayisi

    def bilgi__(self, istenilen_bilgi_ID, kullanici_id):
        return _v_._kullanici_bilgi__(istenilen_bilgi_ID, kullanici_id)

    def ekle__(self, bilgi_list):
        _v_._kullanici_ekle_ = bilgi_list

    @property
    def id_(self):
        return _v_._user_id

    @id_.setter
    def id_(self, ID):
        _v_._user_id = ID


class Salon():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self.bilet = Bilet()
        self.izleme = Izleme()
        self.gelir = Gelir()

    def isim__(self, isim_ID):
        return _v_._salon_isim__(isim_ID)

    def film_ismi__(self, film_ID):
        return _v_._film_isim__(film_ID)


#------------------------- VEK
class VEK():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self.genel = Genel()
        self.id = iD()
        self.salon = Salon()
        self.kullanici = Kullanici()
