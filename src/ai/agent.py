import time
import random


class Agent:
    def __init__(self, level, self_marker, opp_marker) -> None:
        self.level = level
        self.self_marker = self_marker
        self.opp_marker = opp_marker
        self.algo = [
            self.algorithm_lvl_0,
            self.algorithm_lvl_1,
            self.algorithm_lvl_2
        ]
    
    def check_winner(self, board, player):
        for i in range(3):
            if all([cell.cget('text') == player for cell in board[i]]):
                return True
            if all([board[j][i].cget('text') == player for j in range(3)]):
                return True
        
        if all([board[i][i].cget('text') == player for i in range(3)]):
            return True
        if all([board[i][2 - i].cget('text') == player for i in range(3)]):
            return True
        
        return False
    
    def check_draw(self, board):
        return all([cell.cget('text') != "" for row in board for cell in row])

    def algorithm_lvl_0(self, board):
        time.sleep(1)  # Simulate AI thinking time
        available_moves = []
        for row in board:
            for cell in row:
                if cell.cget('text') == "":
                    available_moves.append(cell)
        
        random.choice(available_moves).config(text=self.self_marker)

    def algorithm_lvl_1(self, board):
        def minimax(board, depth, is_maximizing):
            best_score = None
            
            if self.check_winner(board, self.self_marker):
                return 1
            if self.check_winner(board, self.opp_marker):
                return -1
            if self.check_draw(board):
                return 0
            
            if is_maximizing:
                best_score = -float("inf")
                for row in board:
                    for cell in row:
                        if cell.cget('text') == "":
                            cell.config(text=self.self_marker)
                            score = minimax(board, depth + 1, False)
                            cell.config(text="")
                            best_score = max(score, best_score)  
            else:
                best_score = float("inf")
                for row in board:
                    for cell in row:
                        if cell.cget('text') == "":
                            cell.config(text=self.opp_marker)
                            score = minimax(board, depth + 1, True)
                            cell.config(text="")
                            best_score = min(score, best_score)
                
            return best_score
        
        move = None
        best_score = -float("inf")
        for row in board:
            for cell in row:
                if cell.cget('text') == "":
                    cell.config(text=self.self_marker)
                    score = minimax(board, 0, False)
                    cell.config(text="")
                    if score > best_score:
                        best_score = score
                        move = cell
                        
        move.config(text=self.self_marker)
    
    def algorithm_lvl_2(self, board):
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

        move = None
        best_score = -float("inf")
        for row in board:
            for cell in row:
                if cell.cget('text') == "":
                    cell.config(text=self.self_marker)
                    score = minimax(board, 0, -float("inf"), float("inf"), False)
                    cell.config(text="")
                    if score > best_score:
                        best_score = score
                        move = cell

        move.config(text=self.self_marker)
     
    def make_move(self, board):
        self.algo[self.level](board)
