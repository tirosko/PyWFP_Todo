# Minimálna Flask aplikácia.

## KROK 1 — Vytvorenie minimálnej Flask aplikácie

Toto je základ, z ktorého vyrastie celý projekt.
Urobíme to tak, aby si to mohol spustiť vo WSL2 aj vo Windows bez chaosu.

**Nainštaluj Flask (odporúčané vo virtuálnom prostredí)**

### WSL2 / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
```

### Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install flask
```

### Vytvor súbor app.py

Do prázdneho priečinka si vytvor súbor:

`app.py`

```python
from flask import Flask
app = Flask(\_\_name\_\_)
@app.route("/")

def index():
    return "<h1>Ahoj Tibor! Flask beží.</h1>"
```

Toto je najmenšia funkčná aplikácia.

## Spusti Flask server

### Linux / WSL2

```bash
flask --app app run --debug
```

### Windows PowerShell

flask --app app run --debug

**Otvor v prehliadači**

➡️ [http://127.0.0.1:5000](http://127.0.0.1:5000/)
Uvidíš text:

**Ahoj Tibor! Flask beží.**

### Čo sme týmto dosiahli?

* máš funkčný Flask server,
* vieš spustiť aplikáciu,
* vieš vytvoriť prvú route,
* máš pripravený základ pre ďalšie kroky.

**KROK 2 (vyber si)**

Čo chceš ako ďalší krok?

1. **Pridať ďalšie stránky (routing)**
2. **Použiť HTML šablóny (Jinja2)**
3. **Vytvoriť projektovú štruktúru (flaskr/)**
4. **Pridať formuláre a POST requesty**
5. **Pridať databázu SQLite**
6. **Pridať login systém (Blueprinty)**