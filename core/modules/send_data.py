import usb
import usb.core


# send_data.py
# Date: 09/26/21
# Author: 0x1CA3


class SendData:
    def __init__(self, device, u_data):
        self.device = device
        self.u_data = u_data
        self.size = 0x800

    def send_data(self):
        i = 0
        dev = self.device
        data = self.u_data
        while i < len(data):
            total = min(len(data) - i, self.size)
            assert dev.ctrl_transfer(0x21, 1, 0, 0, data[i:i + total], 5000) == total
            i += total