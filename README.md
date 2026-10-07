# Bonbonroppantó

Candy Crush-szerű, hármas párosítós böngészős játék iPhone-ra. Egyetlen fájl (`index.html`), nincs build lépés, nincs függőség.

## Futtatás

- Gépen: nyisd meg az `index.html`-t böngészőben, vagy indíts egy helyi szervert: `python -m http.server 8765`
- iPhone-on: a Claude artifact linkjéről, vagy bármilyen statikus tárhelyről (pl. GitHub Pages). Safariban Megosztás → Főképernyőhöz adás, és appként indul.

## Játékelemek

- Különleges bonbonok: csíkos (4 egy sorban), csomagolt (L/T alak), csokibomba (5 egy sorban), ezek kombinálhatók is.
- Akadályok: zselé (1–2 réteg), lakat (nem mozdítható bonbon), karamellkocka (1–2 ütés, elzárja az esést, a bonbonok átlósan csúsznak mellette).
- Szintcélok: pontszám, színgyűjtés, zselétakarítás. A szintek elrendezése a szintszámból generálódik (`makeLevel`), így újrapróbálásnál ugyanaz marad.
- Pályaformák (`SHAPES`): négyzet, széles, kör, kereszt, szív, fánk, homokóra, ikertorony. A `#` mező, a `.` lyuk; a bonbonok a lyukakon átesnek, az új bonbonok minden oszlop legfelső mezőjén érkeznek.
- Kezdőképernyő: animált cukrászda-jelenet (`drawHome`). Egy épületre koppintva alulról felcsúszik a fejlesztési panel; alul a Játék, Szintek és Szabályok gomb.
- Cukrászda (bázis, `BUILDINGS`): a szintekért cukor, kakaó és zselé jár (vesztes szintért 40%). Négy épület, egyenként 5 szinttel:
  - Konyha: +1 lépés szintenként
  - Csokoládéüzem: különleges bonbonok a tábla indulásakor
  - Fakanálműhely: fakanál-töltések, bármely mezőt szétüti lépés nélkül
  - Kirakat: több nyersanyag
- A haladás, a nyersanyagok és az épületek a böngésző `localStorage`-ában tárolódnak.

## Artifact közzététel

A `<!-- ARTIFACT-START -->` és `<!-- ARTIFACT-END -->` közötti rész az artifact tartalma (a `</head>` és `<body>` sorok nélkül); a Claude artifact saját maga adja hozzá a keretet.
