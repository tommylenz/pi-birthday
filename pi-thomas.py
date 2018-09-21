# Das Pi-Problem
# Python 2.7.10 auf iMac

from math import pi
from string import *

worked = False

# Checkt ob das Geburtsdatum das richtige Format hat und korrigiert das Format ggf.
def CheckIfCorrectFormat(str):
    try: int(str)
    except ValueError: return 0
    else: return 1

# Sucht nach der Pi-Stelle des Geburtsdatums
def PiDecimalPlace(birthday):
    index = str(pi).find(birthday) - 1
    nicebirthday= birthday[0] + birthday[1] + "." + birthday[2] + birthday[3] + "." + birthday[4] + birthday[5] + birthday[6] + birthday[7]
    print "Der Geburtstag (" + nicebirthday + ") befindet sich an der " + str(index) + ". Nachkommastelle von Pi."

# Startet die beiden Funktionen
def main():
    global worked # Sorgt dafuer, dass worked nicht nur in main() veraendert wird sondern global
    birthday = raw_input("Wann hast du Geburtstag? (Format: TagMonatJahr): ")
    if CheckIfCorrectFormat(birthday) == True:
        birthday = birthday
        PiDecimalPlace(birthday)
        print ""
        worked = True
    elif CheckIfCorrectFormat(birthday.replace(".", "", 2)) == True:
        print "Geburtsdatum wird umgeformt..." # Nur zu Entwicklungszwecken
        birthday = birthday.replace(".", "", 2)
        PiDecimalPlace(birthday)
        worked = True
    else:
        print "Das war kein richtiges Geburtsdatum. Versuch's doch nochmal!"
        print ""
        worked = False

# - - - Eigentlicher Programmablauf - - -

while worked == False:
    main()

print ""
raw_input("ENTER ZUM BEENDEN.")
