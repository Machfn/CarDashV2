# Hexadecimal VendorID= 0x4e8 & 0x6860 
import usb.core
import usb.util
import sys
import time
import os
import logging

VID_GALAXY_NEXUS_DEBUG = 0x04e8
PID_GALAXY_NEXUS_DEBUG = 0x6860

VID_ANDROID_ACCESSORY = 0x18d1
PID_ANDROID_ACCESSORY = 0x2d01

def get_accessory():
    print("Looking for Phone")
    print("VID: 0x%0.4x - PID: 0x%0.4x" % (VID_GALAXY_NEXUS_DEBUG, PID_GALAXY_NEXUS_DEBUG))
    dev = usb.core.find(idVendor=VID_GALAXY_NEXUS_DEBUG, idProduct=PID_GALAXY_NEXUS_DEBUG)
    return dev

def set_protocol(ldev):
    try:
        ldev.set_configuration()
    except usb.core.USBError as e:
        if e.errno == 16:
            print('Device already configured, should be OK')
        else:
            sys.exit("Configuratino failed")
    ret = ldev.ctrl_transfer(0xC0, 51, 0, 0, 2)
    # dunno how to translate: array ('B', [2, 0])
    protocol = ret[0]
    print('Protocol version: %i' % protocol)
    if protocol < 2:
        sys.exit('Android Open Accessory v2 not supported')
    return


# this should be the same as the res/xml/accessory_filter.xml
def set_strings(ldev):
    send_string(ldev, 0, "_ArnO_")
    send_string(ldev, 1, "PyAndroidAccessory")
    send_string(ldev, 2, "A Python based Android accessory")
    send_string(ldev, 3, "0.1.0")
    send_string(ldev, 4, "http://zombiebrainzhuice.cc/py-android-accessory/")
    send_string(ldev, 5, "2254711SerialNo.")
    return


def send_string(ldev, str_id, str_val):
    ret = ldev.ctrl_transfer(0x40, 52, 0, str_id, str_val, 0)
    if ret != len(str_val):
        sys.exit('Failed to send string %i' % str_id)
    return


def set_accessory_mode(ldev):
    ret = ldev.ctrl_transfer(0x40, 52, 0, 0, '', 0)
    if ret:
        sys.exit('Start-up failed')
    time.sleep(1)
    return


def getAudio(ldev):
    # os.environ['']
    # logger = logging.getLogger(__name__)

    # ldev.ctrl_transfer(0xc0, 51, 0, 0, 2)
    set_protocol(ldev)
    #requestion audio
    ldev.ctrl_transfer(0x40, 0x3a, 1, 0, "")

    #pu tdevice in to accesory info 
    set_accessory_mode(ldev)



getAudio(get_accessory())
    



# def set_host_mode(ldev):
#     ret = ldev.ctrl_transfer(0x40, 52, 0, 0, '', 0)
#     if ret:
#         sys.exit("Start-up failed")
#     time.sleep(1)
#     return