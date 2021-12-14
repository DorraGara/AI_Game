from State import State
from Action import Action
import time

class MinMax:
    def __init__(self) -> None:
        self.nb_nodes = 0
        self.is_player1 = True
        self.execution_time = 0

    def choose_action(self, state):
        start_time = time.time()
        #------------------------------------------------------------
        actions = state.generate_actions()
        max_value = float('-inf')
        max_action = actions[0]
        for action in actions:
            self.nb_nodes = self.nb_nodes + 1
            min_value = self.min_value(action.execute())
            if(max_value<min_value):
                max_value = min_value
                max_action = action
        #------------------------------------------------------------
        end_time = time.time()
        self.execution_time += (end_time - start_time)*1000
        return max_action

    def max_value(self, state):
        if (state.is_final()): return -1
        actions = state.generate_actions()
        max_value= float('-inf')
        for action in actions:
            self.nb_nodes = self.nb_nodes + 1            
            max_value = max(max_value,self.min_value(action.execute()))
        return max_value
        
    def min_value(self,state):
        if (state.is_final()): return 1
        actions = state.generate_actions()
        min_value= float('inf')
        for action in actions:
            self.nb_nodes = self.nb_nodes + 1
            min_value = min(min_value,self.max_value(action.execute()))
        return min_value
    
    def set_player(self, player_number):
        if(player_number==1):
            self.is_player1 = True
        else:
            self.is_player1 = False

    def losing_message(self):
        return f"\n{self.player_message()} Lost\nnumber of nodes visited: {self.nb_nodes}\ntotal decision making time: {int(self.execution_time)} ms"
    
    def winning_message(self):
        return f"\n{self.player_message()} Won!\nnumber of nodes visited: {self.nb_nodes}\ntotal decision making time: {int(self.execution_time)} ms"
    
    def player_message(self):
        if(self.is_player1):
            return "Player 1 [ MinMax ]"
        else:
            return "Player 2 [ MinMax ]"