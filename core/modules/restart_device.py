import usb
from usb.core import *
from usb.util import *


# restart_device.py
# Date: 09/26/21
# Author: 0x1CA3


class RestartDevice:
    def __init__(self, dev):
        self.dev = dev

    def restart(self):
        device = self.dev
        device.ctrl_transfer(0x40, 0, 0, 0, 'setenv debug-uarts 3' + '\x00', 30000)
        device.ctrl_transfer(0x40, 0, 0, 0, 'saveenv' + '\x00', 30000)
        try:
            device.ctrl_transfer(0x40, 0, 0, 0, 'reboot' + '\x00', 30000)
        except usb.core.USBError:
            pass
        usb.util.dispose_resources(device)
        RestartDevice.restart()