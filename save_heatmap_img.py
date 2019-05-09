#! /usr/bin/env python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# np.save("/home/aarons/catkin_kinect/src/yumi_grasp/src/grasp_est.npy", points_out)

INPUT_FOLDER = './input'
OUTPUT_FOLDER = './output'
FILE_NAME = 'grasp_est'


fig, ax = plt.subplots()
c = np.load(os.path.join(INPUT_FOLDER,FILE_NAME) +'.npy')
print(c.shape)

ax = sns.heatmap(c, cmap='jet', xticklabels=False, yticklabels=False, cbar=True)
ax.axis('off')
fig.add_axes(ax)
fig.canvas.draw()
data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

print(data.shape)
X = np.array(fig.canvas.renderer._renderer)
print(X.shape)
print(X[1,1,:])
ax.figure.savefig(os.path.join(OUTPUT_FOLDER, FILE_NAME) + '.png')
plt.show()
plt.close()