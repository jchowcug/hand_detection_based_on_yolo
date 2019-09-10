import os
from utils.tools import *
import tqdm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


width = []
height = []
dir = '/media/j/DA18EBFA09C1B27D/RHD_v1-1/RHD_published_v2/evaluation/mask'
imgs_name_list = sorted(os.listdir(dir))
for img_name in tqdm.tqdm(imgs_name_list):
    img_path = dir + '/' +img_name
    boxes = boxes_from_mask(img_path)
    for box in boxes:
        if box[0] != None:
            w = box[2] - box[0]
            h = box[3] - box[1]
            width.append(w)
            height.append(h)

plt.hist(width, bins=50, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
plt.xlabel('range')
plt.ylabel('frequency')
plt.savefig('width distribution')
plt.show()
plt.close()
plt.hist(height, bins=50, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
plt.xlabel('range')
plt.ylabel('frequency')
plt.savefig('height distribution')
plt.show()
plt.close()