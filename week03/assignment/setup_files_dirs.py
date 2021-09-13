"""
CSE251
Program to split videos into individual files
"""

import os
import platform

def create_dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def create_images(video_file, folder):
    # limit the number of frames to 300
    if platform.system() == 'Windows':
        command = rf'ffmpeg -i {video_file} -vframes 300 {folder}/image%3d.png'
    else:
        command = rf'./ffmpeg -i {video_file} -vframes 300 {folder}/image%3d.png'
    os.system(command)

def main():
    # Create sub folders 
    create_dir('green')
    create_dir('elephant')
    create_dir('processed')

    # Create the image files
    create_images('elephants.mp4', 'elephant')
    create_images('green.mp4', 'green')

main()
