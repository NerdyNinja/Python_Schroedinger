# Verkaufspreis = float(input("Geben Sie den Verkaufspreis ein"))
# bezahltes_geld = float(input("Wieviel Geld hat der Kunde gegeben?"))
Verkaufspreis = input("Geben Sie den Verkaufspreis ein")
bezahltes_geld = input("Wieviel Geld hat der Kunde gegeben?")

Verkaufspreis = float(Verkaufspreis)
bezahltes_geld = float(bezahltes_geld)

if Verkaufspreis < bezahltes_geld:
    Rückgeld = bezahltes_geld - Verkaufspreis
    print("Der Kunde bekommt", Rückgeld, "€ zurrück!")

elif Verkaufspreis > bezahltes_geld:
    GeldFehlt = Verkaufspreis - bezahltes_geld
    print("Der Kunde hat", GeldFehlt, "€ zuwenig bezahlt!")

else:
    print("Das stimmt so!")
