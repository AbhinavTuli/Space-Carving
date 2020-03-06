import numpy as np
import os
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#converting images from RGB to grayscale
img1 = Image.open("E1.jpg").convert('L') 
img2 = Image.open("E2.jpg").convert('L')

#thresholding images to convert to binary
threshold=150
img1 = img1.point(lambda p: p > threshold and 255) 
img2 = img2.point(lambda p: p > threshold and 255) 

# img1.save('1.png')
# img2.save('2.png')

#creating 3 voxel arrays of 100x100x100
N1 = 100
N2 = 100
N3 = 100
ma1 = np.zeros((N1,N2,N3))
ma2 = np.zeros((N1,N2,N3))
ma = np.zeros((N1,N2,N3))

pixels1=img1.load()
pixels2=img2.load()

#getting projection of 2 different views
for i in range(img1.size[0]): 
    for j in range(img1.size[1]):
            for k in range(100):
                ma2[j,i,k]=255-pixels1[i,j]

for k in range(img2.size[0]): 
    for j in range(img2.size[1]):
            for i in range(100):
                ma1[i,j,k]=255-pixels2[k,j]

#combining the projections
for i in range(img1.size[0]): 
    for j in range(img1.size[1]):
            for k in range(100):
                if ma1[i,j,k]==255 and ma2[i,j,k]==255:
                    ma[i,j,k]=255
                else:
                    ma[i,j,k]=0


# for i in range(100):
#     for j in range(100):
#         print(ma2[i,j])

#plotting the merged projections
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.voxels(ma, edgecolor="k")

plt.show()


        
