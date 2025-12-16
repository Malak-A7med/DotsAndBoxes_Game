size = 5
def take_action(self, state, action):
    H, V, h_own, v_own, box_own, f_score, s_score, turn = state
    new_H = [row[:] for row in H]
    new_V = [row[:] for row in V]
    new_h_own = [row[:] for row in h_own]
    new_v_own = [row[:] for row in v_own]
    new_box_own = [row[:] for row in box_own]
    new_f_score, new_s_score = f_score, s_score
    new_turn = turn
    
    typ, r, c = action
    owner = 1 if turn == 'f' else 2  # 1=Human, 2=AI
    
    if typ == "H":
        new_H[r][c] = 1
        new_h_own[r][c] = owner
    else:
        new_V[r][c] = 1
        new_v_own[r][c] = owner

    points = 0
    if typ == 'H':
        if r > 0 and new_H[r-1][c] and new_V[r-1][c] and new_V[r-1][c+1]:
            points += 1
            new_box_own[r-1][c] = owner
        if r < size-1 and new_H[r+1][c] and new_V[r][c] and new_V[r][c+1]:
            points += 1
            new_box_own[r][c] = owner
    else:
        if c > 0 and new_V[r][c-1] and new_H[r][c-1] and new_H[r+1][c-1]:
            points += 1
            new_box_own[r][c-1] = owner
        if c < size-1 and new_V[r][c+1] and new_H[r][c] and new_H[r+1][c]:
            points += 1
            new_box_own[r][c] = owner

    if points > 0:
        if turn == 'f':
            new_f_score += points
        else:
            new_s_score += points
    else:
        new_turn = 's' if turn == 'f' else 'f'

    return (new_H, new_V, new_h_own, new_v_own, new_box_own, new_f_score, new_s_score, new_turn)
