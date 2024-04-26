import yt_dlp
import os
import time
import sys

""" Download Video(s) from Youtube and Play them in VLC

Usage:
python watch.py <url>

url: Youtube playlist url
"""

def get_video_links(url):
    ydl_opts = {
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if 'entries' in info:
            # URL is a playlist
            video_links = [entry['url'] for entry in info['entries']]
        else:
            # URL is a single video
            video_links = [info['url']]
    return video_links

def download_video(url, output_dir):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def vlc_play(video_path):
    os.system(f'vlc "{video_path}"')

def watch(playlist_url):
    output_dir = os.path.join(os.getcwd(), 'youtube')
    os.makedirs(output_dir, exist_ok=True)
    
    video_links = get_video_links(playlist_url)
    for video_link in video_links:
        download_video(video_link, output_dir)
        video_files = os.listdir(output_dir)
        video_path = os.path.join(output_dir, video_files[0])
        vlc_play(video_path)
        time.sleep(1)  # Wait for a short duration before removing the file
        cleanup(video_path)

def cleanup(video_path):
    os.remove(video_path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        playlist_url = sys.argv[1]
    else:
        playlist_url = input("Enter the YouTube playlist URL: ")
        
    watch(playlist_url) 
