# Introduction

## Qu'est-ce que Minetest ?

Minetest est un **clone** de Minecraft sous **licence open source**.

Dans le monde des logiciels, on parle de
*[clone](https://fr.wikipedia.org/wiki/Clone_%28informatique%29)*
lorsqu'on crée un nouveau logiciel tout en copiant les fonctionnalités d'un
autre logiciel. Dans notre cas, `minetest` à été reprogrammé complètement
tout en s'efforçant d'implémenter les mêmes fonctionnalités que Minecraft
au fil du temps.

:bell: TODO: license open source


## Vérification de notre installation

Tout d'abord nous allons vérifier que Python peut correctement communiquer
avec Minetest. Pour cela nous allons exécuter Minetest, sélectionner le
monde `coderdojo` et cliquer sur le bouton `Play Game`.

Une fois dans le jeu nous allons taper la commande suivante:

    /py hello

Cette commande va tenter d'exécuter le script `hello.py` qui se trouve dans
le répertoire de travail accessible via le raccourci `coderdojo-minetest`
que l'on peut trouver sur notre bureau.

![](https://i.imgur.com/BXrJUUR.png)

Si tout s'est bien passé nous devrions voir le texte *"Hello from CoderDojo"*
s'afficher en haut à gauche de la fenêtre de jeu.

![](https://i.imgur.com/0LTTqH5.png)

Si ce n'est pas le cas il faut revoir l'installation et s'assurer que les
[instructions ont été suivies à la lettre](https://github.com/amigrave/coderdojo-minetest#installation).


## Notre premier programme pour Minetest

Voici le code source du premier programme que nous venons d'exécuter en
tapant la commande `/py hello`:

```python
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Hello from CoderDojo !")
```

Les deux premières lignes sont nécessaires afin d'obtenir un objet python
qui est lié au monde Minetest que nous avons ouvert en jeu.

:exclamation: Afin de rester consistants, nous donnerons le nom `mc` à cet
objet dans tous nos programmes.

Une fois que nous avons cet objet, nous pouvons appeler ses méthodes afin
d'interagir avec le monde. La première méthode que nous allons apprendre est
donc `postToChat(message)`. Cette fonction prend un seul argument qui est le
message que l'on veut poster sur le *chat* du jeu. Essayons de modifier le
programme `hello.py` afin de changer le message affiché, exemple:

```python
mc.postToChat("Coucou !!!")
```

Pour exécuter notre programme nous avons deux options:

1. utiliser la commande `/py <nom_du_programme>` dans la fenêtre Minetest
2. exécuter le fichier python de manière traditionnelle, par exemple via
   le bouton `Run` de l'éditeur de code:

![](https://i.imgur.com/fqaZJQX.png)

## La 3D

:bell: TODO: notions 3D

## Création d'un nouveau monde

Pour créer un nouveau monde il suffit de cliquer sur le bouton ``New``, une
fois le nom du monde choisi on clique sur ``Create``

![Creation d'un nouveau monde](https://i.imgur.com/HIYGR2i.png)


ensuite il nous faudra cliquer sur `Configure` afin d'ouvrir la fenêtre de
configuration de notre nouveau mode

![](https://i.imgur.com/ZOgUM79.png)

dans cette fenêtre il nous faudra activer le module
[raspberryjammod](https://github.com/arpruss/raspberryjammod-minetest) en le
sélectionnant et en cliquant sur la case `enabled`, pour terminer nous
cliquerons sur le bouton `Save`.

![](https://i.imgur.com/wEQVweK.png)
