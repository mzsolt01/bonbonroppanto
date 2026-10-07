# Bonbonroppantó

Candy Crush-szerű, hármas párosítós böngészős játék iPhone-ra. Egyetlen fájl (`index.html`), nincs build lépés, nincs függőség.

## Futtatás

- Online: https://mzsolt01.github.io/bonbonroppanto/ (GitHub Pages, a `master` ágból).
- iPhone-on: nyisd meg a fenti címet Safariban, majd Megosztás → Főképernyőhöz adás. Saját ikonnal, teljes képernyőn indul, és az első megnyitás után internet nélkül is működik.
- Gépen: `python -m http.server 8765`, majd http://127.0.0.1:8765/

## Kiadás

1. Módosítsd az `index.html`-t.
2. Növeld a `VERSION` értékét az `sw.js`-ben (pl. `bonbon-v2`), különben a telefonok a régi, eltárolt változatot mutatják tovább.
3. `git commit` és `git push`; a GitHub Pages pár percen belül frissül.

Az ikonokat a `tools/make_icons.py` állítja elő.

## Játékelemek

- Különleges bonbonok: csíkos (4 egy sorban), csomagolt (L/T alak), csokibomba (5 egy sorban), ezek kombinálhatók is.
- Akadályok: zselé (1–2 réteg), lakat (nem mozdítható bonbon), karamellkocka (1–2 ütés, elzárja az esést, a bonbonok átlósan csúsznak mellette).
- Szintcélok: pontszám, színgyűjtés, zselétakarítás. A szintek elrendezése a szintszámból generálódik (`makeLevel`), így újrapróbálásnál ugyanaz marad.
- Pályaformák (`SHAPES`): négyzet, széles, kör, kereszt, szív, fánk, homokóra, ikertorony. A `#` mező, a `.` lyuk; a bonbonok a lyukakon átesnek, az új bonbonok minden oszlop legfelső mezőjén érkeznek.
- Kezdőképernyő: animált cukrászda-jelenet (`drawHome`). Egy épületre koppintva alulról felcsúszik a fejlesztési panel; alul a Játék, Szintek és Szabályok gomb.
- Cukrászda (bázis, `BUILDINGS`): a szintekért cukor, kakaó és zselé jár (vesztes szintért 40%). Öt épület, egyenként 5 szinttel:
  - Konyha: +1 lépés szintenként, a 2. szinttől szabad csere
  - Csokoládéüzem: különleges bonbonok a tábla indulásakor, a 3. szinttől csokiöntés
  - Cukrászműhely: habverő
  - Fakanálműhely: fakanál
  - Kirakat: több nyersanyag
- Boosterek (`BOOSTS`, egyik sem kerül lépésbe): fakanál (egy mező), habverő (egy sor), csokiöntés (egy szín), szabad csere, keverés (szintenként 1). Vesztéskor +5 lépés vásárolható nyersanyagért, szintenként egyszer.
- A haladás, a nyersanyagok és az épületek a böngésző `localStorage`-ában tárolódnak.

## Artifact közzététel

A `<!-- ARTIFACT-START -->` és `<!-- ARTIFACT-END -->` közötti rész az artifact tartalma (a `</head>` és `<body>` sorok nélkül); a Claude artifact saját maga adja hozzá a keretet.
