# TicTacToe_GUI.py

"""A tic-tac-toe game built with Python and Tkinter."""

import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class player(NamedTuple):
    label : str
    color : str

class move(NamedTuple):
    row : int
    color : int
    label : str = ""

class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self.current_move = []
        self._has_winner = False
        self._winning_combos = []
        self.setup_board()


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe The game by Baloshi69")
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue"
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

def main():
    """Create the game's board and run its main loop."""
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()