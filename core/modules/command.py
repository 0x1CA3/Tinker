import usb
from usb.core import *
from usb.util import *


# command.py
# Date: 09/26/21
# Author: 0x1CA3


class SendCommand:
    def __init__(self, dev, device_command):
        self.dev = dev
        self.device_command = device_command

    def send_command(self):
        device = self.dev
        device.ctrl_transfer(0x40, 0, 0, 0, self.device_command + '\x00', 30000)
        usb.util.dispose_resources(device)