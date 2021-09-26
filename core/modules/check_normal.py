import usb
import usb.core


# check_normal.py
# Date: 09/22/21
# Author: 0x1CA3


class Check_Normal:
    def check():
        device = usb.core.find(idVendor=0x5AC, idProduct=0x12a8)
        if device is None: print("Your iOS device is not connected!\n")
        else: print("Device is connected! [0x5AC, 0x12A8]\n")