import tkinter as tk
import random
import numpy as np

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")
        self.size = 4
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.high_score = 0
        self.score = 0

        self.frame = tk.Frame(self.root)
        self.frame.grid()

        self.high_score_label = tk.Label(self.frame, text=f"High Score: {self.high_score}", font=('Arial', 16))
        self.high_score_label.grid(row=0, column=0, columnspan=self.size)

        self.score_label = tk.Label(self.frame, text=f"Score: {self.score}", font=('Arial', 16))
        self.score_label.grid(row=1, column=0, columnspan=self.size)

        self.tiles = [[tk.Label(self.frame, text='', bg='white', font=('Arial', 24), width=4, height=2) for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].grid(row=i+2, column=j, padx=5, pady=5)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=self.size+2, column=0, columnspan=self.size//2, sticky="ew")

        self.play_again_button = tk.Button(self.frame, text="Play Again", command=self.reset_game)
        self.play_again_button.grid(row=self.size+2, column=self.size//2, columnspan=self.size//2, sticky="ew")

        self.add_new_tile()
        self.add_new_tile()
        self.update_gui()

        self.root.bind('<Key>', self.key_handler)

    def reset_game(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()
        self.update_gui()
        self.root.bind('<Key>', self.key_handler)

    def add_new_tile(self):
        empty_positions = list(zip(*np.where(self.board == 0)))
        if empty_positions:
            i, j = random.choice(empty_positions)
            self.board[i, j] = 2 if random.random() < 0.9 else 4

    def slide_and_merge_row_left(self, row):
        non_zero = row[row != 0]
        new_row = np.zeros_like(row)
        skip = False
        j = 0
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                new_row[j] = 2 * non_zero[i]
                self.score += new_row[j]
                skip = True
            else:
                new_row[j] = non_zero[i]
            j += 1
        return new_row

    def slide_left(self):
        new_board = np.zeros_like(self.board)
        for i in range(self.size):
            new_board[i] = self.slide_and_merge_row_left(self.board[i])
        if not np.array_equal(self.board, new_board):
            self.board = new_board
            self.add_new_tile()

    def slide_right(self):
        self.board = np.fliplr(self.board)
        self.slide_left()
        self.board = np.fliplr(self.board)

    def slide_up(self):
        self.board = self.board.T
        self.slide_left()
        self.board = self.board.T

    def slide_down(self):
        self.board = self.board.T
        self.slide_right()
        self.board = self.board.T

    def can_move(self):
        if np.any(self.board == 0):
            return True
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i, j] == self.board[i, j + 1] or self.board[j, i] == self.board[j + 1, i]:
                    return True
        return False

    def update_gui(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.high_score_label.config(text=f"High Score: {self.high_score}")
        self.score_label.config(text=f"Score: {self.score}")
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                self.tiles[i][j].config(text=str(value) if value != 0 else '', bg=self.get_color(value))

    def get_color(self, value):
        colors = {
            0: '#cdc1b4', 2: '#eee4da', 4: '#ede0c8', 8: '#f2b179',
            16: '#f59563', 32: '#f67c5f', 64: '#f65e3b', 128: '#edcf72',
            256: '#edcc61', 512: '#edc850', 1024: '#edc53f', 2048: '#edc22e'
        }
        return colors.get(value, '#3c3a32')

    def key_handler(self, event):
        moves = {
            'Up': self.slide_up,
            'Down': self.slide_down,
            'Left': self.slide_left,
            'Right': self.slide_right
        }
        if event.keysym in moves:
            moves[event.keysym]()
            self.update_gui()
            if not self.can_move():
                self.end_game()

    def end_game(self):
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].config(bg='red')
        self.root.unbind('<Key>')

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
