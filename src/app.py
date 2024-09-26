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
    
    def __init__(self, player_x="X", player_y="Y"):
        self.player_x_marker = player_x
        self.player_o_marker = player_y
        self.column = self.row = 3
        self.bord = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.win_condition = 3
        
        self.__config_window()
        self.__build_utility_ui()
        self.__build_game_bord()
        
    def __config_window(self):
        self.window = tk.Tk()
        self.window.title(Game.TITLE)
        self.window.geometry(Game.DEFAULT_SIZE)
        self.window.resizable(False, False)
        self.window.configure(background=Game.COLOR_SHEMA["border"])
        self.window.grid_columnconfigure(0, weight=1)
        
    def __restart_game(self):
        print("Game Restarted")
        
    def __handle_user_click(self, row, column):
        row = row - 1
        print(f"User Clicked on {row}, {column}")
    
    def __build_utility_ui(self):
        self.current_player_label = tk.Label(
            text="Current Player: X",
            font=(Game.FONT, Game.FONT_SIZE),
            foreground=Game.COLOR_SHEMA["text"],
            background=Game.COLOR_SHEMA["border"],
        )
                
        self.restart_button = tk.Button(
			text="Restart",
			font=(Game.FONT, Game.FONT_SIZE),
			background=Game.COLOR_SHEMA["grid_cell"],
			foreground=Game.COLOR_SHEMA["text"],
   			command=lambda: self.__restart_game()
		)
        
        self.current_player_label.grid(row=0, column=0, columnspan=self.column, sticky="ew")
        self.restart_button.grid(row=self.row+1, column=0, columnspan=self.column, sticky="ew", padx=6, pady=6)
        
    def __build_game_bord(self):
        for row in range(1, self.row+1):
            for column in range(self.column):
                cell = tk.Button(
                    self.window,
                    width= 10,
                    height= 5,
                    bg=Game.COLOR_SHEMA["grid_cell"],
                    command=lambda row=row, column=column: self.__handle_user_click(row, column)
				)
                cell.grid(row=row, column=column, padx=6, pady=6)
    
    def __gameloop(self):
        self.window.mainloop()
        
    def run(self):
        self.__gameloop()
        

if __name__ == "__main__":
    Game().run()
