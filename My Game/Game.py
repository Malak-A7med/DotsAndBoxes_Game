import pygame
import math
import sys

# ================= Basic Screen Settings =================
CELL = 90 
WIDTH = 1000 
HEIGHT = 695 

# Colors
WHITE = (255, 255, 255)
BLACK = (10, 10, 15)
RED = (255, 80, 80)
BLUE = (80, 160, 255)
GRAY = (50, 50, 50)
GREEN = (0, 255, 127)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots and Boxes - 3D AI Edition")

# Load Images and Icons
try:
    # Main menu background
    bg_menu = pygame.image.load("background.jpg")
    bg_menu = pygame.transform.scale(bg_menu, (WIDTH, HEIGHT))
    
    # Game background
    bg_game = pygame.image.load("game_bg.png")
    bg_game = pygame.transform.scale(bg_game, (WIDTH, HEIGHT))
    
    # Game over background
    bg_gameover = pygame.image.load("gameoverBG.jpg")
    bg_gameover = pygame.transform.scale(bg_gameover, (WIDTH, HEIGHT))

    # Help screen background scaled to 600x700
    img_help_raw = pygame.image.load("HelpBG.png")
    help_w, help_h = 600, 700
    img_help_screen = pygame.transform.scale(img_help_raw, (help_w, help_h))
    
    # Icons
    icon_main = pygame.image.load("home_icon.png") 
    icon_main = pygame.transform.scale(icon_main, (35, 35))
    
    icon_exit = pygame.image.load("exit_icon.png")
    icon_exit = pygame.transform.scale(icon_exit, (35, 35))
    
    icon_help = pygame.image.load("help_icon.png")
    icon_help = pygame.transform.scale(icon_help, (35, 35))
except Exception as e:
    print(f"Error loading images: {e}")
    bg_menu = bg_game = bg_gameover = icon_main = icon_exit = icon_help = img_help_screen = None

font_small = pygame.font.SysFont('Arial', 22, bold=True)
font_medium = pygame.font.SysFont('Arial', 32, bold=True)
font_big = pygame.font.SysFont('Arial', 65, bold=True)

# ================= GUI Functions =================

def draw_transparent_button(rect, text, is_active, base_clr):
    s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    alpha = 200 if is_active else 120
    pygame.draw.rect(s, (*base_clr, alpha), (0, 0, rect.width, rect.height), border_radius=12)
    win.blit(s, (rect.x, rect.y))
    txt_clr = WHITE if not is_active else BLACK
    txt_surf = font_small.render(text, True, txt_clr)
    win.blit(txt_surf, (rect.centerx - txt_surf.get_width()//2, rect.centery - txt_surf.get_height()//2))

# Help screen with transparent button and no white border
def show_help_screen():
    if not img_help_screen:
        return

    help_rect = img_help_screen.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    # Define "CONTINUE" button
    btn_w, btn_h = 200, 50
    continue_btn_rect = pygame.Rect(WIDTH // 2 - btn_w // 2, help_rect.bottom - 80, btn_w, btn_h)

    waiting = True
    while waiting:
        if bg_game: win.blit(bg_game, (0, 0))
        else: win.fill(BLACK)
        
        win.blit(img_help_screen, help_rect.topleft)

        # Draw fully transparent button
        mouse_pos = pygame.mouse.get_pos()
        is_hover = continue_btn_rect.collidepoint(mouse_pos)
        
        # Create transparent surface for the button (Alpha)
        # 150 is medium transparency, 190 is clearer on hover
        s = pygame.Surface((continue_btn_rect.width, continue_btn_rect.height), pygame.SRCALPHA)
        alpha_val = 190 if is_hover else 150
        # Brownish color to match typical UI styles
        pygame.draw.rect(s, (139, 69, 19, alpha_val), (0, 0, btn_w, btn_h), border_radius=15)
        win.blit(s, (continue_btn_rect.x, continue_btn_rect.y))
        
        # Button text
        txt_clr = BLACK if is_hover else WHITE
        btn_txt = font_small.render("CONTINUE", True, txt_clr)
        win.blit(btn_txt, (continue_btn_rect.centerx - btn_txt.get_width()//2, 
                           continue_btn_rect.centery - btn_txt.get_height()//2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    if continue_btn_rect.collidepoint(event.pos):
                        waiting = False

def start_menu():
    mode = "AI vs Human"
    diff = "Medium"
    btn_w, btn_h = 220, 50
    left_x = WIDTH // 2 - btn_w - 70
    right_x = WIDTH // 2 + 70
    while True:
        if bg_menu: win.blit(bg_menu, (0,0))
        else: win.fill(BLACK)
        
        modes = ["Human vs Human", "AI vs Human", "AI vs AI"]; mode_rects = []
        for i, m in enumerate(modes):
            r = pygame.Rect(left_x, 250 + i*70, btn_w, btn_h); mode_rects.append(r)
            draw_transparent_button(r, m, mode == m, BLUE)
            
        diffs = ["Easy", "Medium", "Hard"]; diff_rects = []
        for i, d in enumerate(diffs):
            r = pygame.Rect(right_x, 250 + i*70, btn_w, btn_h); diff_rects.append(r)
            draw_transparent_button(r, d, diff == d, RED)
            
        start_btn = pygame.Rect(WIDTH//2 - 125, HEIGHT - 120, 250, 70)
        s_start = pygame.Surface((start_btn.width, start_btn.height), pygame.SRCALPHA)
        pygame.draw.rect(s_start, (*GREEN, 220), (0, 0, start_btn.width, start_btn.height), border_radius=15)
        win.blit(s_start, (start_btn.x, start_btn.y))
        
        st_txt = font_medium.render("START GAME", True, BLACK)
        win.blit(st_txt, (start_btn.centerx - st_txt.get_width()//2, start_btn.centery - st_txt.get_height()//2))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos): return mode, diff
                for i, r in enumerate(mode_rects):
                    if r.collidepoint(event.pos): mode = modes[i]
                for i, r in enumerate(diff_rects):
                    if r.collidepoint(event.pos): diff = diffs[i]

def get_player_names(game_mode):
    p1_name, p2_name = "Player 1", "Player 2"
    if game_mode == "AI vs Human": p1_name, p2_name = "Human", "AI"
    elif game_mode == "AI vs AI": return "AI 1", "AI 2"
    active_box, input_text1, input_text2 = 1, "", ""
    while True:
        if bg_menu: win.blit(bg_menu, (0,0))
        else: win.fill(BLACK)
        box1 = pygame.Rect(WIDTH//2 - 100, 250, 200, 50)
        box2 = pygame.Rect(WIDTH//2 - 100, 330, 200, 50)
        draw_transparent_button(box1, input_text1 if input_text1 else "Player 1", active_box == 1, BLUE)
        if game_mode == "Human vs Human":
            draw_transparent_button(box2, input_text2 if input_text2 else "Player 2", active_box == 2, RED)
        start_btn = pygame.Rect(WIDTH//2 - 100, 450, 200, 60)
        draw_transparent_button(start_btn, "CONTINUE", False, GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box1.collidepoint(event.pos): active_box = 1
                elif box2.collidepoint(event.pos) and game_mode == "Human vs Human": active_box = 2
                elif start_btn.collidepoint(event.pos):
                    if input_text1.strip(): p1_name = input_text1
                    if input_text2.strip() and game_mode == "Human vs Human": p2_name = input_text2
                    return p1_name, p2_name
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if active_box == 1: input_text1 = input_text1[:-1]
                    else: input_text2 = input_text2[:-1]
                elif event.key == pygame.K_RETURN:
                    if game_mode == "AI vs Human" or active_box == 2:
                        if input_text1.strip(): p1_name = input_text1
                        if input_text2.strip() and game_mode == "Human vs Human": p2_name = input_text2
                        return p1_name, p2_name
                    else: active_box = 2
                else:
                    if event.unicode.isprintable():
                        if active_box == 1 and len(input_text1) < 12: input_text1 += event.unicode
                        elif active_box == 2 and len(input_text2) < 12: input_text2 += event.unicode
        pygame.display.update()

def show_game_over_custom(result, f_score, s_score, p1, p2):
    while True:
        if bg_gameover: win.blit(bg_gameover, (0, 0))
        else: win.fill(BLACK)
        if result == 1: msg, clr = f"{p2} WON!", RED
        elif result == -1: msg, clr = f"{p1} WON!", BLUE
        else: msg, clr = "IT'S A DRAW!", WHITE
        title_surf = font_big.render(msg, True, clr)
        win.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, HEIGHT//2 - 150))
        score_text = f"{p1}: {f_score}   |   {p2}: {s_score}"
        score_surf = font_medium.render(score_text, True, WHITE)
        win.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, HEIGHT//2 - 50))
        btn_w, btn_h = 200, 60
        restart_rect = pygame.Rect(WIDTH//2 - btn_w - 20, HEIGHT//2 + 80, btn_w, btn_h)
        exit_rect = pygame.Rect(WIDTH//2 + 20, HEIGHT//2 + 80, btn_w, btn_h)
        mx, my = pygame.mouse.get_pos()
        draw_transparent_button(restart_rect, "RESTART", restart_rect.collidepoint(mx, my), GREEN)
        draw_transparent_button(exit_rect, "EXIT", exit_rect.collidepoint(mx, my), RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos): return "restart"
                if exit_rect.collidepoint(event.pos): pygame.quit(); sys.exit()

# ================= Game Logic Class =================

class lines_and_dots:
    def __init__(self, size, difficulty_depth):
        self.size = size
        self.horizontal = [[0 for _ in range(size - 1)] for _ in range(size)]
        self.vertical = [[0 for _ in range(size)] for _ in range(size - 1)]
        self.h_owners = [[0 for _ in range(size - 1)] for _ in range(size)]
        self.v_owners = [[0 for _ in range(size)] for _ in range(size - 1)]
        self.box_owners = [[0 for _ in range(size - 1)] for _ in range(size - 1)]
        self.first_player_score = 0
        self.second_player_score = 0
        self.turn = 'f' 
        self.difficulty_depth = difficulty_depth

    def get_state(self):
        return ([row[:] for row in self.horizontal], [row[:] for row in self.vertical],
                [row[:] for row in self.h_owners], [row[:] for row in self.v_owners],
                [row[:] for row in self.box_owners], self.first_player_score,
                self.second_player_score, self.turn)

    def check_terminal(self, state):
        H, V, _, _, _, f_score, s_score, _ = state
        total = sum(sum(row) for row in H) + sum(sum(row) for row in V)
        if total == self.size * (self.size - 1) * 2:
            return 1 if s_score > f_score else (-1 if f_score > s_score else 0)
        return "Not terminal"

    def take_action(self, state, action):
        H, V, h_own, v_own, box_own, f_score, s_score, turn = state
        new_H, new_V = [r[:] for r in H], [r[:] for r in V]
        new_h_own, new_v_own = [r[:] for r in h_own], [r[:] for r in v_own]
        new_box_own = [r[:] for r in box_own]
        typ, r, c = action
        owner = 1 if turn == 'f' else 2
        if typ == "H": new_H[r][c], new_h_own[r][c] = 1, owner
        else: new_V[r][c], new_v_own[r][c] = 1, owner
        pts = 0
        if typ == 'H':
            if r > 0 and new_H[r-1][c] and new_V[r-1][c] and new_V[r-1][c+1]: pts += 1; new_box_own[r-1][c] = owner
            if r < self.size-1 and new_H[r+1][c] and new_V[r][c] and new_V[r][c+1]: pts += 1; new_box_own[r][c] = owner
        else:
            if c > 0 and new_V[r][c-1] and new_H[r][c-1] and new_H[r+1][c-1]: pts += 1; new_box_own[r][c-1] = owner
            if c < self.size-1 and new_V[r][c+1] and new_H[r][c] and new_H[r+1][c]: pts += 1; new_box_own[r][c] = owner
        new_turn = turn if pts > 0 else ('s' if turn == 'f' else 'f')
        return (new_H, new_V, new_h_own, new_v_own, new_box_own, f_score + (pts if turn == 'f' else 0), s_score + (pts if turn == 's' else 0), new_turn)

    def alphabeta(self, state, depth, alpha, beta):
        res = self.check_terminal(state)
        if res != "Not terminal": return res*1000, None
        if depth == 0: return state[6] - state[5], None
        actions = []
        H, V = state[0], state[1]
        for r in range(self.size):
            for c in range(self.size-1):
                if H[r][c] == 0: actions.append(("H", r, c))
        for r in range(self.size-1):
            for c in range(self.size):
                if V[r][c] == 0: actions.append(("V", r, c))
        best_move = None
        if state[7] == 's':
            val = -math.inf
            for act in actions:
                e, _ = self.alphabeta(self.take_action(state, act), depth-1, alpha, beta)
                if e > val: val, best_move = e, act
                alpha = max(alpha, val)
                if beta <= alpha: break
            return val, best_move
        else:
            val = math.inf
            for act in actions:
                e, _ = self.alphabeta(self.take_action(state, act), depth-1, alpha, beta)
                if e < val: val, best_move = e, act
                beta = min(beta, val)
                if beta <= alpha: break
            return val, best_move

# ================= Main Game Loop =================

def main_game(game_mode, difficulty_str, p1, p2):
    if difficulty_str == "Easy":
        current_size = 4
        ai_depth = 3
    elif difficulty_str == "Hard":
        current_size = 6
        ai_depth = 4 
    else: 
        current_size = 5
        ai_depth = 4

    game = lines_and_dots(size=current_size, difficulty_depth=ai_depth)
    state = game.get_state()
    
    start_x = 25  
    spacing = 55  
    rect_main = pygame.Rect(start_x, HEIGHT - 60, 35, 35)
    rect_exit = pygame.Rect(start_x + spacing, HEIGHT - 60, 35, 35)
    rect_help = pygame.Rect(start_x + spacing * 2, HEIGHT - 60, 35, 35)
    
    while True:
        if bg_game: win.blit(bg_game, (0, 0))
        else: win.fill(BLACK)

        H, V, h_own, v_own, box_own, f_score, s_score, turn = state
        
        grid_width = (current_size - 1) * CELL
        offset_x = (WIDTH - grid_width) // 2
        offset_y = (HEIGHT - grid_width) // 2
        
        # Draw Boxes
        for r in range(current_size-1):
            for c in range(current_size-1):
                if box_own[r][c]:
                    clr = BLUE if box_own[r][c] == 1 else RED
                    dark_clr = (max(0, clr[0]-80), max(0, clr[1]-80), max(0, clr[2]-80))
                    rx = offset_x + c*CELL + 6
                    ry = offset_y + r*CELL + 6
                    rw = CELL - 12
                    pygame.draw.rect(win, dark_clr, (rx, ry, rw, rw), border_radius=6)
                    s = pygame.Surface((rw, rw), pygame.SRCALPHA)
                    s.fill((*clr, 190)) 
                    win.blit(s, (rx, ry - 4))

        # Draw Lines
        for r in range(current_size):
            for c in range(current_size-1):
                if H[r][c]:
                    clr = BLUE if h_own[r][c] == 1 else RED
                    lx, ly = offset_x + c*CELL, offset_y + r*CELL
                    pygame.draw.line(win, (20, 20, 20), (lx, ly + 4), (lx + CELL, ly + 4), 8)
                    pygame.draw.line(win, clr, (lx, ly), (lx + CELL, ly), 5)

        for r in range(current_size-1):
            for c in range(current_size):
                if V[r][c]:
                    clr = BLUE if v_own[r][c] == 1 else RED
                    lx, ly = offset_x + c*CELL, offset_y + r*CELL
                    pygame.draw.line(win, (20, 20, 20), (lx + 4, ly), (lx + 4, ly + CELL), 8)
                    pygame.draw.line(win, clr, (lx, ly), (lx, ly + CELL), 5)

        # Draw Dots
        for r in range(current_size):
            for c in range(current_size):
                dx, dy = offset_x + c*CELL, offset_y + r*CELL
                pygame.draw.circle(win, (15, 15, 15), (dx + 3, dy + 3), 8)
                pygame.draw.circle(win, WHITE, (dx, dy), 6)

        # Scores and Icons
        txt1 = font_medium.render(f"{p1}: {f_score}", True, BLUE)
        txt2 = font_medium.render(f"{p2}: {s_score}", True, RED)
        win.blit(txt1, (50, 30)); win.blit(txt2, (WIDTH - txt2.get_width() - 50, 30))

        if icon_main: win.blit(icon_main, rect_main)
        if icon_exit: win.blit(icon_exit, rect_exit)
        if icon_help: win.blit(icon_help, rect_help)

        pygame.display.update()

        res = game.check_terminal(state)
        if res != "Not terminal":
            pygame.time.wait(1000)
            return show_game_over_custom(res, f_score, s_score, p1, p2)

        moved = False
        if (turn == 'f' and game_mode != "AI vs AI") or (turn == 's' and game_mode == "Human vs Human"):
            while not moved:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = event.pos
                        if rect_main.collidepoint(mx, my): return "restart"
                        if rect_exit.collidepoint(mx, my): pygame.quit(); sys.exit()
                        if rect_help.collidepoint(mx, my):
                            show_help_screen()
                            # Redraw game immediately after closing help
                            moved = False
                            break
                        
                        tol = 25
                        for r in range(current_size):
                            for c in range(current_size-1):
                                x1, y = offset_x+c*CELL, offset_y+r*CELL
                                if x1 < mx < x1+CELL and y-tol < my < y+tol and state[0][r][c] == 0:
                                    state = game.take_action(state, ("H", r, c)); moved = True
                        for r in range(current_size-1):
                            for c in range(current_size):
                                x, y1 = offset_x+c*CELL, offset_y+r*CELL
                                if x-tol < mx < x+tol and y1 < my < y1+CELL and state[1][r][c] == 0:
                                    state = game.take_action(state, ("V", r, c)); moved = True
                if not moved: break # Break to update the UI
        else: 
            pygame.time.wait(600)
            _, best = game.alphabeta(state, game.difficulty_depth, -math.inf, math.inf)
            if best: state = game.take_action(state, best)

if __name__ == "__main__":
    while True:
        mode_choice, diff_choice = start_menu()
        name1, name2 = get_player_names(mode_choice)
        res = main_game(mode_choice, diff_choice, name1, name2)
        if res != "restart": break