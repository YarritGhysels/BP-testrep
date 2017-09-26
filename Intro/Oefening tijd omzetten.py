dagen = int(input("Geef het aantal dagen op = "))
uren = int(input("Geef het aantal uren op = "))
minuten = int(input("Geef het aantal minuten op = "))
seconden = int(input("Geef het aantal seconden op = "))

totaalseconden = (dagen*24*3600) +(uren*3600) + (minuten*60) + seconden

print(totaalseconden)