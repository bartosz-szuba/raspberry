# Program główny: czujnik -> wygładzanie -> kolor -> dioda

from time import sleep

# nasze własne pliki z tego samego folderu
from sensors import odleglosc_cm
from display import kolor_dla_odleglosci, dioda

# jaką część drogi do nowego odczytu robimy w każdym obrocie
# 1 = bez wygładzania (drga), 0 = stoi w miejscu
WYGLADZANIE = 0.33

# wartość startowa - musi istnieć przed pętlą
gladkie_cm = odleglosc_cm()

while True:
    cm = odleglosc_cm()

    # przesuwamy gladkie_cm o kawałek w stronę nowego odczytu
    gladkie_cm = gladkie_cm + WYGLADZANIE * (cm - gladkie_cm)

    # kolor z wygładzonej odległości, żeby dioda nie drgała
    kolor = kolor_dla_odleglosci(gladkie_cm)
    dioda.color = kolor

    print(f"surowa: {cm:5.1f} cm   gładka: {gladkie_cm:5.1f} cm")

    # 50 odczytów na sekundę
    sleep(0.02)
