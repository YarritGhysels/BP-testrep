aantalseconden = int(input("Geef het aantal seconden op = "))

minuten, seconden = divmod(aantalseconden, 60)
uren, minuten = divmod(minuten, 60)
dagen, uren = divmod(uren, 24)

print("d:h:m:s = " , dagen,":",uren,":",minuten,":",seconden)