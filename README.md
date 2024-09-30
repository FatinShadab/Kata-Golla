#  XO কাটা-গোল্লা (Kata-Golla) - Minimax & α-β Pruning

## Project Overview

This project is a Tic-Tac-Toe game developed for the **AI Lab course**. The main focus of the project is the implementation of an AI player using the **Minimax algorithm** and **Alpha-Beta Pruning** to optimize the decision-making process. The game allows a human player to compete against the AI, which is designed to make optimal moves based on the current state of the game board.

### Key Features:
- **Minimax Algorithm**: The AI uses the Minimax algorithm to evaluate future game states and select the best possible move.
- **Alpha-Beta Pruning**: A more efficient version of the Minimax algorithm is implemented, which reduces the number of nodes evaluated by the AI.
- **AI Difficulty Levels**: 
  - **Level 0**: AI makes random moves.
  - **Level 1**: AI uses the basic Minimax algorithm.
  - **Level 2**: AI uses Minimax with Alpha-Beta Pruning for more efficient decision-making.

## Game Features
- **3x3 Tic-Tac-Toe Grid**: The classic game grid where players take turns placing their markers.
- **Human vs AI**: A human player can compete against the AI.
- **Win/Draw Detection**: The game checks for win or draw conditions after each move.
- **Restart Functionality**: Players can restart the game at any time.
- **Visual Interface**: The game uses **Tkinter** to provide a graphical interface.

## AI Implementation

### Minimax Algorithm:
The AI uses the **Minimax algorithm** to recursively evaluate all possible future game states. It assigns a score to each state:
- +1 for an AI win.
- -1 for a human win.
- 0 for a draw.

The AI then selects the move that maximizes its chances of winning while minimizing the chances of losing.

### Alpha-Beta Pruning:
To improve the efficiency of the AI, **Alpha-Beta Pruning** is applied to the Minimax algorithm. This technique allows the algorithm to cut off branches in the decision tree that are not likely to affect the final decision, thus reducing the computation time.

## Files and Structure

```
.
├── src/
│   ├── ai/
│   │   ├── __init__.py
│   │   └── agent.py        # Contains the AI logic (Minimax & Alpha-Beta Pruning)
│   └── app.py              # Main game logic using Tkinter for the GUI
├── assets/
│   └── icon.png            # Game icon
├── README.md               # This file
└── requirements.txt        # List of required packages (Tkinter, etc.)
```

### Main Files:
1. **`app.py`**:
   - Manages the Tic-Tac-Toe game board, player turns, and the overall game flow using Tkinter for the GUI.
   - It interacts with the AI through the `Agent` class.
   
2. **`agent.py`**:
   - Implements the **AI** logic for the Tic-Tac-Toe game.
   - Contains three levels of AI difficulty, with Level 2 utilizing Minimax with Alpha-Beta Pruning to make efficient and optimal moves.

### Game Flow:
1. The human player selects their move.
2. The AI analyzes the game board and makes its move based on the current difficulty level.
3. The game checks for a win, loss, or draw after each move and displays the result.
4. The game can be restarted at any time.

## How to Run

### Prerequisites:
- **Python 3.x**
- **Tkinter**: Make sure Tkinter is installed (it’s included with most Python distributions).
  
   If Tkinter is not installed, you can install it using:
   ```bash
   sudo apt-get install python3-tk  # Linux (Debian/Ubuntu)
   ```

### Running the Game:
1. Clone the repository or download the project files.
2. Navigate to the project directory and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python src/app.py
   ```

## AI Levels

- **Level 0**: The AI picks moves randomly, suitable for easy difficulty.
- **Level 1**: The AI uses the basic **Minimax algorithm**, evaluating all possible future moves.
- **Level 2**: The AI uses **Minimax with Alpha-Beta Pruning** to efficiently evaluate and choose the best moves, optimized for performance and more challenging gameplay.

## Minimax Algorithm with Alpha-Beta Pruning

The **Minimax algorithm** works by simulating all possible future moves and assigning a score to each outcome. The AI then selects the move that maximizes its chances of winning while minimizing the human player’s chances.

**Alpha-Beta Pruning** enhances this algorithm by cutting off unnecessary branches in the search tree, reducing the time complexity, and allowing the AI to make decisions faster.

### Example of Minimax with Alpha-Beta Pruning:

```python
def minimax(board, depth, alpha, beta, is_maximizing):
    if self.check_winner(board, self.self_marker):
        return 1
    if self.check_winner(board, self.opp_marker):
        return -1
    if self.check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for row in board:
            for cell in row:
                if cell.cget('text') == "":
                    cell.config(text=self.self_marker)
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    cell.config(text="")
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for row in board:
            for cell in row:
                if cell.cget('text') == "":
                    cell.config(text=self.opp_marker)
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    cell.config(text="")
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval
```

## Future Enhancements
- Implement additional difficulty levels by adjusting the depth of the Minimax algorithm.
- Add support for playing with two human players.
- Letting the AI make move first
- Enhance the UI with animations or sound effects.
