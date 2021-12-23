from State import State
from Action import Action
import time

class Smart:
    def __init__(self) -> None:
        self.nb_nodes = 0
        self.is_player1 = True
        self.execution_time = 0
        self.name = "Smart"

    def choose_action(self, state):
        start_time = time.time()
        #------------------------------------------------------------
        actions = state.generate_actions()
        max_value = float('-inf')
        max_action = None
        for action in actions:
            wins_action, loss_action = self.calculate_win_loss(action.execute())
            min_value = wins_action / (wins_action + loss_action)
            print(f"{(wins_action), (loss_action)} {min_value} {action.to_string()}")
            if(max_value<min_value):
                max_value = min_value
                max_action = action
        #------------------------------------------------------------
        end_time = time.time()
        self.execution_time += (end_time - start_time)*1000
        return max_action

    def calculate_win_loss(self, state):
        self.nb_nodes += 1
        if (state.is_final()): return self.utility(state)
        actions = state.generate_actions()
        #print("start calculate win loss\n")
        wins = 0
        loss = 0
        for action in actions:
            wins_action, loss_action = self.calculate_win_loss(action.execute())
            wins += wins_action
            loss += loss_action
            #print(f"{(wins_action, loss_action)} {(wins, loss)}")
        return (wins, loss)

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
            return "Player 1 [ Smart ]"
        else:
            return "Player 2 [ Smart ]"

    def utility(self, state):
        if(state.is_player1()!=self.is_player1):
            #won
            return (1,0)
        else:
            #lost
            return (0,1)