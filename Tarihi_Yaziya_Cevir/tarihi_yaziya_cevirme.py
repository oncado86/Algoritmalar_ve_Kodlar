class TRH():

    def __init__(self) -> None:
        super().__init__()
        self.e_t()
        self.trh = []

    def trh_al(self):
        gecerli = "0123456789./"
        s = []
        k = ""
        while not k:
            k = input("Tarih giriniz: ")
        else:
            for i in k:
                if i in gecerli:
                    if k == "." or k == "/":
                        return self.trh_al()
                    else:
                        if k.endswith("/") or k.endswith(".") or k.startswith("/") or k.startswith("."):
                            k = k.replace("/", "").replace(".",
                                                           "")
                        k = k.replace("/", ".")
                        s.clear()
                        s = k.split(".")

                else:
                    print("Hatalı giriş yapıldı.. Lütfen tarih verisi giriniz.")
                    return self.trh_al()
            self.trh_kntrl(s)

    def trh_kntrl(self, t):
        self.trh.clear()
        sa = len(t)
        if sa == 3:
            gn = int(t[0])
            ay = int(t[1])
            yl = int(t[2])
            if (0 < gn and gn <= 31):
                if (0 < ay and ay <= 12):
                    if 0 < yl <= 999999:
                        gn = str(gn)
                        ay = str(ay)
                        yl = str(yl)
                        self.trh.append(gn)
                        self.trh.append(ay)
                        self.trh.append(yl)
                    else:
                        print("Yıl hatası")
                        return self.trh_al()
                else:
                    print("Ay hatası")
                    return self.trh_al()
            else:
                print("Gün Hatası")
                return self.trh_al()
            self.trh_cvr(self.trh)
        else:
            print("Eksik giriş.. Lütfen tarih bilgisi giriniz.(XX.XX.XXXX)")
            self.trh_al()

    def trh_cvr(self, trh):

        def bin(x):
            binler = ['Bin', 'İki Bin', 'Üç Bin', 'Dört Bin',
                      'Beş Bin', 'Altı Bin', 'Yedi Bin', 'Sekiz Bin', 'Dokuz Bin']
            indx = int(x)-1
            _bin = binler[indx]

            # alternatif
            # _bin = x.replace("1", "bin").replace(
            #     "2", "iki bin").replace("3", "üç bin").replace("4", "dört bin").replace("5", "beş bin").replace("6", "altı bin").replace("7", "yedi bin").replace("8", "sekiz bin").replace("9", "dokuz bin").replace("0", "")
            return _bin.title()

        def yuz(x):
            yuzler = ['Yüz', 'İki Yüz', 'Üç Yüz', 'Dört Yüz',
                      'Beş Yüz', 'Altı Yüz', 'Yedi Yüz', 'Sekiz Yüz', 'Dokuz Yüz']
            indx = int(x)-1
            _yuz = yuzler[indx]

            # alternatif
            # _yuz = x.replace("1", "yüz").replace(
            #     "2", "iki yüz").replace("3", "üç yüz").replace("4", "dört yüz").replace("5", "beş yüz").replace("6", "altı yüz").replace("7", "yedi yüz").replace("8", "sekiz yüz").replace("9", "dokuz yüz").replace("0", "")
            return _yuz.title()

        def on(x):
            _on = x.replace("1", "on").replace(
                "2", "yirmi").replace("3", "otuz").replace("4", "kırk").replace("5", "elli").replace("6", "atmış").replace("7", "yetmiş").replace("8", "seksen").replace("9", "doksan").replace("0", "")
            return _on.title()

        def bir(x):
            _bir = x.replace("1", "bir").replace(
                "2", "iki").replace("3", "üç").replace("4", "dört").replace("5", "beş").replace("6", "altı").replace("7", "yedi").replace("8", "sekiz").replace("9", "dokuz").replace("01", "bir").replace(
                "02", "iki").replace("03", "üç").replace("04", "dört").replace("05", "beş").replace("06", "altı").replace("07", "yedi").replace("08", "sekiz").replace("09", "dokuz").replace("0", "")

            return _bir.title()

        def _ay(x):
            ay = ""
            aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
                     'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
            indx = int(x)-1
            ay = aylar[indx]
            return ay

        def _gun(x):
            islm = [bir, on]
            x_ters = []
            for i in range(len(x)):
                x_ters.append(x[i])
            x_ters.reverse()
            bs = len(x)
            s = []
            for i in range(bs):
                if x_ters[i] != '0':
                    s.append(islm[i](x_ters[i]))
            s.reverse()
            gn = ""
            for i in range(len(s)):
                gn = gn+" "+s[i]

            return gn

        def _yil(x):
            islm = [bir, on, yuz, bin]
            x_ters = []
            for i in range(len(x)):
                x_ters.append(x[i])
            x_ters.reverse()
            bs = len(x)
            s = []
            for i in range(bs):
                if x_ters[i] != '0':
                    s.append(islm[i](x_ters[i]))
            s.reverse()
            yl = ""
            for i in range(len(s)):
                yl = yl+" "+s[i]

            return yl

        def cvr(trh):
            gun = trh[0]
            gun = _gun(gun)
            ay = trh[1]
            ay = _ay(ay)
            y = trh[2]
            y = _yil(y)
            print(f"{gun} {ay} {y}")

        cvr(trh)
        self.tekrar()

    def tekrar(self):
        s = ""

        while not s:
            s = input("\n1.Tekrar\n2.Çıkış\n-->")
        else:
            if s == "1" or s == "2":
                if s == "1":
                    self.e_t()
                    self.trh_al()
                else:
                    quit()
            else:
                print("Hatalı seçim")
                return self.tekrar()

    def e_t(self):
        import os
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
        print("".center(109, "~"))
        print("OnCaDo".center(109))
        print("".center(109, "~"))
        print("\n")


t = TRH()
t.trh_al()
