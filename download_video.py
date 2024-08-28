import yt_dlp

def download_video(url, output_path='.'):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = 'https://youtu.be/VnHJIKS4l6g?si=HTnGU4m9Abh7nVhj'
download_video(video_url, output_path='/home/ndanu/Desktop')
