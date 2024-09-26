import tkinter as tk


class Game:
    TITLE = "XO কাট-গোল্লা"
    DEFAULT_WIDTH = 360
    DEFAULT_HEIGHT = 480
    DEFAULT_SIZE = f"{DEFAULT_WIDTH}x{DEFAULT_HEIGHT}"
    FONT = "Impact"
    FONT_SIZE = 32
    COLOR_SHEMA = {
        "grid_cell": "#3C3D37",
        "border": "#181C14",
        "text": "#F2EFE9",
    }

    def __init__(self, player_x="X", player_o="O"):
        self.player_x_marker = player_x
        self.player_o_marker = player_o
        self.current_player = self.player_x_marker
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.win_condition = 3
        self.moves = 0

        self.__config_window()
        self.__build_utility_ui()
        self.__build_game_board()

    def __config_window(self):
        self.window = tk.Tk()
        self.window.title(Game.TITLE)
        self.window.geometry(Game.DEFAULT_SIZE)
        self.window.resizable(False, False)
        self.window.configure(background=Game.COLOR_SHEMA["border"])
        self.window.grid_columnconfigure(0, weight=1)

    def __restart_game(self):
        # Reset the board and UI
        for row in range(3):
            for column in range(3):
                self.board[row][column].config(text="", state="normal")
        self.current_player = self.player_x_marker
        self.current_player_label.config(text=f"Current Player: {self.current_player}")
        self.moves = 0

    def __handle_user_click(self, row, column):
        # Handle player move
        if self.board[row][column].cget('text') == "":
            self.board[row][column].config(text=self.current_player)
            self.moves += 1
            if self.__check_winner():
                self.__end_game(f"Player {self.current_player} wins!")
            elif self.moves == 9:
                self.__end_game("It's a draw!")
            else:
                self.current_player = self.player_o_marker if self.current_player == self.player_x_marker else self.player_x_marker
                self.current_player_label.config(text=f"Current Player: {self.current_player}")

    def __check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0].cget('text') == self.board[i][1].cget('text') == self.board[i][2].cget('text') != "":
                return True
            if self.board[0][i].cget('text') == self.board[1][i].cget('text') == self.board[2][i].cget('text') != "":
                return True
        if self.board[0][0].cget('text') == self.board[1][1].cget('text') == self.board[2][2].cget('text') != "":
            return True
        if self.board[0][2].cget('text') == self.board[1][1].cget('text') == self.board[2][0].cget('text') != "":
            return True
        return False

    def __end_game(self, message):
        # Disable buttons and show the result
        for row in range(3):
            for column in range(3):
                self.board[row][column].config(state="disabled")
        self.current_player_label.config(text=message)

    def __build_utility_ui(self):
        # Create utility UI components
        self.current_player_label = tk.Label(
            text=f"Current Player: {self.current_player}",
            font=(Game.FONT, Game.FONT_SIZE),
            foreground=Game.COLOR_SHEMA["text"],
            background=Game.COLOR_SHEMA["border"],
        )

        self.restart_button = tk.Button(
            text="Restart",
            font=(Game.FONT, Game.FONT_SIZE),
            background=Game.COLOR_SHEMA["grid_cell"],
            foreground=Game.COLOR_SHEMA["text"],
            highlightbackground=Game.COLOR_SHEMA["border"],
            command=lambda: self.__restart_game()
        )

        self.current_player_label.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.restart_button.grid(row=4, column=0, columnspan=3, sticky="ew")

    def __build_game_board(self):
        # Create the game grid of buttons
        for row in range(3):
            for column in range(3):
                self.board[row][column] = tk.Button(
                    text="", font=(Game.FONT, Game.FONT_SIZE),
                    background=Game.COLOR_SHEMA["grid_cell"],
                    foreground=Game.COLOR_SHEMA["text"],
                    highlightbackground=Game.COLOR_SHEMA["border"],
                    width=4, height=2,
                    command=lambda row=row, column=column: self.__handle_user_click(row, column)
                )
                self.board[row][column].grid(row=row+1, column=column)

    def __gameloop(self):
        self.window.mainloop()

    def run(self):
        self.__gameloop()


if __name__ == "__main__":
    Game().run()
