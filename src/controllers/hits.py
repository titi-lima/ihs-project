class HitsController:
    def __init__(self, screen_controller):
        self.screen_controller = screen_controller

        self.history_1 = []
        self.history_2 = []
        pass

    def check_hits(self, switch_controller, target):
        print("Checking hits...")
        print(target[::-1])
        target = target[::-1]
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

        # Desenha o histórico de acertos
        for i in self.history_1:
            self.screen_controller.draw_circles(i)
        for i in self.history_2:
            self.screen_controller.draw_circles(i)

        # Update circles
        self.screen_controller.draw_circles(circles_1)
        self.screen_controller.draw_circles(circles_2)

        # Update history
        self.history_1.append(circles_1)
        self.history_2.append(circles_2)
        pass


