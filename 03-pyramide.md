# Pyramide

Maintenant que nous avons un script pour réinitialiser notre aire de travail
nous allons tenter de construire une pyramide par essai et erreur.
Nous ajouterons donc notre ligne qui efface notre espace de travail au début
du programme histoire de nous faciliter la vie.

## Essai #1

Durant les Dojos précédents nous avons utilise les boucles. Par exemple pour
exécuter un bout de code 5 fois, nous pouvons utiliser ceci:

```python
for i in range(5):
    print(i)
```

Ce qui nous donne:

```
0
1
2
3
4
```

Nous allons faire un premier essai pour notre pyramide et nous allons écrire le
code suivant dans le fichier `pyramide.py`:

```python
from mcpi import block, minecraft
mc = minecraft.Minecraft.create()

mc.setBlocks(-50, 0, -50, 50, 50, 50, block.AIR)

hauteur = 10

for i in range(hauteur):
    x1 = i
    y1 = i
    z1 = i

    x2 = x1 + hauteur
    y2 = y1
    z2 = z1 + hauteur

    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.SAND)
```

Observons le résultat...
Bon, c'est intéressant ! ... Mais ce n'est pas ce que l'on veut.
La première chose que l'on peut constater est que chaque palier de notre
pyramide devrait voir sa taille diminuer au fur et à mesure que la pyramide
prend de la hauteur.

## Essai #2

```python
for i in range(hauteur):
    x1 = i
    y1 = i
    z1 = i

    x2 = x1 + (hauteur - i)
    y2 = y1
    z2 = z1 + (hauteur - i)

    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.SAND)```
```

Faisons le tour de notre édifice...
Bon cela commence à ressembler à une demi pyramide. Il apparait clairement que
notre base devrait avoir des cotés deux fois plus grands, ... ainsi que le
deuxième palier, ainsi que le troisième, ...

## Essai #3

```python
for i in range(hauteur):
    x1 = i
    y1 = i
    z1 = i

    x2 = x1 + (hauteur * 2 - i)
    y2 = y1
    z2 = z1 + (hauteur * 2 - i)

    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.SAND)```
```

Nous y sommes presque. Il faudrait juste que les paliers s'arrêtent plus tôt
à chaque itération. Pour le palier correspondant à `i == 1` on devrait
soustraire un bloc à `x2` et `z2`. Pour le palier correspondant à `i == 2` on
devrait soustraire deux blocs a `x2` et `z2`, ...

## Essai #4

```python
for i in range(hauteur):
    x1 = i
    y1 = i
    z1 = i

    x2 = x1 + (hauteur * 2 - i * 2)
    y2 = y1
    z2 = z1 + (hauteur * 2 - i * 2)

    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.SAND)
```

AH ! Ca y est ! Voilà notre pyramide !
Par contre notre pyramide a un défaut. Essayons de l'examiner pour trouver ce
qui cloche...

## Essai #5

L'anomalie que l'on a détecte dans notre pyramide est causée par le fait que
sa base est trop grande de 2 blocs. Nous allons y remédier.


```python
for i in range(hauteur):
    x1 = i
    y1 = i
    z1 = i

    x2 = x1 + (hauteur * 2 - i * 2 - 2)
    y2 = y1
    z2 = z1 + (hauteur * 2 - i * 2 - 2)

    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.SAND)
```

🎺🎺🎺 Et voilà ! 🎉🎉🎉

## Passage de paramètre

Maintenant que nous avons un script pour construire des pyramides on peut
l'appeler facilement dans Minetest en tapant la commande

    /py pyramide

Nous aimerions cependant pouvoir faire des pyramides de tailles différentes.
Lorsqu'on ajoute quelque chose après le nom du programme on peut récupérer
cette information sous forme de paramètres. Donc lorsque l'on utilise ceci:

    /py pyramide 5

Notre programme pourrait accéder à ce paramètre et l'utiliser pour réagir
différemment. Voici comment faire:

```python
import sys
hauteur = int(sys.argv[1])
```

Nous pouvons même demander à python d'essayer de lire le paramètre, mais
d'utiliser une valeur par défaut s'il n'y arrive pas. Par exemple dans le cas
où nous aurions fourni un nombre invalide ou si nous aurions tout simplement
oublié de passer un paramètre:

```python
try:
    hauteur = int(sys.argv[1])
except Exception:
    hauteur = 10
```

## Exercice #1

Il est fortement déconseillé d'utiliser un paramètre trop grand pour la taille
de la pyramide autrement ton ordinateur pourrait carrément planter !

Essaie de modifier ton programme `pyramide.py` afin d'empêcher que l'on donne
une taille plus grande que 20.

Pour cela tu auras besoin d'utiliser les conditions comme nous l'avons fait
durant les Dojos précédents, tu te rappelle probablement avoir utilisé les
`if`, `elif` et `else`, voici un exemple pour te mettre sur la piste:

```python
if hauteur == 100:
    mc.postToChat("Mais vous êtes fou ?")
```

## Exercice #2

Nous aimerions maintenant que notre pyramide se compose de matériaux différents
un palier sur deux. Le premier palier devrait être en sable (`block.SAND`) le
deuxième en pierre (`block.STONE`) le troisième en sable, le quatrième en
pierre, ...

Pour cela tu auras également besoin d'un opérateur qui permet de connaitre le
reste d'une division entière. Cet opérateur est le modulo et en Python on
l'exprime comme ceci: `%`

Nous savons que lorsqu'on fait une divise entière de 4 par 2, le résultat est
2 et il n'y a pas de reste. Une division entière de 5 par 2 nous donne un
résultat de 2 avec un reste de 1.

Voici la même chose exprimée en Python:

```python
>>> 4 % 2
0  # il n'y a pas de reste

>>> 5 % 2
1  # le reste de la division entiere est egal a 1
```

Tu auras compris que cela nous permet de savoir si un nombre est pair ou
impair. C'est un fameux indice pour résoudre l'exercice !

N'hésite pas a te faire aider par un coach si tu ne trouves pas la solution !


[⬅️ Retour au sommaire](./README.md)
