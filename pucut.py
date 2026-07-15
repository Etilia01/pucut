#colorscheme: 574964, 9F8383, C8AAAA, FFDAB3
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog as fd
bg_color = "#574964"
font_color= "#FFDAB3"
happyness= 10
tired= 10
window = Tk()
window.geometry("400x400")
window.title("Pucut <3")
icon_image = tkinter.PhotoImage(file="images/icon.png")
window.iconphoto(False, icon_image)
window.configure(background = bg_color)
pet= PhotoImage(file="images/virtual pet 1.png")
petzoomed= pet.zoom(4)
petexpressions["images/virtual pet 1.png", "images/virtual pet happy.png", "images/virtual pet sad.png", "images/virtual pet sleeping.png", "images/virtual tired.png", "images/virtual pet very happy.png"]
mainframe = Frame (
    bg= bg_color
)
mainframe.pack(pady=2, padx=2)
def hauptloop():
    global happyness, tired, pet, petzoomed
    #wait few seconds idk how many yet
    happyness -=1
    if happyness<=3 and tired>=3:
        #make bg music sad here
        pet = petexpressions[3]
    if happyness>=4 and tired>=3:
        pet = petexpressions[1]
    if happyness>=6 and tired>=3:
        pet = petexpressions[2]
    if happyness>=8 and tired>=3:
        pet = petexpressions[6]
    if tired<=3:
        pet= petexpressions[5]
    petzoomed= pet.zoom(4)
    pucut.config(image=petzoomed)
pucut = tkinter.Label(mainframe, image=petzoomed, background= bg_color)
pucut.pack(anchor=S, pady=5)
window.mainloop()