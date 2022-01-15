def kasten(text, zeichen="*", wieviele=10):
    '''Ein Kasten mit text wird ausgegeben'''
    print(zeichen*wieviele)
    print(text)
    print(zeichen*wieviele)


kasten(text="1. Hallo")
kasten(text="2. Hallo", wieviele=7)
kasten(zeichen="-", wieviele=3, text="3. Hallo")
