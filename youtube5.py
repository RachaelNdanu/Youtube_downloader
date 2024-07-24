import youtube_dl

def download_video(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage:
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
download_video(video_url)
