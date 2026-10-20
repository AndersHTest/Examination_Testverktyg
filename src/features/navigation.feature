#noinspection CucumberUndefinedStep
# language: sv


# User Story x
Egenskap: Navigering
  Scenariomall: Testa navigering
    # Som en användare på Läslistan
    # vill jag kunna navigera på hemsidan utan problem
    # så att jag enkelt kan se alla vyer
    Givet att du är på Läslistans startsida
    När jag klickar på <vy>
    Så ser jag <elementen>


    Exempel:
    |vy|elementen|
    |"Katalog"|elementen_a|
    |"Lägg till bok"|elementen_b|
    |"Mina Böcker"|elementen_c|
    |"Statistik"|elementen_d|