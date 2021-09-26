import usb
import usb.core


# battery.py
# Date: 09/26/21
# Author: 0x1CA3


class Battery:
    def __init__(self, dev):
        self.dev = dev

    def battery(self):
        device = self.dev
        for i in range(500):
            try:
                device.reset()
            except usb.core.USBError:
                pass