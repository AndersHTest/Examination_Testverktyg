# language: sv

Egenskap: Statistik
  Scenario: Visa statistik över favoritmarkerade böcker
  # User Story: Statistik
  # Som en användare på Läslistan
  # vill jag kunna se statistik över hur många böcker
  # som finns och som hur många som är favoritmarkerade
  # så att jag kan se hur många böcker
  # som finns och hur många favoriter som har sparats

  Givet att du är på Läslistans startsida
  När du klickar på knappen "Statistik"
  Så verifierar du att du kan se hur många böcker som är tillgängliga i katalogen
  Och verifierar du att du kan se hur många böcker som har favoritmarkerats


  Scenariomall: Visa rätt antal hjärtmarkerade böcker i statistiken
  # User Story: Statistik antal hjärtmarkerade böcker
  # Som en användare på Läslistan
  # vill jag kunna se statistik på hjärtmarkerade böcker
  # så att jag kan se hur många böcker som har hjärtmarkerats totalt
    Givet att du är på Läslistans startsida
    När du hjärtmarkerar <antal> böcker
    Och klickar på statistik
    Så stämmer <antal> hjärtmarkerade böcker

  Exempel:
  |antal|
  |2    |
  |4    |
  |6    |


  Scenario: Visa statistik över antal böcker i katalogen
  # User Story: Statistik antal böcker i katalogen
  # Som en användare på Läslistan
  # vill jag kunna se statistik på hur många böcker som finns tillagda i katalogen
  # så att jag snabbt får en översikt över hur många böcker som finns
    Givet att du är på Läslistans startsida
    Och att det från början finns 13 böcker i katalogen
    Och att det finns två nya böcker tillagda
    När jag klickar på statistik
    Så visar statistiken lika många böcker som det finns i katalogen
