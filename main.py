import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import requests
import pytube
from pytube import Playlist

width = 700
height = 350

root = Tk()
root.geometry('%dx%d' % (width, height))
root.title("Download Manager")
root.config(background='#1d3557')

# turn off tabs
style = ttk.Style()
style.layout('TNotebook.Tab', [])

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True)

# create frames
home_frame = Frame(notebook, width=width, height=height, bg='#1d3557')
any_file_frame = Frame(notebook, width=width, height=height, bg='#1d3557')
youtube_frame = Frame(notebook, width=width, height=height, bg='#1d3557')
playlist_frame = Frame(notebook, width=width, height=height, bg='#1d3557')
manger_frame = Frame(notebook, width=width, height=height, bg='#1d3557')
test = Frame(notebook, width=width, height=height, bg='#1d3557')

home_frame.pack(fill='both', expand=True)
any_file_frame.pack(fill='both', expand=True)
youtube_frame.pack(fill='both', expand=True)
playlist_frame.pack(fill='both', expand=True)
manger_frame.pack(fill='both', expand=True)
test.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(home_frame)
notebook.add(any_file_frame)
notebook.add(youtube_frame)
notebook.add(playlist_frame)
notebook.add(manger_frame)
notebook.add(test)


# <------Home Frame------>
# select tap number
def select(num):
    notebook.select(num)


choose_label = Label(home_frame, text="Choose Option..!", foreground='#f1faee',
                     background='#1d3557', font=("Helvetica", 30))
choose_label.grid(row=0, column=0, columnspan=4, pady=30)

Any_file_button = Button(home_frame, text="Any File", fg='#f1faee', bg='#e63946', width=9, bd=0,
                         font=("Helvetica", 14), command=lambda: select(1))
Any_file_button.grid(row=1, column=0, padx=30, pady=20)

youtube_button = Button(home_frame, text="Youtube", fg='#f1faee', bg='#e63946', width=9, bd=0,
                        font=("Helvetica", 14), command=lambda: select(2))
youtube_button.grid(row=1, column=1, padx=30, pady=20)

playlist_button = Button(home_frame, text="Playlist", fg='#f1faee', bg='#e63946', width=9, bd=0,
                         font=("Helvetica", 14), command=lambda: select(3))
playlist_button.grid(row=1, column=2, padx=30, pady=20)

manage_button = Button(home_frame, text="Manage", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=lambda: select(4))
manage_button.grid(row=1, column=3, padx=30, pady=20)


# <------Any File Screen------>
# select download directory
def select_dir():
    dir_entry.delete(0, 'end')
    name = fd.askdirectory(parent=root, initialdir="/home/", title='Please select a directory')
    dir_entry.insert(0, str(name))


def download():
    # https://www.wepal.net/ar/uploads/2732018-073911PM-1.jpg
    url = str(link_entry.get())
    dir = str(dir_entry.get())
    try:
        if url.find('/'):
            name = url.rsplit('/', 1)[1]
        r = requests.get(url)
        with open('{0}/{1}'.format(dir, name), 'wb') as f:
            f.write(r.content)
        messagebox.showinfo("showinfo", "Downloaded Successfully")
    except Exception:
        messagebox.showerror("Error", "Could not download file")


link_label = Label(any_file_frame, text='Download Link', foreground='#f1faee',
                   background='#1d3557', font=("Helvetica", 14))
link_label.grid(column=0, row=0, padx=10, pady=20)

link_entry = Entry(any_file_frame, width=30, font=("Helvetica", 14))
link_entry.grid(column=1, row=0)

dir_label = Label(any_file_frame, text='Directory', foreground='#f1faee',
                  background='#1d3557', font=("Helvetica", 14))
dir_label.grid(column=0, row=1, padx=10, pady=0)

dir_entry = Entry(any_file_frame, width=30, font=("Helvetica", 14))
dir_entry.grid(column=1, row=1)

browse_button = Button(any_file_frame, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=select_dir)
browse_button.grid(column=2, row=1, padx=20)

start_button = Button(any_file_frame, text="Start", fg='#f1faee', bg='#e63946', width=9, bd=0,
                      font=("Helvetica", 14), command=download)
start_button.grid(column=0, row=2, columnspan=2)

home_button = Button(any_file_frame, text="Home", fg='#f1faee', bg='#e63946', width=9, bd=0,
                     font=("Helvetica", 14), command=lambda: select(0))
home_button.grid(column=1, row=2, columnspan=2, pady=20)

# <------Youtube Video Screen------>

quality = IntVar()


def select_dir():
    vid_dir_entry.delete(0, 'end')
    name = fd.askdirectory(parent=root, initialdir="/home/", title='Please select a directory')
    vid_dir_entry.insert(0, str(name))


def download_vid():
    # 'https://www.youtube.com/watch?v=y6Mi9ARyCzA'
    global video
    url = str(vid_link_entry.get())
    dir = str(vid_dir_entry.get())
    try:
        youtube = pytube.YouTube(url)
        if quality.get() == 0:
            video = youtube.streams.first()
        if quality.get() == 1:
            video = youtube.streams.get_highest_resolution()
        video.download(dir)
        messagebox.showinfo("showinfo", "Downloaded Successfully")
    except Exception:
        messagebox.showerror("Error", "Could not download file")


def quality_selected():
    if quality.get() == 0:
        low_qu_button.config(fg='#e63946')
        high_qu_button.config(fg='#f1faee')
    if quality.get() == 1:
        high_qu_button.config(fg='#e63946')
        low_qu_button.config(fg='#f1faee')


vid_link_label = Label(youtube_frame, text='Video Link', foreground='#f1faee',
                       background='#1d3557', font=("Helvetica", 14))
vid_link_label.grid(column=0, row=0, padx=10, pady=20)

vid_link_entry = Entry(youtube_frame, width=30, font=("Helvetica", 14))
vid_link_entry.grid(column=1, row=0)

dir_label = Label(youtube_frame, text='Directory', foreground='#f1faee',
                  background='#1d3557', font=("Helvetica", 14))
dir_label.grid(column=0, row=1, padx=10, pady=0)

vid_dir_entry = Entry(youtube_frame, width=30, font=("Helvetica", 14))
vid_dir_entry.grid(column=1, row=1)

browse_button = Button(youtube_frame, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=select_dir)
browse_button.grid(column=2, row=1, padx=10)

vid_qu_label = Label(youtube_frame, text='Quality', foreground='#f1faee',
                     background='#1d3557', font=("Helvetica", 14))
vid_qu_label.grid(column=0, row=2)

low_qu_button = Radiobutton(youtube_frame, text="Lowest", variable=quality, value=0, command=quality_selected,
                            bg='#1d3557', fg='#f1faee', font=("Helvetica", 16), bd=0)
low_qu_button.grid(column=0, row=2, columnspan=2)

high_qu_button = Radiobutton(youtube_frame, text="Highest", variable=quality, value=1, command=quality_selected,
                             bg='#1d3557', fg='#f1faee', font=("Helvetica", 16), bd=0)
high_qu_button.grid(column=1, row=2, columnspan=2, pady=20)

start_button = Button(youtube_frame, text="Start", fg='#f1faee', bg='#e63946', width=9, bd=0,
                      font=("Helvetica", 14), command=download_vid)
start_button.grid(column=0, row=4, columnspan=2)

home_button = Button(youtube_frame, text="Home", fg='#f1faee', bg='#e63946', width=9, bd=0,
                     font=("Helvetica", 14), command=lambda: select(0))
home_button.grid(column=1, row=4, columnspan=2)

# <------Youtube Playlist Screen------>

playlist_quality = IntVar()


def select_dir():
    play_dir_entry.delete(0, 'end')
    name = fd.askdirectory(parent=root, initialdir="/home/", title='Please select a directory')
    play_dir_entry.insert(0, str(name))


def download_playlist():
    # https://youtube.com/playlist?list=PLRfY4Rc-GWzhdCvSPR7aTV0PJjjiSAGMs
    link = str(play_link_entry.get())
    dir = str(play_dir_entry.get())
    try:
        playlist = Playlist(link)
        for video in playlist.videos:
            if playlist_quality.get() == 0:
                video.streams.first().download(dir)
            if playlist_quality.get() == 1:
                video.streams.get_highest_resolution().download(dir)
        messagebox.showinfo("showinfo", "Downloaded Successfully")
    except Exception:
        messagebox.showerror("Error", "Could not download file")


def quality_selected():
    if quality.get() == 0:
        low_playlist_qu.config(fg='#e63946')
        high_playlist_qu.config(fg='#f1faee')
    if quality.get() == 1:
        high_playlist_qu.config(fg='#e63946')
        low_playlist_qu.config(fg='#f1faee')


play_link_label = Label(playlist_frame, text='Playlist Link', foreground='#f1faee',
                        background='#1d3557', font=("Helvetica", 14))
play_link_label.grid(column=0, row=0, padx=10, pady=20)

play_link_entry = Entry(playlist_frame, width=30, font=("Helvetica", 14))
play_link_entry.grid(column=1, row=0)

dir_label = Label(playlist_frame, text='Directory', foreground='#f1faee',
                  background='#1d3557', font=("Helvetica", 14))
dir_label.grid(column=0, row=1, padx=10, pady=0)

play_dir_entry = Entry(playlist_frame, width=30, font=("Helvetica", 14))
play_dir_entry.grid(column=1, row=1)

browse_button = Button(playlist_frame, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=select_dir)
browse_button.grid(column=2, row=1, padx=10)

play_qu_label = Label(playlist_frame, text='Quality', foreground='#f1faee',
                      background='#1d3557', font=("Helvetica", 14))
play_qu_label.grid(column=0, row=2)

low_playlist_qu = Radiobutton(playlist_frame, text="Lowest", variable=quality, value=0, command=quality_selected,
                              bg='#1d3557', fg='#f1faee', font=("Helvetica", 16), bd=0)
low_playlist_qu.grid(column=0, row=2, columnspan=2)

high_playlist_qu = Radiobutton(playlist_frame, text="Highest", variable=quality, value=1, command=quality_selected,
                               bg='#1d3557', fg='#f1faee', font=("Helvetica", 16), bd=0)
high_playlist_qu.grid(column=1, row=2, columnspan=2, pady=20)

start_button = Button(playlist_frame, text="Start", fg='#f1faee', bg='#e63946', width=9, bd=0,
                      font=("Helvetica", 14), command=download_playlist)
start_button.grid(column=0, row=4, columnspan=2)

home_button = Button(playlist_frame, text="Home", fg='#f1faee', bg='#e63946', width=9, bd=0,
                     font=("Helvetica", 14), command=lambda: select(0))
home_button.grid(column=1, row=4, columnspan=2)


# <------Manage Screen------>
def select_file():
    global filename
    directory_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/home/', filetypes=filetypes)
    directory_entry.insert(0, str(filename))
    name_entry.insert(0, str(filename.rsplit('/', 1)[-1]))


def select_dir():
    new_dir_entry.delete(0, 'end')
    filename = fd.askdirectory(title='Select Directory', initialdir="/home/")
    new_dir_entry.insert(0, str(filename))


def rename():
    dir = str(directory_entry.get())
    newdir = dir.rsplit('/', 1)[0] + '/'
    newname = str(name_entry.get())
    try:
        subprocess.check_output("mv {0} {1}{2}".format(dir, newdir, newname), shell=True)
        os.system("mv {0} {1}{2}".format(dir, newdir, newname))
        messagebox.showinfo("showinfo", "Done Successfully")
    except:
        messagebox.showerror("Error", "Could Not Do This Operation")


def remove():
    dir = str(directory_entry.get())
    try:
        subprocess.check_output("rm {0}".format(dir), shell=True)
        os.system("rm {0}".format(dir))
        messagebox.showinfo("showinfo", "Done Successfully")
    except :
        messagebox.showerror("Error", "Could Not Do This Operation")


def change_dir():
    dir = str(directory_entry.get())
    newdir = str(new_dir_entry.get() + "/" + dir.split('/')[-1])
    try:
        subprocess.check_output("mv {0} {1}".format(dir, newdir), shell=True)
        os.system("mv {0} {1}".format(dir, newdir))
        messagebox.showinfo("showinfo", "Done Successfully")
    except :
        messagebox.showerror("Error", "Could Not Do This Operation")


dir_label = Label(manger_frame, text='Directory', foreground='#f1faee',
                  background='#1d3557', font=("Helvetica", 14))
dir_label.grid(column=0, row=0, padx=10, pady=20)

directory_entry = Entry(manger_frame, width=30, font=("Helvetica", 14))
directory_entry.grid(column=1, row=0)

browse_button = Button(manger_frame, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=select_file)
browse_button.grid(column=2, row=0, padx=10)

dir_label = Label(manger_frame, text='New Directory', foreground='#f1faee',
                  background='#1d3557', font=("Helvetica", 14))
dir_label.grid(column=0, row=1, padx=10)

new_dir_entry = Entry(manger_frame, width=30, font=("Helvetica", 14))
new_dir_entry.grid(column=1, row=1)

browse_button = Button(manger_frame, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=select_dir)
browse_button.grid(column=2, row=1, padx=10)

name_label = Label(manger_frame, text='File Name', foreground='#f1faee',
                   background='#1d3557', font=("Helvetica", 14))
name_label.grid(column=0, row=2, padx=10, pady=20)

name_entry = Entry(manger_frame, width=30, font=("Helvetica", 14))
name_entry.grid(column=1, row=2)

rename_button = Button(manger_frame, text="Rename", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=rename)
rename_button.grid(column=0, row=3, padx=10, pady=30)

remove_button = Button(manger_frame, text="Remove", fg='#f1faee', bg='#e63946', width=9, bd=0,
                       font=("Helvetica", 14), command=remove)
remove_button.grid(column=1, row=3)

change_dir_button = Button(manger_frame, text="Change dir", fg='#f1faee', bg='#e63946', width=9, bd=0,
                           font=("Helvetica", 14), command=change_dir)
change_dir_button.grid(column=2, row=3)

home_button = Button(manger_frame, text="Home", fg='#f1faee', bg='#e63946', width=9, bd=0,
                     font=("Helvetica", 14), command=lambda: select(0))
home_button.grid(column=0, row=4, columnspan=4)

root.mainloop()
