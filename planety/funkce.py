import json
import numpy as np
import matplotlib.pyplot as plt


G = 6.67430e-11  # gravitacni konstanta


def nacti_planety(soubor: str) -> dict:
    """
    Nacte planety ze souboru a vrati slovnik planet.

    :param soubor: cesta k JSON souboru
    :return: slovnik ve formatu {jmeno: {'mass': float, 'position': [x, y], 'velocity': [vx, vy]}}
    """
    f = open(soubor, 'r')
    data = json.load(f)
    f.close()
    return data


def vypocet_zrychleni(planety: dict) -> dict:
    """
    Vypocita zrychleni pusobici na kazdou planetu vlivem gravitace vsech ostatnich teles.

    :param planety: slovnik ve formatu {jmeno: {'mass': float, 'position': [x, y], 'velocity': [vx, vy]}}
    :return: slovnik ve formatu {jmeno: [ax, ay]}
    """
    zrychleni = {}
    for planeta, data_a in planety.items():
        ax, ay = 0.0, 0.0
        for jmena, data_b in planety.items():
            if planeta != jmena:
                dx = data_b['position'][0] - data_a['position'][0]
                dy = data_b['position'][1] - data_a['position'][1]
                r = np.sqrt(dx**2 + dy**2)
                Fg = G * data_a['mass'] * data_b['mass'] / r**2
                nx = dx / r
                ny = dy / r  # n jako normalizovany vektor
                ax += Fg * nx / data_a['mass']
                ay += Fg * ny / data_a['mass']
        zrychleni[planeta] = [ax, ay]
    return zrychleni


def vykresleni_poloh(planety : dict) -> None:
    """Vykresli aktualni polohy planet v 2D prostoru."""
    for planeta in planety:
        x, y = planety[planeta]['position']
        plt.plot(x, y, 'o', label=planeta)
    plt.title("Aktualni polohy planet")  
    plt.xlabel("x [m]")                 
    plt.ylabel("y [m]")        
    plt.legend()
    plt.show()


def uloz_polohy(planety: dict, historie: dict) -> dict:
    """
    Ulozi aktualni polohy vsech planet do historie pro pozdejsi vykresleni trajektorii.
    
    Pokud historie pro danou planetu jeste neexistuje, vytvori se novy seznam.
    """
    for jmeno, data in planety.items():
        if jmeno not in historie:
            historie[jmeno] = []
        
        aktualni_poloha = list(data['position'])
        
        historie[jmeno].append(aktualni_poloha)
        
    return historie


def proved_krok(planety: dict, dt: float) -> dict:
    """
    Provede jeden casovy krok simulace - aktualizuje polohy a rychlosti vsech planet.

    :param planety: slovnik ve formatu {jmeno: {'mass': float, 'position': [x, y], 'velocity': [vx, vy]}}
    :param dt: velikost casoveho kroku v sekundach
    :return: aktualizovany slovnik planet
    """
    zrychleni = vypocet_zrychleni(planety)
    for jmeno, data in planety.items():
        x, y = data["position"]
        vx, vy = data["velocity"]
        ax, ay = zrychleni[jmeno]
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        data["velocity"] = [vx, vy]
        data["position"] = [x, y]
    return planety


def simulace(planety: dict, dt: float, kroky: int) -> dict:
    """
    Spusti simulaci po zadany pocet kroku a vrati historii poloh vsech planet.

    :param planety: slovnik ve formatu {jmeno: {'mass': float, 'position': [x, y], 'velocity': [vx, vy]}}
    :param dt: velikost casoveho kroku v sekundach
    :param kroky: pocet casovych kroku simulace
    :return: slovnik ve formatu {jmeno: [[x0, y0], [x1, y1], ...]}
    """
    historie = {}
    for j in range(kroky):
        uloz_polohy(planety, historie)
        proved_krok(planety, dt)
    return historie


def vykresli_trajektorie(historie: dict) -> None:
    """
    Vykresli trajektorie vsech planet na zaklade ulozene historie poloh.

    :param historie: slovnik ve formatu {jmeno: [[x0, y0], [x1, y1], ...]}
    """
    for jmeno, polohy in historie.items():
        x = [p[0] for p in polohy]
        y = [p[1] for p in polohy]
        plt.plot(x, y, label=jmeno)
        plt.plot(x[-1], y[-1], 'o')
    plt.title("Trajektorie planet")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.legend()
    plt.show()