#colorscheme: 574964, 9F8383, C8AAAA, FFDAB3
# basics almost done, to-do: adding (more) variants, maybe a mini-game for playing? also "time without incident" and "record time"
#planned variants: foresty, bot  maybe?
import ctypes
import os
import pygame
from tkinter import *
from tkinter import font as f
import tkinter.messagebox
from tkinter import filedialog as fd
import random
bg_color = "#574964"
font_color= "#FFDAB3"
happyness= 10
tired= 10
window = Tk()
window.geometry("420x580")
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
playbutton= PhotoImage(file="images/play.png")
bigplaybutton= playbutton.zoom(2)
foodbutton= PhotoImage(file="images/food.png")
bigfoodbutton= foodbutton.zoom(2)
sleepbutton= PhotoImage(file="images/sleep.png")
bigsleepbutton= sleepbutton.zoom(2)
petexpressions=["images/virtual pet 1.png", "images/virtual pet happy.png", "images/virtual pet sad.png", "images/virtual pet sleeping.png", "images/virtual pet tired.png", "images/virtual pet very happy.png", "images/virtual pet 2.png"]
pygame.init()
pygame.mixer.music.load("music/happy song.mp3")
pygame.mixer.music.play()
nameset = tkinter.StringVar()
fontpath1 = os.path.abspath("fonts/Kablammo/Kablammo-Regular-VariableFont_MORF.ttf")
fontpath2 = os.path.abspath("fonts/Rubik_Glitch/RubikGlitch-Regular.ttf")
current_variant= "none"
commonvariants= ["regular", "space", "red"]
uncommonvariants= ["lolita"]
variantchance= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
loopwithoutminus= False
readablemode= False
incident= False
longesttimewithoutincident= 0
timewithoutincident= 0
incidentcounter1= None
incidentcounter2= None
happinesscounter= None
tiredcounter= None

try:
    libfc = ctypes.CDLL("libfontconfig.so.1")
    ttf1 = fontpath2.encode('utf-8')
    ttf2 = fontpath1.encode('utf-8')
    libfc.FcConfigAppFontAddFile(None, ttf1)
    libfc.FcConfigAppFontAddFile(None, ttf2)
except Exception as e:
    print(f"Font couldnt be loaded cuz {e}")
font1 = f.Font(family="Rubik Glitch", size=15)
font2 = f.Font(family="Kablammo", size=15)

edge1 = tkinter.Label(window, image=edgedecor1, background= bg_color)
edge1.place(relx=0.0, rely=0.0, anchor=tkinter.NW)
edge2 = tkinter.Label(window, image=edgedecor2big, background= bg_color)
edge2.place(relx=1.0, rely=0.0, anchor=tkinter.NE)
edge3 = tkinter.Label(window, image=edgedecor3big, background= bg_color)
edge3.place(relx=1.0, rely=1.0, anchor=tkinter.SE)
edge4 = tkinter.Label(window, image=edgedecor4big, background= bg_color)
edge4.place(relx=0.0, rely=1.0, anchor=tkinter.SW)
mainframe = Frame (
    bg= bg_color
)
buttonframe = Frame (
    mainframe,
    bg =bg_color
)
mainframe.pack(pady=50, padx=2)


def setname():
    global petname
    petname= nameset.get()
    file = open("save.txt","w")
    file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
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
    global petname, musicactive, current_variant, petexpressions, loopwithoutminus, readablemode, longesttimewithoutincident
    file = open("save.txt","r")
    file_list = eval(file.read())
    file.close()
    petname, musicactive, current_variant, readablemode, longesttimewithoutincident= file_list
    if current_variant== "none":
        chance= random.choice(variantchance)
        if chance==1:
            current_variant= random.choice(uncommonvariants)
        else:
            current_variant= random.choice(commonvariants)
        file = open("save.txt","w")
        file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
        file.close()
        print(current_variant)
    if petname== "none":
        print("name is none")
        namepet()
    else:
        desc.config(text= petname +  " says hi!")
    if musicactive== False:
        pygame.mixer.music.stop()
    if current_variant== "space":
        petexpressions=["images/space 1.png", "images/space happy.png", "images/space sad.png", "images/space sleeping.png", "images/space tired.png", "images/space very happy.png", "images/space 2.png"]
        loopwithoutminus = True
        hauptloop()
    if current_variant== "lolita":
        petexpressions=["images/cutet 1.png", "images/cute happy.png", "images/cute sad.png", "images/cute sleeping.png", "images/cute tired.png", "images/cute very happy.png", "images/cute 2.png"]
        loopwithoutminus = True
        hauptloop()
    if current_variant== "red":
        petexpressions=["images/r 1.png", "images/r happy.png", "images/r sad.png", "images/r sleeping.png", "images/r tired.png", "images/r very happy.png", "images/r 2.png"]
        loopwithoutminus = True
        hauptloop()
    if readablemode:
        desc.config(font= "Arial")
    incidentloop()
def hauptloop():
    global happyness, tired, pet, petzoomed, loopwithoutminus, incident
    
    if sleeping is False and loopwithoutminus== False:
        if happynesscycle:
            if happyness >=0:
                happyness -=1
            if tired >=0:
               tired -=1
        if happyness<=3 and tired>=3:
        #make bg music sad here
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[2])
            if readablemode== False:
                desc.config(text= petname +  " is sad :(", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " is sad :(", font= "Arial", fg= font_color)
        if happyness>=4 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[0])
            if readablemode== False:
                desc.config(text= petname +  " doesnt feel so great", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " doesnt feel so great", font= "Arial", fg= font_color)
        if happyness>=6 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[1])
            if readablemode== False:
                desc.config(text= petname +  " feels alright!", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " feels alright!", font= "Arial", fg= font_color)
        if happyness>=8 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[5])
            if readablemode== False:
                desc.config(text= petname +  " is very happy and feels loved :D", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " is very happy and feels loved :D", font= "Arial", fg= font_color)
        if tired<=3 and happyness >=2:
            incident=False
            pet= tkinter.PhotoImage(file= petexpressions[4])
            if readablemode== False:
                desc.config(text= petname +  " is very tired and slowly sinking into existential dread.", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " is very tired and slowly sinking into existential dread.", font= "Arial", fg= font_color)
        if tired<=3 and happyness <=1:
            incident=True
            pet= tkinter.PhotoImage(file= petexpressions[6])
            if readablemode== False:
                desc.config(text= "IzhsbskuoIGUFVsuiazgboa", font= font1, fg= "black")
            else:
                desc.config(text= "IzhsbskuoIGUFVsuiazgboa", font= "Arial", fg= "black")
    
        petzoomed= pet.zoom(4)
        pucut.config(image=petzoomed)
        print ("restarting loop")
        window.after(10000, hauptloop)
    if sleeping== False and loopwithoutminus == True:
        if happyness<=3 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[2])
            if readablemode== False:
                desc.config(text= petname +  " is sad :(", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " is sad :(", font= "Arial", fg= font_color)
        if happyness>=4 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[0])
            if readablemode== False:
                desc.config(text= petname +  " doesnt feel so great", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " doesnt feel so great", font= "Arial", fg= font_color)
        if happyness>=6 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[1])
            if readablemode== False:
                desc.config(text= petname +  " feels alright!", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " feels alright!", font= "Arial", fg= font_color)
        if happyness>=8 and tired>=3:
            incident=False
            pet = tkinter.PhotoImage(file= petexpressions[5])
            if readablemode== False:
                desc.config(text= petname +  " is very happy and feels loved :D", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " is very happy and feels loved :D", font= "Arial", fg= font_color)
        if tired<=3 and happyness >=2:
            incident=False
            pet= tkinter.PhotoImage(file= petexpressions[4])
            if readablemode== False:
                desc.config(text= petname +  " is very tired and slowly sinking into existential dread.", font= font2, fg= font_color)
            else:
                desc.config(text= petname +  " is very tired and slowly sinking into existential dread.", font= "Arial", fg= font_color)
        if tired<=3 and happyness <=1:
            incident=True
            pet= tkinter.PhotoImage(file= petexpressions[6])
            if readablemode== False:
                desc.config(text= "IzhsbskuoIGUFVsuiazgboa", font= font1, fg= "black")
            else:
                desc.config(text= "IzhsbskuoIGUFVsuiazgboa", font= "Arial", fg= "black")
        petzoomed= pet.zoom(4)
        pucut.config(image=petzoomed)
        loopwithoutminus= False
        window.after(10000, hauptloop)
    

    #maybe i should update the window here? idk
def incidentloop():
    global incident, longesttimewithoutincident, timewithoutincident
    if incident==False:
        timewithoutincident +=1
        if longesttimewithoutincident<=timewithoutincident:
            longesttimewithoutincident= timewithoutincident
            file = open("save.txt","w")
            file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
            file.close()
    else:
        timewithoutincident= 0
    window.after(1000, incidentloop)
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
        if happyness<=5 and musictone!= "sad" and tired >=4:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/sad song.mp3")
            pygame.mixer.music.play()
            musictone= "sad"
        if happyness>=6 and musictone!= "happy":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/happy song.mp3")
            pygame.mixer.music.play()
            musictone= "happy"
        if tired<=3 and happyness <=1 and musictone!= "eldritch":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/better eldritch.mp3")
            pygame.mixer.music.play()
            musictone= "eldritch"
        window.after(1000, musicloop)

def food():
    global happyness, loopwithoutminus
    if happyness <= 10:
        happyness +=1
        loopwithoutminus = True
        hauptloop()
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
    global happyness, tired, loopwithoutminus
    if happyness <=10:
        happyness +=2
        tired-=1
        loopwithoutminus = True
        hauptloop()
    else:
        desc.config(text= petname + " is already very happy and doesnt want to play!")
    
def newtype():
    global current_variant, petexpressions, loopwithoutminus
    chance= random.choice(variantchance)
    if chance==2:
        current_variant= random.choice(uncommonvariants)
    else:
        current_variant= random.choice(commonvariants)
    file = open("save.txt","w")
    file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
    file.close()
    print(current_variant)
    if current_variant== "space":
        petexpressions=["images/space 1.png", "images/space happy.png", "images/space sad.png", "images/space sleeping.png", "images/space tired.png", "images/space very happy.png", "images/space 2.png"]
        loopwithoutminus = True
        hauptloop()
    if current_variant=="regular":
        petexpressions=["images/virtual pet 1.png", "images/virtual pet happy.png", "images/virtual pet sad.png", "images/virtual pet sleeping.png", "images/virtual pet tired.png", "images/virtual pet very happy.png", "images/virtual pet 2.png"]
        loopwithoutminus = True
        hauptloop()
    if current_variant=="lolita":
        petexpressions=["images/cutet 1.png", "images/cute happy.png", "images/cute sad.png", "images/cute sleeping.png", "images/cute tired.png", "images/cute very happy.png", "images/cute 2.png"]
        loopwithoutminus = True
        hauptloop()

def changereadablemode():
    global readablemode, loopwithoutminus
    if readablemode:
        readablemode=False
    else:
        readablemode= True 
    file = open("save.txt","w")
    file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
    file.close()
    loopwithoutminus= True
    hauptloop()     

def open_settings():
    settings_win = tkinter.Toplevel(
        bg= bg_color,)
    settings_win.title("Settings")
    settings_win.geometry("250x200")
    settings_win.attributes('-topmost', True)
    edge12 = tkinter.Label(settings_win, image=edgedecor, background= bg_color)
    edge12.place(relx=0.0, rely=0.0, anchor=tkinter.NW)
    edge22 = tkinter.Label(settings_win, image=edgedecor2, background= bg_color)
    edge22.place(relx=1.0, rely=0.0, anchor=tkinter.NE)
    edge32 = tkinter.Label(settings_win, image=edgedecor3, background= bg_color)
    edge32.place(relx=1.0, rely=1.0, anchor=tkinter.SE)
    edge42 = tkinter.Label(settings_win, image=edgedecor4, background= bg_color)
    edge42.place(relx=0.0, rely=1.0, anchor=tkinter.SW)
    anotherframe = Frame (
    settings_win,
    bg =bg_color
    )
    anotherframe.pack(pady=10, padx=2)
    submit = tkinter.Button(
    anotherframe,
    text="Disable/Enable Music",   
    padx=1,         
    pady=2,             
    command=musicsettings,
    bg= "#9F8383",
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= "#C8AAAA",)
    submit.pack(pady=10)
    readable = tkinter.Button(
    anotherframe,
    text="Disable/Enable Readable Mode",   
    padx=1,         
    pady=2,             
    command=changereadablemode,
    bg= "#9F8383",
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= "#C8AAAA",)
    readable.pack(pady=10)
    submit2 = tkinter.Button(
    anotherframe,
    text="Rename your Pucut",   
    padx=1,         
    pady=2,             
    command=namepet,
    bg= "#9F8383",
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= "#C8AAAA",)
    submit2.pack(pady=10)
    submit3 = tkinter.Button(
    anotherframe,
    text="Reroll Pucut Type",   
    padx=1,         
    pady=2,             
    command=newtype,
    bg= "#9F8383",
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= "#C8AAAA",)
    submit3.pack(pady=10)


def open_numberwin():
    global incidentcounter1, incidentcounter2, happinesscounter, tiredcounter
    number_win = tkinter.Toplevel(
        bg= bg_color,)
    number_win.title("Settings")
    number_win.geometry("235x225")
    number_win.attributes('-topmost', True)
    statsheading= tkinter.Label(number_win, text= "Health & More", background=bg_color, fg=font_color, font= 15)
    statsheading.pack(pady=10)
    idkframe = Frame(
        number_win,
        bg=bg_color
    )
    idkframe.pack(pady=10)
    idkframe2 = Frame(
        number_win,
        bg=bg_color
    )
    idkframe2.pack(pady=10)
    edge13 = tkinter.Label(number_win, image=edgedecor, background= bg_color)
    edge13.place(relx=0.0, rely=0.0, anchor=tkinter.NW)
    edge23 = tkinter.Label(number_win, image=edgedecor2, background= bg_color)
    edge23.place(relx=1.0, rely=0.0, anchor=tkinter.NE)
    edge33 = tkinter.Label(number_win, image=edgedecor3, background= bg_color)
    edge33.place(relx=1.0, rely=1.0, anchor=tkinter.SE)
    edge43 = tkinter.Label(number_win, image=edgedecor4, background= bg_color)
    edge43.place(relx=0.0, rely=1.0, anchor=tkinter.SW)
    
    incidentcounter1= tkinter.Label(idkframe, text= "Time since last incident: " + str(timewithoutincident), background=bg_color, fg=font_color)
    incidentcounter1.pack(pady=5)
    incidentcounter2= tkinter.Label(idkframe, text= "Record time since last incident: " + str(longesttimewithoutincident), background=bg_color, fg=font_color)
    incidentcounter2.pack(pady= 5)
    happinesscounter= tkinter.Label(idkframe2, text= "Happiness: " + str(happyness), background=bg_color, fg=font_color)
    happinesscounter.pack(pady=5)
    tiredcounter= tkinter.Label(idkframe2, text= "Tiredness: " + str(tired), background=bg_color, fg=font_color)
    tiredcounter.pack(pady= 5)
    update_cycle()

def update_cycle():
    if incidentcounter1 is not None:
        incidentcounter1.config(text= "Time since last incident: " + str(timewithoutincident))
        incidentcounter2.config(text= "Record time since last incident: " + str(longesttimewithoutincident))
        happinesscounter.config(text= "Happiness: " + str(happyness))
        tiredcounter.config(text= "Tiredness: " + str(tired))
        window.after(1000, update_cycle)    

    
def musicsettings():
    global musicactive
    if musicactive:
        musicactive= False
        pygame.mixer.music.stop()
        file = open("save.txt","w")
        file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
        file.close()
    else:
        musicactive = True
        musicloop()
        file = open("save.txt","w")
        file.write(str([petname, musicactive, current_variant, readablemode, longesttimewithoutincident]))
        file.close()

buttonframe.pack(pady=1, padx=1)
framebelowbutton = Frame (
    mainframe,
    bg =bg_color
)
framebelowbutton.pack(pady=1, padx=1)

food_button = tkinter.Button(
    buttonframe,
    width=60, 
    height=60,  
    padx=4,         
    pady=4,             
    command=food,
    image= bigfoodbutton,
    text= "food",
    bg= "#9F8383",
    activebackground= "#C8AAAA",
    bd= 2,
    fg= font_color,
    highlightthickness=0
)
food_button.pack(side=LEFT, padx=3)
sleep_button = tkinter.Button(
    buttonframe,
    width=60, 
    height=60,  
    padx=4,         
    pady=4,             
    command=sleep,
    image= bigsleepbutton,
    text = "sleep",
    bg= "#9F8383",
    activebackground= "#C8AAAA",
    bd= 2,
    fg= font_color,
    highlightthickness=0
)
sleep_button.pack(side=LEFT, padx=3)
play_button = tkinter.Button(
    buttonframe,
    width=60, 
    height=60,  
    padx=4,         
    pady=4,             
    command=play,
    text= "play",
    image= bigplaybutton,
    bg= "#9F8383",
    activebackground= "#C8AAAA",
    bd= 2,
    fg= font_color,
    highlightthickness=0
)
play_button.pack(side=LEFT, padx=3)
label1= tkinter.Label(framebelowbutton, background= bg_color, text= "food", fg= font_color)
label1.pack(side=LEFT, pady=3, padx=32)
label2= tkinter.Label(framebelowbutton, background= bg_color, text= "sleep", fg= font_color)
label2.pack(side=LEFT, pady=3, padx=5)
label3= tkinter.Label(framebelowbutton, background= bg_color, text= "play", fg= font_color)
label3.pack(side=LEFT, pady=3, padx=32)
#happiness= tkinter.Label(mainframe, background= bg_color, text= "Happiness: " + str(happyness), fg= font_color)
#happiness.pack(side=LEFT, pady=3, padx=1)
pucut = tkinter.Label(mainframe, image=petzoomed, background= bg_color)
pucut.pack(anchor=S, pady=5)
desc= tkinter.Label(mainframe, background= bg_color, text= petname + " is happy", font= font2, fg= font_color, wraplength=300
)
desc.pack(anchor=S, pady=3)
morebuttonframe = Frame (
    mainframe,
    bg =bg_color
)
morebuttonframe.pack(side= BOTTOM)
settings_button = tkinter.Button(
    morebuttonframe,
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
settings_button.pack(side= LEFT, padx=5, pady= 20)
stats_button = tkinter.Button(
    morebuttonframe,
    text="Health & More", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    bg= bg_color,
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= bg_color,
    command=open_numberwin)

stats_button.pack(side= LEFT, padx=5, pady= 20)


hauptloop()
musicloop()
iniiiiiit()
window.mainloop()