# Úvod do vývoja WEB aplikácii
  
Pokúsime sa využiť Python Framework Flask pre úvod do problematiky WEB stránok  
Aby sme riešili profesionálne, tak sa aktuálne zaoberáme jazyom HTML a CSS  

## Todo aplikácia

Aplikáciu spustíš v termináli príkazom:

```powershell
.\.venv\Scripts\python.exe app.py
```

Potom otvor v prehliadači adresu `http://127.0.0.1:5000`. Úlohy sa ukladajú do súboru `tasks.txt`.
Pri pridávaní úlohy môžeš voliteľne zadať termín dokončenia v slovenskom kalendári a čas v 24-hodinovom formáte. Hodinu a potom minúty zadávaš bez dvojbodky; minúty sa zaokrúhlia na najbližších 5. Kalendár sa dá ovládať klávesnicou: šípkami sa pohybuješ po dňoch, `Home`/`End` vyberie začiatok/koniec týždňa, `Page Up`/`Page Down` mení mesiac a `Enter` potvrdí dátum.
Ak je úloh viac ako tri, zoznam úloh sa dá posúvať. Tlačidlom **Upraviť** pri úlohe sa jej názov a termín načítajú do formulára hore, kde môžeš zmeny uložiť alebo úpravu zrušiť.
V kalendári sú dni s naplánovanými úlohami farebne označené; tlačidlom so šípkou pri dni otvoríš samostatný denný plán. Časová os zobrazuje hodiny od 6:00 do 22:00, úlohy môžeš medzi hodinami presúvať potiahnutím a ich minúty zostanú zachované.


