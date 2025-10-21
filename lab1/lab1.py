from math import factorial


class Potencija:
    def __init__(self, koeficjent, potencija):
        self.potencija = potencija
        self.koeficjent = koeficjent

    def __add__(self, other):
        if (self.potencija != other.potencija):
            raise Exception("Nemoguce zbrojiti dvije razlicite potencije")

        return Potencija(self.koeficjent + other.koeficjent, self.potencija)

    def __mul__(self, other):
        return Potencija(self.koeficjent * other.koeficjent, self.potencija + other.potencija)

    def __repr__(self):
        return f"{self.koeficjent}x^{self.potencija}"


class EksponencijalnaIzvodnica:
    def __init__(self, start=None):
        self.koeficjenti = {}
        if start != None:
            for i in range(start + 1):
                self.koeficjenti[i] = Potencija(1 / factorial(i), i)

    def dodaj_potenciju(self, potencija):
        if (potencija.potencija not in self.koeficjenti):
            self.koeficjenti[potencija.potencija] = Potencija(
                0, potencija.potencija)

        self.koeficjenti[potencija.potencija] += potencija

    def dohvati_potenciju(self, potencija):
        if potencija not in self.koeficjenti:
            return 0
        return self.koeficjenti[potencija].koeficjent * factorial(potencija)

    @staticmethod
    def pomnozi_vise(lista):
        res = EksponencijalnaIzvodnica(0)
        for izvodnica in lista:
            res *= izvodnica

        return res

    def __mul__(self, other):
        nova_izvodnica = EksponencijalnaIzvodnica()
        for p1 in self.koeficjenti.values():
            for p2 in other.koeficjenti.values():
                nova_izvodnica.dodaj_potenciju(p1 * p2)

        return nova_izvodnica


def lab1(a, b, c, d, e, L):
    konacna = EksponencijalnaIzvodnica.pomnozi_vise([EksponencijalnaIzvodnica(a), EksponencijalnaIzvodnica(
        b), EksponencijalnaIzvodnica(c), EksponencijalnaIzvodnica(d), EksponencijalnaIzvodnica(e)])

    return konacna.dohvati_potenciju(L)


def main():
    duljine_slvoa = input("")
    a, b, c, d, e = duljine_slvoa.split(" ")
    L = input("")
    rez = lab1(int(a), int(b), int(c), int(d), int(e), int(L))
    print(rez)


if __name__ == "__main__":
    main()
