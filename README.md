# BAJAOBE - A MUSIC PLAYER APP

___

Our project is a Music player with as simple as possible Graphical User Interface. The interface is quite attractive and interaction with user is simple.

## SOLUTION DESIGN

___

We used tkinter toolkit for GUI. We also used "pygame", "eyed3", "mutagen", "os", "threading", "time", "sys" modules of python. All the widgets used are simplified for the ease of interaction between application and user.

**HOME SCREEN**

This is the page the user will see when he opens the application or (runs home.py). As seen below we have added many functions like pause,play, stop or repeat the song. The meta data like artist, album, etc. is shown. On the left is the playlist where we can add, delete songs. There is also a volume scroll to control the volume. There is a label showing time of song versus remaining time. There is also a status bar showing status every second.There are interactive buttons like "Pause"/"Play", "Stop", "Replay", "Mute".

![2](https://github.com/Garmode3073/BajaoBe/tree/main/ss/2.png)

![1](https://github.com/Garmode3073/BajaoBe/tree/main/ss/1.png)

## IMPLEMENTATION PLAN

___

We have used python language, tkinter library mostly for the GUI of application. We have used "pygame" module of python for playing music. We used  "eyed3" and "mutagen" libraries for the recovery of metadata of any audio file.  We have also used "Time" module of python for fetching time every second the application is running. We used "os", "threading" and "sys" modules of python for ease of running the application on desktop. All the exceptions are handled carefully. The GUI is quite easy to understand. 

## HOW TO RUN LOCALLY

___

1. Download the following dependencies using pip

   * ```
        pip install tkinter
     ```
     
   * ```
        pip install time
     ```
     
   * ```
     pip install pygame
     ```
     
   * ```
        pip install eyed3
        ```
        
   * ```
        pip install mutagen
        ```
   
3. Go to Project Folder and run home.py

## CONTRIBUTER

---

Harshad Karanjule

* [Github](https://github.com/hkaranjule77 "Github")
* [Linkedin](https://www.linkedin.com/in/harshad-karanjule-5b076818b "Linkedin")

Raj Jadhav

* [Github](https://github.com/deathonation "Github")
* [Linkedin](https://www.linkedin.com/in/raj-jadhav-0309961aa "Linkedin")

Gaurav Garmode

* [Github](https://github.com/Garmode3073 "Github")
* [Linkedin](https://www.linkedin.com/in/gaurav-garmode-ab537a175 "Linkedin")
