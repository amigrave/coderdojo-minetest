import os
import platform
import sys

# TODO: check if we are running python2, in such case re-exec python3

def launch(cmd, sudo=False):
    if sudo and os.geteuid() != 0:
        cmd = "sudo %s" % cmd
    print("[cmd] %s" % cmd)
    os.system(cmd)

system = platform.system()
dist = platform.dist()

if not (system == "Linux" and dist[0].lower() in ("ubuntu", "debian")):
    sys.exit("Unsupported system")

launch("apt install -y minetest lua-socket curl", sudo=True)
launch("pip3 install --user --upgrade coderdojo-minetest")
launch("pip3 install --user mu-editor")
launch("mkdir -p ~/.minetest")

data_url = "https://github.com/amigrave/coderdojo-minetest/releases/download/0.0.1/coderdojo-minetest-data.tgz"
launch("curl -L %s | tar zx -C ~/.minetest" % data_url)

launch("ln -s ~/.minetest/mods/raspberryjammod/coderdojo ~/Desktop/coderdojo-minetest")
