from app.grid import GridWorld
from app.agent import Agent

def run():
    grid = GridWorld(10, 10)

    # Add agents
    for i in range(5):
        # TODO: random positions, avoid overlap
        agent = Agent(i, x=..., y=...)
        grid.add_agent(agent)

    for step in range(100):
        for agent in grid.agents:
            agent.step(grid)
        # TODO: Add visualization or print state

if __name__ == "__main__":
    run()
