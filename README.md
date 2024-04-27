# yt-vlc

Stream YouTube urls directly to VLC or download and play the videos locally, will remove downloads after VLC exits.

example usage:
```
python watch.py https://youtube.com/<link>
python watch.py https://www.youtube.com/playlist?list=<playlist>
python watch.py https://youtube.com/<link> -d 
python watch.py https://youtube.com/<link> --download
```
 
This command will download all the videos in the specified YouTube playlist to files in the "youtube" directory, create an M3U playlist, and play the playlist with VLC.

## Requirements

* Python 3.x
* Windows 10/11
* yt-dlp
* VLC media player

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/

2. Install the yt-dlp library by running the following command:
`pip install yt-dlp`

3. Install VLC media player from the official website: https://www.videolan.org/vlc/

## Notes

- By default, the script streams the YouTube video or playlist directly with VLC. To download the videos instead, use the `-d` or `--download` option.

- The script assumes that VLC is installed in the default location: `C:\Program Files\VideoLAN\VLC\vlc.exe`. If VLC is installed in a different location, modify the `vlc_executable` variable in the script accordingly.

- When downloading videos, the script creates a `/youtube` directory in the current working directory to store the downloaded files. The downloaded videos are played from this directory and cleaned up after playback.

- The script supports streaming and downloading individual YouTube videos as well as entire playlists.
