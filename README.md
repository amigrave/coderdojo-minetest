# CoderDojo Minetest

## Introduction

Ce repository contient tout le materiel necessaire pour les
ateliers CoderDojo minetest.

[Le cours se trouve ici](https://amigrave.github.io/coderdojo-minetest)

## Installation

### Linux

```
wget -O - https://raw.githubusercontent.com/amigrave/coderdojo-minetest/master/install.py | python3
```
<details>
    <summary>Command details</summary>
```
sudo apt install -y minetest lua-socket curl
pip3 install --user --upgrade coderdojo-minetest mu-editor
mkdir -p ~/.minetest
curl -L https://github.com/amigrave/coderdojo-minetest/releases/download/0.0.1/coderdojo-minetest-data.tgz | tar zx -C ~/.minetest
ln -s ~/.minetest/mods/raspberryjammod/coderdojo ~/Desktop/coderdojo-minetest
```
</details>

### Windows

- Install python3
- Install coderdojo-minetest module

    pip3 install --user --upgrade coderdojo-minetest

- Unzip the [release file](https://github.com/amigrave/coderdojo-minetest/releases/download/0.0.1/minetest-0.4.16-coderdojo.zip) in the user dir
- Add shortcut `<minetest>/mods/raspberryjammod/coderdojo` -> `<Desktop>/coderdojo-minetest`
- Add `bin/minetest.exe` shortcut to desktop

**Note:** on some setups the Microsoft Visual C++ 2010 might need to be reinstalled:

https://download.microsoft.com/download/5/B/C/5BC5DBB3-652D-4DCE-B14A-475AB85EEF6E/vcredist_x86.exe
