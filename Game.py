from State import State
from Action import Action
from MinMax import MinMax
from AlphaBeta import AlphaBeta
from Human import Human
from Smart import Smart
import sys
import time

sys.setrecursionlimit(5000)
init_state = State([9])

def play_game(algorithm1, algorithm2, n):
    state = State([n])
    algorithm1.set_player(1)
    algorithm2.set_player(2)
    while(not state.is_final()):
        print(state.to_string())
        if(state.is_player1()):
            action = algorithm1.choose_action(state)
            player_message = algorithm1.player_message()
        else:
            action = algorithm2.choose_action(state)
            player_message = algorithm2.player_message()
        print(f"\n{player_message}: {action.to_string()}")
        state = action.execute()
    print(state.to_string())
    if(state.is_player1()):
        print(algorithm2.winning_message())
        print(algorithm1.losing_message())
    else:
        print(algorithm1.winning_message())
        print(algorithm2.losing_message())

play_game(MinMax(), MinMax(), 10)
print("\n")