from core.help import *
from core.clear import *
from core.shell import *
from core.modules.battery import *
from core.modules.check_dfu import *
from core.modules.send_data import *
from core.modules.check_dfu import *
from core.modules.check_normal import *
from core.modules.check_recovery import *


# commands.py
# Date: 09/22/21
# Author: 0x1CA3


load_recovery_commands = {
    "?": HelpMenu.load_recovery_help_menu,
    "help": HelpMenu.load_recovery_help_menu,
    "clear": clear_screen,
}

load_dfu_commands = {
    "?": HelpMenu.load_dfu_help_menu,
    "help": HelpMenu.load_dfu_help_menu,
    "clear": clear_screen,
}

load_normal_commands = {
    "?": HelpMenu.load_normal_help_menu,
    "help": HelpMenu.load_normal_help_menu,
    "clear": clear_screen,
}

commands = {
    "?": HelpMenu.help_commands,
    "help": HelpMenu.help_commands,
    "tinker-help": HelpMenu.tinker_help,
    "device-help": HelpMenu.device_help,
    "check-dfu": Check_DFU.check,
    "check-normal": Check_Normal.check,
    "check-recovery": Check_Recovery.check,
    "clear": clear_screen,
    "exit": exit
}