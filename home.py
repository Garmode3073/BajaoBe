from tkinter import *
from tkinter import filedialog
import pygame
from eyed3 import id3
import tkinter.messagebox
from mutagen.mp3 import MP3
import os
import threading
import time
import sys


# for exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# file to be played
fileop = ''
play = False
stop = True
tag = id3.Tag()
mute = False
time_format = '00 : 00'
time_length = 0
restart = False
index_playlist = 0
playlist_music = {}
has_called = False
t1 = threading.Thread()

# create and edit tkinter window
player = Tk()
player.title("BajaoBe")
player.geometry("1000x700")
player.config(bg='DarkOrchid4')
datafile = "F:\\python\\BajaoBe\\icon.ico"
if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), datafile)
else:
    datafile = os.path.join(sys.prefix, datafile)
pygame.init()
pygame.mixer.init()
player.iconbitmap(default=resource_path(datafile))

# center panel
center_panel = Canvas(player, bg='MediumOrchid', relief="solid", border=5, height=540, width=925)
center_panel.place(x=20, y=30)


# actions of buttons
def show_now(t):
    global play
    global time_format
    global restart
    global has_called
    t = round(t)
    has_called = False
    current_time_var = 0
    while current_time_var <= t and pygame.mixer.music.get_busy():
        if has_called:
            current_time_var = t - 1
            continue
        if not play:
            continue
        if restart:
            current_time_var = 0
            restart = False
            continue
        else:
            mins, secs = divmod(current_time_var, 60)
            mins = round(mins)
            secs = round(secs)
            current_time = '{:02d} : {:02d}'.format(mins, secs)
            total_time['text'] = current_time + ' / ' + time_format
            time.sleep(1)
            current_time_var = current_time_var + 1


def show_time_music():
    file_data = os.path.splitext(fileop)
    global time_length
    if file_data[1] == '.mp3':
        song = MP3(fileop)
        time_length = song.info.length
    else:
        a = pygame.mixer.Sound(fileop)
        time_length = a.get_length()
    mins, secs = divmod(time_length, 60)
    mins = round(mins)
    secs = round(secs)
    global time_format
    time_format = '{:02d} : {:02d}'.format(mins, secs)
    total_time['text'] = '00 :00 / ' + time_format
    global t1
    t1 = threading.Thread(target=show_now, args=(time_length,))
    t1.setDaemon(True)
    t1.start()


def browse():
    file_is = filedialog.askopenfilename(title='Select a File', filetype=(('mp3', '*.mp3'),))
    return file_is


def select_f():
    global fileop
    global stop
    global has_called
    global index_playlist
    fileop = browse()
    if fileop == '':
        return
    art.config(text='-')
    alb.config(text='-')
    albart.config(text='-')
    name = os.path.basename(fileop)
    playlist_music.update({index_playlist: fileop})
    playlist.insert(index_playlist, name)
    index_playlist = index_playlist + 1
    has_called = True
    time.sleep(1)
    pygame.mixer.music.load(fileop)
    pygame.mixer.music.play()
    global play
    play = True
    stop = False
    pause_play_button.config(image=photo2)
    global tag
    tag.parse(fileop)
    global current
    current.config(text=tag.title)
    art.config(text=tag.artist)
    alb.config(text=tag.album)
    albart.config(text=tag.album_artist)
    status['text'] = 'Playing ' + tag.title
    show_time_music()


def pause_play_f(rewindo):
    try:
        global play
        global stop
        global pause_play_button
        global fileop
        global time_length
        global has_called
        global tag
        global current
        if play:
            if playlist.curselection() != ():
                song = playlist.curselection()
                fileop = playlist_music[song[0]]
                art.config(text='-')
                alb.config(text='-')
                albart.config(text='-')
                has_called = True
                time.sleep(1)
                pygame.mixer.music.load(fileop)
                pygame.mixer.music.play()
                play = True
                stop = False
                pause_play_button.config(image=photo2)
                tag.parse(fileop)
                current.config(text=tag.title)
                art.config(text=tag.artist)
                alb.config(text=tag.album)
                albart.config(text=tag.album_artist)
                status['text'] = 'Playing ' + tag.title
                show_time_music()
                playlist.selection_clear(first=0, last=END)
            else:
                pygame.mixer.music.pause()
                play = False
                pause_play_button.config(image=photo1)
                status['text'] = 'Music Paused'
        else:
            if playlist.curselection() != ():
                song = playlist.curselection()
                fileop = playlist_music[song[0]]
                art.config(text='-')
                alb.config(text='-')
                albart.config(text='-')
                has_called = True
                time.sleep(1)
                pygame.mixer.music.load(fileop)
                pygame.mixer.music.play()
                play = True
                stop = False
                pause_play_button.config(image=photo2)
                tag.parse(fileop)
                current.config(text=tag.title)
                art.config(text=tag.artist)
                alb.config(text=tag.album)
                albart.config(text=tag.album_artist)
                status['text'] = 'Playing ' + tag.title
                show_time_music()
                playlist.selection_clear(first=0, last=END)
            if stop:
                pygame.mixer.music.play()
                if not rewindo:
                    t1 = threading.Thread(target=show_now, args=(time_length,))
                    t1.setDaemon(True)
                    t1.start()
                stop = False
            else:
                pygame.mixer.music.unpause()
            play = True
            pause_play_button.config(image=photo2)
            status['text'] = 'Playing ' + tag.title
    except:
        tkinter.messagebox.showerror('Cannot play!!!', 'No music file selected. Therefore cannot play anything!!!')


def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)


def about_us():
    tkinter.messagebox.showinfo('About BajaoBe', '\'BajaoBe\' is a music player app created by Gaurav Garmode, Harshad '
                                                 'Karanjule and Raj Jadhav from Datta Meghe College of Engineering, '
                                                 'Airoli, Navi Mumbai using Python, Tkinter, etc.')


def stop_music(restartf):
    pygame.mixer.music.stop()
    global play
    global stop
    stop = True
    play = False
    pause_play_button.config(image=photo1)
    status['text'] = 'Music Stopped'
    if restartf:
        global restart
        restart = True
        pause_play_f(True)


def mute_unmute():
    global mute
    if mute:
        x = scale.get()
        set_vol(x)
        mute_button['image'] = photo5
        mute = False
        status['text'] = 'Playing ' + tag.title
    else:
        pygame.mixer.music.set_volume(0)
        mute_button['image'] = photo6
        mute = True
        status['text'] = 'Mute ' + 'Playing ' + tag.title


def add_in_playlist():
    global index_playlist
    new_song = browse()
    if new_song == '' or (new_song in playlist_music.values()):
        return
    name = os.path.basename(new_song)
    playlist_music.update({index_playlist: new_song})
    playlist.insert(index_playlist, name)
    index_playlist = index_playlist + 1


def delete_in_playlist():
    try:
        song = playlist.curselection()
        playlist.delete(song[0])
        x = playlist_music.pop(song[0])
    except:
        return


# menubar
menu_bar = Menu(player)
player.config(menu=menu_bar)
# submenu
submenu = Menu(menu_bar, tearoff=0, bg='MediumOrchid', fg='White')
menu_bar.add_cascade(menu=submenu, label='File')
submenu.add_command(label='Open', command=select_f)
submenu.add_command(label='Exit', command=player.destroy)

submenu = Menu(menu_bar, tearoff=0, bg='MediumOrchid', fg='White')
menu_bar.add_cascade(menu=submenu, label='Help')
submenu.add_command(label='About Us', command=about_us)

# list
playlist = Listbox(center_panel, height=30, width=50, bg='MediumOrchid4', fg='White', border=5, relief=GROOVE,
                   font=('Fixedsys'), selectmode=MULTIPLE)
playlist.place(x=10, y=10)

# button
add_song = Button(center_panel, text='Add song', font=('Fixedsys', 14), width=18, relief=GROOVE, bg='MediumOrchid4',
                  fg='White', border=3, command=add_in_playlist)
add_song.place(x=10, y=505)

delete_song = Button(center_panel, text='Delete song', font=('Fixedsys', 14), width=18, relief=GROOVE,
                     bg='MediumOrchid4', fg='White', border=3, command=delete_in_playlist)
delete_song.place(x=231, y=505)

photo2 = PhotoImage(file=r'F:\python\BajaoBe\pause.png')
photo1 = PhotoImage(file=r'F:\python\BajaoBe\play.png')
photo3 = PhotoImage(file=r'F:\python\BajaoBe\stop.png')
photo4 = PhotoImage(file=r'F:\python\BajaoBe\restart.png')
photo5 = PhotoImage(file=r'F:\python\BajaoBe\unmute.png')
photo6 = PhotoImage(file=r'F:\python\BajaoBe\mute.png')
pause_play_button = Button(player, image=photo1, width=35, height=35, command=lambda: pause_play_f(False))
pause_play_button.place(x=20, y=600)

stop_button = Button(player, image=photo3, width=35, height=35, command=lambda: stop_music(False))
stop_button.place(x=70, y=600)

restart_button = Button(player, image=photo4, width=35, height=35, command=lambda: stop_music(True))
restart_button.place(x=120, y=600)

mute_button = Button(player, image=photo5, width=35, height=35, command=mute_unmute)
mute_button.place(x=170, y=600)

total_time = Label(player, text='-- : -- / -- : --', relief=GROOVE, bg='MediumOrchid', fg='DarkOrchid4',
                   font=('Times new Roman', 20, 'bold'), border=5)
total_time.place(x=220, y=598)

scale = Scale(player, from_=0, to=100, command=set_vol, orient=HORIZONTAL, bg='MediumOrchid', troughcolor='DarkOrchid4',
              fg='white')
scale.set(75)
pygame.mixer.music.set_volume(0.75)
scale.place(x=800, y=600)

current = Button(center_panel, text='CURRENT SONG', font=('Comic sans ms', 16, 'bold'), bg='DarkOrchid4', fg='White')
current.place(x=425, y=10)

status = Label(player, text='Welcome to BajaoBe!!', relief=SUNKEN, bg='MediumOrchid', fg='DarkOrchid4',
               font=('Times new Roman', 14, 'bold'), anchor=W)
status.pack(side=BOTTOM, fill=X)


#metadata

Label(player, text='Artist            :', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 15), relief=GROOVE).place(x=445, y=120)
art = Label(player, text='-', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 15), relief=GROOVE)
art.place(x=615, y=120)

Label(player, text='Album            :', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 15), relief=GROOVE).place(x=445, y=170)
alb = Label(player, text='-', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 15), relief=GROOVE)
alb.place(x=615, y=170)

Label(player, text='Album Artist  :', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 15), relief=GROOVE).place(x=445, y=220)
albart = Label(player, text='-', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 15), relief=GROOVE)
albart.place(x=615, y=220)

# activate
player.mainloop()
