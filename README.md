# CoderDojo Minetest

## Introduction

Ce repository contient tout le materiel necessaire pour les
ateliers CoderDojo minetest.

[Le cours se trouve ici](https://amigrave.github.io/coderdojo-minetest)

## Installation

### Linux

```
sudo apt install -y minetest lua-socket
pip3 install --user --upgrade coderdojo-minetest
```

:bell: TODO:
- [ ] copy mod + world + hello.py
- [ ] ln -s ~/.minetest/mods/raspberryjammod/coderdojo ~/Desktop/coderdojo-minetest

# Windows

- Install python3
- Install coderdojo-minetest module

    pip3 install --user --upgrade coderdojo-minetest

- Unzip the release file somewhere
- Shortcut `<minetest>/mods/raspberryjammod/coderdojo` -> `<Desktop>/coderdojo-minetest`
- Launch minetest `bin/minetest.exe`


## :bell: TODO

Single installer for all OSes/distros (not working yet)

```
curl -s https://raw.githubusercontent.com/amigrave/coderdojo-minetest/master/install.py | python
```
