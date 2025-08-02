class GridWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.agents = []

    def add_agent(self, agent):
        if self.is_occupied(agent.x, agent.y):
            pass
        else:
            self.agents.append(agent)

    def is_occupied(self, x, y):
        for agent in self.agents:
            if agent.x == x and agent.y == y:
                return True
        return False

    def move_agent(self, agent, new_x, new_y):
        if not self.is_occupied(new_x, new_y):
            agent.x = new_x
            agent.y = new_y
        else:
            pass
