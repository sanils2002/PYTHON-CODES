# importing required libraries
import matplotlib.pyplot as plt
import matplotlib.image as img

# reading the image
testImage = img.imread('g4g.png')

# displaying the image
plt.imshow(testImage)

# displaying the image as an array
print(testImage)

###############################################

# In the output image, only the mode of the image is modified

# reading the image
testImage = img.imread('g4g.png')
  
# displaying the shape of the image
print(testImage.shape)
  
# modifying the shape of the image
modifiedImage = testImage[:, :, 0]
  
# displaying the modified image
plt.imshow(modifiedImage)

# Here the height of the image is 150 pixels (displaying from the 50th pixel), 
# width is 100 pixels (displaying from the 100th pixel) and mode value is 1.

# reading the image
testImage = img.imread('g4g.png')

# displaying the shape of the image
print(testImage.shape)

# modifying the shape of the image
modifiedImage = testImage[50:200, 100:200, 1]

# displaying the modified image
plt.imshow(modifiedImage)


