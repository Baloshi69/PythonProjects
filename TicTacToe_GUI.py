# TicTacToe_GUI.py

"""A tic-tac-toe game built with Python and Tkinter."""

import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super.__init__()
        self.title("Tic-Tac-Toe The game by Baloshi69")
        self._cells = {}

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()