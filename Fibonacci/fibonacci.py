class FB():
    def __init__(self) -> None:
        self.f_l = [1, 1]
        self.tanim = """
Fibonacci serisinin ilk iki elemanı 1'dir ve diğer elemanları,
kendisinden önce gelen son iki elemanın toplamıdır.
Klavyeden bir sayı okuyarak, girilen sayı kadar Fibonacci Serisinin elemanını ekrana bastıran kodu yazınız.
"""

    def ekran_temizle(self):
        import os
        if os.name == "nt":
            _ = os.system("cls")
        else:
            _ = os.system("clear")
        print("".center(120, "~"))
        print("OnCaDo".center(120))
        print("".center(120, "~"))

    def s_al(self):
        s = None
        rkm = "0123456789"
        while not s:
            s = input("Seri adedi: ")
        else:
            for i in s:
                if i in rkm:
                    s = int(s)
                    if s != 0:
                        return s
                    else:
                        print("0 değeri tanımsız")
                        return self.s_al()
                else:
                    print("Lütfen sayı giriniz..")
                    return self.s_al()

    # alternatif
    def s_al2(self):
        s = None
        while not s:
            s = input("Seri adedi: ")
        else:
            try:
                s = int(s)
                if s != 0:
                return s
            else:
                print("0 değeri tanımsız.")
                return s_al2()
            except Exception as er:
                print("Hatalı giriş. Lütfen sayı giriniz.")
                return s_al2()

    def tekrar(self):
        s = ""

        while not s:
            s = input("\n1.Tekrar\n2.Çıkış\n-->")
        else:
            if s == "1" or s == "2":
                self.f_l = [1, 1]
                if s == "1":
                    self.ekran_temizle()
                    self.fib(self.s_al())
                else:
                    quit()
            else:
                print("Hatalı seçim")
                return self.tekrar()

    def fib(self, x):
        a, b, s, c = self.f_l[0], self.f_l[1], 1, 0
        self.x = int(x)

        def seri(k):
            s = 1
            for i in k:
                print(f"{s})\t{i}")
                s += 1
        if self.x == 1:
            print(f"1)\t1")
            self.tekrar()

        elif self.x == 2:
            seri(self.f_l)
            self.tekrar()
        else:
            self.x -= 2
            while s <= self.x:
                c = a+b
                a, b = b, c
                self.f_l.append(c)
                s += 1
            seri(self.f_l)
            self.tekrar()


f = FB()
f.ekran_temizle()
print(f.tanim)
f = f.fib(f.s_al())
