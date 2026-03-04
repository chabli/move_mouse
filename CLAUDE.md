# CLAUDE.md

## Projet

Script Python minimaliste de déplacement automatique de souris (anti-veille).

## Lancer le script

```bash
source venv/bin/activate && python move_mouse.py
```

## Environnement

- Python 3.13
- Dépendance unique : `pyautogui` (installée dans `venv/`)
- macOS (utilise PyObjC en backend)

## Structure

```
move_mouse.py   # script principal
exec.txt        # commande de lancement tout-en-un
venv/           # environnement virtuel (ignoré par git)
```

## Conventions

- Pas de tests automatisés (script d'utilité simple)
- Pas de configuration externe, tout est hardcodé dans `move_mouse.py`
- Pour modifier le comportement : éditer directement `max_offset` ou `sleep_time` dans le script
