import os
import platform
import sys

# TODO: check if we are running python2, in such case re-exec python3

def launch(cmd, sudo=False):
    if sudo and os.geteuid() != 0:
        cmd = f"sudo {cmd}"
    print(f"[cmd] {cmd}")
    os.system(cmd)

system = platform.system()
dist = platform.dist()

if not (system == "Linux" and dist[0].lower() in ("ubuntu", "debian")):
    sys.exit("Unsupported system")

launch("apt install -y minetest lua-socket", sudo=True)
launch("pip3 install --user --upgrade coderdojo-minetest mu-editor")
launch("mkdir -p ~/.minetest")

data_url = "https://github.com/amigrave/coderdojo-minetest/releases/download/0.0.1/coderdojo-minetest-data.tgz"
launch(f"curl -L {data_url} | tar zx -C ~/.minetest")

launch("ln -s ~/.minetest/mods/raspberryjammod/coderdojo ~/Desktop/coderdojo-minetest")
