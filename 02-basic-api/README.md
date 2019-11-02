# Les fonctions de base

Pour cet atelier nous allons nous limiter à quelques fonctions de bases que
nous propose Minetest. Nous ne nous attarderons pas non plus sur certains
paramètres optionnels que peuvent offrir ces fonctions.

**Note:** en informatique, la liste des fonctions, méthodes, classes ... exposées par
un programme
[se nomme API](https://fr.wikipedia.org/wiki/Interface_de_programmation),
nous utiliserons ce terme a partir de maintenant.

## .postToChat(message)

Affiche un message dans le *chat* du jeu.

```python
from mcpi import minecraft
mc = minecraft.Minecraft.create()

mc.postToChat("Salut tout le monde!")
```

Nous avons déjà vu cette fonction dans l'introduction donc nous ne attarderons
pas dessus.


## .setBlock(x, y, z, id)

Place un bloc aux coordonnées X, Y et Z.
Le paramètre `id` doit contenir le type de bloc que l'on veut créer. La liste
complète des types des blocs
[se trouve ici](https://github.com/amigrave/coderdojo-minetest/blob/6451bc3/mcpi/block.py#L43)
en voici quelques uns:

- `AIR` (de l'air, du vide)
- `STONE` (pierre)
- `GRASS` (herbe)
- `WATER` (eau)
- `WOOD` (bois)
- `GLASS` (verre)
- `ICE` (glace)


```python
from mcpi import block, minecraft
mc = minecraft.Minecraft.create()

mc.setBlock(0, 25, 0, block.BRICK_BLOCK)
```

Essayons maintenant de créer un fichier `test.py` dans le même répertoire que
`hello.py` avec le contenu ci-dessus. Exécutons le en utilisant la commande

    /py test

et regardons au dessus de notre tète (dans Minetest évidemment !)

