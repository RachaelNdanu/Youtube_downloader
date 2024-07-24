from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
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
