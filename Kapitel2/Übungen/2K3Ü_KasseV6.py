# While erstmal rausgenommen, nach aktuellem Wissensstand
# Lösung nicht perfekt da nicht geprüft wird ob er beim 2. Nachzahlen wirklich alles abgedeckt hat

i = "J"

while i == "J":
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

    Rückgeld = bezahltes_geld - VerkaufspreisRabatt

    if VerkaufspreisRabatt < bezahltes_geld:
        print("Der Kunde bekommt", Rückgeld, "€ zurrück!")
        print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
        i = input("Nochmal? J/N ")

    elif VerkaufspreisRabatt > bezahltes_geld:
        GeldFehlt = VerkaufspreisRabatt - bezahltes_geld
        print("Der Kunde hat", GeldFehlt, "€ zuwenig bezahlt!")
        Nachzahlen = float(input("Bezahlen Sie das resliche Geld! "))

        if GeldFehlt == Nachzahlen:
            print("Danke, Sie haben nun die Differenz ausgegliechen!")
        elif Nachzahlen > GeldFehlt:
            Rückgeld2 = Nachzahlen - GeldFehlt 
            print("Der Kunde bekommt", Rückgeld2, "zurück! ")
        else:
            print("Das reicht nicht!")
            GeldFehlt2 = float(input("Bezahl nun endlich den rest! V2"))

        print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
        i = input("Nochmal? J/N")

    else:
        print("Das stimmt so!")
        print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
        i = input("Nochmal? J/N")
