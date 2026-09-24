# odczyt odległości z czujnika ultradźwiękowego HC-SR04
# KROK 5: zamieniamy plik w "moduł" - z funkcją, którą inne pliki mogą użyć

# Z biblioteki gpiozero (obsługa pinów malinki) bierzemy gotowe "narzędzie"
# do czujnika odległości - dzięki niemu nie musimy sami mierzyć czasu echa.
from gpiozero import DistanceSensor

# sleep(x) - każe programowi poczekać x sekund.
from time import sleep

# Tworzymy obiekt czujnika i zapisujemy go w zmiennej "czujnik".
# Podajemy numery pinów GPIO, do których jest podłączony:
#   trigger - pin, którym każemy czujnikowi wysłać "pisk"
#   echo    - pin, na którym czujnik mówi nam, że wróciło echo (przez dzielnik napięcia)
# max_distance domyślnie = 1 m, więc odczyty są od 0 do 100 cm.
czujnik = DistanceSensor(echo=24, trigger=23)


# Funkcja, która zwraca aktualną odległość w centymetrach.
# To ją będzie wołał main.py.
def odleglosc_cm():
    # czujnik.distance daje odległość w METRACH (0..1), mnożymy przez 100 -> cm.
    return czujnik.distance * 100


# Ten blok wykona się TYLKO wtedy, gdy uruchomisz ten plik bezpośrednio:
#     python3 sensors.py
# Kiedy inny plik zrobi "from sensors import ...", ten blok zostanie POMINIĘTY.
# Dzięki temu możemy tu trzymać test czujnika i nie przeszkadza on w main.py.
if __name__ == "__main__":
    # Pętla nieskończona - aż zatrzymasz program klawiszami Ctrl+C.
    while True:
        # Wypisujemy odległość z 1 cyfrą po przecinku (":.1f").
        print(f"{odleglosc_cm():.1f} cm")
        # Czekamy pół sekundy (2 odczyty na sekundę).
        sleep(0.5)
