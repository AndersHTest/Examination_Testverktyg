#noinspection CucumberUndefinedStep
# language: sv

Egenskap: Lägg till en ny bok
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
