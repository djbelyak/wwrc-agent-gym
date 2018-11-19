from environment import Environment
from agent import Agent

if __name__ == '__main__':
    env = Environment()
    agent = Agent(env)

    action = agent.forward(env.state)
    print(f'state: {env.state} action: {action}')
    env.action(action)
