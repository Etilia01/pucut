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
sleeping= False
happynesscycle= True
petzoomed= pet.zoom(4)
petexpressions=["images/virtual pet 1.png", "images/virtual pet happy.png", "images/virtual pet sad.png", "images/virtual pet sleeping.png", "images/virtual pet tired.png", "images/virtual pet very happy.png"]
mainframe = Frame (
    bg= bg_color
)
mainframe.pack(pady=2, padx=2)

def hauptloop():
    global happyness, tired, pet, petzoomed
    
    if sleeping is False:
        if happynesscycle:
            if happyness <=10 and happyness >=0:
                happyness -=1
            if tired <=10 and tired >=0:
               tired -=1
        if happyness<=3 and tired>=3:
        #make bg music sad here
            pet = tkinter.PhotoImage(file= petexpressions[2])
        if happyness>=4 and tired>=3:
            pet = tkinter.PhotoImage(file= petexpressions[0])
        if happyness>=6 and tired>=3:
            pet = tkinter.PhotoImage(file= petexpressions[1])
        if happyness>=8 and tired>=3:
            pet = tkinter.PhotoImage(file= petexpressions[5])
        if tired<=3:
            pet= tkinter.PhotoImage(file= petexpressions[4])
        petzoomed= pet.zoom(4)
        pucut.config(image=petzoomed)
        print ("restarting loop")
        window.after(1000, hauptloop)

    #maybe i should update the window here? idk

def food():
    global happyness
    happyness +=1
def sleep():
    global pet, petzoomed, tired, sleeping
    sleeping = True
    if tired<=9:
        pet = tkinter.PhotoImage(file= petexpressions[3])
        petzoomed= pet.zoom(4)
        pucut.config(image=petzoomed)
        tired+=1
        print (tired)
        window.after(1000, sleep)
    else:
        pet = tkinter.PhotoImage(file= petexpressions[1])
        sleeping= False
        hauptloop()
def play():
    global happyness, tired
    happyness +=2
    tired-=1

pucut = tkinter.Label(mainframe, image=petzoomed, background= bg_color)
pucut.pack(anchor=S, pady=5)
food_button = tkinter.Button(
    mainframe,
    width=10, 
    height=5,  
    padx=2,         
    pady=2,             
    command=food,
    relief= None
)
food_button.pack(side=LEFT, padx=3)
sleep_button = tkinter.Button(
    mainframe,
    width=10, 
    height=5,  
    padx=2,         
    pady=2,             
    command=sleep,
)
sleep_button.pack(side=LEFT, padx=3)
play_button = tkinter.Button(
    mainframe,
    width=10, 
    height=5,  
    padx=2,         
    pady=2,             
    command=play,
)
play_button.pack(side=LEFT, padx=3)
hauptloop()
window.mainloop()