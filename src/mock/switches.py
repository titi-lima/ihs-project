class SwitchController:
    # Get switch binary array
    def get_switch_array(self):
        return "000000001000000110"
    
    def get_switch_number_1(self):
        switch = self.get_switch_array()[0:9]
        return int(switch, 2)
    
    def get_switch_number_2(self):
        switch = self.get_switch_array()[9:18]
        return int(switch, 2)

    # Get individual switch binary value
    def get_switch_value(self, switch):
        return 1