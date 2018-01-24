# Tu votes, tu comptes

Pàgina web per la visualització del recompte de vots de la campanya Tu votes, tu comptes.

Aquesta web és accessible a l'adreça: [https://tcrcat.github.io/tuvotestucomptes](https://tcrcat.github.io/tuvotestucomptes)

## Scripts de generació de dades

### csv_to_json.py

Script que permet generar les dades de vots per mesa (`vots_per_mesa.json`), vots
per municipi (`vots_per_municipi.json`) i estat del recompte (`estat_recompte.json`)
a partir dels fitxers `votscdr.csv` i `meses.csv`.

A continuació es detallen els passos per actualitzar les dades de la web:

1. Copiar els nous fitxers `votscdr.csv` i `meses.csv` al directori `data`.
2. Executar el script: `python csv_to_json.py`
3. Comprovar que no surti cap alerta d'incoherència de dades. Si fos així no fer el següent pas i caldria revisar les dades. Les dades incorrectes es guarden en el fitxer `incorrectes.csv`.
4. Fer commit i push dels fitxers `vots_per_mesa.json`, `vots_per_municipi.json` i `estat_recompte.json` del directori `data`.

Les dades de la web s'actualitzaran automàticament.
