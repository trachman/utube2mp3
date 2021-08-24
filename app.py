#!/usr/bin/env python3
import os
import sys
import shutil
import youtube_dl

def download_media(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def save_to_library():
    """
    only works for MacOS
    """
    path_to_music = os.path.join(os.path.expanduser('~'), 'Music/iTunes/iTunes Media/Automatically Add to Music.localized/')
    cwd = os.listdir(os.getcwd())
    if len(cwd) > 4: # ensures that the media download was successful
        for file in cwd:
            print(len(cwd))
            if file not in ('app.py','LICENSE','README.md','.git'):
                shutil.move(os.path.abspath(file), os.path.join(path_to_music,file))
    else:
        print('Download failed.')

def main():
    """
    1) download the music/podcast
    2) send it to apple music so it is automatically on our phones
    """
    url = sys.argv[1:] 
    download_media(url) # step 1
    save_to_library() # step 2

if __name__ == '__main__':
    main()   