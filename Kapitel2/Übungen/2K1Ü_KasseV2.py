
Verkaufspreis = int(input("Geben Sie den Verkaufspreis ein! "))
rabatt = float(input("Wieviel % Rabatt? "))


Verkaufspreis = float(Verkaufspreis)
rabatt = float(rabatt)

rabattumgerechnet = rabatt / 100
rabattwert = float(Verkaufspreis * rabattumgerechnet)

VerkaufspreisRabatt = float(Verkaufspreis) - float(rabattwert)
print("Der rabattierter Preis beträgt", VerkaufspreisRabatt, "€!")

bezahltes_geld = int(input("Wieviel Geld hat der Kunde gegeben? "))
bezahltes_geld = float(bezahltes_geld)

if VerkaufspreisRabatt < bezahltes_geld:
    Rückgeld = bezahltes_geld - VerkaufspreisRabatt
    print("Der Kunde bekommt", Rückgeld, "€ zurrück!")


elif VerkaufspreisRabatt > bezahltes_geld:
    GeldFehlt = VerkaufspreisRabatt - bezahltes_geld
    print("Der Kunde hat", GeldFehlt, "€ zuwenig bezahlt!")

else:
    print("Das stimmt so!")

print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
