import cv2 
# Read an Image  
im=cv2.imread('image.jpg',1)
cv2.imshow('Original Image',im) 
w,h,c=im.shape 
print(w,h) 
# Scaling by scale factors 
scale_x = 0.5 
scale_y = 0.5 
reduced_im=cv2.resize(im,None,fx=scale_x,  
fy=scale_y,interpolation=cv2.INTER_CUBIC) 
print(reduced_im.shape)
 
cv2.imshow('Reduced Gray Image',reduced_im) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

