# move_mouse

Petit script Python qui déplace la souris aléatoirement pour éviter la mise en veille de l'écran.

## Fonctionnement

Le script boucle indéfiniment et, à chaque itération :
- déplace la souris d'un offset aléatoire (±50px) par rapport à sa position actuelle
- attend entre 1 et 3 secondes avant le prochain mouvement

Arrêt propre avec **Ctrl-C**.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install pyautogui
```

## Utilisation

```bash
python move_mouse.py
```

Ou en une seule commande (depuis `exec.txt`) :

```bash
source venv/bin/activate && pip install pyautogui && python move_mouse.py
```

## Dépendances

- [pyautogui](https://pyautogui.readthedocs.io/) — contrôle de la souris
- Python 3.x
