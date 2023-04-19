import os
from fcntl import ioctl

RD_SWITCHES   = 24929
fd = os.open('/dev/mydev', os.O_RDWR)


class SwitchController:
    # Get switch binary array
    def get_switch_array(self):
        ioctl(fd, RD_SWITCHES)
        red = os.read(fd, 4)  # read 4 bytes and store in red var
        return "{0:b}".format(int.from_bytes(red, 'little')).zfill(18)

    # Get individual switch binary value
    def get_switch_value(self, switch):
        ioctl(fd, RD_SWITCHES)
        red = os.read(fd, 4)  # read 4 bytes and store in red var
        return (int.from_bytes(red, 'little') >> switch) & 1
