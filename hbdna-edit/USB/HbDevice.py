import sys
import usb.core
import usb.util
import usb.control
import codecs

class HbDevice :
    '''
    This Class initiate USB connection with the DNAfx_git hardware device.
    It contains all usefull information to identify and use the device.

    Usage : my_hb_device = HbDevice()

    '''

    def __init__(self):

        self.HB_ID_VENDOR = 0x0483
        self.HB_ID_PRODUCT = 0x5703

        self.HB_PSET_IRQ2_INIT1 = '080000000000000000'
        self.HB_PSET_IRQ2_INIT2 = '08aa55020000001297'
        self.HB_IRQ_PSET_GET1 = '08aa55020031013412'
        self.HB_IRQ_PSET_GET2 = '08aa550200a0011fc8'
        self.HB_HIB_DT_SZ = 64

        self.dev = usb.core.find(idVendor=self.HB_ID_VENDOR, 
                                 idProduct=self.HB_ID_PRODUCT)
        print("Dev = ", self.dev)
        print(" Manufacturer :", self.dev.manufacturer)
        # self.dev.default_timeout = 0
        print ("timeout : ", self.dev.default_timeout)
        print(self.dev.serial_number)

        # Initiating USB connection

        if self.dev:

            self.if_num = self.dev[0].interfaces()[0].bInterfaceNumber
            if self.dev.is_kernel_driver_active(self.if_num):
                self.dev.detach_kernel_driver(self.if_num)
        self.dev.set_configuration()

        self.ep_it_in = self.dev[0].interfaces()[0].endpoints()[0]
        self.ep_it_out = self.dev[0].interfaces()[0].endpoints()[1]


    def get_device_presets(self):

        if self.dev :
            set = self.HB_IRQ_PSET_GET1.ljust(128,'0')
            print("set 1 : ",set)
            msg =  bytearray.fromhex(set)
            res = self.ep_it_out.write(msg)
            print("Res preset : res 1 = ", res)

            set = self.HB_IRQ_PSET_GET2.ljust(128,'0')
            msg= bytearray.fromhex(set)
            res = self.ep_it_out.write(msg)
            print("Res preset : res 2 = ", res)

    def read_device(self):
       if self.dev:
            for i in range(10):
                buff = self.ep_it_in.read(64)
                print(" From IRQ IN : ", buff)
    



if __name__ == '__main__':

    hbdna = HbDevice()
    hbdna.read_device()






        
 

