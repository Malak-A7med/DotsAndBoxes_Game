def take_action(self, state, action):
        H, V, f_score, s_score, turn = state
        new_H = [row[:] for row in H]
        new_V = [row[:] for row in V]
        new_f_score, new_s_score = f_score, s_score
        new_turn = turn
        type_act, r, c = action
        if type_act == "H": new_H[r][c] = 1
        else: new_V[r][c] = 1

        points = 0
        if type_act == 'H':
            if r > 0 and new_H[r-1][c] and new_V[r-1][c] and new_V[r-1][c+1]: points += 1
            if r < size-1 and new_H[r+1][c] and new_V[r][c] and new_V[r][c+1]: points += 1
        else:
            if c > 0 and new_V[r][c-1] and new_H[r][c-1] and new_H[r+1][c-1]: points += 1
            if c < size-1 and new_V[r][c+1] and new_H[r][c] and new_H[r+1][c]: points += 1

        if points > 0:
            if turn == 'f': new_f_score += points
            else: new_s_score += points
        else:
            new_turn = 's' if turn == 'f' else 'f'

        return (new_H, new_V, new_f_score, new_s_score, new_turn)