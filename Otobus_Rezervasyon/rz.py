import os


class RZR():

    class bilgiler():

        class veri_tabanı():

            class sabit():

                hexa = ["0", "1", "2", "3", "4",
                        "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
                abc = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

                class oto():

                    ob_model = "ot_model"
                    ob_mesafe = "ot_mesafe"
                    ob_kapasite = "ob_kapasite"
                    ob_per_say = "ob_per_say"
                    ob_sfr_durumu = "ob_sfr_durum"
                    ob_uzun_mesafe = "Uzun Yol Aracı"
                    ob_normal_mesafe = "Normal Araç"
                    ob_sfr_var = "VAR"
                    ob_sfr_yok = "YOK"
                    ob_dolu_kltk = "dolu_koltuklar"

                class sfr():
                    sb_no = "sfr_no"
                    sb_oto_no = "sfr_oto_no"
                    sb_bas_sa = "sfr_bas_saat"
                    sb_bas_dk = "sfr_bit_dak"
                    sb_bas_seh = "sfr_bas_sehri"
                    sb_bit_sa = "sfr_bit_saat"
                    sb_bit_dk = "sfr_bit_dak"
                    sb_bit_seh = "sfr_bit_sehri"
                    sb_is_has = "sfr_is_has"
                    sb_kb_uc = "sfr_kb_ucrt"

                class menuler():
                    class ana_menu():
                        ad = "OnCaDo"
                        mesaj = """
                                    1-Firma Girişi
                                    2-Müşteri Girişi

                                        5-Çıkış

                                    Lütfen bir giriş yapınız:-> """

                    class firma():
                        ad = "Firma Menüsü"
                        mesaj = """
                                    1-Otobüs Bilgisi Ekle
                                    2-Otobüs Listele
                                    3-Sefer Bilgisi Ekle
                                    4-Sefer/Koltuk Bilgisi
                                        5-Bir Üst Menüye Dön

                                    Lütfen bir giriş yapınız:-> """

                    class musteri():
                        ad = "Müşteri Menüsü"
                        mesaj = """
                                    1-Seferleri Listele
                                    2-Sefer Rezervasyon Yap
                                    3-Rezervasyon Göster
                                        4-Bir Üst Menüye Dön

                                    Lütfen bir giriş yapınız:-> """

                class fonks():
                    class oto_sfr_ekle():
                        mesaj = "\n1-Yeni Kayıt\n2-Üst Menü\n\tLütfen bir giriş yapınız:->"

                    class sefr_koltuk_secim():
                        ad = "Sefer/Koltuk Menüsü:"
                        mesaj = """
                    Detaylı Bilgi İçin Sefer Numarsını giriniz
                        2-Bir Üst Menüye Dön

                    Lütfen bir giriş yapınız:-> """

                    class sefer_bilgi_detay():
                        mesaj = """

                    2-Bir Üst Menüye Dön
                    Lütfen bir giriş yapınız:-> """

                class musteri():
                    ad = "m_ad"
                    soyad = "m_sad"
                    koltuk = "k_no"
                    sefer = "s_no"
                    rez_no = "r_no"

            class dgskn():
                class oto():
                    bilgi = {}
                    ob_no = None
                    ob_dolu_kltklr = []

                class sfr():
                    bilgi = {}
                    # sefer_numarasi = None
                    secilmis_sefer_no = None
                    hexa_liste = []

                class musteri():
                    bilgi = {}
                    secilen_rez_no = None
                    rez_list = []

        class sefer():
            class getir():

                def _sferler():
                    return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi

                def _sfr_nolar_lst():
                    sfr = RZR.bilgiler.sefer.getir._sferler()
                    s = sfr.keys()
                    s = list(s)
                    return s

                def _sfr_sayisi():
                    s = len(RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi)
                    return s

                class bilgi():
                    def secilmis_sefer_no():
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.secilmis_sefer_no

                    def sefer_bilgi(sfr_no):
                        sfr = RZR.bilgiler.sefer.getir.ayrinti
                        print(f"""\t{sfr_no} Nolu Seferin:
                        # Oto no: {sfr.oto_no(sfr_no)}
                        # Başlama: {sfr.baslangic(sfr_no)}
                        # Bitiş: {sfr.bitis(sfr_no)}
                        # Hasılat: {sfr.is_hslt(sfr_no)}
                        # Bilet: {sfr.kb_ucrt(sfr_no)}
                        """)

                    def sefer_detayi(sfr_no):
                        sfr = RZR.bilgiler.sefer.getir.ayrinti
                        oto = RZR.bilgiler.oto.getir.ayrinti
                        o_no = sfr.oto_no(sfr_no)
                        o_kps = oto.kapasite(o_no)
                        dl_kltk_sa = oto.dolu_klt_sayisi(o_no)
                        kbu = sfr.kb_ucrt(sfr_no)

                        bos = o_kps-dl_kltk_sa
                        hslt = dl_kltk_sa * kbu

                        print(f"""\t{sfr_no} Nolu Seferin:
                        # Otobüs No:\t\t{o_no}
                        # Otobüs Kapasitesi:\t{o_kps}
                        # Başlama:\t\t{sfr.baslangic(sfr_no)}
                        # Bitiş:\t\t{sfr.bitis(sfr_no)}
                        # Hasılat:\t\t{sfr.is_hslt(sfr_no):.2f} ₺
                        # Bilet Ücreti:\t\t{kbu:.2f} ₺
                        # Toplam Has:\t\t{hslt:.2f} ₺
                        # Boş Koltuk:\t\t{bos}
                        """)

                    def tum_seferler():
                        ssa = RZR.bilgiler.sefer.getir._sfr_sayisi()
                        sfr = RZR.bilgiler.sefer.getir.bilgi.sefer_bilgi
                        no = RZR.bilgiler.sefer.getir._sfr_sayisi()
                        for i in range(ssa):
                            sfr(no[i])

                    def sfr_oztler():
                        def sfr_ozet(sfr_no):
                            sfr = RZR.bilgiler.sefer.getir.ayrinti
                            print(f"""
                            # {sfr_no} Nolu Seferin Özeti: Oto no: {sfr.oto_no(sfr_no)}, Başlama: {sfr.baslangic(sfr_no)}, Bitiş: {sfr.bitis(sfr_no)}
                            """)
                        ssa = RZR.bilgiler.sefer.getir._sfr_sayisi()
                        no = RZR.bilgiler.sefer.getir._sfr_nolar_lst()
                        for i in range(ssa):
                            sfr_ozet(no[i])

                    def sfr_ozt_msteri_icin():
                        def sfr_ozt(sfr_no):
                            sfr = RZR.bilgiler.sefer.getir.ayrinti
                            oto = RZR.bilgiler.oto.getir.ayrinti
                            o_no = sfr.oto_no(sfr_no)
                            o_kps = oto.kapasite(o_no)
                            dl_kltk_sa = oto.dolu_klt_sayisi(o_no)
                            kbu = sfr.kb_ucrt(sfr_no)
                            bos = o_kps-dl_kltk_sa
                            print(f"""
                    # {sfr_no} Nolu Seferin Özeti: 
                    Oto no: {sfr.oto_no(sfr_no)}, Başlama: {sfr.baslangic(sfr_no)}, Bitiş: {sfr.bitis(sfr_no)}, Boş Koltuk: {bos}, Bilet Ücreti: {kbu:.2f} ₺
                            """)
                        ssa = RZR.bilgiler.sefer.getir._sfr_sayisi()
                        no = RZR.bilgiler.sefer.getir._sfr_nolar_lst()
                        no.reverse()

                        for i in range(ssa):
                            sfr_ozt(no[i])

                class ayrinti():

                    def oto_no(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_oto_no]

                    def baslangic(sfr_no):
                        sa = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_sa]
                        dk = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_dk]
                        seh = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_seh]
                        zmn = f"{sa}:{dk} {seh}"
                        return zmn

                    def bitis(sfr_no):
                        sa = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_sa]
                        dk = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_dk]
                        seh = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_seh]
                        zmn = f"{sa}:{dk} {seh}"
                        return zmn

                    def bas_sa_dk(sfr_no):
                        sa = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_sa]
                        dk = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_dk]
                        zmn = f"{sa}:{dk}"
                        return zmn

                    def bit_sa_dk(sfr_no):
                        sa = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_sa]
                        dk = RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][
                            RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_dk]
                        zmn = f"{sa}:{dk}"
                        return zmn

                    def bas_sa(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_sa]

                    def bit_sa(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_sa]

                    def bas_dk(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_dk]

                    def bit_dk(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_dk]

                    def bas_seh(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bas_seh]

                    def bit_seh(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_bit_seh]

                    def is_hslt(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_is_has]

                    def kb_ucrt(sfr_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi[sfr_no][RZR.bilgiler.veri_tabanı.sabit.sfr.sb_kb_uc]

            class ekle():
                def sefer_bilgi(s_no, o_no, b_sa, b_dk, b_seh, v_sa, v_dk, v_seh, is_ha, kb_uc):
                    sbt = RZR.bilgiler.veri_tabanı.sabit.sfr
                    ot_no = sbt.sb_oto_no
                    bas_sa = sbt.sb_bas_sa
                    bas_dk = sbt.sb_bas_dk
                    bas_shr = sbt.sb_bas_seh
                    bit_sa = sbt.sb_bit_sa
                    bit_dk = sbt.sb_bit_dk
                    bit_shr = sbt.sb_bit_seh
                    is_hasl = sbt.sb_is_has
                    kb_h = sbt.sb_kb_uc

                    sb = {s_no: {ot_no: o_no, bas_sa: b_sa, bas_dk: b_dk,
                                 bas_shr: b_seh, bit_sa: v_sa, bit_dk: v_dk, bit_shr: v_seh, is_hasl: is_ha, kb_h: kb_uc}}

                    RZR.bilgiler.veri_tabanı.dgskn.sfr.bilgi.update(sb)

                def secilmis_sefer_no(sfr_no):
                    RZR.bilgiler.veri_tabanı.dgskn.sfr.secilmis_sefer_no = sfr_no

        class oto():
            class getir():
                def _otolar():
                    return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi

                def _oto_nolar_lst():
                    oto = RZR.bilgiler.oto.getir._otolar()
                    s = oto.keys()
                    s = list(s)
                    return s

                def _oto_sayisi():
                    s = len(RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi)
                    return s

                class bilgi():
                    def oto_bilgi(oto_no):
                        oto = RZR.bilgiler.oto.getir.ayrinti

                        print(f"""\t{oto_no} Nolu Aracın:
                        # Modeli:\t\t{oto.model(oto_no)}
                        # Kapasitesi:\t\t{oto.kapasite(oto_no)}
                        # Personel Sayısı:\t{oto.per_sayi(oto_no)}
                        # Türü:\t\t\t{oto.mesafe(oto_no)}
                        # Sefer Durumu:\t\t{oto.sefer_durumu(oto_no)}
                        """)

                    def tum_otolar():
                        no = RZR.bilgiler.oto.getir._oto_nolar_lst()
                        oto = RZR.bilgiler.oto.getir.bilgi.oto_bilgi
                        for i in no:
                            oto(i)

                    def oto_sfr_icin_listele(msf):
                        no = RZR.bilgiler.oto.getir._oto_nolar_lst()
                        oto = RZR.bilgiler.oto.getir.bilgi.oto_bilgi
                        o_m = RZR.bilgiler.oto.getir.ayrinti.mesafe
                        arac_no = []
                        mesafe = RZR.bilgiler.veri_tabanı.sabit.oto.ob_uzun_mesafe
                        if msf == mesafe:
                            for i in no:
                                if o_m(i) == mesafe:
                                    if RZR.bilgiler.oto.getir.ayrinti.sefer_durumu(i) == RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_yok:
                                        oto(i)
                                        arac_no.append(i)
                        else:
                            for i in no:
                                if RZR.bilgiler.oto.getir.ayrinti.sefer_durumu(i) == RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_yok:
                                    oto(i)
                                    arac_no.append(i)
                        if len(arac_no) > 0:
                            return arac_no
                        else:
                            s = input(
                                "Sefer için uygun araç bulunamadı.. Lütfen önce uygun bir araç ekleyiniz..\n")
                            RZR.menuler.oto_bilgi_ekle()

                class ayrinti():
                    def model(oto_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_model]

                    def mesafe(oto_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_mesafe]

                    def kapasite(oto_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_kapasite]

                    def per_sayi(oto_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_per_say]

                    def sefer_durumu(oto_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_durumu]

                    def dolu_koltuklar(oto_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_dolu_kltk]

                    def dolu_klt_sayisi(oto_no):
                        return len(
                            RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][RZR.bilgiler.veri_tabanı.sabit.oto.ob_dolu_kltk])

            class ekle():
                def oto_bilgi(model, mesafe, kapasite, per_sa):
                    ks = RZR.bilgiler.oto.getir._oto_sayisi()
                    sbt = RZR.bilgiler.veri_tabanı.sabit.oto
                    dgskn = RZR.bilgiler.veri_tabanı.dgskn.oto
                    no = dgskn.ob_no
                    dolu_kltk = dgskn.ob_dolu_kltklr
                    if ks == 0:
                        no = 1
                    else:
                        no = ks+1

                    mdl = sbt.ob_model
                    msf = sbt.ob_mesafe
                    kpst = sbt.ob_kapasite
                    p_sa = sbt.ob_per_say
                    sfr_drm = sbt.ob_sfr_durumu
                    dl_kltk = sbt.ob_dolu_kltk

                    ob = {no: {mdl: model, msf: mesafe, kpst: kapasite,
                               p_sa: per_sa, sfr_drm: sbt.ob_sfr_yok, dl_kltk: dolu_kltk}}
                    RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi.update(ob)

                def sfr_drm_guncelle(oto_no):
                    RZR.bilgiler.veri_tabanı.dgskn.oto.bilgi[oto_no][
                        RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_durumu] = RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_var
                    model = RZR.bilgiler.oto.getir.ayrinti.model(oto_no)
                    print(f"""
                        {oto_no} NOLU ve {model} MODEL otobüsün sefer durumu:
                        {RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_var} olarak güncellendi.
                        """)

                def dolu_koltuk_ekle(o_no, k_no):
                    klt = RZR.bilgiler.oto.getir.ayrinti.dolu_koltuklar(o_no)
                    klt.append(k_no)
                    klt = set(klt)
                    klt = list(klt)
                    klt.sort()

        class musteri():
            class getir():
                def _rezler():
                    return RZR.bilgiler.veri_tabanı.dgskn.musteri.bilgi

                def _rez_nolar_lst():
                    rez = RZR.bilgiler.musteri.getir._rezler()
                    s = rez.keys()
                    s = list(s)
                    return s

                class bilgi():
                    def rez_bilgi(rez_no):
                        ad = RZR.bilgiler.musteri.getir.ayrinti.ad(rez_no)
                        soyad = (
                            RZR.bilgiler.musteri.getir.ayrinti.s_ad(rez_no))
                        s_no = (RZR.bilgiler.musteri.getir.ayrinti.sefer(rez_no))
                        sfr = RZR.bilgiler.sefer.getir.ayrinti
                        ono = RZR.bilgiler.sefer.getir.ayrinti.oto_no(s_no)
                        koltuk = (
                            RZR.bilgiler.musteri.getir.ayrinti.koltuk(rez_no))
                        baslangic = RZR.bilgiler.sefer.getir.ayrinti.baslangic(
                            s_no)
                        bitis = RZR.bilgiler.sefer.getir.ayrinti.bitis(s_no)
                        bitis = RZR.bilgiler.sefer.getir.ayrinti.oto_no(s_no)
                        arc_mdl = RZR.bilgiler.oto.getir.ayrinti.model(ono)
                        ucret = RZR.bilgiler.sefer.getir.ayrinti.kb_ucrt(s_no)

                        print(f"""\tMerhaba Say. {ad} {soyad}
                        {rez_no} Nolu Rezervasyonunuzun Detayları
                        Bilet: {ucret:.2f} ₺
                        {s_no} Nolu seferin araç modeli {arc_mdl}
                        Sefer Planı: {sfr.baslangic(s_no)} - {sfr.bitis(s_no)}
                        Koltuk NO: {koltuk}
                        """)

                    # def tum_rezler():
                    #     no = RZR.bilgiler.musteri.getir._rez_nolar_lst()
                    #     for i in no:
                    #         print(i)

                class ayrinti():
                    def ad(rez_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.musteri.bilgi[rez_no][RZR.bilgiler.veri_tabanı.sabit.musteri.ad]

                    def s_ad(rez_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.musteri.bilgi[rez_no][RZR.bilgiler.veri_tabanı.sabit.musteri.soyad]

                    def koltuk(rez_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.musteri.bilgi[rez_no][RZR.bilgiler.veri_tabanı.sabit.musteri.koltuk]

                    def sefer(rez_no):
                        return RZR.bilgiler.veri_tabanı.dgskn.musteri.bilgi[rez_no][RZR.bilgiler.veri_tabanı.sabit.musteri.sefer]

    class fnks():

        def ekran_temizle():
            if os.name == 'nt':
                _ = os.system('cls')
            else:
                _ = os.system('clear')

        def menu_baslik(menu_adi):
            print("~".center(109, "~"))
            print(f"{menu_adi}".center(109))
            print("~".center(109, "~"))

        def calistir(liste, secim):
            liste[secim]()

        def menu_secimleri(menu_adi, mesaj, scnklr):
            scm = None
            while not scm:
                RZR.fnks.ekran_temizle()
                RZR.fnks.menu_baslik(menu_adi)
                scm = input(mesaj)
            else:
                if not scm in scnklr.keys():
                    RZR.fnks.menu_secimleri(menu_adi, mesaj, scnklr)
                else:
                    RZR.fnks.calistir(scnklr, scm)

        def secim_yap(mesaj, scnklr):
            scm = None
            while not scm:
                scm = input(mesaj)
            else:
                scm = scm.upper()
                if not scm in scnklr.keys():
                    RZR.fnks.secim_yap(mesaj, scnklr)
                else:
                    RZR.fnks.calistir(scnklr, scm)

        def oto_listele():
            print("\nGüncel Liste:\n")
            RZR.bilgiler.oto.getir.bilgi.tum_otolar()

        def sefer_cikmamis_oto():
            arac = 0
            no_lst = RZR.bilgiler.oto.getir._oto_nolar_lst()
            for i in no_lst:
                if RZR.bilgiler.oto.getir.ayrinti.sefer_durumu(i) == RZR.bilgiler.veri_tabanı.sabit.oto.ob_sfr_yok:
                    arac += 1
            return arac

        def sefer_koltuk_secim():
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik(
                RZR.bilgiler.veri_tabanı.sabit.fonks.sefr_koltuk_secim.ad)
            sfr_nolar = RZR.bilgiler.sefer.getir._sfr_nolar_lst()
            sfr_sayi = RZR.bilgiler.sefer.getir._sfr_sayisi()
            if sfr_sayi > 0:
                RZR.bilgiler.sefer.getir.bilgi.sfr_oztler()
                s = None
                while not s:
                    s = input(
                        RZR.bilgiler.veri_tabanı.sabit.fonks.sefr_koltuk_secim.mesaj)
                else:
                    s = s.upper()
                    sfr_nolar.append('2')
                    if s in sfr_nolar:
                        try:
                            if s == "2":
                                RZR.menuler.firma_ekran()
                            else:
                                RZR.bilgiler.sefer.ekle.secilmis_sefer_no(s)
                                RZR.fnks.sefer_bilgi_detay()
                        except Exception:
                            print("Hatalı giriş yapıldı..")
                            return RZR.fnks.sefer_koltuk_secim()
                    else:
                        print("Hatalı giriş yapıldı..")
                        return RZR.fnks.sefer_koltuk_secim()
            else:
                print("Hiç kayıt yok")
                # sefer ekleme fnk

        def sefer_bilgi_detay():
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik("Sefer/Koltuk Detayları")
            sfr_no = RZR.bilgiler.veri_tabanı.dgskn.sfr.secilmis_sefer_no
            RZR.bilgiler.sefer.getir.bilgi.sefer_detayi(sfr_no)

            oto_no = RZR.bilgiler.sefer.getir.ayrinti.oto_no(sfr_no)
            kpst = RZR.bilgiler.oto.getir.ayrinti.kapasite(oto_no)
            dolu = RZR.bilgiler.oto.getir.ayrinti.dolu_koltuklar(oto_no)

            RZR.fnks.koltuk_listele(kpst, dolu)

            s = ""
            while not s:
                s = input(
                    RZR.bilgiler.veri_tabanı.sabit.fonks.sefer_bilgi_detay.mesaj)
            else:
                if s == '2':
                    RZR.fnks.sefer_koltuk_secim()
                else:
                    RZR.fnks.sefer_bilgi_detay()

        def koltuk_listele(kapasite, dolu_kultuklar):
            s1 = 1
            s2 = 1
            kp = kapasite
            i_ = kp//4
            _i = kp % 4
            i_sinir = i_+_i
            dolu = dolu_kultuklar
            dolu = set(dolu)
            dolu = list(dolu)
            dolu.sort()
            print("")
            for i in range(0, i_sinir):
                if s2 < 10:
                    if s2 in dolu:
                        print(f"\n{s2}  [D]", end="")
                    else:
                        print(f"\n{s2}  [ ]", end="")
                else:
                    if s2 in dolu:
                        print(f"\n{s2} [D]", end="")
                    else:
                        print(f"\n{s2} [ ]", end="")
                for j in range(1, 5):
                    if j > 1:
                        if s1 < 10:
                            if s1 in dolu:
                                print(f"\t\t{s1}  [D]", end="")
                            else:
                                print(f"\t\t{s1}  [ ]", end="")
                        else:
                            if s1 in dolu:
                                print(f"\t\t{s1} [D]", end="")
                            else:
                                print(f"\t\t{s1} [ ]", end="")
                    s1 += 1
                    if s1 > kp:
                        break
                s2 += 4
                if s2 > kp or s1 > kp:
                    break
            print("")

        def koltuk_isaretle(kapasite, dolu_koltuklar, isaretle):
            s1 = 1
            s2 = 1
            kp = kapasite
            i_ = kp//4
            _i = kp % 4
            i_sinir = i_+_i
            dolu = dolu_koltuklar
            dolu = set(dolu)
            dolu = list(dolu)
            dolu.sort()
            print("")
            for i in range(0, i_sinir):
                if s2 < 10:
                    if s2 in dolu:
                        print(f"\n{s2}  [D]", end="")
                    elif s2 == isaretle:
                        print(f"\n{s2}  [R]", end="")
                    else:
                        print(f"\n{s2}  [ ]", end="")
                else:
                    if s2 in dolu:
                        print(f"\n{s2} [D]", end="")
                    elif s2 == isaretle:
                        print(f"\n{s2}  [R]", end="")
                    else:
                        print(f"\n{s2} [ ]", end="")
                for j in range(1, 5):
                    if j > 1:
                        if s1 < 10:
                            if s1 in dolu:
                                print(f"\t\t{s1}  [D]", end="")

                            elif s1 == isaretle:
                                print(f"\t\t{s1}  [R]", end="")

                            else:
                                print(f"\t\t{s1}  [ ]", end="")
                        else:
                            if s1 in dolu:
                                print(f"\t\t{s1} [D]", end="")

                            elif s1 == isaretle:
                                print(f"\t\t{s1}  [R]", end="")

                            else:
                                print(f"\t\t{s1} [ ]", end="")
                    s1 += 1
                    if s1 > kp:
                        break
                s2 += 4
                if s2 > kp or s1 > kp:
                    break
            print("")

        def kayit_yok(hangi_kayit):
            s = input(
                f"Hiç {hangi_kayit} kaydı bununamadı.\nLütfen önce kayıt oluşturunuz..\nDevam etmek için ENTER tuşuna basınız.\n")

        def kayit_yok_mstr(hangi_kayit):
            s = input(
                f"Hiç {hangi_kayit} kaydı bununamadı.\nLütfen firma yetkilisiyle görüşünüz..\nDevam etmek için ENTER tuşuna basınız.\n")

        def ust_menuye_git():
            s = input(
                "Üst menüye gitmek için ENTER tuşuna basınız..\n")

        def tekrar_et(mesaj, scnk):
            scm = None
            while not scm:
                scm = input(mesaj)
            else:
                if not scm in scnk.keys():
                    RZR.fnks.menu_secimleri(mesaj, scnk)
                else:
                    RZR.fnks.calistir(scnk, scm)

        def oto_ekle():
            print("")

            def ot_model():
                o_m = None
                while not o_m:
                    o_m = input("Otobüs Modeli: ")
                else:
                    return o_m.upper()

            def ot_kapasite():
                o_k = None
                while not o_k:
                    o_k = input("Aracın Kapasitesi: ")
                else:
                    try:
                        o_k = int(o_k)
                        if 24 <= o_k <= 52:
                            return o_k
                        else:
                            print("Kapasite 24-52 olmalıdır..")
                            return ot_kapasite()

                    except Exception:
                        print("Hatalı giriş yapıldı.. ")
                        return ot_kapasite()

            def ot_per_sayi(kapasite):
                p_sa = None
                while not p_sa:
                    p_sa = input("Personel Sayısı: ")
                else:
                    try:
                        p_sa = int(p_sa)
                        if 2 <= p_sa <= 3:
                            if kapasite >= 30:
                                if p_sa == 3:
                                    return p_sa
                                else:
                                    print("Personel sayısı yetersiz..")
                                    return ot_per_sayi(kapasite)
                            else:
                                return p_sa
                        else:
                            print("Personel sayısı 2 ya da 3 kişi olmalıdır..")
                            return ot_per_sayi(kapasite)
                    except Exception:
                        print("Hatalı giriş yapıldı..")
                        return ot_per_sayi(kapasite)

            def ot_mes_bul(kapasite):
                if kapasite >= 30:
                    return RZR.bilgiler.veri_tabanı.sabit.oto.ob_uzun_mesafe
                else:
                    return RZR.bilgiler.veri_tabanı.sabit.oto.ob_normal_mesafe

            def kayit_olustur():

                mdl = ot_model()
                kpst = ot_kapasite()
                per_sa = ot_per_sayi(kpst)
                msf = ot_mes_bul(kpst)

                RZR.bilgiler.oto.ekle.oto_bilgi(mdl, msf, kpst, per_sa)

            kayit_olustur()
            RZR.fnks.oto_listele()

        def sefer_ekle():
            def sfr_NO():
                def hx_uret():
                    import random
                    no = '81'
                    hx = random.sample(RZR.bilgiler.veri_tabanı.sabit.hexa, 4)
                    a = ""
                    for i in hx:
                        a += i
                    no += a
                    return no

                def hex_kontrol(kod):
                    if RZR.bilgiler.veri_tabanı.dgskn.sfr.hexa_liste.count(kod) > 0:
                        return hx_uret()
                    else:
                        return kod

                hx = hx_uret()
                hx_no = hex_kontrol(hx)
                RZR.bilgiler.veri_tabanı.dgskn.sfr.hexa_liste.append(hx_no)
                return hx_no

            def saat_al(hangi):
                s = None
                while not s:
                    s = input(f"Sefer {hangi} Saati: ")
                else:
                    try:
                        s = int(s)
                        if 0 <= s <= 23:
                            return s
                        else:
                            print("24 Saat dilimi olmalıdır..")
                            return saat_al(hangi)
                    except Exception:
                        print("Hatalı giriş..")
                        return saat_al(hangi)

            def dakika_al(hangi):
                s = None
                while not s:
                    s = input(f"Sefer {hangi} Dakikası: ")
                else:
                    try:
                        s = int(s)
                        if 0 <= s <= 59:
                            return s
                        else:
                            print("24 Saat dilimi olmalıdır..")
                            return saat_al(hangi)
                    except Exception:
                        print("Hatalı giriş..")
                        return saat_al(hangi)

            def sfr_mesafe_hesapla(bas_sa, bas_dak, bit_sa, bit_dk):
                b_s, b_d, v_s, v_d = bas_sa, bas_dak, bit_sa, bit_dk
                dort_saat = 4*60
                yol_saat = (b_s-v_s)*60
                if yol_saat < 0:
                    yol_saat *= -1
                yol_dak = b_d-v_d
                if yol_dak < 0:
                    yol_dak *= -1

                yolculuk = yol_saat+yol_dak
                if yolculuk > dort_saat:
                    return RZR.bilgiler.veri_tabanı.sabit.oto.ob_uzun_mesafe
                else:
                    return RZR.bilgiler.veri_tabanı.sabit.oto.ob_normal_mesafe

            def sehir_al(hangi):
                s = None
                while not s:
                    s = input(f"{hangi} Şehri: ")
                else:
                    for i in s:
                        if i in RZR.bilgiler.veri_tabanı.sabit.abc:
                            return s.title()
                        else:
                            print(f"Lüfren {hangi}ı giriniz")
                            return sehir_al(hangi)
                    else:
                        print(f"Lüfren {hangi}ı giriniz")
                        return sehir_al(hangi)

            def ot_no_sec(ono):
                try:
                    no = None
                    while not no:
                        no = input("Otobüs NO Seçiniz: ")
                    else:
                        no = int(no)
                        if no in ono:
                            return no
                        else:
                            print("Hatalı giriş.. Listede olan :")
                            return ot_no_sec(ono)
                except Exception:
                    print("Hatalı giriş yapıldı.. Lütfen Otobüs NO seçiniz: ")
                    return ot_no_sec(ono)

            def ist_has():
                hslt = None
                while not hslt:
                    hslt = input("İstenilen hasıtlat miktarı: ")
                else:
                    try:
                        hslt = int(hslt)
                        if hslt == 0:
                            print("Hasılat miktarı 0 olamaz..")
                            return ist_has()
                        else:
                            return hslt
                    except Exception:
                        print("Hatalı giriş yapıldı..")
                        return ist_has()

            def kb_ucrt(is_has, o_no):
                kpst = RZR.bilgiler.oto.getir.ayrinti.kapasite(o_no)
                kb = is_has/kpst
                return kb

            ot_sa = RZR.bilgiler.oto.getir._oto_sayisi()
            cikmamis_oto = RZR.fnks.sefer_cikmamis_oto()
            if ot_sa > 0:
                if cikmamis_oto > 0:
                    sefer_no = sfr_NO()
                    bas_sa = saat_al('Başlama')
                    bas_dk = dakika_al('Başlama')
                    bit_sa = saat_al('Bitiş')
                    bit_dk = dakika_al('Bitiş')
                    mesafe = sfr_mesafe_hesapla(bas_sa, bas_dk, bit_sa, bit_dk)
                    baslangic_seh = sehir_al('Başlangıç')
                    bitis_seh = sehir_al('Bitiş')

                    if mesafe == RZR.bilgiler.veri_tabanı.sabit.oto.ob_uzun_mesafe:
                        print("\n\nUzun bir yolculuk..")
                    else:
                        print("\n\nNormal bir yolculuk..")

                    onumlar = RZR.bilgiler.oto.getir.bilgi.oto_sfr_icin_listele(
                        mesafe)
                    ot_no = ot_no_sec(onumlar)

                    istenilen_has = ist_has()
                    kisi_bas_has = kb_ucrt(istenilen_has, ot_no)

                    RZR.bilgiler.sefer.ekle.sefer_bilgi(
                        sefer_no, ot_no, bas_sa, bas_dk, baslangic_seh, bit_sa, bit_dk, bitis_seh, istenilen_has, kisi_bas_has)

                    RZR.bilgiler.oto.ekle.sfr_drm_guncelle(ot_no)

                else:
                    print("Boşta otobüs kalmadı.. Yeni kayıt eklenmeli")
                    RZR.fnks.oto_ekle()
            else:
                RZR.fnks.kayit_yok("Otobüs")
                RZR.fnks.oto_ekle()

        def rez_secim():
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik("Rezervasyon Seçim Ekranı")
            sfr_nolar = RZR.bilgiler.sefer.getir._sfr_nolar_lst()
            sfr_sayi = RZR.bilgiler.sefer.getir._sfr_sayisi()
            if sfr_sayi > 0:
                RZR.bilgiler.sefer.getir.bilgi.sfr_ozt_msteri_icin()
                s = None
                while not s:
                    s = input(
                        RZR.bilgiler.veri_tabanı.sabit.fonks.sefr_koltuk_secim.mesaj)
                else:
                    s = s.upper()
                    sfr_nolar.append('2')

                    if s in sfr_nolar:
                        print("Başarılı")
                        print(s)
                        if s == "2":
                            RZR.menuler.musteri_ekran()
                        else:
                            RZR.bilgiler.sefer.ekle.secilmis_sefer_no(s)
                            RZR.fnks.rez_olustur()
                    else:
                        print("Hatalı giriş.. Listeden seçiniz..")
                        RZR.fnks.rez_secim()
            else:
                RZR.fnks.kayit_yok_mstr("Sefer")
                RZR.menuler.musteri_ekran()

        def rez_olustur():
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik("Rezervasyon Yap")
            s_no = RZR.bilgiler.sefer.getir.bilgi.secilmis_sefer_no()
            o_no = RZR.bilgiler.sefer.getir.ayrinti.oto_no(s_no)
            dolu_koltuk = RZR.bilgiler.oto.getir.ayrinti.dolu_klt_sayisi(o_no)
            dolular = RZR.bilgiler.oto.getir.ayrinti.dolu_koltuklar(o_no)
            kapasite = RZR.bilgiler.oto.getir.ayrinti.kapasite(o_no)
            mb = RZR.bilgiler.veri_tabanı.sabit.musteri
            bos_koltuk = kapasite-dolu_koltuk

            if bos_koltuk > 0:
                def ad_al(hangisi):
                    s = None
                    while not s:
                        s = input(f"{hangisi}: ")
                    else:
                        for i in s:
                            if i in RZR.bilgiler.veri_tabanı.sabit.abc:
                                return s.title()
                            else:
                                print(f"Lüfren {hangisi}ı giriniz")
                                return ad_al(hangisi)
                        else:
                            print(f"Lüfren {hangisi}ı giriniz")
                            return ad_al(hangisi)

                def koltuk_no_al():
                    s = None
                    while not s:

                        s = input("Boş bir koltuk seçiniz: ")
                    else:
                        s = int(s)
                        if s in dolular:
                            print(
                                "Dolu bir koltuk seçtiniz.. Lütfen boş bir koluk seçiniz..")
                            return koltuk_no_al()
                        else:
                            if 0 < s <= kapasite:
                                return s
                            else:
                                print("Hatalı seçim yapıldı")
                                return koltuk_no_al()

                def onay_al():
                    s = None
                    while not s:
                        s = input("Onaylıyor musunuz? (E/H)\n")
                    else:
                        if ((s == "e" or s == "h")) or ((s == "E") or (s == "H")):
                            return s.upper()
                        else:
                            print("Hatalı giriş..")
                            return onay_al()

                def rez_NO():

                    def hx_uret():
                        import random
                        hx = random.sample(
                            RZR.bilgiler.veri_tabanı.sabit.hexa, 8)
                        no = ""
                        for i in hx:
                            no += i
                        return no.upper()

                    def hex_kontrol(kod):
                        if RZR.bilgiler.veri_tabanı.dgskn.musteri.rez_list.count(kod) > 0:
                            return hx_uret()
                        else:
                            return kod

                    hx = hx_uret()
                    hx_no = hex_kontrol(hx)
                    RZR.bilgiler.veri_tabanı.dgskn.musteri.rez_list.append(
                        hx_no)
                    return hx_no

                print("Boş Koltuklar")
                RZR.fnks.koltuk_listele(kapasite, dolular)
                ad = ad_al("\nAdınız")
                soyad = ad_al("Soyadınız")
                koltuk = koltuk_no_al()

                RZR.fnks.koltuk_isaretle(kapasite, dolular, koltuk)

                onay = onay_al()

                if (onay == "e") or (onay == "E"):
                    RZR.bilgiler.oto.ekle.dolu_koltuk_ekle(o_no, koltuk)
                    r_no = rez_NO()

                    mstr = {r_no: {mb.sefer: s_no, mb.ad: ad,
                                   mb.soyad: soyad, mb.koltuk: koltuk}}
                    RZR.bilgiler.veri_tabanı.dgskn.musteri.bilgi.update(mstr)

                    print(f"\nLütfen sefer numaranızı {r_no} saklayınız")
                    RZR.fnks.ust_menuye_git()
                    RZR.menuler.musteri_ekran()
                RZR.menuler.musteri_ekran()

            else:
                s = input(
                    "Bu sefer için boş koltuk kalmamıştır..lüften başka bir sefer seçiniz")
                RZR.fnks.rez_secim()

        def rez_no_sor():
            s = None
            while not s:
                s = input("Rezervasyon Numarası: ")
            else:
                return s.upper()

    class menuler():
        # ------------ANA MENU
        def ana_ekran():
            scnklr = {'1': RZR.menuler.firma_ekran,
                      '2': RZR.menuler.musteri_ekran, '5': quit}
            ana = RZR.bilgiler.veri_tabanı.sabit.menuler.ana_menu
            RZR.fnks.menu_secimleri(ana.ad, ana.mesaj, scnklr)

        # ------------Firma
        def firma_ekran():
            scnklr = {'1': RZR.menuler.oto_bilgi_ekle,
                      '2': RZR.menuler.oto_listele, '3': RZR.menuler.sefer_bilgi_ekle, '4': RZR.menuler.sefer_koltuk_bilgi, '5': RZR.menuler.ana_ekran}

            firma = RZR.bilgiler.veri_tabanı.sabit.menuler.firma
            RZR.fnks.menu_secimleri(firma.ad, firma.mesaj, scnklr)

        def oto_bilgi_ekle():
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik('Otobüs Bilgi EKleme')
            RZR.fnks.oto_ekle()

            s = {'1': RZR.menuler.oto_bilgi_ekle, '2': RZR.menuler.firma_ekran}
            RZR.fnks.tekrar_et(
                RZR.bilgiler.veri_tabanı.sabit.fonks.oto_sfr_ekle.mesaj, s)

        def oto_listele():
            # Üst menü Firma
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik('Otobüs Listesi')
            osa = RZR.bilgiler.oto.getir._oto_sayisi()
            if osa > 0:
                RZR.fnks.oto_listele()
                RZR.fnks.ust_menuye_git()
                RZR.menuler.firma_ekran()

            else:
                RZR.fnks.kayit_yok("Otobüs")
                RZR.menuler.oto_bilgi_ekle()

        def sefer_bilgi_ekle():
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik("Sefer Bilgisi Ekleme")
            osa = RZR.bilgiler.oto.getir._oto_sayisi()
            if osa > 0:
                RZR.fnks.sefer_ekle()
                s = {'1': RZR.menuler.sefer_bilgi_ekle,
                     '2': RZR.menuler.firma_ekran}
                RZR.fnks.tekrar_et(
                    RZR.bilgiler.veri_tabanı.sabit.fonks.oto_sfr_ekle.mesaj, s)
            else:
                RZR.fnks.kayit_yok("Otobüs")
                RZR.menuler.oto_bilgi_ekle()

        def sefer_koltuk_bilgi():
            # Üst menü Firma
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik("Sefer/Koltul Menüsü")
            os = RZR.bilgiler.oto.getir._oto_sayisi()
            ss = RZR.bilgiler.sefer.getir._sfr_sayisi()
            if os > 0:
                if ss > 0:
                    RZR.fnks.sefer_koltuk_secim()
                else:
                    RZR.fnks.kayit_yok('Sefer')
                    RZR.menuler.sefer_bilgi_ekle()
            else:
                RZR.fnks.kayit_yok('Otobüs')
                RZR.menuler.oto_bilgi_ekle()

        # ------------Müşteri
        def musteri_ekran():
            sc = {'1': RZR.menuler.sefer_listele_mstr,
                  '2': RZR.fnks.rez_secim, '3': RZR.menuler.rez_goster, '4': RZR.menuler.ana_ekran}
            RZR.fnks.menu_secimleri(
                RZR.bilgiler.veri_tabanı.sabit.menuler.musteri.ad, RZR.bilgiler.veri_tabanı.sabit.menuler.musteri.mesaj, sc)

        def sefer_listele_mstr():
            # üst menü müşteri
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik('Sefer Listesi')
            ss = RZR.bilgiler.sefer.getir._sfr_sayisi()
            if ss > 0:
                RZR.bilgiler.sefer.getir.bilgi.sfr_ozt_msteri_icin()
                RZR.fnks.ust_menuye_git()
                RZR.menuler.musteri_ekran()
            else:
                RZR.fnks.kayit_yok_mstr("Sefer")
                RZR.menuler.musteri_ekran()

        def rez_goster():
            # ust menü müşteri
            RZR.fnks.ekran_temizle()
            RZR.fnks.menu_baslik("Rezervasyon Detay")

            ss = RZR.bilgiler.sefer.getir._sfr_sayisi()
            if ss > 0:
                rz_lst = RZR.bilgiler.musteri.getir._rez_nolar_lst()
                print(rz_lst)
                rz_no = RZR.fnks.rez_no_sor()
                if rz_no in rz_lst:
                    RZR.bilgiler.musteri.getir.bilgi.rez_bilgi(rz_no)
                    a = input("İyi yolculuklar dileriz..")
                    RZR.menuler.musteri_ekran()
                else:
                    a = input(
                        "Eksik ya da hatalı bir giriş yapıldı, lütfen tekrar deneyiniz..")
                    RZR.menuler.musteri_ekran()
            else:
                RZR.fnks.kayit_yok_mstr("Sefer")
                RZR.menuler.musteri_ekran()
