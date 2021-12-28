#WorkInProgress!!
#Rechnung funktioniert noch nicht richtig ca. Line 45 bzw alles mit der Liste
#Liste wird später im Buch behandelt, solange lasse ich es hier broken
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

    if VerkaufspreisRabatt < bezahltes_geld:
        Rückgeld = bezahltes_geld - VerkaufspreisRabatt
        print("Der Kunde bekommt", Rückgeld, "€ zurrück!")
        print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
        i = input("Nochmal? J/N ")

    elif VerkaufspreisRabatt > bezahltes_geld:
        GeldFehlt = VerkaufspreisRabatt - bezahltes_geld
        print("Der Kunde hat", GeldFehlt, "€ zuwenig bezahlt!")
        Nachzahlen = input("Bezahlen Sie das resliche Geld! ")

        if GeldFehlt == Nachzahlen:
            print("Danke, Sie haben nun die Differenz ausgegliechen!")
        while GeldFehlt != Nachzahlen:
            print("Das reicht nicht!")
            GeldFehltListe = []
            float.GeldFehltListe
            GeldFehlt2 = float(input("Bezahl nun endlich den rest! V2"))
            GeldFehltListe.append(GeldFehlt2)
            NachzahlSumme = GeldFehlt - sum(GeldFehltListe)

            if NachzahlSumme == Nachzahlen:
                print("Danke, Sie haben nun die Differenz ausgegliechen!")
            elif NachzahlSumme != Nachzahlen:
                GeldFehlt3 = float(input("Bezahl nun endlich den rest! V3"))
                GeldFehltListe.append(GeldFehlt3)

                if GeldFehlt3 == NachzahlSumme:
                    print("Danke, Sie haben nun die Differenz ausgeglichen!")
                    break
                elif GeldFehlt3 != NachzahlSumme:
                    print("Ach komm leck mich, lass stecken!")
            NachzahlSumme - GeldFehlt3

        print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
        i = input("Nochmal? J/N")

    else:
        print("Das stimmt so!")
        print("Der Kunde hat insgesamt ", rabattwert, "gespart!")
        i = input("Nochmal? J/N")
