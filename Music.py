# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 08:18:37 2020

@author: Vismay Shah
"""
#%% import
from os import chdir
from os import listdir
from pygame import mixer as mxr
from random import choice
#%% tkinter imports
from tkinter import Scrollbar
from tkinter import HORIZONTAL
from tkinter import VERTICAL
from tkinter import ACTIVE
from tkinter import SINGLE
from tkinter import Tk
from tkinter import Listbox
from tkinter import StringVar
from tkinter import Label
from tkinter import Scale
from tkinter import Button as Btn
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font 
#%% window
window=Tk()
mxr.init()
#%% music window
window.title("Music Player by Vismay")
window.geometry("600x900")

#%% vol control    
vollevel=Scale(window,from_=0,to_=1.0,orient=HORIZONTAL,resolution=0.01,bg='sky blue')



#%% song mane
var=StringVar()
songtitle=Label(window,textvariable=var)

#%% functions
        
def play():
    mxr.music.load(playlist.get(ACTIVE))
    mxr.music.set_volume(vollevel.get())
    mxr.music.play()
    var.set(playlist.get(ACTIVE))  
    
def pause():
    mxr.music.pause()

def resume():
    mxr.music.unpause()
    
def rewind():
    mxr.music.rewind()
      
def stop():
    mxr.music.stop()
    
def selectfolder():
    foldername=filedialog.askdirectory()
    return foldername

def nextsong():
    global songlist
    songlist = songlist[1:] +[songlist[0]] # move current song to the back of the list
    mxr.music.load(songlist[0])
    mxr.music.play()
     
def randomsong():
    global var,songlist
    var=choice(songlist)
    mxr.music.load(var)
    mxr.music.set_volume(vollevel.get())
    mxr.music.play()


#%%


messagebox.showinfo("How to use",'Hello !\nPLease Note the following !\nSelect a folder with music files in it.\nYou need to replay the song after adjusting the volume.\nContact me if u are facing any problems.\nEnjoy !!')
#%% playlist pt1

x=selectfolder()
chdir(x)
songlist=listdir()

#%% scroll bar

scrollbar1=Scrollbar(window,orient=VERTICAL)

#%%playlist pt2
playlist=Listbox(window,bg='Pale Turquoise3',highlightcolor='saddlebrown',selectmode=SINGLE,yscrollcommand=scrollbar1.set(0.001,0.2))

playlist.config(yscrollcommand=scrollbar1.set)

scrollbar1.config(command=playlist.yview)



print(songlist.reverse()) # prints the list in alphabetical order

for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos+=1
    

#%%fonts
font1 = font.Font(family = 'Lucida Sans Typewriter',size= 12)
font1_bold = font.Font(family = 'Lucida Sans Typewriter',size= 12, weight = 'bold')
#%% buttons
    
Button1=Btn(window,width=5,height=3,font=font1_bold,text="Play",bg='OliveDrab1',activebackground='lemon chiffon',activeforeground='burlywood4',command=play)
Button2=Btn(window,width=5,height=3,font=font1_bold,text="Stop",bg='OrangeRed3',highlightcolor='wheat1',activebackground='navajowhite4',activeforeground='cyan',command=stop)
Button3=Btn(window,width=5,height=3,font=font1_bold,text="Pause",bg='OliveDrab2',activebackground='lemon chiffon',activeforeground='burlywood4',command=pause)
Button4=Btn(window,width=5,height=3,font=font1_bold,text="Resume",bg='DarkOliveGreen2',activebackground='lemon chiffon',activeforeground='burlywood4',command=resume)
Button5=Btn(window,width=5,height=3,font=font1_bold,text="Rewind",bg='DarkOliveGreen1',activebackground='lemon chiffon',activeforeground='burlywood4',command=rewind) 
Button6=Btn(window,width=5,height=3,font=font1_bold,text="Next Song",bg='DarkOliveGreen1',activebackground='lemon chiffon',activeforeground='burlywood4',command=nextsong)
Button7=Btn(window,width=5,height=3,font=font1_bold,text="Shuffle",bg='DarkOliveGreen2',activebackground='lemon chiffon',activeforeground='burlywood4',command=randomsong)

#%%pack 
songtitle.pack(side='top',fill='both')

Button2.pack(side='bottom',fill='both',pady=4,padx=4)
Button5.pack(side='bottom',fill='both',pady=4,padx=4)
Button6.pack(side='bottom',fill='both',pady=4,padx=4)
Button7.pack(side='bottom',fill='both',pady=4,padx=4)
Button4.pack(side='bottom',fill='both',pady=4,padx=4)
Button3.pack(side='bottom',fill='both',pady=4,padx=4)
Button1.pack(side='bottom',fill='both',pady=4,padx=4)

scrollbar1.pack(side='right',fill='y')

vollevel.pack(fill='x')

playlist.pack(fill='both',expand='yes')

#%%
window.mainloop()