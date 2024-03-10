import cv2
import numpy as np

def getPixelValue(x, y, image):
    #getting the pixel value using the [x, y ] method, ang pixel nga gekuha nako ani kay coordinate x og y na value
    pixelVal = image[x,y]

    return pixelVal
#activity 1
eagleFile = "pheagle.jpg"

#grayscaled imgae para gamiton sa thresholding
img2 = cv2.imread(eagleFile, cv2.IMREAD_GRAYSCALE)
# ako gekuha ang dimension sa image ron makuha nako ang size or ang height og width sa image 
dimensions = img2.shape
print("shape of the image load ", img2.shape)
#converting image to black and white by thresholding the img2 which is already in grayscaled
ret, blackWhiteImg = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)



while True:
        
    print("MENU: Select flag to display image:")
    print("input [1] to get the size of an Image")
    print("input [2] to get BGR pixel of an image")
    print("input [3] for Unchange Image flag")
    print("input [4] for Black and White Image")
    print("input [5] to get BGR values of a pixel")

    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        print("Image heigt: {} Image width: {}".format(dimensions[0], dimensions[1]))
    elif selected == "2":
        x = int(input("Input Coordinate X: "))
        y = int(input("Input Coordinate y: "))
        
        pixelVal = getPixelValue(x,y, blackWhiteImg)
        #since colored manining img1 kay gamit og flag na cv2.IMREAD_COLOR so naa ni 3 ka values which is ang BGR
        print(f"Pixel Value at {x}, {y} = {pixelVal}")
    # elif selected == "3":
    # elif selected == "4":
    #     cv2.imshow('ealgeBW', blackWhiteImg)
    # elif selected == "5":
        
    else:
        print("The inputted Value is not in the Menu")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

