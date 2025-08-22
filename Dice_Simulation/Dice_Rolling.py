import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Dice Rolling")
root.geometry("300x400")
root.configure(background="#ffb6c1")

# list of the given images (use forward slashes)
img_list = [
    "Dice_Simulation/d1.png",
    "Dice_Simulation/d2.png",
    "Dice_Simulation/d3.png",
    "Dice_Simulation/d4.png",
    "Dice_Simulation/d5.png",
    "Dice_Simulation/d6.png"
]

lbl = tk.Label(root, font="Lucida 16", bg="#ffb6c1")
lbl.pack(pady=10)

# keep a reference to the current image
current_image = None

def pressed():
    global current_image
    choose_img = random.choice(img_list)
    current_image = ImageTk.PhotoImage(Image.open(choose_img))
    lbl.configure(image=current_image)

btn_rolled = tk.Button(
    root,
    text="Roll Dice",
    font="Lucida 14",
    bg="#ff1493",
    fg="Black",
    width=20,
    command=pressed
)
btn_rolled.pack(pady=20)

root.mainloop()
