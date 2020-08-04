from pytube import YouTube
import os
from tkinter import *

root = Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')





label = Label(root, text = "Paste the Youtube link here", font = ("bold", 28))
label.place(x = 120, y = 20)

my_link = StringVar()

entry = Entry(root, width = 60, textvariable = my_link)
entry.place(x = 140, y = 80)


def download_video():
    x = str(my_link.get())
    ytvideo = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    ytvideo.download('./download')

Button(root, text = "Download Video", width = 20, bg = 'green', fg = 'white', command = download_video).place(x = 220, y = 110)


root.mainloop()