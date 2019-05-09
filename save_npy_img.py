#! /usr/bin/env python
import cv2
import os
import numpy as np

# np.save("/home/aarons/catkin_kinect/src/yumi_grasp/src/grasp_est.npy", points_out)
INPUT_FOLDER = './input'
OUTPUT_FOLDER = './output'
FILE_NAME = 'RGB'


c = np.load(os.path.join(INPUT_FOLDER,FILE_NAME) + '.npy')
print(c.shape)

cv2.imshow(FILE_NAME, c)
cv2.imwrite(os.path.join(OUTPUT_FOLDER, FILE_NAME) + '.png', c)

cv2.waitKey(0)
