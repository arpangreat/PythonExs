import cv2 
# Load images using OpenCV 
image1 = cv2.imread('image.jpg',1)
cv2.imshow('Dog',image1) 
# Flipping Vertically 
image2=cv2.flip(image1,0) 
cv2.imshow('Vertical',image2) 
# Flipping Horizontally 
image3=cv2.flip(image1,1) 
cv2.imshow('Horizontal',image3) 
# Flipping 
image4=cv2.flip(image1,-1) 
cv2.imshow('Flipping(Both)',image4) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

