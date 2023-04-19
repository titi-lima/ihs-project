import os
from fcntl import ioctl

RD_PBUTTONS = 24930
fd = os.open('/dev/mydev', os.O_RDWR)


class ButtonController:
    # Get button binary array
    def get_button_array():
        ioctl(fd, RD_PBUTTONS)
        red = os.read(fd, 4)  # read 4 bytes and store in red var
        return int.from_bytes(red, 'little')

    # Get individual button binary value
    def get_button_value(button):
        ioctl(fd, RD_PBUTTONS)
        red = os.read(fd, 4)  # read 4 bytes and store in red var
        print("red 0x%X" % int.from_bytes(red, 'little'))
        return (int.from_bytes(red, 'little') >> button) & 1
