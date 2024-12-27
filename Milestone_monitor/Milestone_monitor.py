import tkinter as tk
from tkinter import font, Label
import numpy as np
import os

root = tk.Tk()
root.title("Milestone Monitor")
bg_color = "#E5FFDA"
root.configure(bg=bg_color)


# Creating a heading frame
title_frame = tk.Frame(root, padx=5)
title_frame.pack(fill = 'both', expand = False, pady = (30, 0))
title_frame.configure(bg = bg_color)
title_frame.grid_rowconfigure(0, weight=1)
title_frame.grid_columnconfigure(0, weight=1)

label = tk.Label(title_frame, text="Milestone Monitor", font = ("Ubuntu", 23, 'bold'), bg=bg_color)
label.grid(sticky = 'nsew')

# Create a Frame with padding
padding_frame = tk.Frame(root, padx=20, pady=20)
padding_frame.pack(fill='both', expand=True)
padding_frame.configure(bg = bg_color)


#data to create Scene
months =[["January", "February", "March", "April", "May", "June"], ["July", "August", "September", "October", "November", "December"]]
color_palette = ["#C7FFCD", "#80DE8A", "#29C73A", "#00790D", "#003E07"]
buttons =  np.full((6,6,7,5), "default")
button_objects = []
month_rows = 6
month_columns = 6
inner_rows = 7
inner_columns = 5


def check_file():
    path = "Milestone_data.txt"
    if os.path.exists(path):
        return 1
    else:
        create_file()

def create_file():
    with open("Milestone_data.txt", "w") as f:
        for i in range(421):
            f.write(f"{color_palette[0]}\n")



def read_from_file():
    check_file()
    with open("Milestone_data.txt", "r") as f:
        list = [1, 3]
        for a in list:
            for b in range(6):
                for c in range(7):
                    for d in range(5):
                        buttons[a][b][c][d] = f.readline()


def get_grid():
    for i in range(month_rows):
        padding_frame.grid_rowconfigure(i, weight=1)

    for i in range(month_columns):
        padding_frame.grid_columnconfigure(i, weight=1)


# Adding widgets
def get_columns_names():
    for i in range(0,3,2):
        for j in range(month_columns):
            k = i
            if i>0:
                k = 1
            heading = tk.Label(padding_frame, text=months[k][j], font=("Helvetica", 16, "bold"), fg=color_palette[4] , bg=bg_color)
            heading.grid(row=i, column=j, padx=10, pady=10, sticky='sew')

def get_inner_grid():
    count = 0
    list = [1, 3]

    for h in list:
        for i in range(month_columns):
            tile = tk.Label(padding_frame, bg=bg_color)
            tile.grid(row=h, column=i, padx=10, pady=5, sticky="nsew")
            a = h
            b = i
            for i in range(inner_rows):
                tile.grid_rowconfigure(i, weight=1)

            for i in range(inner_columns):
                tile.grid_columnconfigure(i, weight=1)

            for j in range(inner_rows):
                for k in range(inner_columns):
                    c = j
                    d = k
                    check_file()
                    button = tk.Button(tile , bg=buttons[a][b][c][d], activebackground=buttons[a][b][c][d])
                    button.config(command=create_callback(button))
                    button.grid(row=j, column=k, padx=1, pady=1, sticky="nsew")
                    button_objects.append(button)

def create_callback(button):
    return lambda: change_color(button)

def change_color(button):
    # Change the button's background color on click
    new_color = color_palette[(color_palette.index(button.cget("bg"))+1)%5]
    button.config(bg=new_color, activebackground=new_color)
    button_objects[button_objects.index(button)] = button

def get_button_status():
    # Print the status of each button
    with open("Milestone_data.txt", "w") as f:
        for button in button_objects:
            text = button.cget("text")
            color = button.cget("bg")
            f.write(f"{color}\n")


# the legend widgets 1
label = tk.Label(padding_frame, text="Less", bg =bg_color, font= font.Font(size=15))
label.grid(row=5, column = 0, padx=1, pady=0, sticky="e")


# This is the Legend Tile 2
tile = tk.Label(padding_frame, bg = bg_color)
tile.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
tile.grid_columnconfigure(0, weight=1)
tile.grid_rowconfigure(0, weight=1)


# The legend subwedgets
for i in range(len(color_palette)):
    button = tk.Button(tile , bg=color_palette[i], activebackground=color_palette[i])
    button.grid(row=0, column=i, padx=1, pady=1, sticky="nsew")

# grid configure to ensure that all the widgets are aligned correctly
for i in range(len(color_palette) + 2):
    tile.grid_columnconfigure(i, weight=1)

# The legend Wedgets 3
label = tk.Label(padding_frame, text="More", bg = bg_color, font= font.Font(size=15))
label.grid(row=5, column=2, padx=0, pady=0, sticky="w")
tile.grid_rowconfigure(0, weight=1)




def save_button():
    button = tk.Button(padding_frame, text = "Save", font = ("Ubuntu", 15, 'bold'), command=get_button_status,bg= color_palette[0], fg = color_palette[4], activebackground=color_palette[1])
    button.grid(row = 5, column = 5, padx=10, pady=10, sticky="nsew")


get_grid()
read_from_file()
get_columns_names()
get_inner_grid()
save_button()
root.mainloop()