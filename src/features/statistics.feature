#noinspection CucumberUndefinedStep
# language: sv


Egenskap: Statistik
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
