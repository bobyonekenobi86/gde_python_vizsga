from datetime import datetime, timedelta
import random



class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, meret, minibar, erkely):
        super().__init__(szobaszam, ar)
        self.meret = meret
        self.minibar = minibar
        self.erkely = erkely


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, meret, minibar, erkely):
        super().__init__(szobaszam, ar)
        self.meret = meret
        self.minibar = minibar
        self.erkely = erkely


class Foglalas:
    def __init__(self, szalloda, szoba, datum):
        self.szalloda = szalloda
        self.szoba = szoba
        self.datum = datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        foglalas_obj = Foglalas(self, szoba, datum)
        # Ellenőrzés, hogy a szoba már foglalt-e az adott dátumon
        if any(
                foglalas.datum == datum and foglalas.szoba == szoba
                for foglalas in self.foglalasok
        ):
            print("Hiba: A megadott időpontra már foglalt a szoba.")
        else:
            self.foglalasok.append(foglalas_obj)
            print("Sikeres foglalás.")

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print("Sikeres lemondás.")
        else:
            print("Hiba: A megadott foglalás nem létezik.")

    def foglalasok_listazasa(self):
        print("\nAktív foglalások:")
        for i, foglalas in enumerate(self.foglalasok, 1):
            print(
                f"{i}. Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}, Ár: {foglalas.szoba.ar} Ft")

    def szobak_listazasa(self):
        print("\nElérhető szobák:")
        for szoba in self.szobak:
            if isinstance(szoba, EgyagyasSzoba):
                print(
                    f"Egyágyas szoba {szoba.szobaszam}: Ár: {szoba.ar} Ft, Méret: {szoba.meret}, Minibar: {szoba.minibar}, Erkély: {szoba.erkely}")
            elif isinstance(szoba, KetagyasSzoba):
                print(
                    f"Kétágyas szoba {szoba.szobaszam}: Ár: {szoba.ar} Ft, Méret: {szoba.meret}, Minibar: {szoba.minibar}, Erkély: {szoba.erkely}")

def feltoltes():
    szalloda = Szalloda("Hotel California")

    szalloda.szobak.append(EgyagyasSzoba(szobaszam=101, ar=74900, meret="kicsi", minibar=True, erkely=False))
    szalloda.szobak.append(KetagyasSzoba(szobaszam=201, ar=94900, meret="nagy", minibar=False, erkely=True))
    szalloda.szobak.append(KetagyasSzoba(szobaszam=202, ar=94900, meret="nagy", minibar=True, erkely=True))

    for _ in range(5):
        szoba = random.choice(szalloda.szobak)
        random_date = datetime.now() + timedelta(days=random.randint(1, 30))
        foglalas = Foglalas(szalloda, szoba, random_date)
        szalloda.foglalasok.append(foglalas)

    return szalloda


def main():
    szalloda = feltoltes()
    print("\nÜdvözli a foglalási rendszer!")
    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Foglalás lemondása")
        print("3. Aktív foglalások listázása")
        print("4. Szobák listázása")
        print("5. Kilépés")


        valasztas = input("Választás: ")

        if valasztas == "1":

            print("\nVálasztható szobák:")
            for szoba in szalloda.szobak:
                print(f"Szoba {szoba.szobaszam}, Ár: {szoba.ar} Ft")

            try:
                szobaszam = int(input("Adja meg a foglalni kívánt szoba számát: "))
                datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
            except (ValueError, ValueError):
                print("Hiba: Érvénytelen adatok. Kérem, próbálja újra.")
                continue

            valasztott_szoba = next((szoba for szoba in szalloda.szobak if szoba.szobaszam == szobaszam), None)

            if valasztott_szoba is not None:
                szalloda.foglalas(valasztott_szoba, datum)
            else:
                print("Hiba: Érvénytelen szoba szám. Kérem, próbálja újra.")

        elif valasztas == "2":

            szalloda.foglalasok_listazasa()

            try:
                foglalas_sorszam = int(input("Adja meg a lemondani kívánt foglalás sorszámát: "))
            except ValueError:
                print("Hiba: Érvénytelen adat. Kérem, próbálja újra.")
                continue

            if 1 <= foglalas_sorszam <= len(szalloda.foglalasok):
                szalloda.lemondas(szalloda.foglalasok[foglalas_sorszam - 1])
            else:
                print("Hiba: Érvénytelen sorszám. Kérem, próbálja újra.")

        elif valasztas == "3":
           szalloda.foglalasok_listazasa()

        elif valasztas == "4":
           szalloda.szobak_listazasa()

        elif valasztas == "5":
            break

        else:
            print("Hiba: Érvénytelen választás. Kérem, próbálja újra.")


if __name__ == "__main__":
    main()