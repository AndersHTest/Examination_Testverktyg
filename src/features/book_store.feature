#noinspection CucumberUndefinedStep
Feature Book store
  Scenario:
    Given: Du har länken till Läslistan
    When: Du klickar på länken
    Then: Katalog-knappen är inaktiverad
    And: De andra tre knapparna är aktiva
    And: Det finns ett h2-element med texten "Välkommen!"
    And: Det finns en paragraf med texten: "Sidan för dig som gillar att läsa. Välj dina favoriter."


  Scenario:
    Given: Du har länken till Läslistan
    When: Du hovrar över din favoritbok och klickar på hjärtknappen
    And: Du klickar på knappen "Mina böcker"
    Then: Din favoritbok finns listad här


  Scenario:
    Given: Du har länken till Läslistan
    When: Du klickar på knappen "Lägg till bok"
    Then: Knappen lägg till bok är inaktiverad


  Scenario:
    Given: Du har länken till Läslistan
    When: Du klickar på knappen "Lägg till bok"
    And: Du fyller i titel och författare
    And: Klickar på "Lägg till bok"
    And: Klickar på knappen "Katalog"
    Then: Boken finns listad i katalogen


  Scenario:
    Given: Du har länken till Läslistan
    When: Du klickar på knappen "Statistik"
    Then: Finns det information om hur många böcker som finns tillgängliga
    And: Du kan se hur många böcker som har favoritmarkerats.




