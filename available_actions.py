def available_actions(self, state):
        H, V = state[0], state[1]
        actions = []
        for r in range(size):
            for c in range(size - 1):
                if H[r][c] == 0: actions.append(("H", r, c))
        for r in range(size - 1):
            for c in range(size):
                if V[r][c] == 0: actions.append(("V", r, c))
        return actions
