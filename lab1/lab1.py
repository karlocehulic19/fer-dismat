from math import factorial


class Potencija:
    def __init__(self, potencija=0, koeficjent=0):
        self.potencija = potencija
        self.koeficjent = 1

    def __add__(self, other):
        if (self.potencija != other.potencija):
            raise Exception("Nemoguce zbrojiti dvije razlicite potencije")

        return Potencija(self.koeficjent + other.koeficjent, self.potencija)

    def __mul__(self, other):
        return Potencija(self.potencija + other.potencija, self.koeficjent * other.koeficjent)

    def __repr__(self):
        return f"{self.koeficjent} x^{self.potencija}"


class EksponencijalnaIzvodnica:
    def __init__(self, start=None):
        self.koeficjenti = {}
        if start:
            for i in range(start + 1):
                self.koeficjenti[i] = Potencija(i, 1 / factorial(i))

    def dodaj_potenciju(self, potencija):
        if (potencija.potencija not in self.koeficjenti):
            self.koeficjenti[potencija.potencija] = Potencija(
                potencija.potencija)

        self.koeficjenti[potencija.potencija] += potencija

    def dohvati_potenciju(self, potencija):
        if potencija not in self.koeficjenti:
            return 0
        return self.koeficjenti[potencija].koeficjenti * factorial(potencija)

    @staticmethod
    def pomnozi_vise(lista):
        res = EksponencijalnaIzvodnica(0)
        for izvodnica in lista:
            res *= izvodnica

        return res

    def __mul__(self, other):
        nova_izvodnica = EksponencijalnaIzvodnica()
        for _, p1 in self.koeficjenti:
            for _, p2 in other.koeficjenti:
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
    rez = lab1(a, b, c, d, e, L)
    print(rez)


def test():
    print("LAB RES: ", lab1(2, 2, 2, 2, 2, 10))
    # assert lab1(2, 2, 2, 2, 2, 10) == 11340
    # assert lab1(2, 2, 2, 2, 2, 1) == 5


if __name__ == "__main__":
    # main()
    test()
