# Decimal VendorID=1256 & ProductID=26720 

# Hexadecimal VendorID= 0x4e8 & 0x6860 


import usb.core
import usb.util

#finding phone
dev = usb.core.find(idVendor=0x4e8, idProduct=0x6860)

#if found
if dev is None:
    raise ValueError("Device is not found")


#checking version
mesg = dev.ctrl_transfer(0xc0, 51, 0,0,2)

#requesting audio
dev.ctrl_transfer(0x40, 0x3a, 1, 0, "")

#put device in accesory mode
dev.ctrl_transfer(0x40, 52, 0, 0, "")