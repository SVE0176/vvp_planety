# Simulace pohybů planet ve 2D

## Popis projektu

Tento projekt se zabývá simulací pohybu planet (těles) ve 2D prostoru, kde všechny objekty mají pro jednoduchost stejnou z souřadnici. Simulace uvažuje gravitační interakce mezi každou dvojicí těles podle Newtonova gravitačního zákona

F_g = G * (m_1 * m_2) / r^2

kde G je gravitační konstanta, m_1 a m_2 jsou hmotnosti těles a r je vzdálenost mezi nimi.

Pohyb těles je počítán pomocí numerické aproximace v diskrétních časových krocích. Projekt umožňuje načítání počátečních podmínek z JSON souborů, výpočet gravitačních zrychlení a vizualizaci pohybu pomocí knihovny Matplotlib.

## Implementované funkce

- načítání počátečních podmínek planet z JSON souboru
- výpočet gravitačního zrychlení mezi všemi dvojicemi těles
- vykreslení aktuálních poloh planet pomocí knihovny Matplotlib
- ukládání historie poloh těles pro pozdější vykreslení trajektorií

## Plánované funkce

- simulace pohybu těles v čase
- vykreslení trajektorií planet
- vytvoření animace simulace
- export animace do video souboru
- generování náhodných scénářů simulace
- experimentování s různou velikostí časového kroku