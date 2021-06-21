# summarizeImageCollection.py

import sys
import os
import cv2
from submodlib.helper import create_kernel
import numpy as np
from submodlib.functions.disparitySum import DisparitySumFunction

dir_path = sys.argv[1]

files = os.listdir(dir_path)
for file in files:
    file_path = os.path.join(dir_path, file)
    if not os.path.isdir(file_path):
        continue
    print("Summarizing ", file)
    input_dir_path = file_path
    output_dir_path = os.path.join(dir_path, file + "_summarized")
    os.mkdir(output_dir_path)
    images = os.listdir(input_dir_path)
    if len(images) <= 300:
        print("Already less than or equal to 300 images. Copying as it is. Not summarizing.")
        os.system("cp " + input_dir_path + "/*" + " " + output_dir_path)
        continue
    features = []
    img_idx = 0
    img_dictionary = {}
    print("Computing color histograms for all images in this collection")
    for image_name in images:
        image_path = os.path.join(input_dir_path, image_name)
        img_dictionary[img_idx]=image_path
        img_idx += 1
        image = cv2.imread(image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv_image],[0, 1],None,[20, 16],[0, 180, 0, 256])
        #print("Shape of histogram: ", hist.shape)
        hist = hist.flatten()
        #print("Shape of flattened histogram: ", hist.shape)
        features.append(hist)
    print("Computing kernel")
    dataArray = np.array(features)
    _, K_dense = create_kernel(dataArray, 'dense','cosine')
    print("Computing summary")
    objDM = DisparitySumFunction(n=len(features), sijs=K_dense, mode="dense", metric="cosine")
    greedyList = objDM.maximize(budget=300,optimizer='NaiveGreedy', stopIfZeroGain=False, stopIfNegativeGain=False, verbose=False)
    print("Copying in summarized folder")
    for elem in greedyList:
        idx = elem[0]
        path = img_dictionary[idx]
        os.system("cp " + path + " " + output_dir_path)    
    




