import usb
from usb.core import *
from usb.util import *


# file_transfer.py
# Date: 09/26/21
# Author: 0x1CA3


class FileTransfer:
    def __init__(self, dev, u_file):
        self.dev = dev
        self.u_file = u_file
        self.size = 0x3000

    def file_transfer(self):
        i = 0
        device = self.dev
        with open(self.u_file) as t_file:
            lines = t_file.read()
        while i < len(lines):
            total = min(len(lines) - i, self.size)
            assert device.ctrl_transfer(0x21, 1, 0, 0, lines[i:i + total], 5000) == total
            i += total