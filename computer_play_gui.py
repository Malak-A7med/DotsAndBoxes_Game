import math
def computer_play_gui(self, state):
    _, best_move = self.alphabeta(state, 4, -math.inf, math.inf)
    if best_move:
        return self.take_action(state, best_move)
    return state
