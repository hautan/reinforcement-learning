import numpy as np

from model.agent import Agent
from model.environment import Environment

def play_game(p1: Agent, p2: Agent, env: Environment, draw=False):
    print("play game!")
    current_layer =None
    
    while not env.game_over():
        #alternate between players
        if current_layer == p1:
            current_layer = p2
        else:
            current_layer = p1
            
        if draw:
            env.draw_board()
            
        #make an action
        current_layer.take_action()
        
        #update state history
        state = env.get_state()
        p1.update_state_history(state)
        p2.update_state_history(state)
    
    if draw:
        env.draw_board()
        
    #do the value function update
    p1.update(env)
    p2.update(env)
    
def get_state_hash_and_winer(env: Environment, i = 0, j = 0):
    results = []
    
    for v in (0, env.x, env.o):
        env.board[i,j] = v #if empty board it should already be 0
        if j == 2:
            #j goes back to 0, incerease i, unless i = 2, then we are done
            if i == 2:
                state = env.get_state()
                ended = env.game_over(forece_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_hash_and_winer(env, i + 1, 0)
        else:
            results += get_state_hash_and_winer(env, i, j + 1)
            
    return results;

def initialV_o(env: Environment, state_winner_triplets):
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triplets:
        is ended:
            if winner == env.o:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V

def initialV_x(env: Environment, state_winner_triplets):
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triplets:
        is ended:
            if winner == env.x:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V
    
def generate_all_binary_numbers(N: int):
    results = []
    child_results = generate_all_binary_numbers(N-1)
    for prefix in ('0', '1'):
        for sufix in child_results:
            new_result = prefix + sufix
            results.append(new_result)
    return results

#def representing_states(Length):
#    k = 0
#    h = 0
#    for i in xrange(Length):
#        for j in xrange(Length):
#            if self.board[i,j] == 0:
#                v = 0
#                elif self.board[i,j] == self.x:
#                    v = 1
#                    elif self.board[i,j] == self.o:
#                        v = 2
#                    h += (3**k) *v
#                    k += 1
#    return h
        
        
        