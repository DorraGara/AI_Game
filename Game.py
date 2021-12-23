from State import State
from Action import Action
from MinMax import MinMax
from AlphaBeta import AlphaBeta
from Human import Human
from Smart import Smart
from Fastest import Fastest
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
        return False
    else:
        print(algorithm1.winning_message())
        print(algorithm2.losing_message())
        return True


def statistics(algorithmType, opponentsList, min_n, max_n):
    test_number = 0
    wins = 0
    result = []
    for index in range(0, max_n - min_n + 1):
        depth = index + min_n
        for opponent in opponentsList:
            player = algorithmType()
            did_win = play_game(player, opponent, depth)
            if(did_win):
                wins+=1
            else:
                pass
            result.append({
                "algorithm":player.name,
                "opponent":opponent.name,
                "nodes_visited":player.nb_nodes,
                "execution_time":player.execution_time,
                "did_win":did_win,
                "depth":depth
            })
            test_number+=1
    print("[")
    for value in result:
        print(f"  {value},")
    print(']')
    print(wins)
    return result


        
#statistics(Smart, [MinMax(), AlphaBeta(), Smart(), Fastest()], 3, 15)
play_game(Human(),MinMax(), 10)
print("\n")