# Dit is commentaar (commentarieer je programma)
# Labo intro oefening 1

inputnaam = input("Wat is jouw naam? \n" )
leeftijd = int(input("Hoe oud ben je? \n"))
nieuweleeftijd = leeftijd + 15

voornaam = "persoon"
naam = "onbekend"

print("Hello world !")
print("Hello world ," , voornaam , "!")
print("welkom" , voornaam  , naam)

print("welkom {0}. Jouw naam is {1}. je bent {2:.2f} jaar".format(voornaam, naam, leeftijd))

print("Hallo, jouw naam is", inputnaam, "en je bent", leeftijd , "jaar.")

print(type(leeftijd))

print("Binnen 15 jaar ben je" , nieuweleeftijd , "jaar")