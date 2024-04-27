import yt_dlp
import subprocess
import time
import os
import sys

def get_video_links(url):
    ydl_opts = {
        'extract_flat': 'in_playlist',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if 'entries' in info:
            # playlist URL
            video_links = [entry['url'] for entry in info['entries'] if entry is not None]
        else:
            # video URL
            video_links = [info['webpage_url']]
    return video_links

def download_video(url, output_dir):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Skipping video: {url} - {str(e)}")

def create_m3u_playlist(video_queue, output_dir):
    playlist_path = os.path.join(output_dir, "playlist.m3u")
    with open(playlist_path, "w", encoding="utf-8") as playlist_file:
        playlist_file.write("#EXTM3U\n")
        for i, video_path in enumerate(video_queue, start=1):
            playlist_file.write(f"#EXTINF:0,Video {i}\n")
            playlist_file.write(f"{video_path}\n")
    return playlist_path

def vlc_play(playlist_path):
    vlc_executable = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    vlc_process = subprocess.Popen([vlc_executable, playlist_path, "--play-and-exit"])
    vlc_process.wait()  # Wait for VLC to finish playing the playlist

def cleanup(output_dir):
    video_extensions = ('.webm', '.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mpg', '.mpeg', '.m4v', '.3gp', '.m3u')
    for file in os.listdir(output_dir):
        if file.endswith(video_extensions):
            file_path = os.path.join(output_dir, file)
            os.remove(file_path)

def watch(url):
    output_dir = os.path.join(os.getcwd(), 'youtube')
    os.makedirs(output_dir, exist_ok=True)

    video_links = get_video_links(url)
    video_queue = []

    for video_link in video_links:
        download_video(video_link, output_dir)

    video_files = os.listdir(output_dir)
    for video_file in video_files:
        video_path = os.path.join(output_dir, video_file)
        video_queue.append(video_path)

    playlist_path = create_m3u_playlist(video_queue, output_dir)
    vlc_play(playlist_path)

    cleanup(output_dir)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube video or playlist URL: ")

    watch(url)
