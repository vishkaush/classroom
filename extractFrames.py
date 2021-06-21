# extractFrames.py

import sys
import cv2
import os

dir_path = sys.argv[1]
files = os.listdir(dir_path)
for file in files:
    resize = False
    file_path = os.path.join(dir_path, file)
    if(os.path.isdir(file_path)):
        continue
    print("Processing ", file)
    name_without_extension = os.path.splitext(file)[0]
    video_folder_path = os.path.join(dir_path, name_without_extension)
    if not os.path.isdir(video_folder_path):
        os.mkdir(video_folder_path)
        vidcap = cv2.VideoCapture(file_path)
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # print("FPS: ", fps)
        # print("Width: ", width)
        # print("Height: ", height)
        if width != 1280 or height != 720:
            resize = True
        frame_count=-1
        num_written = 0
        while(vidcap.isOpened()):
            ret, frame = vidcap.read()
            if ret == False:
                #print("End of stream!")
                break
            frame_count += 1
            if frame_count % (5*fps) == 0:
                print(".", end="", flush=True)
                if resize:
                    frame = cv2.resize(frame, (1280, 720))
                cv2.imwrite(os.path.join(video_folder_path, name_without_extension + "_" + str(frame_count) + ".jpg"), frame)
                num_written += 1
        print("")
        print(num_written, " frames written")
        vidcap.release()
    else:
        print("Already extracted.", end=" ")
        vidcap = cv2.VideoCapture(file_path)
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        num_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        seconds = int(num_frames / fps)
        images = os.listdir(video_folder_path)
        num_images = len(images)
        if num_images < int(seconds/5):
            print("ERROR!")
            print("FPS: ", fps)
            print("Video duration: ", seconds)
            print("Expected number of images: ", seconds/5)
            print("Actual number of images extracted: ", num_images)
        else:
            print("OK!")
        
        


