import os
from fcntl import ioctl

WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

fd = os.open('/dev/mydev', os.O_RDWR)

class LedController:
    def set_green_leds(self, data):
        # data to write
        ioctl(fd, WR_GREEN_LEDS)
        retval = os.write(fd, data.to_bytes(4, 'little'))
        print("wrote %d bytes"%retval)
    
    def set_red_leds(self, data):
        # data to write
        ioctl(fd, WR_RED_LEDS)
        retval = os.write(fd, data.to_bytes(4, 'little'))
        print("wrote %d bytes"%retval)