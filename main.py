# Designer: 1809853Z-I011-0045 Wang Yuyang

import tkinter as tk
from PIL import ImageTk, Image
import pygame

# event
def nextMusic(event):
    listindex = musicBox.curselection()[0]
    if listindex < 5:
        musicBox.select_clear(listindex)
        listindex = listindex + 1
        musicBox.select_set(listindex)

def prevMusic(event):
    listindex = musicBox.curselection()[0]
    if listindex > 0:
        musicBox.select_clear(listindex)
        listindex = listindex - 1
        musicBox.select_set(listindex)

def playMusic(event):
    pygame.mixer.music.load("src/rainAfterSummer.mp3")
    pygame.mixer.music.play()

# setting
pygame.init()
window = tk.Tk()
topFrame = tk.Frame(window)
topFrame.pack(side=tk.TOP, pady=15)
middleFrame = tk.Frame(window)
middleFrame.pack(side=tk.TOP, pady=20)
bottomFrame = tk.Frame(window)
bottomFrame.pack(side=tk.TOP, pady=30)

window.title("MusicPlayer")
window.geometry("700x850")

window.resizable(0, 0)  # cannot resize
window.configure(background='black')

# main frame
# cover image
img = ImageTk.PhotoImage(Image.open('src/cover.png').resize((500, 500), Image.ANTIALIAS))
panel = tk.Label(topFrame, image=img)
panel.pack(fill="both", expand="yes")

# music list
list = tk.Label(middleFrame, text='Play List')
list.pack()
musicBox = tk.Listbox(middleFrame, width=60, height=7)
musicBox.insert(1, "1. 千与千寻と神隠し")
musicBox.insert(2, "2. 信仰は儚き人間の為に")
musicBox.insert(3, "3. 少女绮想曲")
musicBox.insert(4, "4. 幽雅に咲かせ、墨染の桜")
musicBox.insert(5, "5. 狂気の瞳")
musicBox.insert(6, "6. 三日月の舞")
musicBox.select_set(0)
musicBox.pack()

# play button
img1 = ImageTk.PhotoImage(Image.open('src/pre.png').resize((30, 30), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open('src/play.png').resize((50, 50), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open('src/next.png').resize((30, 30), Image.ANTIALIAS))

btn_playprev = tk.Button(bottomFrame, image=img1)
btn_playprev.pack(side=tk.LEFT, padx=10)
btn_playprev.bind('<Button-1>', prevMusic)

btn_play = tk.Button(bottomFrame, image=img2)
btn_play.pack(side=tk.LEFT, padx=10)
btn_play.bind('<Button-1>', playMusic)

btn_playnext = tk.Button(bottomFrame, image=img3)
btn_playnext.pack(side=tk.LEFT, padx=10)
btn_playnext.bind('<Button-1>', nextMusic)

# execute
window.mainloop()