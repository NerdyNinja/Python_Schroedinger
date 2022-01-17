
def rückgabe(zahl):
    if zahl <= 0:
        print("Ich bin kleiner als 0")
        return 0
    elif zahl >= 10:
        print("Ich bin größer als 10")
        return 10
    else:
        print("Ich bin was ganz anderes!")
        return zahl


rückgabe(zahl=5)
