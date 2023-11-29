import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        balls_drawn = []
        for i in range(num_balls):
            idx = random.randrange(len(self.contents))
            balls_drawn.append(self.contents.pop(idx))
        return balls_drawn
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for k, v in expected_balls.items():
        for i in range(v):
            expected_balls_list.append(k)
    num_success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for ball in expected_balls_list:
            if ball not in balls_drawn:
                success = False
                break
            balls_drawn.remove(ball)
        if success:
            num_success += 1
    return num_success / num_experiments