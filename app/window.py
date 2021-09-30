from tkinter import *
import tkinter as tk
import os
from tkinter import PhotoImage
from datetime import datetime
from app.main import *


global state
global searchTF
searchTF = False
state = 0

window = tk.Tk()  # define window
window.geometry('400x600+850+50')
window.resizable(False, False)
window.title('MPirate3')

#  load images
parentPath = os.path.split(os.path.dirname(__file__))[0]
homeIcon = PhotoImage(file=f'{parentPath}/images/home.png')
searchIcon = PhotoImage(file=f'{parentPath}/images/search.png')
libraryIcon = PhotoImage(file=f'{parentPath}/images/library.png')

#  makes the window always on top and sets color hex 60b26c to transparent
window.wm_attributes('-transparentcolor', '#60b26c')
window.wm_attributes('-topmost', 1)


#  close screen with esc key
def close(event):
    now = datetime.now()
    time = now.strftime('%d/%m/%Y %H:%M:%S')

    file = open('temp/log', 'a+')
    file.write(f'{event} : {time}\n')
    file.close()

    sys.exit()  # close


def switchHome():
    global state
    global searchTF

    if state != 0 and searchTF is True:
        searchTF = False
        xCord = 10
        currWidth = 380
        for i in range(380):
            xCord += 0.5
            currWidth -= 1
            searchBox.place(x=xCord,
                            y=10,
                            width=currWidth,
                            height=38)
            window.update()
    state = 0
    loadMenu()


def switchSearch():
    global state
    global searchTF
    if state != 1 and searchTF is False:
        searchTF = True
        searchBox.delete(0, END)
        searchBox.insert(0, "Search For a Song, Artist or Playlist")
        state = 1
        xCord = 200
        currWidth = 0
        for i in range(380):
            xCord -= 0.5
            currWidth += 1
            searchBox.place(x=xCord,
                            y=10,
                            width=currWidth,
                            height=38)
            window.update()
    loadMenu()


def switchLibrary():
    global state
    global searchTF
    if state != 2 and searchTF is True:
        searchTF = False
        state = 2
        xCord = 10
        currWidth = 380
        for i in range(380):
            xCord += 0.5
            currWidth -= 1
            searchBox.place(x=xCord,
                            y=10,
                            width=currWidth,
                            height=38)
            window.update()
    loadMenu()


#  -----define look of frame-----
lowFrame = Frame(window,
                 bg='black')
mainFrame = Frame(window,
                  width=400,
                  height=600,
                  bg='#60b26c')
homeLabel = tk.Label(lowFrame,
                     text="",
                     font='Bahnschrift 30',
                     bg='black',
                     fg='gray17',
                     height=1,
                     padx=20)
homeBtn = tk.Button(lowFrame,
                    image=homeIcon,
                    bg='black',
                    bd=0,
                    activebackground='black',
                    command=switchHome)
searchBtn = tk.Button(lowFrame,
                      image=searchIcon,
                      bg='black',
                      bd=0,
                      activebackground='black',
                      command=switchSearch)
libraryBtn = tk.Button(lowFrame,
                       image=libraryIcon,
                       bg='black',
                       bd=0,
                       activebackground='black',
                       command=switchLibrary)

searchBox = tk.Entry(window,
                     bg='grey17',
                     fg='white',
                     font='SansSerif 12',
                     insertbackground='white',
                     bd=0)

lowFrame.pack(side='bottom',
              fill=tk.X)
mainFrame.pack()
homeLabel.pack(side='right')
homeBtn.place(x=80,
              y=0)
searchBtn.place(x=180,
                y=0)
libraryBtn.place(x=280,
                 y=5)


def loadMenu():
    if state == 0:  # home state
        searchBox.place_forget()

    elif state == 1:  # search state
        pass
    elif state == 2:  # library state
        searchBox.place_forget()


def delText(event):
    if (searchBox.get() == 'Search For a Song, Artist or Playlist'):
        searchBox.delete(0, END)


def linearSearch(event):
    query = searchBox.get()
    songs = []
    playlists = []

    # get playlists
    playlists = os.listdir(os.path.split(os.path.dirname(__file__))[0] + r'\Songs')
    for i in range(len(playlists)):
        playlists[i] = os.path.split(os.path.dirname(__file__))[0] + r'\songs' + '\\' + f'{playlists[i]}'

    # get songs
    for i in range(len(playlists)):
        for file in os.listdir(playlists[i]):
            if file.endswith('.mp3'):
                songs.append(os.path.join(playlists[i], file))

    print(playlists)
    print(songs)


loadMenu()

#  exits app when ESC key is pressed
window.bind('<Escape>', close)
searchBox.bind('<Button-1>', delText)
searchBox.bind('<Return>', linearSearch)


window.mainloop()
