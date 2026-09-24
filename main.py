# program główny: czujnik -> kolor -> dioda
# KROK 5: TWOJE ZADANIE - zamień każde ___ na właściwy kod

from time import sleep

# "import" z NASZYCH plików - Python szuka pliku sensors.py / display.py w tym samym folderze.
from sensors import odleglosc_cm                  # funkcja: zwraca odległość w cm
from display import kolor_dla_odleglosci, dioda   # funkcja: cm -> kolor, oraz obiekt diody

while True:
    # 1) Odczytaj odległość z czujnika (wywołaj funkcję z sensors.py).
    cm = ___

    # 2) Zamień odległość na kolor (wywołaj funkcję z display.py, daj jej cm).
    kolor = ___

    # 3) Ustaw ten kolor na diodzie.
    ___

    # 4) Wypisz odległość i kolor, żeby widzieć, co się dzieje.
    print(f"{cm:.1f} cm -> {kolor}")

    # 5) Poczekaj chwilkę - 0.1 s, czyli 10 odczytów na sekundę.
    sleep(0.1)
