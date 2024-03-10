import cv2
import numpy as np

#activity 1
eagleFile = "pheagle.jpg"

#reading the eagle image
#firstFlag
img1 = cv2.imread(eagleFile, cv2.IMREAD_COLOR)
#2nd flag
img2 = cv2.imread(eagleFile, cv2.IMREAD_GRAYSCALE)
print("shape of the image load ", img1.shape)
#thirdFlag
img3 = cv2.imread(eagleFile, cv2.IMREAD_UNCHANGED)
#converting image to black and white by thresholding the img2 which is already in grayscaled
ret, blackWhiteImg = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

#getting the pixel value using the [x, y ] method, ang pixel nga gekuha nako ani kay ang top left corner nga pinakauna
pixelVal = img1[0,0]


while True:
        
    print("MENU: Select flag to display image:")
    print("input [1] for Colored Image flag")
    print("input [2] for Grayscale Image flag")
    print("input [3] for Unchange Image flag")
    print("input [4] for Black and White Image")
    print("input [5] to get BGR values of a pixel")

    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        cv2.imshow('ealge', img1)
    elif selected == "2":
        cv2.imshow('ealge', img2)
    elif selected == "3":
        cv2.imshow('ealge', img3)
    elif selected == "4":
        cv2.imshow('ealgeBW', blackWhiteImg)
    elif selected == "5":
        #since colored manining img1 kay gamit og flag na cv2.IMREAD_COLOR so naa ni 3 ka values which is ang BGR
        print("Pixel Blue value: {} Pixel Green Value: {} Pixel Red Value: {}".format(pixelVal[0], pixelVal[1], pixelVal[2]))
    else:
        print("The inputted Value is not in the Menu")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


