#noinspection CucumberUndefinedStep
# language: sv


Egenskap: Mina Böcker
  Scenario: Lägg till favoritbok
  # User Story: Lägg till favoritbok
  # Som en användare på Läslistan
  # vill jag kunna lägga till mina favoritböcker
  # så att jag lätt kan komma åt och se dom under "Mina böcker"
  Givet att du är på Läslistans startsida
  När du klickar på hjärtknappen till vänster om boken du vill favoritmarkera
  Och du klickar på knappen "Mina Böcker"
  Så  är din favoritbok listad på sidan
