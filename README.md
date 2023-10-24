# UI_ObchodnyCestujuci
2C - Variant 1 aj 2

### Zadanie

Zadanie č. 2c

Úloha

Obchodný cestujúci má navštíviť viacero miest. V jeho záujme je minimalizovať cestovné náklady a cena prepravy je úmerná dĺžke cesty, preto snaží sa nájsť najkratšiu možnú cestu tak, aby každé mesto navštívil práve raz. Keďže sa nakoniec musí vrátiť do mesta z ktorého vychádza, jeho cesta je uzavretá krivka.

Zadanie Je daných aspoň 20 miest (20 – 40) a každé má určené súradnice ako celé čísla X a Y. Tieto súradnice sú náhodne vygenerované. (Rozmer mapy môže byť napríklad 200 * 200 km.) Cena cesty medzi dvoma mestami zodpovedá Euklidovej vzdialenosti – vypočíta sa pomocou Pytagorovej vety. Celková dĺžka trasy je daná nejakou permutáciou (poradím) miest. Cieľom je nájsť takú permutáciu (poradie), ktorá bude mať celkovú vzdialenosť čo najmenšiu.

Výstupom je poradie miest a dĺžka zodpovedajúcej cesty.

### Variant 1 - Genetický algoritmus

Genetický algoritmus

Genetická informácia je reprezentovaná vektorom, ktorý obsahuje index každého mesta v nejakom poradí (nejaká permutácia miest). Keďže hľadáme najkratšiu cestu, je najlepšie vyjadriť fitnes jedinca ako prevrátenú hodnotu dĺžky celej cesty.

(Bud hladam lokalne maximum alebo minimum. Ked mam algo nastaveny na maximum tak by to bolo ze cim dlhsia draha tym lepsia. Preto to potrebujem obratit)

Jedincov v prvej generácii inicializujeme náhodne – vyberáme im náhodnú permutáciu miest. Jedincov v generácii by malo byť tiež aspoň 20. Je potrebné implementovať aspoň dve metódy výberu rodičov z populácie.

Kríženie je možné robiť viacerými spôsobmi, ale je potrebné zabezpečiť, aby vektor génov potomka bol znovu permutáciou všetkých miest. Často používaný spôsob je podobný dvojbodovému kríženiu. Z prvého rodiča vyberieme úsek cesty medzi dvoma náhodne zvolenými bodmi kríženia a dáme ho do potomka na rovnaké miesto. Z druhého rodiča potom vyberieme zvyšné mestá v tom poradí, ako sa nachádzajú v druhom rodičovi a zaplníme tým ostatné miesta vo vektore.

Mutácie potomka môžu byť jednoduché – výmena dvoch susedných miest alebo zriedkavejšie používaná výmena dvoch náhodných miest. Tá druhá výmena sa používa zriedkavo, lebo môže rozhodiť blízko optimálne riešenie. Často sa však používa obrátenie úseku – znova sa zvolia dva body a cesta medzi nimi sa obráti. Sú možné aj ďalšie mutácie, ako napríklad posun úseku cesty niekam inam.

Dokumentácia musí obsahovať konkrétne použitý algoritmus, opis konkrétnej reprezentácie génov, inicializácie prvej generácie a presný spôsob tvorby novej generácie. Dôležitou časťou dokumentácie je zhodnotenie vlastností vytvoreného systému a porovnanie dosahovaných výsledkov aspoň pre dva rôzne spôsoby tvorby novej generácie alebo rôzne spôsoby selekcie. Dosiahnuté výsledky (napr. vývoj fitness) je vhodné zobraziť grafom. Dokumentácia by mala tiež obsahovať opis vylepšovania, dolaďovania riešenia.

### Variant 2 - Zakázané prehľadávanie (tabu search)

Zakázané prehľadávanie patrí do skupiny algoritmov, ktoré využívajú na hľadanie riešenia v priestore možných stavov lokálne vylepšovanie (optimalizáciu). To znamená, že z aktuálneho stavu si vytvorí nasledovníkov a presunie sa do takého, ktorý má lepšie ohodnotenie (najlepšieho takého). Ak neexistuje nasledovník s lepším ohodnotením (a nenašli sme dostatočne dobré riešenie), tak sme v lokálnom extréme a je potrebné sa z neho dostať.

(Ako viem kedy som v lokalnom extreme a kedy v globalnom?)

(Robim si zoznam lokalnych extremov. Akonahle najdem najlepsi extrem z tych lokalnych tak to je globalny extrem)

Tento algoritmus si teda vyberie horšieho nasledovníka a zároveň si uloží aktuálny stav do tzv. zoznamu zakázaných stavov (tabu list). Je to nevyhnutné, aby sme sa z toho horšieho nasledovníka znovu nedostali do tohto lokálneho extrému a nevytvorili tak nekonečný cyklus. Zoznam zakázaných stavov je pomerne krátky, aby nám netrvala dlho jeho kontrola. Keď sa zaplní a je doň potrebné vložiť nový stav, tak ten najstarší sa zahodí.

(Cize ta velkost bude povedzme 3 a ked dojde novy tak najstarsi vyhodim?)

(Ano)

Problém je opäť reprezentovaný vektorom, ktorý obsahuje index každého mesta v nejakom poradí (nejaká permutácia miest). Nasledovníci sú vektory, v ktorých je vymenené poradie niektorej dvojice susedných uzlov.

Dôležitým parametrom tohto algoritmu je dĺžka zoznamu zakázaných stavov. Príliš krátky zoznam spôsobí, že algoritmus bude často pendlovať medzi niekoľkými lokálnymi extrémami, príliš dlhý zoznam natiahne čas riešenia, lebo bude dlho trvať kontrola každého stavu, či nie je zakázaný. Je potrebné nájsť jeho vhodnú dĺžku.

Dokumentácia musí obsahovať opis konkrétne použitého algoritmu a reprezentácie údajov. Dôležitou časťou dokumentácie je zhodnotenie vlastností vytvoreného systému a opis závislosti jeho vlastností na dĺžke zoznamu zakázaných stavov. Použite aspoň dva rôzne počty miest (napr. 20 a 30).

Ten graf (asi) mas cvaknuty na telefone

### Napad co dat do dokumentacie

- Porovnanie variant
- Popis kodu
- Presnu evaluaciu casov
- Reprezentaciu udajov
- Popis algoritmu
- Zhodnotenie a opis systemu zvislosti na jeho vlastnosti na dlzke zoznamu zakázaných stavov.

## Chyby v minulej dokumentacie

- Popis kodu
- Presne casy
