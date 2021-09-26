import usb
import usb.core


# check_dfu.py
# Date: 09/22/21
# Author: 0x1CA3


class Check_DFU:
    def check():
        dev = usb.core.find(idVendor=0x5AC, idProduct=0x1227)
        if dev is None: print("Your iOS device is not connected in DFU mode!\n")
        else: print("Device is connected in DFU mode! [0x5AC, 0x1227]\n")