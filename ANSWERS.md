### Teorifrågor

1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
<pre>
<b>Enhetstest</b> skapas normalt sett i samband med att en funktion eller en metod är skapas.
Det är antingen utvecklaren själv eller en testare som skriver enhetstestet.
Med ett enhetstest vill man testa funktionen eller metoden isolerat, utan att blanda in annan kod.
Om funktionen kräver utomstående kod för att fungera kan man fejka eller mocka de utomstående delarna,
för att få den input man behöver för att köra funktionen. Testet blir då isolerat till endast den
funktionen man testar, vilket är hela syftet med ett enhetstest. Om ett enhetstest går igenom som det ska
men någonting felar i ett integrationstest så har man antingen missuppfattat vilken input man ska få från andra
funktioner eller så ligger felet troligtvis i de utomstående funktionera. Detta kan göras med olika metoder t.ex TDD, eller BDD.

<b>integrationstest</b> skapas normalt sett av testare. Man testar att funktioner och/eller metoder
fungerar som de ska tillsammans med andra funktioner/metoder. Detta kan göras med olika metoder t.ex TDD, eller BDD.

<b>Regressionstest</b> är en samling av grundläggande enhetstest och integrationstest.
Testerna körs kontinuerligt, men främst efter att ny kod har introducerats.
Detta görs för att kontrollera att nya ändringar inte förstör befintlig kod i ett projekt.

<b>Prestandatest</b> hanterar icke-funktionella krav som rör prestandan.
T.ex svarstider, belastningstålighet och skalbarhet.
Man kan även testa effektiviteten på funktioner med hjälp av pytest-benchmark.
Med pytest-benchmark kan man mäta hur lång tid det tar att köra en funktion och behandla data.
Det är viktigt att sträva efter att försöka skriva så effektiv kod som möjligt.
</pre>
2. Beskriv hur det går till när man arbetar med TDD.
<pre>
<b>TDD</b> står för Test-Driven Development och bygger på att man skriver sina tester innan man skriver koden som ska testas.
Man följer 'Red Green Refactor' och börjar med att skriva testet. Testet felar och blir rött på grund av att det inte finns någon kod att testa.
Sedan skriver man den kod som krävs för att testet ska gå igenom och bli grönt.
Slutligen förbättrar man koden utan att ändra den grundläggande funktionaliteten.

I den första, röda fasen, ska man tänka på vad man vill utveckla.
I den andra, gröna fasen, ska man tänka på hur man ska få igenom sina tester.
I den tredje, refactor-fasen, ska man tänka på hur man kan förbättra koden.

Fördelar med denna metod är att hitta buggar tidigt i systemutvecklingsprocessen.
Det tvingar utvecklarna att fokusera på kraven man har innan man börjar skriva logiken.
</pre>
3. Beskriv hur BDD skiljer sig från TDD.
<pre>
<b>BDD</b> är designat för att testa en applikations beteende utifrån kundens synvinkel och skrivs i naturligt språk med hjälp av Gherkin-syntax.
Det kan med fördel översättas till det språk som används på den arbetsplatsen man arbetar på.
Detta förenklar samarbetet mellan utvecklingsteamet, produktägare och andra intressenter,
i och med att man inte behöver lägga så mycket tid på att översätta programmeringsspråk.

BDD använder Scenarier där tillvägagångssättet för att testa en funktion beskrivs i naturlig språk.
Dessa scenarier läggs i en feature-fil och fungerar både som dokumentation och som grund för automatiserade tester.
När man har skrivit ett scenario lägger man till en step-fil där man skriver kod till ett steg i taget.
Det blir lätt för alla intressenter att följa stegen i testet.
Det kan vara fördelaktigt att kombinera BDD och TDD i sina tester och använda TDD främst till enhetstester och BDD främst till integrationstester.
Det är oftast integrationstester som är relevanta för produktägare och andra intressenter.
</pre>
4. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend.
Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
<pre>
Jag hade velat använda TDD för backend och skriva både enhetstester och integrationstester med hjälp av denna metod.
För frontend hade jag velat kombinera BDD och playwright för att i BDD tydligt kunna visa mina testscenarier och teststeg.
Playwright vill jag använda för att det är ett smidigt verktyg för att lokalisera olika element på en webbsida,
och därmed kunna navigera på en hemsida 'som en användare'. Jag tycker att det är sunt att använda flera olika tekniker och verktyg vid test.
Under uppbyggnadsfasen eller vid felsökning kan man med fördel köra testen i slowmotion och välja att visa webbläsarfönstret så att man kan följa testen visuellt.
När testen är implementerade körs testen till fördel i bakgrunden.
I tilläg vill jag använda page-filer (POM - Page Object Model) där man kan spara ner och återanvända lokaliserare.
Vid en ändring av ett element på hemsidan krävs ofta bara en motsvarande ändring på lokaliseraren i page-filen för att hålla testen intakta.
Utan page-filen blir man tvungen att ändra lokaliseraren på alla ställen den används, direkt i testerna.
När ändringar på hemsidan görs kan man spara mycket tid när man ska underhålla sina tester om man använder sig av en page-fil.
</pre>