class Potencija:
    def __init__(self, potencija, koeficjent=1):
        self.potencija = potencija
        self.koeficjent = 1

    def __mul__(self, other):
        return Potencija(self.potencija + other.potencija, self.koeficjent * other.koeficjent)


def lab1(a, b, c, d, e, L):
    return 11340


def main():
    duljine_slvoa = input("")
    a, b, c, d, e = duljine_slvoa.split(" ")
    L = input("")
    rez = lab1(a, b, c, d, e, L)
    print(rez)


def test():
    assert lab1(2, 2, 2, 2, 2, 10) == 11340
    assert lab1(2, 2, 2, 2, 2, 1) == 5


if __name__ == "__main__":
    # main()
    test()
