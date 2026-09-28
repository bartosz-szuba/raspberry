# Obsługa diody RGB: odległość -> kolor (blisko czerwony, daleko niebieski)

from gpiozero import RGBLED
from time import sleep
import colorsys

BLISKO_CM = 10    # tak blisko lub bliżej -> całkiem czerwony
DALEKO_CM = 90    # tak daleko lub dalej  -> całkiem niebieski

dioda = RGBLED(red=17, green=27, blue=25)


def kolor_dla_odleglosci(cm):
    # t = "procent drogi" od BLISKO_CM (0) do DALEKO_CM (1)
    t = (cm - BLISKO_CM) / (DALEKO_CM - BLISKO_CM)

    # przycinamy t do zakresu 0..1
    if t < 0:
        t = 0
    if t > 1:
        t = 1

    # koło kolorów: 0° czerwony, 60° żółty, 120° zielony, 240° niebieski
    stopnie = t * 240

    # colorsys chce ułamek koła (0..1), a nie stopnie
    odcien = stopnie / 360

    # (odcień, nasycenie, jasność) -> (R, G, B), każda wartość 0..1
    czerwony, zielony, niebieski = colorsys.hsv_to_rgb(odcien, 1, 1)

    return (czerwony, zielony, niebieski)


# Test diody - tylko przy "python3 display.py", pomijany przy imporcie
if __name__ == "__main__":
    for cm in [0, 10, 30, 50, 70, 90, 120]:
        kolor = kolor_dla_odleglosci(cm)
        print(f"{cm} cm -> kolor {kolor}")
        dioda.color = kolor
        sleep(2)

    print("koniec")
    dioda.off()
