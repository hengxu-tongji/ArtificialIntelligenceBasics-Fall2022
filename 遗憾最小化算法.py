import numpy as np
from prettytable import PrettyTable
 
class Opponent:
    def __init__(self):
        # 对手采取石头，剪刀，布的概率
        self.probs = (1/3, 1/3, 1/3)
 
    def action(self):
        return np.random.choice(len(self.probs), 1, p=self.probs).item(0)
 
class Agent:
    def __init__(self):
        self.cum_regret = np.array([0.1, 0.1, 0.1])
 
    def action(self):
        # regret matching
        return np.argmin(self.cum_regret)
 
    def update_regret(self, action, regret):
        self.cum_regret[action] += regret
 
class Game:
    def __init__(self):
        self.payoff = [
            #石头  剪刀  布
            [0,   1,  -1], # 石头
            [-1,   0,  1], # 剪刀
            [1,   -1,  0]  # 布
          ]
 
    @property
    def best_payoff(self):
        return 1
 
    def play(self, agent_action, opponent_action):
        return self.payoff[agent_action][opponent_action]
 
game = Game()
opponet = Opponent()
agent = Agent()
table = PrettyTable(['round','opponent','agent', 'current round regret', 'cum_regret'])
for round in range(100):
    agent_action = agent.action()
    opponent_action = opponet.action()
    payoff = game.play(agent_action, opponent_action)
    regret = game.best_payoff - payoff
    agent.update_regret(agent_action, regret)
    table.add_row([round, opponent_action, agent_action, regret, str(agent.cum_regret)])
 
print(table)