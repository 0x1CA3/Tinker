import subprocess
from core.handler import *
from core.modules.command import *
from core.modules.battery import *
from core.modules.send_data import *
from core.modules.file_transfer import *
from core.modules.restart_device import *


# shell.py
# Date: 09/22/21
# Author: 0x1CA3


class LoadRecoveryShell:
    def __init__(self):
        self.display = "iPhone [0x5AC, 0x1281] -> "
    
    def shell(self) -> None:
        try:
            dev = usb.core.find(idVendor=0x5AC, idProduct=0x1281)
            while True:
                command = input(f"{self.display}")
                if command == "exit": break
                elif command == "send-data":
                    data = input("\nEnter Data [0x5AC, 0x1281] -> ")
                    SendData(dev, data).send_data()
                elif command == "battery": Battery(dev).battery()
                elif command == "restart": RestartDevice(dev).restart()
                elif command == "command":
                    device_command = input("\nEnter Data [0x5AC, 0x1281] -> ")
                    SendCommand(dev, device_command).send_command()
                elif command == "file":
                    u_file = input("\nEnter Filename [0x5AC, 0x1281] -> ")
                    FileTransfer(dev, u_file).file_transfer()
                else: Handler(command).load_dfu_handler()
        except KeyboardInterrupt:
                print("\nMake sure to exit properly!\n")

class LoadDFUShell:
    def __init__(self):
        self.display = "iPhone [0x5AC, 0x1227] -> "
    
    def shell(self) -> None:
        try:
            dev = usb.core.find(idVendor=0x5AC, idProduct=0x1227)
            while True:
                command = input(f"{self.display}")
                if command == "exit": break
                elif command == "send-data":
                    data = input("\nEnter Data [0x5AC, 0x1227] -> ")
                    SendData(dev, data).send_data()
                elif command == "battery": Battery(dev).battery()
                elif command == "command":
                    device_command = input("\nEnter Data [0x5AC, 0x1227] -> ")
                    SendCommand(dev, device_command).send_command()
                elif command == "file":
                    u_file = input("\nEnter Filename [0x5AC, 0x1227] -> ")
                    FileTransfer(dev, u_file).file_transfer()
                else: Handler(command).load_dfu_handler()
        except KeyboardInterrupt:
                print("\nMake sure to exit properly!\n")

class LoadNormalShell:
    def __init__(self):
        self.display = "iPhone [0x5AC, 0x12A8] -> "
    
    def shell(self) -> None:
        dev = usb.core.find(idVendor=0x5AC, idProduct=0x12a8)
        while True:
            try:
                command = input(f"{self.display}")
                if command == "exit": break
                elif command == "send-data":
                    data = input("\nEnter Data [0x5AC, 0x12A8] -> ")
                    SendData(dev, data).send_data()
                elif command == "battery": Battery(dev).battery()
                elif command == "command":
                    device_command = input("\nEnter Data [0x5AC, 0x12A8] -> ")
                    SendCommand(dev, device_command).send_command()
                elif command == "file":
                    u_file = input("\nEnter Filename [0x5AC, 0x12A8] -> ")
                    FileTransfer(dev, u_file).file_transfer()
                else: Handler(command).load_normal_handler()
            except KeyboardInterrupt:
                print("\nMake sure to exit properly!\n")

class Shell:
    def __init__(self):
        self.display = "-> "

    def shell(self) -> None:
        while True:
            try:
                command = input(f"{self.display}")
                if command == "load-normal":
                    device = usb.core.find(idVendor=0x5AC, idProduct=0x12a8)
                    if device is None: print("Your iOS device is not connected!\n")
                    else: print("Use '?' for commands.\n"); LoadNormalShell().shell()
                elif command == "load-dfu":
                    dev = usb.core.find(idVendor=0x5AC, idProduct=0x1227)
                    if dev is None: print("Your iOS device is not connected in DFU mode!\n")
                    else: print("Use '?' for commands.\n"); LoadDFUShell().shell()
                elif command == "load-recovery":
                    device = usb.core.find(idVendor=0x5AC, idProduct=0x1281)
                    if device is None: print("Your iOS device is not connected!\n")
                    else: print("Use '?' for commands.\n"); LoadRecoveryShell().shell()
                elif "$" in command:
                    trimmed_command = command.replace("$", "")
                    subprocess.call(f"{trimmed_command}", shell=True)
                else: Handler(command).handler()
            except KeyboardInterrupt:
                print("\nUse the 'exit' command to exit the framework!\n")