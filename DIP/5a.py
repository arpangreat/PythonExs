import cv2 
col_image=cv2.imread('image.jpg',1)
cv2.imshow('Original Color_Image',col_image) 
# Convert a color Image into a grascale image 
gray_image=cv2.cvtColor(col_image,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray-scale Image', gray_image) 
negative_col_image=255-col_image 
cv2.imshow('Negative of Color Image', negative_col_image) 
negative_gray_image=255-gray_image 
cv2.imshow('Negative of Gray-scale Image', negative_gray_image) 
cv2.waitKey(0)  
cv2.destroyAllWindows() 

