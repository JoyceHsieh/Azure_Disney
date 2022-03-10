# import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import utils
import seaborn as sns
from cv2 import cv2


def centroid_histogram(clt):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)

	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()

	# return the histogram
	return hist

def plot_colors(hist, centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0

	# loop over the percentage of each cluster and the color of
	# each cluster
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	
	# return the bar chart
	return bar

def opencv_open_into_rgb( image_file_name ):
    """ open image_file_name and convert to rgb """
    image_raw = cv2.imread(image_file_name, cv2.IMREAD_COLOR)  # reads into BGR
    image_rgb = cv2.cvtColor(image_raw, cv2.COLOR_BGR2RGB)     # convert from BGR to RGB
    return image_rgb


def color_quantization(file_name):

    image=opencv_open_into_rgb(f"static/{file_name}") 

    pixel_vals = image.reshape((-1,3))
  
    # Convert to float type
    pixel_vals = np.float32(pixel_vals)
	

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    retval, labels, centers = cv2.kmeans(pixel_vals, 7 , None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)


    center = np.uint8(centers)
    segmented_data = center[labels.flatten()] 
    
    # reshape data into the original image dimensions
    segmented_image = segmented_data.reshape((image.shape))
    

    return segmented_image

