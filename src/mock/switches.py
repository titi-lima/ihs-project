class SwitchController:
    switch_array = "000000001000000110"
    
    def __init__(self, switch_array):
        self.switch_array = switch_array
    
    # Get switch binary array
    def get_switch_array(self):
        return self.switch_array
    
    def get_switch_number_1(self):
        switch = self.get_switch_array()[0:9]
        return int(switch, 2)
    
    def get_switch_number_2(self):
        switch = self.get_switch_array()[9:18]
        return int(switch, 2)

    # Get individual switch binary value
    def get_switch_value(self, switch):
        return self.switch_array[switch]
    
    def set_switch_array_value(self, value):
        self.switch_array = value
        return 1