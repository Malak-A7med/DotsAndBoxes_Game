# 🎮 Dots and Boxes Game — Human vs AI

A modern take on the classic Dots and Boxes board game implemented with Python and Pygame. Compete against a computer opponent powered by an Alpha-Beta Pruning AI — try to complete more boxes than the AI to win.

## Game Overview
The board is made up of dots arranged in a grid. Players alternate turns drawing a single horizontal or vertical line between two adjacent dots. When a player draws the fourth side of a box, they claim that box, score a point, and immediately get another turn. The match ends when every possible line has been drawn; the player with the most boxes wins.

## Key Features
- Lightweight and responsive UI built with Pygame
- Distinct color scheme to tell Human and AI moves apart
- AI opponent uses Alpha-Beta Pruning for smarter play
- Live score display during the game
- End-of-game screen that shows the winner or a draw, then closes automatically

## Color Scheme
- Human: Blue
- AI: Red
- Grid Dots: White

## How to Play
- Use the mouse to click and draw a line between two neighboring dots.
- Valid moves:
  - Horizontal lines
  - Vertical lines
- Complete a box to score a point and take another turn.
- If you don't complete a box, control passes to the AI.

## End of Game
When all lines have been placed, a results screen appears:
- "You Win!" — if the Human has a higher score
- "AI Wins!" — if the AI has a higher score
- "Draw" — if the scores are tied

The results are shown briefly before the game window closes automatically.

## Requirements
- Python 3.x
- pygame

Install Pygame with:
```bash
pip install pygame
```

## Running the Game
1. Make sure you have Python 3 installed.
2. Install the pygame dependency if needed.
3. From the project directory run:
```bash
python main.py
```
(Replace `main.py` with the actual entry script name if different.)

## AI Details
- Algorithm: Alpha-Beta Pruning
- Search depth: 4 plies
- Objective: maximize AI boxes while minimizing the human player's boxes

## Possible Improvements
- Local multiplayer mode
- UI/UX polish and animations
- Support for different board sizes
- In-game restart button
- Multiple difficulty levels


## Contributing
Contributions and suggestions are welcome. Please open an Issue or submit a Pull Request with improvements or bug fixes.

Enjoy the game — challenge the AI and have fun!
