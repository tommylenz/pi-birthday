# Das Pi-Problem
# Python 3.6.5 auf Windows

from math import pi
from string import *
from mpmath import mp
import time
import random

mp.dps = 100000  # Stellt länge von Pi ein
worked = False

# Checkt ob das Geburtsdatum das richtige Format hat und korrigiert das Format ggf.
def CheckIfCorrectFormat(str):
    try:
        int(str)
    except ValueError: return 0
    return 1

# Sucht nach der Pi-Stelle des Geburtsdatums
def PiDecimalPlace(birthday):
    nicebirthday = birthday[0] + birthday[1] + "." + birthday[2] + birthday[3] + "." + birthday[4] + birthday[5] + birthday[6] + birthday[7]
    then = time.time()
    try:
        position = str(mp.pi).index(birthday)
        now = time.time()
        print("Es hat funktioniert!")
        print("Es hat ", now-then, " Sekunden gedauert.")
        print("Der Geburtstag " + nicebirthday + " befindet sich an der " + str(position) + ". Nachkommastelle von Pi.")
    except ValueError:
        now = time.time()
        print("Leider befindet sich dein Geburtstag nicht dabei.")
        print("Es hat ", now-then, " Sekunden gedauert.")

# Startet die beiden Funktionen
def main():
    global worked # Sorgt dafuer, dass worked nicht nur in main() veraendert wird sondern global
    birthday = input("Wann hast du Geburtstag? (Format: TagMonatJahr): ")
    if CheckIfCorrectFormat(birthday) == True:
        birthday = birthday # Eigentlich useless aber fuer's Aussehen ganz nett
        PiDecimalPlace(birthday)
        print()
        worked = True
    elif CheckIfCorrectFormat(birthday.replace(".", "", 2)) == True:
        print("Geburtsdatum wird umgeformt...") # Nur zu Entwicklungszwecken
        birthday = birthday.replace(".", "", 2)
        PiDecimalPlace(birthday)
        worked = True
    else:
        print("Das war kein richtiges Geburtsdatum. Versuch's doch nochmal!")
        print()
        worked = False

# - - - Eigentlicher Programmablauf - - -

while worked == False:
    print(pi)
    main()

print()
input("ENTER ZUM BEENDEN.")
