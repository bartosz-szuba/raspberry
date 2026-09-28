# Odczyt odległości z czujnika ultradźwiękowego HC-SR04

from gpiozero import DistanceSensor
from time import sleep

# trigger - każemy czujnikowi piszczeć, echo - wraca echo (przez dzielnik napięcia)
# max_distance domyślnie 1 m -> odczyty 0..100 cm
czujnik = DistanceSensor(echo=24, trigger=23)


def odleglosc_cm():
    # czujnik.distance jest w metrach -> zamiana na cm
    return czujnik.distance * 100


# Test czujnika - tylko przy "python3 sensors.py", pomijany przy imporcie
if __name__ == "__main__":
    while True:
        print(f"{odleglosc_cm():.1f} cm")
        sleep(0.5)
