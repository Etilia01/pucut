#colorscheme: 574964, 9F8383, C8AAAA, FFDAB3
# basics almost done, to-do for tmmrw: longer happyiness cycles, styling, maybe a mini-game for playing?
import pygame
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog as fd
bg_color = "#574964"
font_color= "#FFDAB3"
happyness= 10
tired= 10
window = Tk()
window.geometry("380x500")
window.title("Pucut <3")
icon_image = tkinter.PhotoImage(file="images/icon.png")
window.iconphoto(False, icon_image)
window.configure(background = bg_color)
pet= PhotoImage(file="images/virtual pet 1.png")
edgedecor= PhotoImage(file="images/edge decor.png")
edgedecor1= edgedecor.zoom(3)
edgedecor2 = PhotoImage(file="images/edge2.png")
edgedecor3 = PhotoImage(file="images/edge3.png")
edgedecor4 = PhotoImage(file="images/edge4.png")
edgedecor2big = edgedecor2.zoom(3)
edgedecor3big = edgedecor3.zoom(3)
edgedecor4big = edgedecor4.zoom(3)
sleeping= False
musicactive = True
musictone = "happy"
petname= "none"
happynesscycle= True
petzoomed= pet.zoom(4)
petexpressions=["images/virtual pet 1.png", "images/virtual pet happy.png", "images/virtual pet sad.png", "images/virtual pet sleeping.png", "images/virtual pet tired.png", "images/virtual pet very happy.png", "images/virtual pet 2.png"]
pygame.init()
pygame.mixer.music.load("music/happy song.mp3")
pygame.mixer.music.play()
nameset = tkinter.StringVar()
edge1 = tkinter.Label(window, image=edgedecor1, background= bg_color)
edge1.pack(side=tkinter.TOP, anchor=tkinter.NW)
edge2 = tkinter.Label(window, image=edgedecor2big, background= bg_color)
edge2.pack(side=tkinter.TOP, anchor=tkinter.NE)

mainframe = Frame (
    bg= bg_color
)
buttonframe = Frame (
    mainframe,
    bg =bg_color
)
mainframe.pack(pady=35, padx=2)


def setname():
    global petname
    petname= nameset.get()
    file = open("save.txt","w")
    file.write(str([petname, musicactive]))
    file.close()
    
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
    padx=1,         
    pady=2,             
    command=setname)
    submit.pack(pady=5)
def iniiiiiit():
    global petname, musicactive
    file = open("save.txt","r")
    file_list = eval(file.read())
    file.close()
    petname, musicactive= file_list
    if petname== "none":
        print("name is none")
        namepet()
    if musicactive== False:
        pygame.mixer.music.stop()
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
        if tired<=3 and happyness >=2:
            pet= tkinter.PhotoImage(file= petexpressions[4])
            desc.config(text= petname +  " is very tired and slowly sinking into existential dread.")
        if tired<=3 and happyness <=1:
            pet= tkinter.PhotoImage(file= petexpressions[6])
            desc.config(text= petname +  " IzhsbskuoIGUFVsuiazgboa")
        petzoomed= pet.zoom(4)
        pucut.config(image=petzoomed)
        print ("restarting loop")
        window.after(10000, hauptloop)

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
def open_settings():
    settings_win = tkinter.Toplevel(
        bg= bg_color,)
    settings_win.title("Settings")
    settings_win.geometry("200x200")
    settings_win.attributes('-topmost', True)
    
    submit = tkinter.Button(
    settings_win,
    text="Disable/Enable Music",   
    padx=1,         
    pady=2,             
    command=musicsettings)
    submit.pack(pady=5)
    submit2 = tkinter.Button(
    settings_win,
    text="Rename your Pucut",   
    padx=1,         
    pady=2,             
    command=namepet)
    submit2.pack(pady=5)
def musicsettings():
    global musicactive
    if musicactive:
        musicactive= False
        pygame.mixer.music.stop()
        file = open("save.txt","w")
        file.write(str([petname, musicactive]))
        file.close()
    else:
        musicactive = True
        musicloop()
        file = open("save.txt","w")
        file.write(str([petname, musicactive]))
        file.close()

buttonframe.pack(pady=1, padx=1)

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
settings_button = tkinter.Button(
    mainframe,
    text="Settings", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    bg= bg_color,
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= bg_color,
    command=open_settings)
settings_button.pack(side= BOTTOM, padx=20, pady= 20)
edge3 = tkinter.Label(window, image=edgedecor3big, background= bg_color)
edge3.pack(side=tkinter.BOTTOM, anchor=tkinter.SE)
edge4 = tkinter.Label(window, image=edgedecor4big, background= bg_color)
edge4.pack(side=tkinter.BOTTOM, anchor=tkinter.SW)
hauptloop()
musicloop()
iniiiiiit()
window.mainloop()