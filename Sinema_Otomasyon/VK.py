class VERILER():
    def __init__(self) -> None:
        # Develped by OnCaDo
        self._salon_adlar = ("RED", "GREEN", "BLUE")
        self._film_adlar = ("Star Wars", "The Lord of The Rings", "Matrix")
        self._txt_modlar = ("w+", "a+")
        self._txt_isimler = ("sifre.txt", "log.txt")
        self._ID = (0, 1, 2, 3, 4, 5)
        self._abc = (
            "a0Ab1Bc2Cç3Çd4De5Ef6Fg7Gğ8Ğh9Hı.Ii,İj'Jk+Kl-Lm/Mn\\No*Oö%Öp&Pr(Rs)Sş=Şt?Tu$Uü{Üv[Vy]Yz}Zq~Qw<W>|:; ")
        self._bilet_bilgi = (20, 30, "Öğrenci", "Tam")
        self._kullanici_ad = []
        self._kullanici_sifre = []
        self._kullanicilar = [self._kullanici_ad, self._kullanici_sifre]
        self._u_idsi = None
        self._salon_1 = [[], [], [], [], []]
        self._salon_2 = [[], [], [], [], []]
        self._salon_3 = [[], [], [], [], []]
        self._salon = [self._salon_1, self._salon_2, self._salon_3]

    # ---------------------------- Tanımlamalar
    @property
    def _sb__toplam_izlenme__ID(self):
        return self._ID[0]

    @property
    def _sb__ogrenci_izleme__ID(self):
        return self._ID[1]

    @property
    def _sb__ogrenci_gelir__ID(self):
        return self._ID[2]

    @property
    def _sb__tam_izleme__ID(self):
        return self._ID[3]

    @property
    def _sb__tam_gelir__ID(self):
        return self._ID[4]

    @property
    def _sb__toplam_gelir__ID(self):
        return self._ID[5]

    @property
    def _ogrenci_ID(self):
        return self._ID[2]

    @property
    def _ogrenci_ucret_ID(self):
        return self._ID[0]

    @property
    def _tam_ID(self):
        return self._ID[3]

    @property
    def _tam_ucret_ID(self):
        return self._ID[1]

    @property
    def _yok(self):
        return self._ID[0]

    @property
    def _var(self):
        return self._ID[1]

    @property
    def _salon_1_ID(self):
        return self._ID[0]

    @property
    def _salon_2_ID(self):
        return self._ID[1]

    @property
    def _salon_3_ID(self):
        return self._ID[2]

    @property
    def _film_1_ID(self):
        return self._ID[0]

    @property
    def _film_2_ID(self):
        return self._ID[1]

    @property
    def _film_3_ID(self):
        return self._ID[2]

    @property
    def _yaz_ID(self):
        return self._ID[0]

    @property
    def _ekle_ID(self):
        return self._ID[1]

    @property
    def _txt_sifre_ID(self):
        return self._ID[0]

    @property
    def _txt_log_ID(self):
        return self._ID[1]

    @property
    def _kullanici_ad_ID(self):
        return self._ID[0]

    @property
    def _kullanici_sifre_ID(self):
        return self._ID[1]

    @property
    def _sifrele_ID(self):
        return self._ID[0]

    @property
    def _cozumle_ID(self):
        return self._ID[1]

    @property
    def _user_id(self):
        return self._u_idsi

    @_user_id.setter
    def _user_id(self, x):
        self._u_idsi = x

    @property
    def _kullanicilar_list(self):
        return self._kullanicilar

    @_kullanicilar_list.setter
    def _kullanici_ekle_(self, x):
        with open(self._txt_ad__(self._txt_sifre_ID), self._mod_turu__(self._ekle_ID)) as d:
            d.write(f"{x[0]} {x[1]}\n")

    @property
    def _kullanici_sayisi(self):
        self._verileri_cek
        return len(self._kullanicilar_list[self._kullanici_ad_ID])

    @property
    def _dosyalari_olustur(self):
        import os
        if not os.path.exists(self._txt_ad__(self._txt_sifre_ID)):
            with open(self._txt_ad__(self._txt_sifre_ID), self._mod_turu__(self._yaz_ID)) as d:
                pass
        if not os.path.exists(self._txt_ad__(self._txt_log_ID)):
            log = ["""~~~~~~~~~~~~~~~~~~~~~~OnCaDo~~~~~~~~~~~~~~~~~~~~~~"""]
            for i in range(3):
                log.append(
                    f"""\n\n--> {self._salon_adlar[i]} salonundaki {self._film_adlar[i]} filminin""")
                for j in range(5):
                    log.append(
                        f"""\n{j+1}. matinede: 0 izlenme (0 Öğrenci: 0 ₺, 0 Tam: 0 ₺)""")
                log.append(
                    f"""\n\n{self._salon_adlar[i]} salonunun toplam geliri: 0 ₺""")
            log.append("""\n\nToplam Hasılat: 0 ₺""")
            with open(self._txt_ad__(self._txt_log_ID), self._mod_turu__(self._yaz_ID)) as d:
                d.writelines(log)

    @property
    def _verileri_goster(self):
        self._verileri_cek
        toplam = 0
        log = ["""~~~~~~~~~~~~~~~~~~~~~~OnCaDo~~~~~~~~~~~~~~~~~~~~~~"""]
        for i in range(3):
            log.append(
                f"""\n\n--> {self._salon_adlar[i]} salonundaki {self._film_adlar[i]} filminin""")
            for j in range(5):
                log.append(
                    f"""\n{j+1}. matinede: {self._salon_bilgisi_getir__(i,j,self._sb__toplam_izlenme__ID)} izlenme ({self._salon_bilgisi_getir__(i,j,self._sb__ogrenci_izleme__ID)} Öğrenci: {self._salon_bilgisi_getir__(i,j,self._sb__ogrenci_gelir__ID)} ₺, {self._salon_bilgisi_getir__(i,j,self._sb__tam_izleme__ID)} Tam: {self._salon_bilgisi_getir__(i,j,self._sb__tam_gelir__ID)} ₺)""")
            log.append(
                f"""\n\n{self._salon_adlar[i]} salonunun toplam geliri: {self._salon_bilgisi_getir__(i,j,self._sb__toplam_gelir__ID)} ₺""")
            toplam += self._salon_bilgisi_getir__(i,
                                                  j, self._sb__toplam_gelir__ID)
        log.append(f"\n\nToplam Hasılat: {toplam} ₺")
        for i in range(len(log)):
            print(log[i], end="")

    @property
    def _verileri_kaydet(self):
        toplam = 0
        log = ["""~~~~~~~~~~~~~~~~~~~~~~OnCaDo~~~~~~~~~~~~~~~~~~~~~~"""]
        for i in range(3):
            log.append(
                f"""\n\n--> {self._salon_adlar[i]} salonundaki {self._film_adlar[i]} filminin""")
            for j in range(5):
                log.append(
                    f"""\n{j+1}. matinede: {self._salon_bilgisi_getir__(i,j,self._sb__toplam_izlenme__ID)} izlenme ({self._salon_bilgisi_getir__(i,j,self._sb__ogrenci_izleme__ID)} Öğrenci: {self._salon_bilgisi_getir__(i,j,self._sb__ogrenci_gelir__ID)} ₺, {self._salon_bilgisi_getir__(i,j,self._sb__tam_izleme__ID)} Tam: {self._salon_bilgisi_getir__(i,j,self._sb__tam_gelir__ID)} ₺)""")
            log.append(
                f"""\n\n{self._salon_adlar[i]} salonunun toplam geliri: {self._salon_bilgisi_getir__(i,j,self._sb__toplam_gelir__ID)} ₺""")
            toplam += self._salon_bilgisi_getir__(i,
                                                  j, self._sb__toplam_gelir__ID)
        log.append(f"\n\nToplam Hasılat: {toplam} ₺")
        with open(self._txt_ad__(self._txt_log_ID), self._mod_turu__(self._yaz_ID)) as d:
            d.writelines(log)

    @property
    def _verileri_cek(self):
        try:
            for i in range(2):
                self._kullanicilar_list[i].clear()
            veri = []
            with open(self._txt_ad__(self._txt_sifre_ID)) as d:
                veri = d.readlines()
            for i in range(len(veri)):
                bilgi = veri[i]
                x = bilgi.split()
                usr, pas = x[0], x[1]
                self._kullanicilar[self._kullanici_ad_ID].append(usr)
                self._kullanicilar[self._kullanici_sifre_ID].append(pas)
            salon = []
            for i in range(5):
                self._salon_1[i].clear()
                self._salon_2[i].clear()
                self._salon_3[i].clear()
            with open(self._txt_ad__(self._txt_log_ID)) as d:
                salon = d.readlines()
            veri.clear()
            for i in range(len(salon)):
                veri.append(salon[i].split())
            for i in range(5):
                self._salon_1[i].append(veri[3+i][2])
                self._salon_1[i].append(veri[3+i][4].replace("(", ""))
                self._salon_1[i].append(veri[3+i][6])
                self._salon_1[i].append(veri[3+i][8])
                self._salon_1[i].append(veri[3+i][10])
                self._salon_2[i].append(veri[12+i][2])
                self._salon_2[i].append(veri[12+i][4].replace("(", ""))
                self._salon_2[i].append(veri[12+i][6])
                self._salon_2[i].append(veri[12+i][8])
                self._salon_2[i].append(veri[12+i][10])
                self._salon_3[i].append(veri[21+i][2])
                self._salon_3[i].append(veri[21+i][4].replace("(", ""))
                self._salon_3[i].append(veri[21+i][6])
                self._salon_3[i].append(veri[21+i][8])
                self._salon_3[i].append(veri[21+i][10])
            self._salon_1.append(veri[9][4])
            self._salon_2.append(veri[18][4])
            self._salon_3.append(veri[27][4])
        except Exception:
            print("Veriler alınırken bir hata oluştu... \nDosya bozulmuş olabilir..")
            exit()

    # ---------------------------- Veri Fonksiyonları
    def _film_isim__(self, film_ID):
        return self._film_adlar[film_ID]

    def _salon_isim__(self, isim_ID):
        return self._salon_adlar[isim_ID]

    def _mod_turu__(self, istenilen_mod_ID):
        return self._txt_modlar[istenilen_mod_ID]

    def _txt_ad__(self, istenilen_txt_ID):
        return self._txt_isimler[istenilen_txt_ID]

    def _kullanici_bilgi__(self, istenilen_bilgi_ID, kullanici_id):
        self._user_id = kullanici_id
        return self._kullanicilar_list[istenilen_bilgi_ID][kullanici_id]

    def _bilet_bilgisi__(self, istenilen_bilgi_ID):
        return self._bilet_bilgi[istenilen_bilgi_ID]

    def _salon_bilgisi_getir__(self, isim_ID, matine_ID, istenilen_bilgi_ID):
        if istenilen_bilgi_ID == self._sb__toplam_gelir__ID:
            return int(self._salon[isim_ID][self._sb__toplam_gelir__ID])
        else:
            return int(self._salon[isim_ID][matine_ID][istenilen_bilgi_ID])

    def _bilgi_guncelle__(self, salon_ID, matine_bilgisi, guncellenecek_veri_ID, yeni_veri):
        if guncellenecek_veri_ID == self._sb__toplam_gelir__ID:
            self._salon[salon_ID][self._sb__toplam_gelir__ID] = yeni_veri
        else:
            self._salon[salon_ID][int(matine_bilgisi)
                                  ][guncellenecek_veri_ID] = yeni_veri

    def _kripto__(self, metin, islem_ID, ilerleme=9):
        sonuc = ""
        for i in range(len(metin)):
            if islem_ID == self._sifrele_ID:
                sonuc += "".join(self._abc[(self._abc.find(metin[i]
                                                           )+ilerleme) % len(self._abc)])
            else:
                sonuc += "".join(self._abc[self._abc.find(metin[i])-ilerleme])
        return sonuc
