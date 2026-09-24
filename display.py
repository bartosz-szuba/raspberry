# obsługa diody RGB (u nas "wyświetlaczem" jest właśnie dioda)
# KROK 5: zamieniamy plik w "moduł" - funkcja i dioda do użycia w main.py

from gpiozero import RGBLED
from time import sleep

# colorsys - wbudowana biblioteka Pythona do przeliczania kolorów.
# Potrzebujemy z niej zamiany "pozycji na kole kolorów" na (R, G, B).
import colorsys

# STAŁE - wartości, których program nie zmienia w trakcie działania.
# Zwyczaj w Pythonie: stałe piszemy WIELKIMI literami, żeby było je widać.
BLISKO_CM = 10    # tak blisko (lub bliżej) -> całkiem czerwony
DALEKO_CM = 90    # tak daleko (lub dalej)  -> całkiem niebieski

# Obiekt diody - piny GPIO dla kolorów czerwonego, zielonego i niebieskiego.
dioda = RGBLED(red=17, green=27, blue=25)


# "def" tworzy FUNKCJĘ - kawałek kodu z nazwą, który można wywoływać wiele razy.
# W nawiasie jest PARAMETR "cm" - liczba, którą dajemy funkcji na wejściu.
def kolor_dla_odleglosci(cm):
    # 1) Zamieniamy odległość na liczbę "t" od 0 do 1:
    #    przy BLISKO_CM wychodzi 0, przy DALEKO_CM wychodzi 1, w połowie 0.5.
    t = (cm - BLISKO_CM) / (DALEKO_CM - BLISKO_CM)

    # 2) Pilnujemy, żeby t nie wyszło poza zakres 0..1.
    if t < 0:
        t = 0
    if t > 1:
        t = 1

    # 3) Wybieramy miejsce na KOLE KOLORÓW (jak tęcza zwinięta w koło):
    #      0°   = czerwony
    #      60°  = żółty
    #      120° = zielony
    #      240° = niebieski
    #    t=0 (blisko) -> 0° (czerwony), t=1 (daleko) -> 240° (niebieski).
    #    Nie idziemy do 360°, bo za niebieskim koło wraca przez fiolet do czerwonego.
    stopnie = t * 240

    # colorsys chce pozycję na kole jako ułamek całego koła (0..1), a nie w stopniach,
    # więc dzielimy przez 360 (pełne koło).
    odcien = stopnie / 360

    # 4) hsv_to_rgb zamienia (odcień, nasycenie, jasność) na trzy liczby R, G, B.
    #    Nasycenie 1 = kolor "czysty", jasność 1 = pełna.
    #    Funkcja zwraca 3 liczby naraz - rozpakowujemy je od razu do 3 zmiennych.
    czerwony, zielony, niebieski = colorsys.hsv_to_rgb(odcien, 1, 1)

    # "return" oddaje wynik funkcji - krotkę (czerwony, zielony, niebieski).
    return (czerwony, zielony, niebieski)


# Test - wykona się TYLKO przy "python3 display.py", a nie przy imporcie z main.py.
if __name__ == "__main__":
    # Pętla "for" bierze po kolei każdą liczbę z listy [ ... ] i wkłada ją do zmiennej cm.
    for cm in [0, 10, 30, 50, 70, 90, 120]:
        kolor = kolor_dla_odleglosci(cm)     # wywołujemy naszą funkcję
        print(f"{cm} cm -> kolor {kolor}")   # wypisujemy, co wyszło
        dioda.color = kolor                  # i pokazujemy to na diodzie
        sleep(2)

    print("koniec")
    dioda.off()
