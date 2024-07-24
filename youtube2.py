from pytube import YouTube

def download_video(url, save_path):
    try:
        print(f"Downloading video from URL: {url}")
        yt = YouTube(url)
        print(f"Video title: {yt.title}")
        
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        print(f"Available streams: {streams}")
        
        highest_res_stream = streams.get_highest_resolution()
        print(f"Downloading highest resolution stream: {highest_res_stream}")
        
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=ydOZ5YAv8Hk"
    save_path = r"C:\Users\Dev-RBQ\Desktop\PYTHON MEDIUM PROJECTS\python medium project 12"

    download_video(url, save_path)
