import sys

import matplotlib.pyplot as plt
import numpy as np

from RozmytyZbior import RozmytyZbior

USAGE = (
    "Niepoprawne uzycie. Zla liczba argumentow. Przyklady uzycia:\n"
    "python app.py 2 3 4\n"
    "python app.py 2 3 4 * 2\n"
    "python app.py 2 3 4 + 5 6 7\n"
)


def normalize_triangle(lp: float, sr: float, pp: float) -> tuple[float, float, float]:
    if not (lp <= sr <= pp):
        raise ValueError
    if lp == sr:
        lp -= 0.01
    if pp == sr:
        pp += 0.01
    return lp, sr, pp


def fuzzy(lp: float, sr: float, pp: float) -> RozmytyZbior:
    return RozmytyZbior(lp, sr, pp, np.arange(lp - 0.2, pp + 0.2, 0.01))


args = sys.argv[1:]

if len(args) == 3:
    try:
        lp, sr, pp = normalize_triangle(float(args[0]), float(args[1]), float(args[2]))
        a = fuzzy(lp, sr, pp)

        plt.figure(figsize=(12, 4))
        a.wyswietl(111)
        print("A:{:<7} {:<7} {:<7}".format(round(a.x1, 2), round(a.m, 2), round(a.x2, 2)))
        plt.title("A")
        plt.xlabel("Wartosc")
        plt.ylabel("Stopien przynaleznosci")
        plt.tight_layout()
        plt.show()
    except ValueError:
        print("Niepoprawne argumenty.")

elif len(args) == 5:
    operator = args[3]
    if operator in ("*", "^"):
        try:
            lp, sr, pp = normalize_triangle(float(args[0]), float(args[1]), float(args[2]))
            liczba = float(args[4])
            a = fuzzy(lp, sr, pp)

            if operator == "*":
                b = getattr(a, "pomn\u00f3\u017c")(liczba)
            else:
                b = getattr(a, "pot\u0119gowanie")(liczba)

            plt.figure(figsize=(12, 4))
            a.wyswietl(311)
            plt.title("A")

            b.wyswietl(312)
            plt.title(f"A{operator}{liczba}")

            a.wyswietl(313)
            b.wyswietl(313)
            plt.title(f"A i A{operator}{liczba}")

            print(
                "A:{:<7} {:<7} {:<7} B:{:<7} {:<7} {:<7}".format(
                    round(a.x1, 2),
                    round(a.m, 2),
                    round(a.x2, 2),
                    round(b.x1, 2),
                    round(b.m, 2),
                    round(b.x2, 2),
                )
            )

            plt.xlabel("Wartosc")
            plt.ylabel("Stopien przynaleznosci")
            plt.tight_layout()
            plt.show()
        except ValueError:
            print("Niepoprawne argumenty.")
    else:
        print("Niepoprawne uzycie. Uzyj: python app.py 2 3 4 * 2 lub python app.py 2 3 4 ^ 2")

elif len(args) >= 7 and (len(args) - 7) % 4 == 0:
    c = None

    for i in range(0, len(args) - 3, 4):
        operator = args[i + 3]
        if operator in ("+", "-", "*"):
            try:
                lp, sr, pp = normalize_triangle(float(args[0]), float(args[1]), float(args[2]))
                lp2, sr2, pp2 = normalize_triangle(
                    float(args[i + 4]), float(args[i + 5]), float(args[i + 6])
                )

                if i >= 4:
                    a = c
                else:
                    a = fuzzy(lp, sr, pp)

                b = fuzzy(lp2, sr2, pp2)

                if operator == "+":
                    c = a.dodaj(b)
                elif operator == "*":
                    c = a.pomnoz_przez_zbior(b)
                else:
                    c = a.odejmij(b)

                plt.figure(figsize=(12, 4))

                a.wyswietl(311)
                b.wyswietl(311)
                plt.title("A i B")

                c.wyswietl(312)
                plt.title(f"A {operator} B")

                a.wyswietl(313)
                b.wyswietl(313)
                c.wyswietl(313)
                plt.title(f"A, B i A {operator} B")

                print(
                    "A:{:<7} {:<7} {:<7} B:{:<7} {:<7} {:<7} C:{:<7} {:<7} {:<7}".format(
                        round(a.x1, 2),
                        round(a.m, 2),
                        round(a.x2, 2),
                        round(b.x1, 2),
                        round(b.m, 2),
                        round(b.x2, 2),
                        round(c.x1, 2),
                        round(c.m, 2),
                        round(c.x2, 2),
                    )
                )

                plt.xlabel("Wartosc")
                plt.ylabel("Stopien przynaleznosci")
                plt.tight_layout()
                plt.show()
            except ValueError:
                print("Niepoprawne argumenty.")
        else:
            print("Niepoprawne uzycie. Uzyj: python app.py 2 3 4 + 5 6 7 lub python app.py 2 3 4 - 5 6 7")
else:
    print(USAGE)
