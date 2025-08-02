import random
from app.grid import GridWorld

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def step(self, grid, direction):
        if direction == 'up':
            grid.move_agent(self.id, self.x, self.y - 1)
        elif direction == 'down':
            grid.move_agent(self.id, self.x, self.y + 1)
        elif direction == 'left':
            grid.move_agent(self.id, self.x - 1, self.y)
        elif direction == 'right':
            grid.move_agent(self.id, self.x + 1, self.y)
        pass
    def random_move(self, grid):
        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)
        self.step(grid, direction)