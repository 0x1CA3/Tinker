import usb
import usb.core


# check_recovery.py
# Date: 09/22/21
# Author: 0x1CA3


class Check_Recovery:
    def check():
        device = usb.core.find(idVendor=0x5AC, idProduct=0x1281)
        if device is None: print("Your iOS device is not connected in Recovery mode!\n")
        else: print("Device is connected in Recovery mode! [0x5AC, 0x1281]\n")