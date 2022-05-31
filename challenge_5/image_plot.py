import matplotlib.pyplot as plt # import dependencies
import cv2
from os import path

IMAGE_PATH = path.join(path.dirname(__file__), "sea.jpg")

image = cv2.imread(IMAGE_PATH) # read image
image = image[:,:,::-1] # convert to RGB, cv2 reads in BGR
image_negative = 255 - image # invert the image

#fig = plt.figure() # create figure

fig, axes = plt.subplots(2, 2) # create figure
axes[0,0] = plt.subplot(2, 2, 1) # override subplot
axes[0,1] = plt.subplot(2, 2, 2) # override subplot
axes[1,0] = plt.subplot(2, 1, 2) # override subplot with double width
axes[1,1] = None # override subplot with None

axes[0,0].imshow(image, interpolation="bilinear") # create image in matplotlib
axes[0,0].axis("off")

axes[0,1].imshow(image_negative, interpolation="bilinear") # create image in matplotlib
axes[0,1].axis("off")

for channel, color in enumerate(["r", "g", "b"]): # iterate over channels
    histr = cv2.calcHist([image], [channel], None, [256], [0, 256]) # calculate histogram
    axes[1,0].plot(histr, color=color) # plot histogram

axes[1,0].set_xlim([0, 256])

fig.canvas.manager.set_window_title("Challenge 5.1: Image Plotting") # set the window title

plt.show() # show the plot