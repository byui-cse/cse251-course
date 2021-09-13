"""
CSE251
Program to create final video from images
"""

import os
import platform

def main():
    # the folder "processed" must exist
    if not os.path.exists('processed'):
        print('\nERROR: the folder "processed" doesn\'t exist\n')
        return 

    if platform.system() == 'Windows':
        command = r'ffmpeg -y -i processed/image%3d.png final.mp4'
    else:
        command = r'./ffmpeg -y -i processed/image%3d.png final.mp4'

    os.system(command)

    print('\nThe video file final.mp4 has been created\n')
    print('Do NOT submit this video for your assignment!!')

main()
