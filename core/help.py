from terminaltables import *


# help.py
# Date: 09/22/21
# Author: 0x1CA3


class HelpMenu:
    def help_commands():
        help_menu = [
            ['Command', 'Description', 'Usage'],
            ['help', 'Displays the available commands', 'help'],
            ['tinker-help', 'Displays commands to connect with a device for tinkering [Device must be connected]', 'tinker-help'],
            ['device-help', 'Displays commands for checking if a device is connected', 'device-help'],
            ['$', 'Lets you execute a system command', '$ [command]'],
            ['clear', 'Clears the screen', 'clear'],
            ['exit', 'Exits the Framework', 'exit'],
            ]
        hmenu = SingleTable(help_menu)
        print(f"{hmenu.table}\n")
    
    def device_help():
        help_menu = [
            ['Command', 'Description', 'Usage'],
            ['check-dfu', 'Checks if a device is connected in DFU mode', 'check-dfu'],
            ['check-normal', 'Checks if a device is connected in normal mode', 'check-normal'],
            ['check-recovery', 'Checks if a device is connected in recovery mode', 'check-recovery'],
            ]
        hmenu = SingleTable(help_menu)
        print(f"{hmenu.table}\n")

    def tinker_help():
        help_menu = [
            ['Command', 'Description', 'Usage'],
            ['load-dfu', 'Loads the device and lets you tinker with it', 'load-dfu'],
            ['load-normal', 'Loads the device and lets you tinker with it', 'load-normal'],
            ['load-recovery', 'Loads the device and lets you tinker with it', 'load-recovery'],
            ]
        hmenu = SingleTable(help_menu)
        print(f"{hmenu.table}\n")

    def load_normal_help_menu():
        help_menu = [
            ['Command', 'Description', 'Usage'],
            ['?', 'Displays the available commands', '?'],
            ['file', 'Attempts to send a file to the device', 'file'],
            ['send-data', 'Lets you send data to the device', 'send-data'],
            ['command', 'Attempts to send a command to the device', 'command'],
            ['battery', 'Makes the Battery go crazy', 'battery'],
            ['clear', 'Clears the screen', 'clear'],
            ['exit', 'Goes back to the main menu', 'exit'],
            ]
        hmenu = SingleTable(help_menu)
        print(f"{hmenu.table}\n")

    def load_dfu_help_menu():
        help_menu = [
            ['Command', 'Description', 'Usage'],
            ['?', 'Displays the available commands', '?'],
            ['file', 'Attempts to send a file to the device', 'file'],
            ['send-data', 'Lets you send data to the device', 'send-data'],
            ['command', 'Attempts to send a command to the device', 'command'],
            ['battery', 'Makes the Battery go crazy', 'battery'],
            ['clear', 'Clears the screen', 'clear'],
            ['exit', 'Goes back to the main menu', 'exit'],
            ]
        hmenu = SingleTable(help_menu)
        print(f"{hmenu.table}\n")

    def load_recovery_help_menu():
        help_menu = [
            ['Command', 'Description', 'Usage'],
            ['?', 'Displays the available commands', '?'],
            ['file', 'Attempts to send a file to the device', 'file'],
            ['send-data', 'Lets you send data to the device', 'send-data'],
            ['command', 'Attempts to send a command to the device', 'command'],
            ['battery', 'Makes the Battery go crazy', 'battery'],
            ['restart', 'Attempts to restart the device', 'restart'],
            ['clear', 'Clears the screen', 'clear'],
            ['exit', 'Goes back to the main menu', 'exit'],
            ]
        hmenu = SingleTable(help_menu)
        print(f"{hmenu.table}\n")