#colorscheme: 574964, 9F8383, C8AAAA, FFDAB3
import pygame
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
musicactive = True
musictone = "happy"
petname= "none"
happynesscycle= True
petzoomed= pet.zoom(4)
petexpressions=["images/virtual pet 1.png", "images/virtual pet happy.png", "images/virtual pet sad.png", "images/virtual pet sleeping.png", "images/virtual pet tired.png", "images/virtual pet very happy.png"]
pygame.init()
pygame.mixer.music.load("music/happy song.mp3")
pygame.mixer.music.play()
nameset = tkinter.StringVar()
mainframe = Frame (
    bg= bg_color
)
buttonframe = Frame (
    mainframe,
    bg =bg_color
)
buttonframe.pack(pady=1, padx=1)
mainframe.pack(pady=2, padx=2)
def setname():
    global petname
    petname= nameset.get()
    
def namepet():
    name_win = tkinter.Toplevel(
        bg= bg_color,)
    name_win.title("Name your Pucut!")
    name_win.geometry("200x200")
    name_win.attributes('-topmost', True)
    nameentry = tkinter.Entry(name_win, textvariable=nameset)
    nameentry.pack(pady=15)
    submit = tkinter.Button(
    name_win,
    text="Name your Pucut!!! :DD",   
    padx=0.5,         
    pady=2,             
    command=setname)
    submit.pack(pady=5)
def iniiiiiit():
    global petname
    file = open("save.txt","r")
    file_list = eval(file.read())
    file.close()
    petname= file_list
    if petname== "none":
        print("name is none")
        namepet()
def hauptloop():
    global happyness, tired, pet, petzoomed
    
    if sleeping is False:
        if happynesscycle:
            if happyness >=0:
                happyness -=1
            if tired >=0:
               tired -=1
        if happyness<=3 and tired>=3:
        #make bg music sad here
            pet = tkinter.PhotoImage(file= petexpressions[2])
            desc.config(text= petname +  " is sad :(")
        if happyness>=4 and tired>=3:
            pet = tkinter.PhotoImage(file= petexpressions[0])
            desc.config(text= petname +  " doesnt feel so great")
        if happyness>=6 and tired>=3:
            pet = tkinter.PhotoImage(file= petexpressions[1])
            desc.config(text= petname +  " feels alright!")
        if happyness>=8 and tired>=3:
            pet = tkinter.PhotoImage(file= petexpressions[5])
            desc.config(text= petname +  " is very happy and feels loved :D")
        if tired<=3:
            pet= tkinter.PhotoImage(file= petexpressions[4])
            desc.config(text= petname +  " is very tired and slowly sinking into existential dread.")
        petzoomed= pet.zoom(4)
        pucut.config(image=petzoomed)
        print ("restarting loop")
        window.after(1000, hauptloop)

    #maybe i should update the window here? idk
def musicloop():
    global musictone
    if musicactive:
        if not pygame.mixer.music.get_busy():
            if happyness<=5:
                pygame.mixer.music.load("music/sad song.mp3")
                pygame.mixer.music.play()
                musictone= "sad"
            else:
                pygame.mixer.music.load("music/happy song.mp3")
                pygame.mixer.music.play()
                musictone= "happy"
        if happyness<=5 and musictone== "happy":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/sad song.mp3")
            pygame.mixer.music.play()
            musictone= "sad"
        if happyness>=6 and musictone== "sad":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/happy song.mp3")
            pygame.mixer.music.play()
            musictone= "happy"
        window.after(1000, musicloop)

def food():
    global happyness
    if happyness <= 10:
        happyness +=1
    else:
        desc.config(text= petname + " is already full. Maybe later :]")
    print (happyness)
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
    if happyness <=10:
        happyness +=2
        tired-=1
    else:
        desc.config(text= petname + " is already very happy and doesnt want to play!")


food_button = tkinter.Button(
    buttonframe,
    width=10, 
    height=2,  
    padx=2,         
    pady=2,             
    command=food,
    text= "food"
)
food_button.pack(side=LEFT, padx=3)
sleep_button = tkinter.Button(
    buttonframe,
    width=10, 
    height=2,  
    padx=2,         
    pady=2,             
    command=sleep,
    text = "sleep"
)
sleep_button.pack(side=LEFT, padx=3)
play_button = tkinter.Button(
    buttonframe,
    width=10, 
    height=2,  
    padx=2,         
    pady=2,             
    command=play,
    text= "play"
)
play_button.pack(side=LEFT, padx=3)
pucut = tkinter.Label(mainframe, image=petzoomed, background= bg_color)
pucut.pack(anchor=S, pady=5)
desc= tkinter.Label(mainframe, background= bg_color, text= petname + " is happy")
desc.pack(anchor=S, pady=3)
hauptloop()
musicloop()
iniiiiiit()
window.mainloop()