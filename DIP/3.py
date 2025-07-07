import cv2 
# Read an Image  
col_image=cv2.imread('image',1)
w,h=col_image.shape[:2] 
# Compute the center of the image 
center = (w//2, h//2) 
# Define rotation angle in degrees 
angle= int(input('Enter an angle in degree(+ve/-ve for clockwise/anti-clockwise :'))
scale = 1 
# Calculate rotation matrix 
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale) 
# Apply the computed rotation matrix to the image 
rotated_image = cv2.warpAffine(col_image, rotation_matrix, (w, h)) 
cv2.imshow('Original Image',col_image) 
cv2.imshow('Rotated Color_Image',rotated_image) 
cv2.waitKey(0)  
cv2.destroyAllWindows() 

