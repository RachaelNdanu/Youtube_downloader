import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download the best available quality
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save file as title.extension
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

# Define your video URL and save path
url = "https://www.youtube.com/watch?v=ydOZ5YAv8Hk"
save_path = r"C:\Users\Dev-RBQ\Desktop\PYTHON MEDIUM PROJECTS\python medium project 12"

download_video(url, save_path)

# Optional: another video URL and save path example
url = "https://youtu.be/vQ2L4qcOXVI?si=nG3GFJnTYqjl5QAp"
save_path = r"C:\Users\Dev-RBQ\Desktop\PYTHON MEDIUM PROJECTS\python medium project 12"

download_video(url, save_path)
