
def kasten(text, zeichen="-", anzahl=17):
    print(zeichen * anzahl)
    print(text)
    print(zeichen * anzahl)


kasten("1 Hallo Schrödinger")
kasten("2 Hallo Schrödinger", "-/")
kasten("3 Hallo Schrödinger", "#", 5)
kasten("4 Hallo Schrödinger", 7)
