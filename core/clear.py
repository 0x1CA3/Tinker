import platform
import subprocess


# clear.py
# Date: 09/22/21
# Author: 0x1CA3


clear_screen = lambda: subprocess.call("clear" if "Linux" in platform.platform() else "cls", shell=True)