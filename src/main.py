from utils.switches import SwitchController

switch_controller = SwitchController()

switch_array = switch_controller.get_switch_array()

print(switch_array)

switch_value = switch_controller.get_switch_value(2)

print(switch_value)