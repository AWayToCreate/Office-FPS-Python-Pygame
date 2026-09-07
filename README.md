# 🎮 Office FPS — Python & Pygame

## 📌 Présentation

Ce projet est un jeu FPS en vue subjective développé en Python avec la bibliothèque Pygame.

L'objectif était de créer un petit environnement 3D dans lequel le joueur peut se déplacer, regarder autour de lui et interagir avec différents éléments du décor.

Le rendu 3D est réalisé à l'aide d'une technique de **ray casting**, permettant de simuler une vue en trois dimensions à partir d'une carte 2D.

## 🛠️ Technologies utilisées

- Python
- Pygame
- Ray casting
- Mathématiques / trigonométrie

## 🎯 Fonctionnalités

- Déplacement du joueur
- Rotation de la caméra avec la souris
- Rendu 3D des murs
- Mini-carte
- Porte interactive
- Ordinateur interactif
- Système de lunettes
- Interface simulant un système de fichiers
- Gestion des collisions

## 🧠 Fonctionnement

Le jeu utilise une carte 2D composée de différentes cases :

- `W` : mur
- `D` : porte
- `C` : ordinateur
- `0` : espace libre

Le moteur lance plusieurs rayons depuis la position du joueur afin de détecter les éléments présents devant lui.

La distance entre le joueur et les objets détectés permet ensuite de calculer leur hauteur à l'écran et de produire l'impression de profondeur.

Le programme utilise actuellement **120 rayons par image** pour construire le rendu 3D.

## 🎮 Commandes

| Touche | Action |
|--------|--------|
| `Z` | Avancer |
| `S` | Reculer |
| `Q` | Déplacement à gauche |
| `D` | Déplacement à droite |
| Souris | Regarder autour de soi |
| `E` | Interagir |
| `L` | Activer / désactiver les lunettes |
| `↑ / ↓` | Naviguer dans les fichiers |
| `Échap` | Fermer une interface / quitter |

## 📂 Structure du projet

```text
fps-pygame/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
