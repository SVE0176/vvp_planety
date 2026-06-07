# Simulace pohybů planet ve 2D

## Popis projektu

Tento projekt se zabývá simulací pohybu planet (těles) ve 2D prostoru, kde všechny objekty mají pro jednoduchost stejnou z souřadnici. Simulace uvažuje gravitační interakce mezi každou dvojicí těles podle Newtonova gravitačního zákona

F_g = G * (m_1 * m_2) / r^2

kde G je gravitační konstanta, m_1 a m_2 jsou hmotnosti těles a r je vzdálenost mezi nimi.

Pohyb těles je počítán pomocí numerické aproximace v diskrétních časových krocích. Projekt umožňuje načítání počátečních podmínek z JSON souborů, výpočet gravitačních zrychlení a vizualizaci pohybu pomocí knihovny Matplotlib.

## Instalace a spuštění

1. Naklonuj repozitář:
git clone <url repozitáře>
2. Nainstaluj požadované knihovny:
pip install numpy matplotlib
3. Spusť ukázky v `examples.ipynb` pomocí Jupyter Notebooku.

## Struktura repozitáře

- `planety/` – knihovna se všemi funkcionalitami
  - `funkce.py` – implementace všech funkcí
  - `__init__.py` – exportuje veřejné API knihovny
- `data/` – testovací data ve formátu JSON
  - `planets.json` – počáteční podmínky planet sluneční soustavy
  - `three_body.json` – scénář tří těles
- `examples.ipynb` – Jupyter notebook s ukázkami použití knihovny

## Implementované funkce

- načítání počátečních podmínek planet z JSON souboru
- výpočet gravitačního zrychlení mezi všemi dvojicemi těles
- vykreslení aktuálních poloh planet
- ukládání historie poloh těles
- spuštění simulace po zadaný počet kroků
- vykreslení trajektorií planet

## Požadované knihovny

numpy, matplotlib