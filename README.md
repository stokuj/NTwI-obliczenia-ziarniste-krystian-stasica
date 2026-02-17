# Obliczenia na Liczbach Rozmytych (Fuzzy Numbers)

Projekt "odleglosc rozmyta granul" z przedmiotu Nowe Technologie w Informatyce.

## Opis projektu

Program implementuje operacje na liczbach rozmytych (fuzzy numbers), reprezentowanych jako trojkatne funkcje przynaleznosci.

W projekcie liczba rozmyta jest reprezentowana przez trzy parametry:
- **x1** (lewy punkt) - dolna granica nosnika funkcji przynaleznosci
- **m** (srodek) - wartosc z maksymalna przynaleznoscia (rowna 1)
- **x2** (prawy punkt) - gorna granica nosnika funkcji przynaleznosci

Program umozliwia wykonywanie operacji:
- wyswietlanie pojedynczej liczby rozmytej,
- mnozenie liczby rozmytej przez liczbe rzeczywista,
- potegowanie liczby rozmytej,
- dodawanie dwoch liczb rozmytych,
- odejmowanie dwoch liczb rozmytych,
- mnozenie dwoch liczb rozmytych.

## Wymagania

- Python 3.10+
- uv

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/username/NTwI-obliczenia-ziarniste-krystian-stasica.git
cd NTwI-obliczenia-ziarniste-krystian-stasica
```

2. Zainstaluj zaleznosci:
```bash
uv sync
```

## Uzycie

### Wyswietlanie pojedynczej liczby rozmytej

```bash
uv run python app.py x1 m x2
```

Przyklad:
```bash
uv run python app.py 2 3 4
```

### Mnozenie przez liczbe rzeczywista lub potegowanie

```bash
uv run python app.py x1 m x2 operator liczba
```

Przyklady:
```bash
uv run python app.py 2 3 4 * 2
uv run python app.py 2 3 4 ^ 2
```

### Operacje na dwoch liczbach rozmytych

```bash
uv run python app.py x1_A m_A x2_A operator x1_B m_B x2_B
```

Przyklady:
```bash
uv run python app.py 2 3 4 + 5 6 7
uv run python app.py 2 3 4 - 1 2 3
uv run python app.py 2 3 4 * 1 2 3
```

### Lancuch operacji na wielu liczbach rozmytych

```bash
uv run python app.py x1_A m_A x2_A operator1 x1_B m_B x2_B operator2 x1_C m_C x2_C ...
```

Przyklad:
```bash
uv run python app.py 2 3 4 + 5 6 7 - 1 2 3
```

## Teoria zbiorow rozmytych

Zbior rozmyty to zbior, w ktorym kazdy element nalezy do zbioru z pewnym stopniem przynaleznosci z przedzialu [0, 1].
W projekcie uzyta jest trojkatna funkcja przynaleznosci okreslona przez parametry `x1`, `m`, `x2`.

## Autor

Krystian Stasica

## Licencja

Projekt jest udostepniony na licencji MIT. Zobacz plik `LICENSE`.
