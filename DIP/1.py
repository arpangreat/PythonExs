import cv2 
# Read and display an Image 
col_image=cv2.imread('image.jpg',1) 
cv2.imshow('Original Color_Image',col_image) 
# Convert a color Image into a grascale image 
gray_image=cv2.cvtColor(col_image,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray-scale Image',gray_image) 
# Convert a Gray Image into a binary image 
_,binary_image=cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY) 
cv2.imshow('Binary Image', binary_image) 
# mean of pixels 
m=int(gray_image.mean()) 
print(m) 
# Convert a Gray Image into a binary image with with threshold value as mean _,binary_image_m=cv2.threshold(gray_image,m,255,cv2.THRESH_BINARY) 
cv2.imshow('Binary Image(Threshold Mean)', binary_image) 
cv2.waitKey(0)  
cv2.destroyAllWindows() 

