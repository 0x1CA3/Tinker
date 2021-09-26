import subprocess
from core.commands import *


# handler.py
# Date: 09/22/21
# Author: 0x1CA3


class Handler:
    def __init__(self, command):
        self.command = command

    def handler(self):
        if self.command in commands: commands[self.command]()
        else: print(f"Error, command [{self.command}] was not found.")

    def load_normal_handler(self):
        if self.command in load_normal_commands: load_normal_commands[self.command]()
        else: print(f"Error, command [{self.command}] was not found.")

    def load_dfu_handler(self):
        if self.command in load_dfu_commands: load_dfu_commands[self.command]()
        else: print(f"Error, command [{self.command}] was not found.")

    def load_recovery_handler(self):
        if self.command in load_recovery_commands: load_recovery_commands[self.command]()
        else: print(f"Error, command [{self.command}] was not found.")