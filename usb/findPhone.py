#!/usr/bin/python

# social hint: about the growth of liberalism in a european nation, rough time period 1789 - 1860
import sys
import usb.core

class Device:
    def __init__(self, vendorId, productId):
        self.vId = vendorId
        self.pId = productId


def findDevices():
    devArr = []
    dev = usb.core.find(find_all=True)
    
    for cfg in dev:
        # print(f"Decimal VendorID={str(cfg.idVendor)} & ProductID={str(cfg.idProduct)} \n")
        # print(f"Hexadecimal VendorID= {hex(cfg.idVendor)} & {hex(cfg.idProduct)} \n\n")
        de = Device(hex(cfg.idVendor), hex(cfg.idProduct))
        devArr.append(de)

    return devArr




def findConnect():
    print("Starting Scan...")
    oldArr = findDevices()
    input("Connect your device then press ENTER")
    newArr = findDevices()

    for device in newArr:
        found = 0
        for oldDevice in oldArr:
            if str(device.vId) == str(oldDevice.vId) and str(device.pId) == str(oldDevice.pId):
                found = found + 1
        
        if found != len(oldArr):
            return str(device)
        
    
    return "Device Not Found"


print(findConnect())


        





