import cv2 
import numpy as np 
# Load a gray-scale image using OpenCV 
im = cv2.imread('image.jpg',0) 
print(im.shape) 
f=np.fft.fft2(im) 
ft=np.fft.fftshift(f) 
w, h = im.shape 
cu, cv = w // 2, h // 2 
sigma = 10  
  
x, y = np.indices((w,h)) 
gaussian = np.exp(-((x - cu)**2 + (y - cv)**2) / (2 * sigma**2)) 
high_pass_filter = 1 - gaussian 
filtered_f_ishift = ft * high_pass_filter 
img_back = np.fft.ifft2(filtered_f_ishift) 
img_back = np.abs(img_back) 
cv2.normalize(img_back, img_back, 0, 255, cv2.NORM_MINMAX) 
sharp_img = np.uint8(img_back) 
  
cv2.imshow('Original Image', im) 
cv2.imshow('Sharpened Image', sharp_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

