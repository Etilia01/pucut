from tkinter import *
import tkinter.messagebox
from tkinter import filedialog as fd
bg_color = "#313244"
font_color= "#cdd6f4"
window = Tk()
window.geometry("400x400")
window.title("Pucut <3")
icon_image = tkinter.PhotoImage(file="images/icon.png")
window.iconphoto(False, icon_image)
window.configure(background = bg_color)

window.mainloop()