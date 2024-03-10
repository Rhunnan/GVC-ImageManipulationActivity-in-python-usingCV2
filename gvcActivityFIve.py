import cv2
import matplotlib.pyplot as plt
import numpy as np


def getPixelValue(x, y, image):
    #getting the pixel value using the [x, y ] method, ang pixel nga gekuha nako ani kay coordinate x og y na value
    pixelVal = image[x,y]

    return pixelVal
#gabuhat kog choice para sa user mo pili og image 
img1 = "peacock.jpg"

image1 = cv2.imread(img1, cv2.IMREAD_COLOR)
grayScaledImage1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)


while True:
        
    print("MENU: Select flag to display image:")
    print("input [1] to display Original Image")
    print("input [2] to display Grayscaled Image")
    print("input [3] to display the GrayScaled Image Histograms")
    print("input [4] to display the properties of the Image")
    print("input [5] to get a value of a pixel in the image")

    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        cv2.imshow('Peacock', image1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected == "2":
        cannyEdges1 = cv2.Canny(grayScaledImage1, 100, 200)
        cv2.imshow('canny Edge',cannyEdges1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected == "3":
        histImage1 = cv2.calcHist([grayScaledImage1], [0], None, [256], [0,256])
        #image1
        figure = plt.figure(figsize=(10,7))

        figure1 = figure.add_subplot(1,2,1)
        figure1.imshow(grayScaledImage1, cmap='gray')
        figure1.axis('off')
        figure1.set_title('GrayscaledImage')
        
        figure2 = figure.add_subplot(1,2,2)
        plt.hist(histImage1, color='gray')
        figure2.axis('off')
        figure2.set_title('Histogram of The Image')
        plt.show()
    elif selected == "4": 
        dimensions =  image1.shape
        print(f"Image heigt: {dimensions[0]} Image width: {dimensions[1]}")

    elif selected == "5":
        x = int(input("Input Coordinate X: "))
        y = int(input("Input Coordinate y: "))
        
        pixelVal = getPixelValue(x,y, image1)
        #since colored manining img1 kay gamit og flag na cv2.IMREAD_COLOR so naa ni 3 ka values which is ang BGR
        print("Pixel Blue value: {} Pixel Green Value: {} Pixel Red Value: {}".format(pixelVal[0], pixelVal[1], pixelVal[2]))
        
    else:
        print("The inputted Value is not in the Menu")
    
    


