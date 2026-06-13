# Poznámky pre vývoj aplikácii vo verziach.

**git tags pre development** sú jeden z najlepších spôsobov, ako mať poriadok vo verziách, release-och, hotfixoch a experimentoch.
Dám ti **kompletný, profesionálny workflow**, ktorý používajú reálne tímy (GitHub, open‑source projekty, Python balíčky).

> **Stručná pointa**

Git tagy slúžia na:

* označenie stabilných verzií (release tags)
* označenie vývojových míľnikov (dev tags)
* označenie hotfixov
* označenie experimentov
* označenie buildov pre CI/CD

A hlavne: **tagy sa nikdy nehýbu** (ak ich nechceš prepisovať).

**1) Typy tagov, ktoré sa používajú pri vývoji**

**✔ 1) Lightweight tag**

Len „nálepka“ na commit.

git tag dev-2024-06-12

**✔ 2) Annotated tag (odporúčané)**

Obsahuje autora, dátum, popis.

git tag -a v1.2.0 -m "Release v1.2.0"

**✔ 3) Pre-release / development tagy**

Používa sa pri vývoji:

* v1.3.0-alpha
* v1.3.0-beta
* v1.3.0-rc1
* v1.3.0-dev.1

git tag -a v1.3.0-dev.1 -m "Development snapshot"

**2) Ako používať tagy počas developmentu**

**A) Tagovanie dôležitých checkpointov**

Keď dokončíš veľkú časť práce:

git tag -a dev-checkpoint-1 -m "Finished physics engine"

**🔹 B) Tagovanie experimentov**

git tag experiment-collision-01

**🔹 C) Tagovanie verzií pre testovanie**

git tag -a v0.9.0-rc1 -m "Release candidate"

**🔹 D) Tagovanie hotfixov**

git tag -a hotfix-2024-06-12 -m "Fix crash in movement system"

**3) Push tagov na GitHub**

**Push jedného tagu:**

git push origin v1.2.0

**Push všetkých tagov:**

git push --tags

**🔄 4) Checkout starého tagu (read‑only mód)**

Ak chceš pozrieť starú verziu:

git checkout v1.2.0

Git ťa prepne do **detached HEAD** — môžeš testovať, ale nie commitovať.

Ak chceš z toho spraviť vetvu:

git switch -c fix-old-version

**5) Mazanie tagov**

**Lokálne:**

git tag -d v1.2.0

**Na GitHube:**

git push origin --delete v1.2.0

**6) Profesionálny workflow pre teba (odporúčanie)**

Toto je **najčistejší systém**, ktorý používajú Python projekty, Docker projekty aj hry:

**✔ main = stabilný kód**

**✔ develop = aktívny vývoj**

**✔ feature/\* = nové veci**

**✔ release tagy = v1.0.0, v1.1.0**

**✔ dev tagy = v1.2.0-dev.1, v1.2.0-dev.2**

**✔ rc tagy = v1.2.0-rc1**

**✔ hotfix tagy = v1.2.1-hotfix1**

**Príklad:**

v1.0.0
v1.1.0
v1.2.0-dev.1
v1.2.0-dev.2
v1.2.0-rc1
v1.2.0
v1.2.1-hotfix1

## Python projekty (FastAPI, Django, Pygame)

**Profesionálny, čistý a praktický systém**, ktorý funguje pre:

* FastAPI
* Django
* Pygame
* akýkoľvek Python projekt s virtualenv/uv
* GitHub workflow

Najlepší workflow pre Python projekty je:

**main = stabilný kód**
**develop = aktívny vývoj**
**feature/**\* = nové veci
**tagy = verzie balíkov, release kandidáty, dev snapshoty**

A tagy sa používajú na:

* verziovanie projektu
* generovanie release balíkov
* označenie stabilných míľnikov
* CI/CD buildy
* pip inštaláciu priamo z GitHubu

**1) Ako vyzerá profesionálne tagovanie Python projektu**

**Stabilné verzie**

v1.0.0
v1.1.0
v1.2.0

**Vývojové verzie**

v1.3.0-dev.1
v1.3.0-dev.2

**Release kandidáty**

v1.3.0-rc1
v1.3.0-rc2

**✔ Hotfixy**

v1.3.1-hotfix1

**2) Ako vytvoriť tag pre Python projekt**

**Annotated tag (odporúčané)**

git tag -a v1.3.0-dev.1 -m "Development snapshot"

**Push na GitHub**

git push origin v1.3.0-dev.1

**3) Ako použiť tag na inštaláciu Python projektu cez pip**

Toto je extrémne užitočné pri testovaní:

pip install git+https://github.com/tvoj-username/tvoj-projekt.git@v1.3.0-dev.1

Alebo:

pip install git+https://github.com/tvoj-username/tvoj-projekt.git@v1.2.0

Takto vieš testovať staré aj nové verzie bez chaosu.

**4) Tagy + virtualenv / uv**

**A) Virtualenv**

python3.13 -m venv venv
source venv/bin/activate
pip install .

**B) uv (najlepší moderný spôsob)**

uv venv
uv pip install .

A keď chceš testovať konkrétny tag:

uv pip install git+https://github.com/tvoj-username/projekt.git@v1.3.0-dev.1

**🚀 5) Tagy + GitHub Releases (Python balíčky)**

Keď vytvoríš tag:

v1.2.0

GitHub vie automaticky:

* vytvoriť release
* pridať changelog
* spustiť CI/CD
* vybuildovať wheel (.whl)
* publikovať na PyPI

Toto je štandard pre Python balíčky.

**🔄 6) Checkout starého tagu (read‑only mód)**

git checkout v1.2.0

Ak chceš z toho spraviť vetvu:

git switch -c fix-legacy-bug

**🧹 7) Mazanie tagov**

**Lokálne:**

git tag -d v1.3.0-dev.1

**Na GitHube:**

git push origin --delete v1.3.0-dev.1

**⭐ Tiborov odporúčaný workflow (presne pre tvoje Python projekty)**

Toto je pre teba najlepšie, podľa toho, ako pracuješ:

**1) develop**

– všetko nové

**2) feature/\*\*\***

– nové moduly, nové mechaniky, nové API

**3) main**

– len stabilné veci

**4) tagy:**

* **v1.0.0** – prvý stabilný release
* **v1.1.0-dev.1** – nový vývoj
* **v1.1.0-dev.2** – ďalší checkpoint
* **v1.1.0-rc1** – testovacia verzia
* **v1.1.0** – finálna verzia
* **v1.1.1-hotfix1** – rýchla oprava

**5) pip inštalácia podľa tagu**

– testovanie bez chaosu

**🔥 Tibor, chceš aby som ti pripravil:**

**A) kompletný Git workflow pre Python projekt (šablóna)**

**B) automatický skript na generovanie tagov + changelog**

**C) GitHub Actions, ktoré automaticky buildnú Python balík pri každom tagu**

**D) presný systém verziovania pre tvoju Pygame hru alebo FastAPI backend**

Stačí povedať, ktorú možnosť chceš.

Tibor, ideme na **A – kompletný Git workflow pre Python projekt**, presne tak, aby si ho mohol okamžite použiť vo svojich projektoch (Pygame, FastAPI, Django, utility skripty).
Toto je **profesionálny, stabilný a čistý systém**, ktorý používajú Python vývojári v reálnych tímoch.

**🎯 Takeaway**

Najlepší workflow pre Python projekt je:

**main = stabilné verzie**
**develop = aktívny vývoj**
**feature/**\* = nové veci
**tagy = verzie projektu (dev, rc, release)**

A k tomu pridáme:

* jasné pravidlá pre commitovanie
* štruktúru verzií
* systém tagovania
* workflow pre pip inštaláciu podľa tagu
* workflow pre testovanie starých verzií

**🧱 1) Štruktúra vetiev (branches)**

**✔ main**

* len stabilné verzie
* každá verzia má tag (v1.0.0, v1.1.0, …)

**✔ develop**

* všetko, čo je pripravené, ale ešte nie je release
* sem sa mergujú feature vetvy

**✔ feature/\***

* každá nová funkcia má vlastnú vetvu
* príklady:
  + feature/collision-physics
  + feature/new-menu-ui
  + feature/api-auth

**✔ hotfix/\***

* rýchle opravy po release
* príklad:
  + hotfix/fix-crash-on-start

**🧩 2) Štruktúra verzií (semantic versioning)**

Používame:

MAJOR.MINOR.PATCH

**Príklady:**

* **1.0.0** – prvý stabilný release
* **1.1.0** – nové funkcie
* **1.1.1** – opravy
* **2.0.0** – veľká zmena, nekompatibilná

**🏷️ 3) Tagovanie verzií (najdôležitejšia časť)**

**✔ Stabilné verzie**

git tag -a v1.0.0 -m "First stable release"

**✔ Vývojové verzie (dev)**

Používa sa počas vývoja:

git tag -a v1.1.0-dev.1 -m "Development snapshot 1"

git tag -a v1.1.0-dev.2 -m "Development snapshot 2"

**✔ Release kandidáty (rc)**

Pred finálnym release:

git tag -a v1.1.0-rc1 -m "Release candidate 1"

**✔ Hotfixy**

git tag -a v1.1.1-hotfix1 -m "Fix crash in physics engine"

**🚀 4) Push tagov na GitHub**

**Jeden tag:**

git push origin v1.1.0-dev.1

**Všetky tagy:**

git push --tags

**📦 5) Použitie tagov v Python workflow**

**✔ Inštalácia projektu cez pip podľa tagu**

Toto je extrémne silné:

pip install git+https://github.com/tvoj-username/tvoj-projekt.git@v1.1.0-dev.1

Alebo stabilná verzia:

pip install git+https://github.com/tvoj-username/tvoj-projekt.git@v1.0.0

**✔ Testovanie starých verzií**

git checkout v1.0.0

Ak chceš z toho spraviť vetvu:

git switch -c fix-legacy-bug

**6) Workflow pre develop → release**

**1) Dokončíš funkcie vo feature vetvách**

**2) Merge do develop**

**3) Testovanie**

**4) Vytvoríš RC tag**

git tag -a v1.2.0-rc1 -m "Release candidate"

git push origin v1.2.0-rc1

**5) Ak je všetko OK → finálny release**

git tag -a v1.2.0 -m "Stable release"

git push origin v1.2.0

**7) Mazanie tagov**

**Lokálne:**

git tag -d v1.1.0-dev.1

**Na GitHube:**

git push origin --delete v1.1.0-dev.1

**Tiborov personalizovaný workflow (optimalizovaný pre tvoje projekty)**

Toto je presne pre teba – podľa toho, ako pracuješ s Pygame, FastAPI, GitHubom a WSL:

**✔ develop**

– všetko nové, priebežné

**✔ feature/\*\*\***

– každá nová mechanika alebo modul

**✔ main**

– len stabilné verzie

**✔ tagy:**

* **v1.0.0** – prvý release
* **v1.1.0-dev.1** – nový vývoj
* **v1.1.0-dev.2** – ďalší checkpoint
* **v1.1.0-rc1** – testovacia verzia
* **v1.1.0** – finálna verzia
* **v1.1.1-hotfix1** – rýchla oprava

**✔ pip inštalácia podľa tagu**

– testovanie bez chaosu

**✔ uv / virtualenv**

– každá verzia testovaná v čistom prostredí

Tibor, tu máš **najlepšiu, modernú a profesionálnu štruktúru pre vývoj Python Flask web stránky** – presne tak, aby bola:

* prehľadná
* rozšíriteľná
* pripravená na Jinja2 šablóny
* pripravená na Blueprinty
* pripravená na API
* pripravená na databázu
* pripravená na Git tagy a CI/CD
* kompatibilná s tvojím WSL workflow

Toto je štruktúra, ktorú používajú reálne Flask projekty v produkcii.

**🎯 Takeaway**

Najlepšia Flask štruktúra má:

* **app/** – celá aplikácia
* **blueprints/** – moduly (auth, admin, api…)
* **templates/** – HTML
* **static/** – CSS, JS, obrázky
* **config.py** – nastavenia
* **wsgi.py** – vstupný bod pre server
* **tests/** – testy
* **instance/** – lokálne nastavenia (DB, secrets)

**🧱 1) Kompletná štruktúra Flask projektu (profesionálna)**

flask\_app/

│

├── app/

│ ├── \_\_init\_\_.py

│ ├── routes.py

│ ├── models.py

│ ├── extensions.py

│ ├── config.py

│ │

│ ├── blueprints/

│ │ ├── \_\_init\_\_.py

│ │ ├── auth/

│ │ │ ├── \_\_init\_\_.py

│ │ │ ├── routes.py

│ │ │ └── forms.py

│ │ └── api/

│ │ ├── \_\_init\_\_.py

│ │ └── routes.py

│ │

│ ├── templates/

│ │ ├── base.html

│ │ ├── index.html

│ │ └── auth/

│ │ └── login.html

│ │

│ └── static/

│ ├── css/

│ │ └── styles.css

│ ├── js/

│ │ └── app.js

│ └── img/

│

├── instance/

│ └── config.py

│

├── tests/

│ ├── \_\_init\_\_.py

│ └── test\_routes.py

│

├── .env

├── .gitignore

├── requirements.txt

├── pyproject.toml

├── wsgi.py

└── README.md

**🧩 2) Vysvetlenie jednotlivých častí**

**✔ app/\_\_init\_\_.py**

Vytvára Flask aplikáciu, registruje Blueprinty, načítava config.

**✔ app/routes.py**

Základné route (napr. homepage).

**✔ app/models.py**

SQLAlchemy modely (ak používaš DB).

**✔ app/extensions.py**

Inicializácia rozšírení:

* SQLAlchemy
* LoginManager
* Migrate
* Mail
* CORS

**✔ app/blueprints/**

Modulárne časti aplikácie:

* auth/ – login, register
* api/ – REST API
* admin/ – admin sekcia

**✔ app/templates/**

Jinja2 HTML šablóny.

**✔ app/static/**

CSS, JS, obrázky.

**✔ instance/config.py**

Lokálne nastavenia (ignorované Gitom).

**✔ wsgi.py**

Vstupný bod pre produkciu (Gunicorn, uWSGI).

**🚀 3) Obsah najdôležitejších súborov**

**✔ wsgi.py**

from app import create\_app

app = create\_app()

if \_\_name\_\_ == "\_\_main\_\_":

app.run(debug=True)

**✔ app/\_\_init\_\_.py**

from flask import Flask

from .config import Config

from .extensions import db

from .blueprints.auth import auth\_bp

from .blueprints.api import api\_bp

def create\_app():

app = Flask(\_\_name\_\_, instance\_relative\_config=True)

app.config.from\_object(Config)

app.config.from\_pyfile("config.py", silent=True)

db.init\_app(app)

app.register\_blueprint(auth\_bp)

app.register\_blueprint(api\_bp, url\_prefix="/api")

return app

**🧪 4) Vývojový workflow (tvoj štýl)**

**1) Vytvoríš virtuálne prostredie**

python3.13 -m venv venv

source venv/bin/activate

**2) Nainštaluješ Flask**

pip install flask flask\_sqlalchemy flask\_login flask\_migrate

**3) Spustíš aplikáciu**

flask --app wsgi run --debug

**🏷️ 5) Git workflow + tagy pre Flask projekt**

**Vývoj:**

develop

feature/auth

feature/api

feature/ui

**Release:**

git tag -a v1.0.0 -m "First stable Flask release"

git push origin v1.0.0

**Dev snapshot:**

git tag -a v1.1.0-dev.1 -m "New API module"

**Personalizovaný Flask setup**

Pre tvoje projekty odporúčam:

* **Blueprinty** (auth, api, admin)
* **Jinja2 šablóny**
* **SQLAlchemy + Migrate**
* **Gunicorn pre produkciu**
* **WSL2 + Python 3.13**
* **Git tagy pre verzie**
* **uv pre rýchle prostredia**