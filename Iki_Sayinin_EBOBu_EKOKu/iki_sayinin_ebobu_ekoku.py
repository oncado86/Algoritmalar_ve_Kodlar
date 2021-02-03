class EBEK():
    def __init__(self) -> None:
        pass

    def a_ek(self):
        print("".center(120, "~"))
        print("OnCaDo".center(120))
        print("".center(120, "~"))

    def s_al(self):
        rkm = "0123456789"
        s = None
        while not s:
            s = input("Sayı giriniz: ")
        else:
            for i in s:
                if not i in rkm:
                    print("Hatalı giriş..")
                    return self.s_al()
            else:
                s = int(s)
                return s

    def ebob(self, a, b):
        buyuk, kucuk, kalan = None, None, None

        if a < b:
            return self.ebob(b, a)
        else:
            buyuk = a
            kucuk = b
            if kucuk == 0:
                return buyuk
            else:
                kalan = buyuk % kucuk
                while kalan != 0:
                    buyuk = kucuk
                    kucuk = kalan
                    kalan = buyuk % kucuk
                    if kalan == 0:
                        break
                return kucuk

    def ekok(self, a, b):
        if b > a:
            return self.ekok(b, a)
        else:
            ekk = (a*b)//self.ebob(a, b)
            return ekk

    def islem_sec(self):
        secenek = "123"
        scm = None
        while not scm:
            scm = input("""
            Lütfen işlem seçiniz:
            1)İki sayının EBOB'unu hesaplama
            2)İki sayının EKOK'unu hesaplama
            3)ÇIKIŞ
    """)
        else:
            for i in scm:
                if not i in secenek:
                    print(f"Hatalı giriş..({scm})")
                    return self.islem_sec()

            scm = int(scm)
            return scm

    def islemler(self, s):
        if s == 1:
            a = self.s_al()
            b = self.s_al()
            ebb = self.ebob(a, b)
            # alternatif
            # eb2 = self.eb2(a, b)
            # eb3 = self.eb3(a, b)

            print(f"\n{a} ve {b} sayılarının\nEBOB'u: {ebb}")
        elif s == 2:
            a = self.s_al()
            b = self.s_al()
            ebb = self.ebob(a, b)
            ekk = self.ekok(a, b)
            # alternatif
            # ek2 = self.ek2(a, b)
            print(f"\n{a} ve {b} sayılarının\nEKOK'u: {ekk}")
        else:
            scm = 3
            return scm

    # alternatif ebob
    def eb2(self, a, b):
        a_bol, b_bol = [], []

        for i in range(1, a+1, 1):
            if a % i == 0:
                a_bol.append(i)
        a_bol = set(a_bol)
        for j in range(1, b+1, 1):
            if b % j == 0:
                b_bol.append(j)
        b_bol = set(b_bol)

        eb = list(a_bol & b_bol)
        eb.sort()
        eb.reverse()
        return eb[0]

    # alternatif ebob
    def eb3(self, a, b):
        x = []
        c = 1
        for i in range(2, a):
            if (a % i == 0) and (b % i == 0):
                x.append(i)
                x.reverse()
                c *= x[0]
        return c

    # alternatif ekok
    def ek2(self, a, b):
        asal_bolen = []
        asallar = []
        indx = 0
        c = 1
        if b > a:
            return self.ek2(b, a)
        else:
            for i in range(2, a):
                asl = True
                for j in range(2, i):
                    if i % j == 0:
                        asl = False
                        break
                if asl:
                    asallar.append(i)

            while asallar[indx] <= a:
                if (a % asallar[indx] == 0) or (b % asallar[indx] == 0):
                    asal_bolen.append(asallar[indx])
                    asal_bolen.reverse()
                    c *= asal_bolen[0]
                    if a % asallar[indx] == 0:
                        a = a//asallar[indx]
                    if b % asallar[indx] == 0:
                        b = b//asallar[indx]
                else:
                    if indx < len(asallar):
                        indx += 1
            return c

    def pro(self):
        self.a_ek()
        scm = self.islem_sec()
        while scm != 3:
            
            self.islemler(scm)
            scm = self.islem_sec()


pr = EBEK()

pr.pro()
