import os
import platform
import sys

# TODO: check if we are running python2, in such case re-exec python3

system = platform.system()
dist = platform.dist()

if not (system == "Linux" and dist[0].lower() in ("ubuntu", "debian")):
    sys.exit("Unsupported system")

cmd = "apt install -y minetest lua-socket"
if os.geteuid() != 0:
    cmd = f"sudo {cmd}"
print(f"[Installing] {cmd}")
os.system(cmd)
