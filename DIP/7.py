import cv2 
import matplotlib 
matplotlib.use('Qt5Agg')  # or 'Qt5Agg', or 'GTK3Agg'
from matplotlib import pyplot as plt
# Load images using OpenCV

im = cv2.imread('image.jpg',0)
print(im.shape) 
# Histogram of the original Image 
hist_im = cv2.calcHist([im],[0],None,[256],[0,256]) 
# Normalize the histogram of the original Image 
hist_im=hist_im/hist_im.sum() 
equ_im = cv2.equalizeHist(im) 
hist_equ_im = cv2.calcHist([equ_im],[0],None,[256],[0,256])
hist_equ_im=hist_equ_im/hist_equ_im.sum() 
fig,axes=plt.subplots(2,2,figsize=(10,8)) 
axes[0,0].imshow(im,'gray') 
axes[0,0].set_title('Original Image') 
axes[0,0].axis('off') 
axes[0,1].plot(hist_im) 
axes[0,1].set_title('Histogram of the Original Image(Normalized)')
axes[0,1].set_xlabel('Intensity') 
axes[0,1].set_ylabel('Frequency') 
axes[0,1].set_xlim([0, 256]) 
axes[1,0].imshow(equ_im,'gray') 
axes[1,0].set_title('Equalized Image') 
axes[1,0].axis('off') 
axes[1,1].plot(hist_equ_im) 
axes[1,1].set_title('Histogram of the Equalized Image(Normalized)') 
axes[1,1].set_xlabel('Intensity') 
axes[1,1].set_ylabel('Frequency') 
axes[1,1].set_xlim([0, 256]) 
fig.tight_layout(pad=1.0) 
plt.show() 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

