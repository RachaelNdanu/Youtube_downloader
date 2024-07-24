import tkinter as tk
from tkinter import filedialog

import youtube_dl

def download_video(url, save_path):
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def download_with_gui():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    url = input("Enter the YouTube URL: ")
    save_path = filedialog.askdirectory()

    if url and save_path:
        print("started downloading.....")
        download_video(url, save_path)
    else:
        print("Invalid URL or save path.")

if __name__ == "__main__":
    download_with_gui()