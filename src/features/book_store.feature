#noinspection CucumberUndefinedStep
# language: sv
Egenskap: Startsida
  Scenario: Kontrollera startsida
    # Som en användare på Läslistan
    # vill jag att startsidan är katalogsidan
    # så att jag kan välja mina favoritböcker
    Givet att du är på Läslistans startsida
    Så är katalog-knappen inaktiverad
    Och de andra tre knapparna är aktiva
    Och det finns ett h2-element med texten "Välkommen!"
    Och det finns en paragraf med texten: "Sidan för dig som gillar att läsa. Välj dina favoriter."


  Scenario: Lägg till favoritböcker
    # Som en användare på Läslistan
    # vill jag kunna lägga till mina favoritböcker
    # så att jag lätt kan komma åt och se dom under "Mina böcker"
    Givet att du är på Läslistans startsida
    När du klickar på hjärtknappen till vänster om boken du vill favoritmarkera
    Och du klickar på knappen "Mina Böcker"
    Så  är din favoritbok listad på sidan


  Scenario: Lägg till en ny bok i katalogen
    # Som en användare på Läslistan
    # vill jag kunna lägga till en bok som inte finns tillagd i "Katalog"
    # så att jag kan se den i katalogen.
    Givet att du är på Läslistans startsida
    När du klickar på knappen "Lägg till bok"
    Och du fyller i titel och författare
    Och du klickar på knappen "Lägg till ny bok"
    Och du klickar på knappen "Katalog"
    Så ska boken finnas listad i katalogen


  Scenario: Visa statistik över favoritmarkerade böcker
    # Som en användare på Läslistan
    # vill jag kunna se statistik över hur många böcker
    # som finns och som hur många som är favoritmarkerade
    # så att jag kan se hur många böcker
    # som finns och hur många favoriter som har sparats
    Givet att du är på Läslistans startsida
    När du klickar på knappen "Statistik"
    Så verifierar du att du kan se hur många böcker som är tillgängliga i katalogen
    Och verifierar du att du kan se hur många böcker som har favoritmarkerats
