import os
from fcntl import ioctl

WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932

fd = os.open('/dev/mydev', os.O_RDWR)

HEX_0 = '40'
HEX_1 = '79'
HEX_2 = '24'
HEX_3 = '30'
HEX_4 = '19'
HEX_5 = '12'
HEX_6 = '02'
HEX_7 = '78'
HEX_8 = '00'
HEX_9 = '04'

HEXES = [HEX_0, HEX_1, HEX_2, HEX_3, HEX_4, HEX_5, HEX_6, HEX_7, HEX_8, HEX_9]

class DisplayController:
    # Get switch binary array
    def set_right_display(self):
        # data to write
        data = 0x01020330;
        ioctl(fd, WR_R_DISPLAY)
        retval = os.write(fd, data.to_bytes(4, 'little'))
        print("wrote %d bytes"%retval)
    
    def set_right_display_number(self, number):
        #
        data = 0x40404040
        number_3 = int(number/100)
        number_2 = int((number-number_3*100)/10)
        number_1 = int((number-number_3*100-number_2*10))
        if number > 99:
            data = data - int('40', 16) * (16**(2*2))
            data = data + int(HEXES[number_3], 16) * (16**(2*2))
        if number > 9:
            data = data - int('40', 16) * (16**(1*2))
            data = data + int(HEXES[number_2], 16) * (16**(1*2))
        data = data - int('40', 16) * (16**(0*2))
        data = data + int(HEXES[number_1], 16) * (16**(0*2))
        
        ioctl(fd, WR_R_DISPLAY)
        retval = os.write(fd, data.to_bytes(4, 'little'))
        print("wrote %d bytes"%retval)

trier = DisplayController()
trier.set_right_display()
trier.set_right_display_number(6)