from VK import VERILER

_v_ = VERILER()


#------------------------- GENEL
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


#------------------------- ID
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
    def salon_1(self):
        return _v_._salon_1_ID

    @property
    def salon_2(self):
        return _v_._salon_2_ID

    @property
    def salon_3(self):
        return _v_._salon_3_ID

    @property
    def film_1(self):
        return _v_._film_1_ID

    @property
    def film_2(self):
        return _v_._film_2_ID

    @property
    def film_3(self):
        return _v_._film_3_ID

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
        self.salon_1 = salon_1_izlenme()
        self.salon_2 = salon_2_izlenme()
        self.salon_3 = salon_3_izlenme()

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


class salon_1_izlenme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_1, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_1, matine_bilgisi, _v_._sb__tam_izleme__ID)

    def toplam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_1, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


class salon_2_izlenme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_2, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_2, matine_bilgisi, _v_._sb__tam_izleme__ID)

    def toplam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_2, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


class salon_3_izlenme():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_3, matine_bilgisi, _v_._sb__ogrenci_izleme__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_3, matine_bilgisi, _v_._sb__tam_izleme__ID)

    def toplam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_.salon_3, matine_bilgisi, _v_._sb__toplam_izlenme__ID)


#------------------------- GELIR
class Gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self.salon_1 = salon_1_gelir()
        self.salon_2 = salon_2_gelir()
        self.salon_3 = salon_3_gelir()

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._salon_1_ID, 0, _v_._sb__toplam_gelir__ID) + _v_._salon_bilgisi_getir__(_v_._salon_2_ID, 0, _v_._sb__toplam_gelir__ID) + _v_._salon_bilgisi_getir__(_v_._salon_3_ID, 0, _v_._sb__toplam_gelir__ID)


class salon_1_gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._salon_1_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._salon_1_ID, matine_bilgisi, _v_._sb__tam_gelir__ID)

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._salon_1_ID, 0, _v_._sb__toplam_gelir__ID)


class salon_2_gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._salon_2_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._salon_2_ID, matine_bilgisi, _v_._sb__tam_gelir__ID)

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._salon_2_ID, 0, _v_._sb__toplam_gelir__ID)


class salon_3_gelir():
    def __init__(self) -> None:
        # Develped by OnCaDo
        pass

    def ogrenci__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._salon_3_ID, matine_bilgisi, _v_._sb__ogrenci_gelir__ID)

    def tam__(self, matine_bilgisi):
        return _v_._salon_bilgisi_getir__(_v_._salon_3_ID, matine_bilgisi, _v_._sb__tam_gelir__ID)

    def toplam(self):
        return _v_._salon_bilgisi_getir__(_v_._salon_3_ID, 0, _v_._sb__toplam_gelir__ID)


#------------------------- KULLANICI
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


#------------------------- SALON
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
