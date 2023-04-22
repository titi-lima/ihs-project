class HitsController:
    def __init__(self, screen_controller):
        self.screen_controller = screen_controller
        pass

    def check_hits(self, switch_controller, target):
        print("Checking hits...")
        print(target)
        # Get circles
        circles_1 = self.screen_controller.circles_1
        circles_2 = self.screen_controller.circles_2

        # Check hits for player 1
        for i in range(9):
            if switch_controller.get_switch_value(i) == target[i]:
                circles_1[i]['color'] = (0, 255, 0)
                self.screen_controller.hits_1 += 1
            else:
                circles_1[i]['color'] = (255, 0, 0)

        # Check hits for player 2
        for i in range(9):
            if switch_controller.get_switch_value(i + 9) == target[i]:
                circles_2[i]['color'] = (0, 255, 0)
                self.screen_controller.hits_2 += 1
            else:
                circles_2[i]['color'] = (255, 0, 0)

        # Update circles
        self.screen_controller.draw_circles(circles_1)
        self.screen_controller.draw_circles(circles_2)
        pass


