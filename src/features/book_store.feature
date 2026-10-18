#noinspection CucumberUndefinedStep
Feature: Startsida
  Scenario: Kontrollera startsida
    # Som en användare på Läslistan
    # vill jag att startsidan är katalogsidan
    # så att jag kan välja mina favoritböcker
    Given Du är på Läslistans startsida
    Then Katalog-knappen är inaktiverad
    And De andra tre knapparna är aktiva
    And Det finns ett h2-element med texten "Välkommen!"
    And Det finns en paragraf med texten: "Sidan för dig som gillar att läsa. Välj dina favoriter."


  Scenario: Lägg till favoritböcker
    # Som en användare på Läslistan
    # vill jag kunna lägga till mina favoritböcker
    # så att jag lätt kan komma åt och se dom under "Mina böcker"
    Given Du är på Läslistans startsida
    When Du klickar på hjärtknappen till vänster om boken du vill favoritmarkera
    And Du klickar på knappen "Mina Böcker"
    Then Din favoritbok finns listad på sidan


  Scenario: Lägg till en ny bok i katalogen
    # Som en användare på Läslistan
    # vill jag kunna lägga till en bok som inte finns tillagd i "Katalog"
    # så att jag kan se den i katalogen.
    Given Du är på Läslistans startsida
    When Du klickar på knappen "Lägg till bok"
    And du fyller i titel och författare
    And Du klickar på knappen "Lägg till ny bok"
    And Du klickar på knappen "Katalog"
    Then Ska boken finnas listad i katalogen


  Scenario: Visa statistik över favoritmarkerade böcker
    # Som en användare på Läslistan
    # vill jag kunna se statistik över hur många böcker
    # som finns och som hur många som är favoritmarkerade
    # så att jag kan se hur många böcker
    # som finns och hur många favoriter som har sparats
    Given Du är på Läslistans startsida
    When Du klickar på knappen "Statistik"
    Then Verifiera att du kan se hur många böcker som är tillgängliga i katalogen
    And Verifiera att du kan se hur många böcker som har favoritmarkerats
