import cv2 
import numpy as np  
# Read and display an Image 
a=cv2.imread('image.jpg',0) 
cv2.imshow('Noisy Image',a) 
m,n=a.shape 
c=np.zeros([m, n])  
for i in range(1,m-1): 
 for j in range(1,n-1): 
     b=[a[i-1,j-1],a[i-1,j],a[i-1,j+1],a[i,j-1],a[i,j],a[i,j+1],a[i+1,j-1],a[i+1,j],a[i+1,j+1]]   
     b=sorted(b) 
     c[i,j]=b[4] 
c = c.astype(np.uint8)  
cv2.imshow('Noisy Image',a) 
cv2.imshow('Median Filtered',c)

# filtered_image = cv2.medianBlur(noisy_image, 3) # cv2.imshow('Median Filtered',filtered_image) 
cv2.waitKey(0)  
cv2.destroyAllWindows() 

