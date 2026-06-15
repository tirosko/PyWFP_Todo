# GitHUB štúdium

Poznámky k spôsobu použitia TAG pre jednotlivé etapy vývoja SW

## Príkazy Git

```bash
git tag -a v1.0.0 -m "Main"
```

```bash
# Stabilné verzie
git tag -a v1.0.0 -m "First stable release"
```

```bash
# Vývojové verzie (dev)
git tag -a v1.1.0-dev.1 -m "Development snapshot 1"
git tag -a v1.1.0-dev.2 -m "Development snapshot 2"
```

```bash
# Release kandidáty (rc)
git tag -a v1.1.0-rc1 -m "Release candidate 1"
```

```bash
# Hotfixy
git tag -a v1.1.1-hotfix1 -m "Fix crash in physics engine"
```

## Push tagov na GitHub

```bash
# Jeden tag
git push origin v1.1.0-dev.1
```

```bash
# Všetky tagy
git push --tags
```

## Použitie tagov v Python workflow

Detailne preskúmať

Inštalácia projektu cez pip podľa tagu
Extrémne silné
pip install git+<https://github.com/tvoj-username/tvoj-projekt.git@v1.1.0-dev.1>

Alebo stabilná verzia
pip install git+<https://github.com/tvoj-username/tvoj-projekt.git@v1.0.0>
