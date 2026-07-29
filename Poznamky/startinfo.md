# Ako nainštalovať Flask prostredie z informácii Geek4geeks

Teória  
<https://www.geeksforgeeks.org/web-tech/web-technology/>  
<https://www.geeksforgeeks.org/websites-apps/web-development-prerequisites/>  

prečo sa učiť WEB development  
<https://www.geeksforgeeks.org/blogs/why-learning-web-development-is-a-great-career-move-in-2025/>  

[Flask - Tutorial](<https://www.geeksforgeeks.org/python/flask-tutorial/>)  
Flask je ľahký webový framework používaný na tvorbu webových aplikácií a API. Nasleduje minimalistický dizajn a poskytuje základné funkcie ako smerovanie, spracovanie požiadaviek a renderovanie šablón, pričom vývojárom umožňuje pridávať rozšírenia podľa potreby. Vďaka svojej jednoduchosti a flexibilite sa široko používa na tvorbu malých až stredne veľkých webových aplikácií.

Inštalácia  

```bash
pip install flask  
```

Pozor inštalácia flask by mala byť urobená do .venv - aby sa neinštaloval centrálne

```bash
pip freeze > requirements.txt
```

Prvá aplikácia  
<https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/>  
[Introduction to Web development using Flask](<https://www.geeksforgeeks.org/python/python-introduction-to-web-development-using-flask/>)

Pokračovanie - routing  
<https://www.geeksforgeeks.org/python/flask-app-routing/>  

Finále - Todo list app using Flask | Python
<https://www.geeksforgeeks.org/python/todo-list-app-using-flask-python/>  

Spustenie aplikácia Flask

```bash
flask --app app run --debug
```
## Príklad2
<https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/>
Príklad 2 je premenovaním app2.py na app.py a využitím template name.html a web - http://127.0.0.1:5000/login

## Routing
<https://www.geeksforgeeks.org/python/flask-app-routing/>  
Príklady -  
app_r.py  
app_rf.py   

```bash
flask --app app_r run --debug
```
## Databáza  
<https://www.geeksforgeeks.org/python/declaring-models-in-flask/>  
Vo Flask modely definujú štruktúru dát a spracovávajú databázové operácie mapovaním databázových tabuliek na Python triedy.  

```bash
pip install flask-sqlalchemy
```
