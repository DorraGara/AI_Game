from State import State
from Action import Action
import time

class Human:
    def __init__(self) -> None:
        self.nb_nodes = 0
        self.is_player1 = True
        self.execution_time = 0
        self.name = "Human"

    def choose_action(self, state):
        start_time = time.time()
        #------------------------------------------------------------
        print(self.player_message())
        while(True):
            index = int(input(f"please enter an index [0, {state.taille-1}]: "))
            if(index < 0 or index >= state.taille):
                print("index out of range\n")
                continue
            partition = int(input(f"partition {state.array[index]} into: "))
            if(partition<1 or partition > state.array[index]-1 or partition == state.array[index]-partition):
                print("invalid partition\n")
                continue
            remainder = state.array[index]-partition
            action = Action(state,index,partition,remainder)
            if (action.verify()):
                break
            else:
                print("Invalid input!")
        #------------------------------------------------------------
        end_time = time.time()
        self.execution_time += (end_time - start_time)*1000
        return action
    
    def set_player(self, player_number):
        if(player_number==1):
            self.is_player1 = True
        else:
            self.is_player1 = False

    def losing_message(self):
        return f"\n{self.player_message()} Lost\nnumber of nodes visited: --\ntotal decision making time: {int(self.execution_time)} ms"
    
    def winning_message(self):
        return f"\n{self.player_message()} Won!\nnumber of nodes visited: --\ntotal decision making time: {int(self.execution_time)} ms"
    
    def player_message(self):
        if(self.is_player1):
            return "Player 1 [ Human ]"
        else:
            return "Player 2 [ Human ]"