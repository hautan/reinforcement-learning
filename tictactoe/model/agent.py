from model.environment import Environment
class Agent:
  def __init__(self):
    print("Bandit init!")
    self.state = None    
    
  def take_action(self):
    print("Take action!")
    
  def update_state_history(self, state):
    print("update_state_history!")
    self.state = state 
    
  def update(self, env: Environment):
    print("do the value function update!")
    