import time

i = input("Wenn du 0 tippst, mache ich wohoo")

while i == str(0):
    print("Schleife wohoo")
    time.sleep(2)
else:
    print("Das war keine 0 du Idiot")

print("Zu ende")
