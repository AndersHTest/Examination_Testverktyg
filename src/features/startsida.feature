# language: sv


Egenskap: Startsida
  Scenario: Kontrollera startsida
    # User Story: Startsida
    # Som en användare på Läslistan
    # vill jag att startsidan är katalogsidan
    # så att jag kan välja mina favoritböcker
    Givet att du är på Läslistans startsida
    Så är katalog-knappen inaktiverad
    Och de andra tre knapparna är aktiva
    Och det finns ett h2-element med texten "Välkommen!"
    Och det finns en paragraf med texten: "Sidan för dig som gillar att läsa. Välj dina favoriter."



  Scenariomall: Klicka på hjärtmarkering flera gånger
    # User Story: Klicka på hjärtmarkering flera gånger
    # Som en användare på Läslistan
    # vill jag undersöka vad som händer om jag trycker på hjärtknappen flera gånger
    # så att jag stillar min nyfikenhet
    Givet att du är på Läslistans startsida
    När du klickar på hjärtknappen <antal> gång(er)
    Så ser du att <knappen ändras>


  Exempel:
    |antal|knappen ändras|
    |1    |det läggs till ett hjärta|
    |2    |hjärtat tas bort         |
    |3    |det läggs till ett hjärta|
