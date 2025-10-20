def anafonk(*args):
    def icfonk():
        toplam = 0
        for şayi in args:
            toplam += şayi
        print(toplam)
    icfonk()