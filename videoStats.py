# videoStats.py

import sys
import cv2
import os

dir_path = sys.argv[1]
files = os.listdir(dir_path)
for file in files:
    file_path = os.path.join(dir_path, file)
    print(file)
    vidcap = cv2.VideoCapture(file_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("FPS: ", fps)
    print("Width: ", width)
    print("Height: ", height)