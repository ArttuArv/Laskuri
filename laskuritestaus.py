################################################################################
#
#   Ensimmäinen versio tyypillisen Windows-laskinta matkivasta laskimesta.
#   Graafinen käyttöliittymä seuraavaan versioon.
#
################################################################################


class Laskuri:

    # Laskufunktiot
    def addition(self, luku1, luku2 ):
        print(f"= {luku1 + luku2}")
        return luku1 + luku2

    def substraction(self, luku1, luku2 ):
        print(f"= {luku1 - luku2}")
        return luku1 - luku2

    def multiplication( self, luku1, luku2 ):
        print(f'= {luku1 * luku2}')
        return luku1 * luku2

    def division( self, luku1, luku2 ):
        if luku2 == 0:
            print("Nollalla ei voi jakaa!")
        else:
            print(f'= {luku1 / luku2}')
            return luku1 / luku2


# Valintafuntio
def valintakysely():
    print("\n(1) Yhteenlasku\n(2) Vähennyslasku\n(3) Kertolasku\n(4) Jakolasku\n(5) Lopetus\n")
    try:
        valinta = int(input("Tee valinta: "))
        if valinta == 1:
            return "+"
        elif valinta == 2:
            return "-"
        elif valinta == 3:
            return "*"
        elif valinta == 4:
            return "/"
        elif valinta == 5:
            return 5
    except ValueError:
        print("\nAnna numero väliltä 1-5!\n")


# Lukujenkyselyfunktio
def lukukysely():
    while True:
        try:
            luku = float(input("Anna luku: "))
            return luku
        except ValueError:
            continue


# Pääohjelma
def main():
    print("\n*******************************")
    print("*                             *")
    print("*      EEPPINEN LASKURI       *")
    print("*                             *")
    print("*******************************\n")
    tulos = lukukysely()
    laskuStringi = str(tulos)

    laskuri = Laskuri()
    
    while True:

        valinta = valintakysely()

        if valinta == "+":
            laskuStringi += " " + valinta + " "
            print(laskuStringi)
            luku = lukukysely()
            laskuStringi += str(luku)
            print(laskuStringi)
            tulos = laskuri.addition(tulos, luku)
        elif valinta == "-":
            laskuStringi += " " + valinta + " "
            print(laskuStringi)
            luku = lukukysely()
            laskuStringi += str(luku)
            print(laskuStringi)
            tulos = laskuri.substraction(tulos, luku)
        elif valinta == "*":
            laskuStringi += " " + valinta + " "
            print(laskuStringi)
            luku = lukukysely()
            laskuStringi += str(luku)
            print(laskuStringi)
            tulos = laskuri.multiplication(tulos, luku)
        elif valinta == "/":
            laskuStringi += " " + valinta + " "
            print(laskuStringi)
            luku = lukukysely()
            if luku != 0:
                laskuStringi += str(luku)
                print(laskuStringi)
                tulos = laskuri.division(tulos, luku)
            else:
                print("Nollalla ei voi jakaa!\n")
                laskuStringi = laskuStringi.replace("/", "")
                laskuStringi = laskuStringi.rstrip()
                print(laskuStringi)
        elif valinta == 5:
            print(f"\nViimeinen tulos:\n\n{tulos}\n\nOhjelma päättyy..\n")
            break
        else:
            print("\nAnna numero väliltä 1-5!\n")

if __name__ == "__main__":
    main()
 