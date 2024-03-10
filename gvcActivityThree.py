import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = "peacock.jpg"
img2 = "pheagle.jpg"

image1 = cv2.imread(img1, cv2.IMREAD_COLOR)
image2 = cv2.imread(img2, cv2.IMREAD_COLOR)


while True:
        
    print("MENU:")
    print("input [1] to display Original Image")
    print("input [2] to display two histogram of Two different Images")
    print("input [3] to display seperate RGB Histograms")
    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        cv2.imshow('Peacock', image1)
        cv2.imshow('Eagle', image2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected == "2":
        grayScaledImage1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        grayScaledImage2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)    

        histImage1 = cv2.calcHist([grayScaledImage1], [0], None, [256], [0,256])
        histImage2 = cv2.calcHist([grayScaledImage2], [0], None, [256], [0,256])
        #image1
        plt.figure()
        plt.title("Historam of Image 1 in grayscaled")
        plt.plot(histImage1)
        #image2
        plt.figure()
        plt.title("Historam of Image 2 in grayscaled")
        plt.plot(histImage2)  
        plt.show()  
    elif selected == "3":
        #splitting the two images into RGB channels
        b1, g1, r1 = cv2.split(image1)
        b2, g2, r2 = cv2.split(image2)

        #calcualting the histograms for each channels or values of the RGB
        #una nga image
        histb1 = cv2.calcHist([b1], [0], None, [256], [0,256])
        histg1 = cv2.calcHist([g1], [0], None, [256], [0,256])
        histr1 = cv2.calcHist([r1], [0], None, [256], [0,256])
        #ikaduha
        histb2 = cv2.calcHist([b2], [0], None, [256], [0,256])
        histg2 = cv2.calcHist([g2], [0], None, [256], [0,256])
        histr2 = cv2.calcHist([r2], [0], None, [256], [0,256])

        #plotting image 1 for histogram using matplotlib package
        plt.figure()
        plt.title("Histogram - Blue Channel - Image1")
        plt.plot(histb1)    
        plt.figure()
        plt.title("Histogram - Green Channel - Image1")
        plt.plot(histg1) 
        plt.figure()
        plt.title("Histogram - Red Channel - Image1")
        plt.plot(histr1)        

        #plotting image 2        
        plt.figure()
        plt.title("Histogram - Blue Channel - Image2")
        plt.plot(histb2)    
        plt.figure()
        plt.title("Histogram - Green Channel - Image2")
        plt.plot(histg2) 
        plt.figure()
        plt.title("Histogram - Red Channel - Image2")
        plt.plot(histr2)        

        plt.show()
    else:
        print("The inputted Value is not in the Menu")
    
    


