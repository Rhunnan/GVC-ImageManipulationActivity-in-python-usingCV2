import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = "peacock.jpg"

image1 = cv2.imread(img1, cv2.IMREAD_COLOR)
grayScaledImage1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)



while True:
        
    print("MENU: Select flag to display image:")
    print("input [1] to display Original Image")
    print("input [2] to display two histogram of Two different Images")
    print("input [3] to display seperate RGB Histograms")
    print("input [3] to display seperate RGB Histograms")
    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        cv2.imshow('Peacock', image1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected == "2":
         cv2.imshow('grayscaledImage', grayScaledImage1)
    elif selected == "3":
        histImage1 = cv2.calcHist([grayScaledImage1], [0], None, [256], [0,256])
        #image1
        plt.figure()
        plt.title("Historam of Image 1 in grayscaled")
        plt.plot(histImage1) 
    else:
        print("The inputted Value is not in the Menu")
    
    


