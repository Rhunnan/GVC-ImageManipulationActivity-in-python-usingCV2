import cv2
import numpy as np

img1 = "peacock.jpg"
img2 = "pheagle.jpg"

image1 = cv2.imread(img1, cv2.IMREAD_COLOR)
image2 = cv2.imread(img2, cv2.IMREAD_COLOR)

while True:
        
    print("MENU: Select flag to display image:")
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
        c
    elif selected == "3":
        cv2.imshow('ealge', img3)
    else:
        print("The inputted Value is not in the Menu")
    
    


