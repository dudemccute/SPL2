#zahlenraten

import random
zufallszahl = True
versuche = 0

zufallszahl = random.randint(1,100)

#Benutze soll Zahl von Benutzer erraten

#Ausgabe: wie viele Verusche waren notwendig
while(zufallszahl):
    eingabe = input("Geben sie eine Zahl zwischen 1-100 ein: ")

    if(eingabe == zufallszahl):
        zufallszahl = False
    elif(eingabe > zufallszahl):
        zufallszahl = True
        versuche = versuche +1
        print("Die gesuchte Zahl ist kleiner")
        
    elif(eingabe < zufallszahl):
        zufallszahl = True
        versuche = versuche +1
        print("Die gesuchte Zahl ist größer")
    else:
        print("bitte geben sie zahlen ein")

print("sie haben richtig geraten")
    
